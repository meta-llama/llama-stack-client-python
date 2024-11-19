import inspect
import yaml
from typing import Any, cast, get_args, get_origin, Type

from rich.console import Console
from llama_stack.distribution.datatypes import StackRunConfig
from llama_stack.distribution.distribution import get_provider_registry
from llama_stack.distribution.resolver import resolve_impls
from llama_stack.distribution.server.endpoints import get_all_api_endpoints
from llama_stack.distribution.server.server import is_streaming_request
from llama_stack.distribution.stack import (
    get_stack_run_config_from_template,
)
from llama_stack.distribution.stack import construct_stack
from pydantic import BaseModel

from ..._base_client import ResponseT
from ..._client import LlamaStackClient
from ..._streaming import Stream
from ..._types import Body, NOT_GIVEN, RequestFiles, RequestOptions


class LlamaStackDirectClient(LlamaStackClient):
    def __init__(self, config: StackRunConfig, **kwargs):
        raise TypeError("Use from_config() or from_template() instead of direct initialization")

    @classmethod
    async def from_config(cls, config: StackRunConfig, **kwargs):
        instance = object.__new__(cls)
        await instance._initialize(config, **kwargs)
        return instance

    @classmethod
    async def from_template(cls, template_name: str, **kwargs):
        config = get_stack_run_config_from_template(template_name)
        console = Console()
        console.print(f"[green]Using template[/green] [blue]{template_name}[/blue] with config:")
        console.print(yaml.dump(config.model_dump(), indent=2, default_flow_style=False))
        instance = object.__new__(cls)
        await instance._initialize(config, **kwargs)
        return instance

    async def _initialize(self, config: StackRunConfig, **kwargs) -> None:
        super().__init__(**kwargs)
        self.endpoints = get_all_api_endpoints()
        self.config = config
        self.impls = None
        await self.initialize()

    async def initialize(self) -> None:
        self.impls = await construct_stack(self.config)

    def _convert_param(self, param_type: Any, value: Any) -> Any:
        origin = get_origin(param_type)
        if origin == list:
            item_type = get_args(param_type)[0]
            if isinstance(item_type, type) and issubclass(item_type, BaseModel):
                return [item_type(**item) for item in value]
            return value

        elif origin == dict:
            _, val_type = get_args(param_type)
            if isinstance(val_type, type) and issubclass(val_type, BaseModel):
                return {k: val_type(**v) for k, v in value.items()}
            return value

        elif isinstance(param_type, type) and issubclass(param_type, BaseModel):
            return param_type(**value)

        # Return as-is for primitive types
        return value

    async def _call_endpoint(self, path: str, method: str, body: dict = None) -> Any:
        for api, endpoints in self.endpoints.items():
            for endpoint in endpoints:
                if endpoint.route == path:
                    impl = self.impls[api]
                    func = getattr(impl, endpoint.name)
                    sig = inspect.signature(func)  #

                    if body:
                        # Strip NOT_GIVENs to use the defaults in signature
                        body = {k: v for k, v in body.items() if v is not NOT_GIVEN}

                        # Convert parameters to Pydantic models where needed
                        converted_body = {}
                        for param_name, param in sig.parameters.items():
                            if param_name in body:
                                value = body.get(param_name)
                                converted_body[param_name] = self._convert_param(param.annotation, value)
                        body = converted_body

                    if is_streaming_request(endpoint.name, body):
                        async for chunk in func(**(body or {})):
                            yield chunk
                    else:
                        yield await func(**(body or {}))

        raise ValueError(f"No endpoint found for {path}")

    async def get(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        options: RequestOptions = None,
        stream: bool = False,
        stream_cls: type[Stream[Any]] | None = None,
    ) -> ResponseT:
        options = options or {}
        async for response in self._call_endpoint(path, "GET"):
            return cast(ResponseT, response)

    async def post(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        options: RequestOptions = None,
        files: RequestFiles | None = None,
        stream: bool = False,
        stream_cls: type[Stream[Any]] | None = None,
    ) -> ResponseT:
        options = options or {}
        async for response in self._call_endpoint(path, "POST", body):
            return cast(ResponseT, response)
