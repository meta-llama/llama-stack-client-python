import argparse

import yaml

from llama_stack_client import LlamaStackDirectClient
from llama_stack_client.types import UserMessage


async def main(config_path: str):
    client = await LlamaStackDirectClient.from_config(config_path)
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
