# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import (
    tools,
    health,
    models,
    safety,
    inspect,
    scoring,
    shields,
    version,
    datasets,
    datasetio,
    inference,
    providers,
    vector_io,
    toolgroups,
    vector_dbs,
    scoring_functions,
    synthetic_data_generation,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.eval import eval
from .resources.files import files
from .resources.agents import agents
from .resources.openai import openai
from .resources.telemetry import telemetry
from .resources.tool_runtime import tool_runtime
from .resources.post_training import post_training

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "LlamaStackClient",
    "AsyncLlamaStackClient",
    "Client",
    "AsyncClient",
]


class LlamaStackClient(SyncAPIClient):
    datasetio: datasetio.DatasetioResource
    inference: inference.InferenceResource
    post_training: post_training.PostTrainingResource
    agents: agents.AgentsResource
    openai: openai.OpenAIResource
    files: files.FilesResource
    eval: eval.EvalResource
    datasets: datasets.DatasetsResource
    models: models.ModelsResource
    scoring_functions: scoring_functions.ScoringFunctionsResource
    shields: shields.ShieldsResource
    telemetry: telemetry.TelemetryResource
    tools: tools.ToolsResource
    toolgroups: toolgroups.ToolgroupsResource
    vector_dbs: vector_dbs.VectorDBsResource
    health: health.HealthResource
    tool_runtime: tool_runtime.ToolRuntimeResource
    vector_io: vector_io.VectorIoResource
    providers: providers.ProvidersResource
    inspect: inspect.InspectResource
    safety: safety.SafetyResource
    scoring: scoring.ScoringResource
    synthetic_data_generation: synthetic_data_generation.SyntheticDataGenerationResource
    version: version.VersionResource
    with_raw_response: LlamaStackClientWithRawResponse
    with_streaming_response: LlamaStackClientWithStreamedResponse

    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous LlamaStackClient client instance.

        This automatically infers the `api_key` argument from the `LLAMA_STACK_CLIENT_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LLAMA_STACK_CLIENT_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("LLAMA_STACK_CLIENT_BASE_URL")
        if base_url is None:
            base_url = f"http://any-hosted-llama-stack.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.datasetio = datasetio.DatasetioResource(self)
        self.inference = inference.InferenceResource(self)
        self.post_training = post_training.PostTrainingResource(self)
        self.agents = agents.AgentsResource(self)
        self.openai = openai.OpenAIResource(self)
        self.files = files.FilesResource(self)
        self.eval = eval.EvalResource(self)
        self.datasets = datasets.DatasetsResource(self)
        self.models = models.ModelsResource(self)
        self.scoring_functions = scoring_functions.ScoringFunctionsResource(self)
        self.shields = shields.ShieldsResource(self)
        self.telemetry = telemetry.TelemetryResource(self)
        self.tools = tools.ToolsResource(self)
        self.toolgroups = toolgroups.ToolgroupsResource(self)
        self.vector_dbs = vector_dbs.VectorDBsResource(self)
        self.health = health.HealthResource(self)
        self.tool_runtime = tool_runtime.ToolRuntimeResource(self)
        self.vector_io = vector_io.VectorIoResource(self)
        self.providers = providers.ProvidersResource(self)
        self.inspect = inspect.InspectResource(self)
        self.safety = safety.SafetyResource(self)
        self.scoring = scoring.ScoringResource(self)
        self.synthetic_data_generation = synthetic_data_generation.SyntheticDataGenerationResource(self)
        self.version = version.VersionResource(self)
        self.with_raw_response = LlamaStackClientWithRawResponse(self)
        self.with_streaming_response = LlamaStackClientWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncLlamaStackClient(AsyncAPIClient):
    datasetio: datasetio.AsyncDatasetioResource
    inference: inference.AsyncInferenceResource
    post_training: post_training.AsyncPostTrainingResource
    agents: agents.AsyncAgentsResource
    openai: openai.AsyncOpenAIResource
    files: files.AsyncFilesResource
    eval: eval.AsyncEvalResource
    datasets: datasets.AsyncDatasetsResource
    models: models.AsyncModelsResource
    scoring_functions: scoring_functions.AsyncScoringFunctionsResource
    shields: shields.AsyncShieldsResource
    telemetry: telemetry.AsyncTelemetryResource
    tools: tools.AsyncToolsResource
    toolgroups: toolgroups.AsyncToolgroupsResource
    vector_dbs: vector_dbs.AsyncVectorDBsResource
    health: health.AsyncHealthResource
    tool_runtime: tool_runtime.AsyncToolRuntimeResource
    vector_io: vector_io.AsyncVectorIoResource
    providers: providers.AsyncProvidersResource
    inspect: inspect.AsyncInspectResource
    safety: safety.AsyncSafetyResource
    scoring: scoring.AsyncScoringResource
    synthetic_data_generation: synthetic_data_generation.AsyncSyntheticDataGenerationResource
    version: version.AsyncVersionResource
    with_raw_response: AsyncLlamaStackClientWithRawResponse
    with_streaming_response: AsyncLlamaStackClientWithStreamedResponse

    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncLlamaStackClient client instance.

        This automatically infers the `api_key` argument from the `LLAMA_STACK_CLIENT_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LLAMA_STACK_CLIENT_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("LLAMA_STACK_CLIENT_BASE_URL")
        if base_url is None:
            base_url = f"http://any-hosted-llama-stack.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.datasetio = datasetio.AsyncDatasetioResource(self)
        self.inference = inference.AsyncInferenceResource(self)
        self.post_training = post_training.AsyncPostTrainingResource(self)
        self.agents = agents.AsyncAgentsResource(self)
        self.openai = openai.AsyncOpenAIResource(self)
        self.files = files.AsyncFilesResource(self)
        self.eval = eval.AsyncEvalResource(self)
        self.datasets = datasets.AsyncDatasetsResource(self)
        self.models = models.AsyncModelsResource(self)
        self.scoring_functions = scoring_functions.AsyncScoringFunctionsResource(self)
        self.shields = shields.AsyncShieldsResource(self)
        self.telemetry = telemetry.AsyncTelemetryResource(self)
        self.tools = tools.AsyncToolsResource(self)
        self.toolgroups = toolgroups.AsyncToolgroupsResource(self)
        self.vector_dbs = vector_dbs.AsyncVectorDBsResource(self)
        self.health = health.AsyncHealthResource(self)
        self.tool_runtime = tool_runtime.AsyncToolRuntimeResource(self)
        self.vector_io = vector_io.AsyncVectorIoResource(self)
        self.providers = providers.AsyncProvidersResource(self)
        self.inspect = inspect.AsyncInspectResource(self)
        self.safety = safety.AsyncSafetyResource(self)
        self.scoring = scoring.AsyncScoringResource(self)
        self.synthetic_data_generation = synthetic_data_generation.AsyncSyntheticDataGenerationResource(self)
        self.version = version.AsyncVersionResource(self)
        self.with_raw_response = AsyncLlamaStackClientWithRawResponse(self)
        self.with_streaming_response = AsyncLlamaStackClientWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class LlamaStackClientWithRawResponse:
    def __init__(self, client: LlamaStackClient) -> None:
        self.datasetio = datasetio.DatasetioResourceWithRawResponse(client.datasetio)
        self.inference = inference.InferenceResourceWithRawResponse(client.inference)
        self.post_training = post_training.PostTrainingResourceWithRawResponse(client.post_training)
        self.agents = agents.AgentsResourceWithRawResponse(client.agents)
        self.openai = openai.OpenAIResourceWithRawResponse(client.openai)
        self.files = files.FilesResourceWithRawResponse(client.files)
        self.eval = eval.EvalResourceWithRawResponse(client.eval)
        self.datasets = datasets.DatasetsResourceWithRawResponse(client.datasets)
        self.models = models.ModelsResourceWithRawResponse(client.models)
        self.scoring_functions = scoring_functions.ScoringFunctionsResourceWithRawResponse(client.scoring_functions)
        self.shields = shields.ShieldsResourceWithRawResponse(client.shields)
        self.telemetry = telemetry.TelemetryResourceWithRawResponse(client.telemetry)
        self.tools = tools.ToolsResourceWithRawResponse(client.tools)
        self.toolgroups = toolgroups.ToolgroupsResourceWithRawResponse(client.toolgroups)
        self.vector_dbs = vector_dbs.VectorDBsResourceWithRawResponse(client.vector_dbs)
        self.health = health.HealthResourceWithRawResponse(client.health)
        self.tool_runtime = tool_runtime.ToolRuntimeResourceWithRawResponse(client.tool_runtime)
        self.vector_io = vector_io.VectorIoResourceWithRawResponse(client.vector_io)
        self.providers = providers.ProvidersResourceWithRawResponse(client.providers)
        self.inspect = inspect.InspectResourceWithRawResponse(client.inspect)
        self.safety = safety.SafetyResourceWithRawResponse(client.safety)
        self.scoring = scoring.ScoringResourceWithRawResponse(client.scoring)
        self.synthetic_data_generation = synthetic_data_generation.SyntheticDataGenerationResourceWithRawResponse(
            client.synthetic_data_generation
        )
        self.version = version.VersionResourceWithRawResponse(client.version)


class AsyncLlamaStackClientWithRawResponse:
    def __init__(self, client: AsyncLlamaStackClient) -> None:
        self.datasetio = datasetio.AsyncDatasetioResourceWithRawResponse(client.datasetio)
        self.inference = inference.AsyncInferenceResourceWithRawResponse(client.inference)
        self.post_training = post_training.AsyncPostTrainingResourceWithRawResponse(client.post_training)
        self.agents = agents.AsyncAgentsResourceWithRawResponse(client.agents)
        self.openai = openai.AsyncOpenAIResourceWithRawResponse(client.openai)
        self.files = files.AsyncFilesResourceWithRawResponse(client.files)
        self.eval = eval.AsyncEvalResourceWithRawResponse(client.eval)
        self.datasets = datasets.AsyncDatasetsResourceWithRawResponse(client.datasets)
        self.models = models.AsyncModelsResourceWithRawResponse(client.models)
        self.scoring_functions = scoring_functions.AsyncScoringFunctionsResourceWithRawResponse(
            client.scoring_functions
        )
        self.shields = shields.AsyncShieldsResourceWithRawResponse(client.shields)
        self.telemetry = telemetry.AsyncTelemetryResourceWithRawResponse(client.telemetry)
        self.tools = tools.AsyncToolsResourceWithRawResponse(client.tools)
        self.toolgroups = toolgroups.AsyncToolgroupsResourceWithRawResponse(client.toolgroups)
        self.vector_dbs = vector_dbs.AsyncVectorDBsResourceWithRawResponse(client.vector_dbs)
        self.health = health.AsyncHealthResourceWithRawResponse(client.health)
        self.tool_runtime = tool_runtime.AsyncToolRuntimeResourceWithRawResponse(client.tool_runtime)
        self.vector_io = vector_io.AsyncVectorIoResourceWithRawResponse(client.vector_io)
        self.providers = providers.AsyncProvidersResourceWithRawResponse(client.providers)
        self.inspect = inspect.AsyncInspectResourceWithRawResponse(client.inspect)
        self.safety = safety.AsyncSafetyResourceWithRawResponse(client.safety)
        self.scoring = scoring.AsyncScoringResourceWithRawResponse(client.scoring)
        self.synthetic_data_generation = synthetic_data_generation.AsyncSyntheticDataGenerationResourceWithRawResponse(
            client.synthetic_data_generation
        )
        self.version = version.AsyncVersionResourceWithRawResponse(client.version)


class LlamaStackClientWithStreamedResponse:
    def __init__(self, client: LlamaStackClient) -> None:
        self.datasetio = datasetio.DatasetioResourceWithStreamingResponse(client.datasetio)
        self.inference = inference.InferenceResourceWithStreamingResponse(client.inference)
        self.post_training = post_training.PostTrainingResourceWithStreamingResponse(client.post_training)
        self.agents = agents.AgentsResourceWithStreamingResponse(client.agents)
        self.openai = openai.OpenAIResourceWithStreamingResponse(client.openai)
        self.files = files.FilesResourceWithStreamingResponse(client.files)
        self.eval = eval.EvalResourceWithStreamingResponse(client.eval)
        self.datasets = datasets.DatasetsResourceWithStreamingResponse(client.datasets)
        self.models = models.ModelsResourceWithStreamingResponse(client.models)
        self.scoring_functions = scoring_functions.ScoringFunctionsResourceWithStreamingResponse(
            client.scoring_functions
        )
        self.shields = shields.ShieldsResourceWithStreamingResponse(client.shields)
        self.telemetry = telemetry.TelemetryResourceWithStreamingResponse(client.telemetry)
        self.tools = tools.ToolsResourceWithStreamingResponse(client.tools)
        self.toolgroups = toolgroups.ToolgroupsResourceWithStreamingResponse(client.toolgroups)
        self.vector_dbs = vector_dbs.VectorDBsResourceWithStreamingResponse(client.vector_dbs)
        self.health = health.HealthResourceWithStreamingResponse(client.health)
        self.tool_runtime = tool_runtime.ToolRuntimeResourceWithStreamingResponse(client.tool_runtime)
        self.vector_io = vector_io.VectorIoResourceWithStreamingResponse(client.vector_io)
        self.providers = providers.ProvidersResourceWithStreamingResponse(client.providers)
        self.inspect = inspect.InspectResourceWithStreamingResponse(client.inspect)
        self.safety = safety.SafetyResourceWithStreamingResponse(client.safety)
        self.scoring = scoring.ScoringResourceWithStreamingResponse(client.scoring)
        self.synthetic_data_generation = synthetic_data_generation.SyntheticDataGenerationResourceWithStreamingResponse(
            client.synthetic_data_generation
        )
        self.version = version.VersionResourceWithStreamingResponse(client.version)


class AsyncLlamaStackClientWithStreamedResponse:
    def __init__(self, client: AsyncLlamaStackClient) -> None:
        self.datasetio = datasetio.AsyncDatasetioResourceWithStreamingResponse(client.datasetio)
        self.inference = inference.AsyncInferenceResourceWithStreamingResponse(client.inference)
        self.post_training = post_training.AsyncPostTrainingResourceWithStreamingResponse(client.post_training)
        self.agents = agents.AsyncAgentsResourceWithStreamingResponse(client.agents)
        self.openai = openai.AsyncOpenAIResourceWithStreamingResponse(client.openai)
        self.files = files.AsyncFilesResourceWithStreamingResponse(client.files)
        self.eval = eval.AsyncEvalResourceWithStreamingResponse(client.eval)
        self.datasets = datasets.AsyncDatasetsResourceWithStreamingResponse(client.datasets)
        self.models = models.AsyncModelsResourceWithStreamingResponse(client.models)
        self.scoring_functions = scoring_functions.AsyncScoringFunctionsResourceWithStreamingResponse(
            client.scoring_functions
        )
        self.shields = shields.AsyncShieldsResourceWithStreamingResponse(client.shields)
        self.telemetry = telemetry.AsyncTelemetryResourceWithStreamingResponse(client.telemetry)
        self.tools = tools.AsyncToolsResourceWithStreamingResponse(client.tools)
        self.toolgroups = toolgroups.AsyncToolgroupsResourceWithStreamingResponse(client.toolgroups)
        self.vector_dbs = vector_dbs.AsyncVectorDBsResourceWithStreamingResponse(client.vector_dbs)
        self.health = health.AsyncHealthResourceWithStreamingResponse(client.health)
        self.tool_runtime = tool_runtime.AsyncToolRuntimeResourceWithStreamingResponse(client.tool_runtime)
        self.vector_io = vector_io.AsyncVectorIoResourceWithStreamingResponse(client.vector_io)
        self.providers = providers.AsyncProvidersResourceWithStreamingResponse(client.providers)
        self.inspect = inspect.AsyncInspectResourceWithStreamingResponse(client.inspect)
        self.safety = safety.AsyncSafetyResourceWithStreamingResponse(client.safety)
        self.scoring = scoring.AsyncScoringResourceWithStreamingResponse(client.scoring)
        self.synthetic_data_generation = (
            synthetic_data_generation.AsyncSyntheticDataGenerationResourceWithStreamingResponse(
                client.synthetic_data_generation
            )
        )
        self.version = version.AsyncVersionResourceWithStreamingResponse(client.version)


Client = LlamaStackClient

AsyncClient = AsyncLlamaStackClient
