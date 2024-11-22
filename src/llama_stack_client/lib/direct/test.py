import argparse

import yaml
from llama_stack.distribution.configure import parse_and_maybe_upgrade_config

from llama_stack_client.lib.direct.direct import LlamaStackDirectClient
from llama_stack_client.types import UserMessage


async def main(config_path: str):
    with open(config_path, "r") as f:
        config_dict = yaml.safe_load(f)

    run_config = parse_and_maybe_upgrade_config(config_dict)

    client = await LlamaStackDirectClient.from_config(run_config)
    await client.initialize()

    response = await client.models.list()
    print(response)

    response = await client.inference.chat_completion(
        messages=[UserMessage(content="What is the capital of France?", role="user")],
        model="Llama3.1-8B-Instruct",
        stream=False,
    )
    print("\nChat completion response:")
    print(response)


if __name__ == "__main__":
    import asyncio

    parser = argparse.ArgumentParser()
    parser.add_argument("config_path", help="Path to the config YAML file")
    args = parser.parse_args()
    asyncio.run(main(args.config_path))
