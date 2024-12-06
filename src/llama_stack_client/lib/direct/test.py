import argparse

from llama_stack_client import LlamaStackDirectClient
from llama_stack_client.types import UserMessage


async def main(config_path: str):
    client = await LlamaStackDirectClient.from_config(config_path)
    await client.initialize()

    response = await client.models.list()
    print(response)

    response = await client.inference.chat_completion(
        messages=[UserMessage(content="What is the capital of France?", role="user")],
        model_id="meta-llama/Llama-3.2-3B-Instruct",
        stream=False,
    )
    print("\nChat completion response:")
    print(response)

    response = await client.memory_banks.register(
        memory_bank_id="test_memory_bank",
        params={
            "embedding_model": "all-MiniLM-L6-v2",
            "chunk_size_in_tokens": 512,
            "overlap_size_in_tokens": 64,
        },
        provider_id="test_memory_bank",
    )
    print("\nRegister memory bank response:")
    print(response)


if __name__ == "__main__":
    import asyncio

    parser = argparse.ArgumentParser()
    parser.add_argument("config_path", help="Path to the config YAML file")
    args = parser.parse_args()
    asyncio.run(main(args.config_path))
