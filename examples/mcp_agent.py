import json
import logging
from urllib.parse import urlparse

import fire
import httpx
from llama_stack_client import Agent, AgentEventLogger, LlamaStackClient
from llama_stack_client.lib import get_oauth_token_for_mcp_server
from rich import print as rprint

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


import tempfile
from pathlib import Path

TMP_DIR = Path(tempfile.gettempdir()) / "llama-stack"
TMP_DIR.mkdir(parents=True, exist_ok=True)

CACHE_FILE = TMP_DIR / "mcp_tokens.json"


def main(model_id: str, mcp_servers: str = "https://mcp.asana.com/sse", llama_stack_url: str = "http://localhost:8321"):
    """Run an MCP agent with the specified model and servers.

    Args:
        model_id: The model to use for the agent.
        mcp_servers: Comma-separated list of MCP servers to use for the agent.
        llama_stack_url: The URL of the Llama Stack server to use.

    Examples:
        python mcp_agent.py "meta-llama/Llama-4-Scout-17B-16E-Instruct" \
             -m "https://mcp.asana.com/sse" \
             -l "http://localhost:8321"
    """
    client = LlamaStackClient(base_url=llama_stack_url)
    if not check_model_exists(client, model_id):
        return

    servers = [s.strip() for s in mcp_servers.split(",")]
    mcp_headers = get_and_cache_mcp_headers(servers)

    toolgroup_ids = []
    for server in servers:
        # we cannot use "/" in the toolgroup_id because we have some tech debt from earlier which uses
        # "/" as a separator for toolgroup_id and tool_name. We should fix this in the future.
        group_id = urlparse(server).netloc
        toolgroup_ids.append(group_id)
        client.toolgroups.register(
            toolgroup_id=group_id, mcp_endpoint=dict(uri=server), provider_id="model-context-protocol"
        )

    agent = Agent(
        client=client,
        model=model_id,
        instructions="You are a helpful assistant who can use tools when necessary to answer questions.",
        tools=toolgroup_ids,
        extra_headers={
            "X-LlamaStack-Provider-Data": json.dumps(
                {
                    "mcp_headers": mcp_headers,
                }
            ),
        },
    )

    session_id = agent.create_session("test-session")

    while True:
        user_input = input("Enter a question: ")
        if user_input.lower() in ("q", "quit", "exit", "bye", ""):
            print("Exiting...")
            break
        response = agent.create_turn(
            session_id=session_id,
            messages=[{"role": "user", "content": user_input}],
            stream=True,
        )
        for log in AgentEventLogger().log(response):
            log.print()


def check_model_exists(client: LlamaStackClient, model_id: str) -> bool:
    models = [m for m in client.models.list() if m.model_type == "llm"]
    if model_id not in [m.identifier for m in models]:
        rprint(f"[red]Model {model_id} not found[/red]")
        rprint("[yellow]Available models:[/yellow]")
        for model in models:
            rprint(f"  - {model.identifier}")
        return False
    return True


def get_and_cache_mcp_headers(servers: list[str]) -> dict[str, dict[str, str]]:
    mcp_headers = {}

    logger.info(f"Using cache file: {CACHE_FILE} for MCP tokens")
    tokens = {}
    if CACHE_FILE.exists():
        with open(CACHE_FILE, "r") as f:
            tokens = json.load(f)
            for server, token in tokens.items():
                mcp_headers[server] = {
                    "Authorization": f"Bearer {token}",
                }

    for server in servers:
        with httpx.Client() as http_client:
            headers = mcp_headers.get(server, {})
            try:
                response = http_client.get(server, headers=headers, timeout=1.0)
            except httpx.TimeoutException:
                # timeout means success since we did not get an immediate 40X
                continue

            if response.status_code in (401, 403):
                logger.info(f"Server {server} requires authentication, getting token")
                token = get_oauth_token_for_mcp_server(server)
                if not token:
                    logger.error(f"No token obtained for {server}")
                    return

                tokens[server] = token
                mcp_headers[server] = {
                    "Authorization": f"Bearer {token}",
                }

    with open(CACHE_FILE, "w") as f:
        json.dump(tokens, f, indent=2)

    return mcp_headers


if __name__ == "__main__":
    fire.Fire(main)
