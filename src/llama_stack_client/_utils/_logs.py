import os
import logging
from rich.logging import RichHandler

logger: logging.Logger = logging.getLogger("llama_stack_client")
httpx_logger: logging.Logger = logging.getLogger("httpx")


def _basic_config() -> None:
    logging.basicConfig(
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)],
    )


def setup_logging() -> None:
    env = os.environ.get("LLAMA_STACK_LOG")
    if env == "debug":
        _basic_config()
        logger.setLevel(logging.DEBUG)
        httpx_logger.setLevel(logging.DEBUG)
    elif env == "info":
        _basic_config()
        logger.setLevel(logging.INFO)
        httpx_logger.setLevel(logging.INFO)
