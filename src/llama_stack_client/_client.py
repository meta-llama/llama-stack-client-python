# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations
import json

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import (
    memory,
    models,
    routes,
    safety,
    inspect,
    scoring,
    shields,
    datasets,
    datasetio,
    inference,
    providers,
    telemetry,
    eval_tasks,
    memory_banks,
    batch_inference,
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
from .resources.agents import agents
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
    agents: agents.AgentsResource
    batch_inference: batch_inference.BatchInferenceResource
    datasets: datasets.DatasetsResource
    eval: eval.EvalResource
    inspect: inspect.InspectResource
    inference: inference.InferenceResource
    memory: memory.MemoryResource
    memory_banks: memory_banks.MemoryBanksResource
    models: models.ModelsResource
    post_training: post_training.PostTrainingResource
    providers: providers.ProvidersResource
    routes: routes.RoutesResource
    safety: safety.SafetyResource
    shields: shields.ShieldsResource
    synthetic_data_generation: synthetic_data_generation.SyntheticDataGenerationResource
    telemetry: telemetry.TelemetryResource
    datasetio: datasetio.DatasetioResource
    scoring: scoring.ScoringResource
    scoring_functions: scoring_functions.ScoringFunctionsResource
    eval_tasks: eval_tasks.EvalTasksResource
    with_raw_response: LlamaStackClientWithRawResponse
    with_streaming_response: LlamaStackClientWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
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
        provider_data: Mapping[str, Any] | None = None,
    ) -> None:
        """Construct a new synchronous llama-stack-client client instance."""
        if base_url is None:
            base_url = os.environ.get("LLAMA_STACK_CLIENT_BASE_URL")
        if base_url is None:
            base_url = f"http://any-hosted-llama-stack.com"

        if provider_data is not None:
            if default_headers is None:
                default_headers = {}
            default_headers["X-LlamaStack-ProviderData"] = json.dumps(provider_data)
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

        self.agents = agents.AgentsResource(self)
        self.batch_inference = batch_inference.BatchInferenceResource(self)
        self.datasets = datasets.DatasetsResource(self)
        self.eval = eval.EvalResource(self)
        self.inspect = inspect.InspectResource(self)
        self.inference = inference.InferenceResource(self)
        self.memory = memory.MemoryResource(self)
        self.memory_banks = memory_banks.MemoryBanksResource(self)
        self.models = models.ModelsResource(self)
        self.post_training = post_training.PostTrainingResource(self)
        self.providers = providers.ProvidersResource(self)
        self.routes = routes.RoutesResource(self)
        self.safety = safety.SafetyResource(self)
        self.shields = shields.ShieldsResource(self)
        self.synthetic_data_generation = synthetic_data_generation.SyntheticDataGenerationResource(self)
        self.telemetry = telemetry.TelemetryResource(self)
        self.datasetio = datasetio.DatasetioResource(self)
        self.scoring = scoring.ScoringResource(self)
        self.scoring_functions = scoring_functions.ScoringFunctionsResource(self)
        self.eval_tasks = eval_tasks.EvalTasksResource(self)
        self.with_raw_response = LlamaStackClientWithRawResponse(self)
        self.with_streaming_response = LlamaStackClientWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
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
    agents: agents.AsyncAgentsResource
    batch_inference: batch_inference.AsyncBatchInferenceResource
    datasets: datasets.AsyncDatasetsResource
    eval: eval.AsyncEvalResource
    inspect: inspect.AsyncInspectResource
    inference: inference.AsyncInferenceResource
    memory: memory.AsyncMemoryResource
    memory_banks: memory_banks.AsyncMemoryBanksResource
    models: models.AsyncModelsResource
    post_training: post_training.AsyncPostTrainingResource
    providers: providers.AsyncProvidersResource
    routes: routes.AsyncRoutesResource
    safety: safety.AsyncSafetyResource
    shields: shields.AsyncShieldsResource
    synthetic_data_generation: synthetic_data_generation.AsyncSyntheticDataGenerationResource
    telemetry: telemetry.AsyncTelemetryResource
    datasetio: datasetio.AsyncDatasetioResource
    scoring: scoring.AsyncScoringResource
    scoring_functions: scoring_functions.AsyncScoringFunctionsResource
    eval_tasks: eval_tasks.AsyncEvalTasksResource
    with_raw_response: AsyncLlamaStackClientWithRawResponse
    with_streaming_response: AsyncLlamaStackClientWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
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
        provider_data: Mapping[str, Any] | None = None,
    ) -> None:
        """Construct a new async llama-stack-client client instance."""
        if base_url is None:
            base_url = os.environ.get("LLAMA_STACK_CLIENT_BASE_URL")
        if base_url is None:
            base_url = f"http://any-hosted-llama-stack.com"

        if provider_data is not None:
            if default_headers is None:
                default_headers = {}
            default_headers["X-LlamaStack-ProviderData"] = json.dumps(provider_data)
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

        self.agents = agents.AsyncAgentsResource(self)
        self.batch_inference = batch_inference.AsyncBatchInferenceResource(self)
        self.datasets = datasets.AsyncDatasetsResource(self)
        self.eval = eval.AsyncEvalResource(self)
        self.inspect = inspect.AsyncInspectResource(self)
        self.inference = inference.AsyncInferenceResource(self)
        self.memory = memory.AsyncMemoryResource(self)
        self.memory_banks = memory_banks.AsyncMemoryBanksResource(self)
        self.models = models.AsyncModelsResource(self)
        self.post_training = post_training.AsyncPostTrainingResource(self)
        self.providers = providers.AsyncProvidersResource(self)
        self.routes = routes.AsyncRoutesResource(self)
        self.safety = safety.AsyncSafetyResource(self)
        self.shields = shields.AsyncShieldsResource(self)
        self.synthetic_data_generation = synthetic_data_generation.AsyncSyntheticDataGenerationResource(self)
        self.telemetry = telemetry.AsyncTelemetryResource(self)
        self.datasetio = datasetio.AsyncDatasetioResource(self)
        self.scoring = scoring.AsyncScoringResource(self)
        self.scoring_functions = scoring_functions.AsyncScoringFunctionsResource(self)
        self.eval_tasks = eval_tasks.AsyncEvalTasksResource(self)
        self.with_raw_response = AsyncLlamaStackClientWithRawResponse(self)
        self.with_streaming_response = AsyncLlamaStackClientWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
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
        self.agents = agents.AgentsResourceWithRawResponse(client.agents)
        self.batch_inference = batch_inference.BatchInferenceResourceWithRawResponse(client.batch_inference)
        self.datasets = datasets.DatasetsResourceWithRawResponse(client.datasets)
        self.eval = eval.EvalResourceWithRawResponse(client.eval)
        self.inspect = inspect.InspectResourceWithRawResponse(client.inspect)
        self.inference = inference.InferenceResourceWithRawResponse(client.inference)
        self.memory = memory.MemoryResourceWithRawResponse(client.memory)
        self.memory_banks = memory_banks.MemoryBanksResourceWithRawResponse(client.memory_banks)
        self.models = models.ModelsResourceWithRawResponse(client.models)
        self.post_training = post_training.PostTrainingResourceWithRawResponse(client.post_training)
        self.providers = providers.ProvidersResourceWithRawResponse(client.providers)
        self.routes = routes.RoutesResourceWithRawResponse(client.routes)
        self.safety = safety.SafetyResourceWithRawResponse(client.safety)
        self.shields = shields.ShieldsResourceWithRawResponse(client.shields)
        self.synthetic_data_generation = synthetic_data_generation.SyntheticDataGenerationResourceWithRawResponse(
            client.synthetic_data_generation
        )
        self.telemetry = telemetry.TelemetryResourceWithRawResponse(client.telemetry)
        self.datasetio = datasetio.DatasetioResourceWithRawResponse(client.datasetio)
        self.scoring = scoring.ScoringResourceWithRawResponse(client.scoring)
        self.scoring_functions = scoring_functions.ScoringFunctionsResourceWithRawResponse(client.scoring_functions)
        self.eval_tasks = eval_tasks.EvalTasksResourceWithRawResponse(client.eval_tasks)


class AsyncLlamaStackClientWithRawResponse:
    def __init__(self, client: AsyncLlamaStackClient) -> None:
        self.agents = agents.AsyncAgentsResourceWithRawResponse(client.agents)
        self.batch_inference = batch_inference.AsyncBatchInferenceResourceWithRawResponse(client.batch_inference)
        self.datasets = datasets.AsyncDatasetsResourceWithRawResponse(client.datasets)
        self.eval = eval.AsyncEvalResourceWithRawResponse(client.eval)
        self.inspect = inspect.AsyncInspectResourceWithRawResponse(client.inspect)
        self.inference = inference.AsyncInferenceResourceWithRawResponse(client.inference)
        self.memory = memory.AsyncMemoryResourceWithRawResponse(client.memory)
        self.memory_banks = memory_banks.AsyncMemoryBanksResourceWithRawResponse(client.memory_banks)
        self.models = models.AsyncModelsResourceWithRawResponse(client.models)
        self.post_training = post_training.AsyncPostTrainingResourceWithRawResponse(client.post_training)
        self.providers = providers.AsyncProvidersResourceWithRawResponse(client.providers)
        self.routes = routes.AsyncRoutesResourceWithRawResponse(client.routes)
        self.safety = safety.AsyncSafetyResourceWithRawResponse(client.safety)
        self.shields = shields.AsyncShieldsResourceWithRawResponse(client.shields)
        self.synthetic_data_generation = synthetic_data_generation.AsyncSyntheticDataGenerationResourceWithRawResponse(
            client.synthetic_data_generation
        )
        self.telemetry = telemetry.AsyncTelemetryResourceWithRawResponse(client.telemetry)
        self.datasetio = datasetio.AsyncDatasetioResourceWithRawResponse(client.datasetio)
        self.scoring = scoring.AsyncScoringResourceWithRawResponse(client.scoring)
        self.scoring_functions = scoring_functions.AsyncScoringFunctionsResourceWithRawResponse(
            client.scoring_functions
        )
        self.eval_tasks = eval_tasks.AsyncEvalTasksResourceWithRawResponse(client.eval_tasks)


class LlamaStackClientWithStreamedResponse:
    def __init__(self, client: LlamaStackClient) -> None:
        self.agents = agents.AgentsResourceWithStreamingResponse(client.agents)
        self.batch_inference = batch_inference.BatchInferenceResourceWithStreamingResponse(client.batch_inference)
        self.datasets = datasets.DatasetsResourceWithStreamingResponse(client.datasets)
        self.eval = eval.EvalResourceWithStreamingResponse(client.eval)
        self.inspect = inspect.InspectResourceWithStreamingResponse(client.inspect)
        self.inference = inference.InferenceResourceWithStreamingResponse(client.inference)
        self.memory = memory.MemoryResourceWithStreamingResponse(client.memory)
        self.memory_banks = memory_banks.MemoryBanksResourceWithStreamingResponse(client.memory_banks)
        self.models = models.ModelsResourceWithStreamingResponse(client.models)
        self.post_training = post_training.PostTrainingResourceWithStreamingResponse(client.post_training)
        self.providers = providers.ProvidersResourceWithStreamingResponse(client.providers)
        self.routes = routes.RoutesResourceWithStreamingResponse(client.routes)
        self.safety = safety.SafetyResourceWithStreamingResponse(client.safety)
        self.shields = shields.ShieldsResourceWithStreamingResponse(client.shields)
        self.synthetic_data_generation = synthetic_data_generation.SyntheticDataGenerationResourceWithStreamingResponse(
            client.synthetic_data_generation
        )
        self.telemetry = telemetry.TelemetryResourceWithStreamingResponse(client.telemetry)
        self.datasetio = datasetio.DatasetioResourceWithStreamingResponse(client.datasetio)
        self.scoring = scoring.ScoringResourceWithStreamingResponse(client.scoring)
        self.scoring_functions = scoring_functions.ScoringFunctionsResourceWithStreamingResponse(
            client.scoring_functions
        )
        self.eval_tasks = eval_tasks.EvalTasksResourceWithStreamingResponse(client.eval_tasks)


class AsyncLlamaStackClientWithStreamedResponse:
    def __init__(self, client: AsyncLlamaStackClient) -> None:
        self.agents = agents.AsyncAgentsResourceWithStreamingResponse(client.agents)
        self.batch_inference = batch_inference.AsyncBatchInferenceResourceWithStreamingResponse(client.batch_inference)
        self.datasets = datasets.AsyncDatasetsResourceWithStreamingResponse(client.datasets)
        self.eval = eval.AsyncEvalResourceWithStreamingResponse(client.eval)
        self.inspect = inspect.AsyncInspectResourceWithStreamingResponse(client.inspect)
        self.inference = inference.AsyncInferenceResourceWithStreamingResponse(client.inference)
        self.memory = memory.AsyncMemoryResourceWithStreamingResponse(client.memory)
        self.memory_banks = memory_banks.AsyncMemoryBanksResourceWithStreamingResponse(client.memory_banks)
        self.models = models.AsyncModelsResourceWithStreamingResponse(client.models)
        self.post_training = post_training.AsyncPostTrainingResourceWithStreamingResponse(client.post_training)
        self.providers = providers.AsyncProvidersResourceWithStreamingResponse(client.providers)
        self.routes = routes.AsyncRoutesResourceWithStreamingResponse(client.routes)
        self.safety = safety.AsyncSafetyResourceWithStreamingResponse(client.safety)
        self.shields = shields.AsyncShieldsResourceWithStreamingResponse(client.shields)
        self.synthetic_data_generation = (
            synthetic_data_generation.AsyncSyntheticDataGenerationResourceWithStreamingResponse(
                client.synthetic_data_generation
            )
        )
        self.telemetry = telemetry.AsyncTelemetryResourceWithStreamingResponse(client.telemetry)
        self.datasetio = datasetio.AsyncDatasetioResourceWithStreamingResponse(client.datasetio)
        self.scoring = scoring.AsyncScoringResourceWithStreamingResponse(client.scoring)
        self.scoring_functions = scoring_functions.AsyncScoringFunctionsResourceWithStreamingResponse(
            client.scoring_functions
        )
        self.eval_tasks = eval_tasks.AsyncEvalTasksResourceWithStreamingResponse(client.eval_tasks)


Client = LlamaStackClient

AsyncClient = AsyncLlamaStackClient
