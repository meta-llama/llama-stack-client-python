# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
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
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "LlamaStackClient",
    "AsyncLlamaStackClient",
    "Client",
    "AsyncClient",
]


class LlamaStackClient(SyncAPIClient):
    agents: resources.AgentsResource
    batch_inferences: resources.BatchInferencesResource
    inspect: resources.InspectResource
    inference: resources.InferenceResource
    memory: resources.MemoryResource
    memory_banks: resources.MemoryBanksResource
    datasets: resources.DatasetsResource
    models: resources.ModelsResource
    post_training: resources.PostTrainingResource
    providers: resources.ProvidersResource
    routes: resources.RoutesResource
    safety: resources.SafetyResource
    shields: resources.ShieldsResource
    synthetic_data_generation: resources.SyntheticDataGenerationResource
    telemetry: resources.TelemetryResource
    datasetio: resources.DatasetioResource
    scoring: resources.ScoringResource
    scoring_functions: resources.ScoringFunctionsResource
    eval: resources.EvalResource
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
    ) -> None:
        """Construct a new synchronous llama-stack-client client instance."""
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

        self.agents = resources.AgentsResource(self)
        self.batch_inferences = resources.BatchInferencesResource(self)
        self.inspect = resources.InspectResource(self)
        self.inference = resources.InferenceResource(self)
        self.memory = resources.MemoryResource(self)
        self.memory_banks = resources.MemoryBanksResource(self)
        self.datasets = resources.DatasetsResource(self)
        self.models = resources.ModelsResource(self)
        self.post_training = resources.PostTrainingResource(self)
        self.providers = resources.ProvidersResource(self)
        self.routes = resources.RoutesResource(self)
        self.safety = resources.SafetyResource(self)
        self.shields = resources.ShieldsResource(self)
        self.synthetic_data_generation = resources.SyntheticDataGenerationResource(self)
        self.telemetry = resources.TelemetryResource(self)
        self.datasetio = resources.DatasetioResource(self)
        self.scoring = resources.ScoringResource(self)
        self.scoring_functions = resources.ScoringFunctionsResource(self)
        self.eval = resources.EvalResource(self)
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
    agents: resources.AsyncAgentsResource
    batch_inferences: resources.AsyncBatchInferencesResource
    inspect: resources.AsyncInspectResource
    inference: resources.AsyncInferenceResource
    memory: resources.AsyncMemoryResource
    memory_banks: resources.AsyncMemoryBanksResource
    datasets: resources.AsyncDatasetsResource
    models: resources.AsyncModelsResource
    post_training: resources.AsyncPostTrainingResource
    providers: resources.AsyncProvidersResource
    routes: resources.AsyncRoutesResource
    safety: resources.AsyncSafetyResource
    shields: resources.AsyncShieldsResource
    synthetic_data_generation: resources.AsyncSyntheticDataGenerationResource
    telemetry: resources.AsyncTelemetryResource
    datasetio: resources.AsyncDatasetioResource
    scoring: resources.AsyncScoringResource
    scoring_functions: resources.AsyncScoringFunctionsResource
    eval: resources.AsyncEvalResource
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
    ) -> None:
        """Construct a new async llama-stack-client client instance."""
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

        self.agents = resources.AsyncAgentsResource(self)
        self.batch_inferences = resources.AsyncBatchInferencesResource(self)
        self.inspect = resources.AsyncInspectResource(self)
        self.inference = resources.AsyncInferenceResource(self)
        self.memory = resources.AsyncMemoryResource(self)
        self.memory_banks = resources.AsyncMemoryBanksResource(self)
        self.datasets = resources.AsyncDatasetsResource(self)
        self.models = resources.AsyncModelsResource(self)
        self.post_training = resources.AsyncPostTrainingResource(self)
        self.providers = resources.AsyncProvidersResource(self)
        self.routes = resources.AsyncRoutesResource(self)
        self.safety = resources.AsyncSafetyResource(self)
        self.shields = resources.AsyncShieldsResource(self)
        self.synthetic_data_generation = resources.AsyncSyntheticDataGenerationResource(self)
        self.telemetry = resources.AsyncTelemetryResource(self)
        self.datasetio = resources.AsyncDatasetioResource(self)
        self.scoring = resources.AsyncScoringResource(self)
        self.scoring_functions = resources.AsyncScoringFunctionsResource(self)
        self.eval = resources.AsyncEvalResource(self)
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
        self.agents = resources.AgentsResourceWithRawResponse(client.agents)
        self.batch_inferences = resources.BatchInferencesResourceWithRawResponse(client.batch_inferences)
        self.inspect = resources.InspectResourceWithRawResponse(client.inspect)
        self.inference = resources.InferenceResourceWithRawResponse(client.inference)
        self.memory = resources.MemoryResourceWithRawResponse(client.memory)
        self.memory_banks = resources.MemoryBanksResourceWithRawResponse(client.memory_banks)
        self.datasets = resources.DatasetsResourceWithRawResponse(client.datasets)
        self.models = resources.ModelsResourceWithRawResponse(client.models)
        self.post_training = resources.PostTrainingResourceWithRawResponse(client.post_training)
        self.providers = resources.ProvidersResourceWithRawResponse(client.providers)
        self.routes = resources.RoutesResourceWithRawResponse(client.routes)
        self.safety = resources.SafetyResourceWithRawResponse(client.safety)
        self.shields = resources.ShieldsResourceWithRawResponse(client.shields)
        self.synthetic_data_generation = resources.SyntheticDataGenerationResourceWithRawResponse(
            client.synthetic_data_generation
        )
        self.telemetry = resources.TelemetryResourceWithRawResponse(client.telemetry)
        self.datasetio = resources.DatasetioResourceWithRawResponse(client.datasetio)
        self.scoring = resources.ScoringResourceWithRawResponse(client.scoring)
        self.scoring_functions = resources.ScoringFunctionsResourceWithRawResponse(client.scoring_functions)
        self.eval = resources.EvalResourceWithRawResponse(client.eval)


class AsyncLlamaStackClientWithRawResponse:
    def __init__(self, client: AsyncLlamaStackClient) -> None:
        self.agents = resources.AsyncAgentsResourceWithRawResponse(client.agents)
        self.batch_inferences = resources.AsyncBatchInferencesResourceWithRawResponse(client.batch_inferences)
        self.inspect = resources.AsyncInspectResourceWithRawResponse(client.inspect)
        self.inference = resources.AsyncInferenceResourceWithRawResponse(client.inference)
        self.memory = resources.AsyncMemoryResourceWithRawResponse(client.memory)
        self.memory_banks = resources.AsyncMemoryBanksResourceWithRawResponse(client.memory_banks)
        self.datasets = resources.AsyncDatasetsResourceWithRawResponse(client.datasets)
        self.models = resources.AsyncModelsResourceWithRawResponse(client.models)
        self.post_training = resources.AsyncPostTrainingResourceWithRawResponse(client.post_training)
        self.providers = resources.AsyncProvidersResourceWithRawResponse(client.providers)
        self.routes = resources.AsyncRoutesResourceWithRawResponse(client.routes)
        self.safety = resources.AsyncSafetyResourceWithRawResponse(client.safety)
        self.shields = resources.AsyncShieldsResourceWithRawResponse(client.shields)
        self.synthetic_data_generation = resources.AsyncSyntheticDataGenerationResourceWithRawResponse(
            client.synthetic_data_generation
        )
        self.telemetry = resources.AsyncTelemetryResourceWithRawResponse(client.telemetry)
        self.datasetio = resources.AsyncDatasetioResourceWithRawResponse(client.datasetio)
        self.scoring = resources.AsyncScoringResourceWithRawResponse(client.scoring)
        self.scoring_functions = resources.AsyncScoringFunctionsResourceWithRawResponse(client.scoring_functions)
        self.eval = resources.AsyncEvalResourceWithRawResponse(client.eval)


class LlamaStackClientWithStreamedResponse:
    def __init__(self, client: LlamaStackClient) -> None:
        self.agents = resources.AgentsResourceWithStreamingResponse(client.agents)
        self.batch_inferences = resources.BatchInferencesResourceWithStreamingResponse(client.batch_inferences)
        self.inspect = resources.InspectResourceWithStreamingResponse(client.inspect)
        self.inference = resources.InferenceResourceWithStreamingResponse(client.inference)
        self.memory = resources.MemoryResourceWithStreamingResponse(client.memory)
        self.memory_banks = resources.MemoryBanksResourceWithStreamingResponse(client.memory_banks)
        self.datasets = resources.DatasetsResourceWithStreamingResponse(client.datasets)
        self.models = resources.ModelsResourceWithStreamingResponse(client.models)
        self.post_training = resources.PostTrainingResourceWithStreamingResponse(client.post_training)
        self.providers = resources.ProvidersResourceWithStreamingResponse(client.providers)
        self.routes = resources.RoutesResourceWithStreamingResponse(client.routes)
        self.safety = resources.SafetyResourceWithStreamingResponse(client.safety)
        self.shields = resources.ShieldsResourceWithStreamingResponse(client.shields)
        self.synthetic_data_generation = resources.SyntheticDataGenerationResourceWithStreamingResponse(
            client.synthetic_data_generation
        )
        self.telemetry = resources.TelemetryResourceWithStreamingResponse(client.telemetry)
        self.datasetio = resources.DatasetioResourceWithStreamingResponse(client.datasetio)
        self.scoring = resources.ScoringResourceWithStreamingResponse(client.scoring)
        self.scoring_functions = resources.ScoringFunctionsResourceWithStreamingResponse(client.scoring_functions)
        self.eval = resources.EvalResourceWithStreamingResponse(client.eval)


class AsyncLlamaStackClientWithStreamedResponse:
    def __init__(self, client: AsyncLlamaStackClient) -> None:
        self.agents = resources.AsyncAgentsResourceWithStreamingResponse(client.agents)
        self.batch_inferences = resources.AsyncBatchInferencesResourceWithStreamingResponse(client.batch_inferences)
        self.inspect = resources.AsyncInspectResourceWithStreamingResponse(client.inspect)
        self.inference = resources.AsyncInferenceResourceWithStreamingResponse(client.inference)
        self.memory = resources.AsyncMemoryResourceWithStreamingResponse(client.memory)
        self.memory_banks = resources.AsyncMemoryBanksResourceWithStreamingResponse(client.memory_banks)
        self.datasets = resources.AsyncDatasetsResourceWithStreamingResponse(client.datasets)
        self.models = resources.AsyncModelsResourceWithStreamingResponse(client.models)
        self.post_training = resources.AsyncPostTrainingResourceWithStreamingResponse(client.post_training)
        self.providers = resources.AsyncProvidersResourceWithStreamingResponse(client.providers)
        self.routes = resources.AsyncRoutesResourceWithStreamingResponse(client.routes)
        self.safety = resources.AsyncSafetyResourceWithStreamingResponse(client.safety)
        self.shields = resources.AsyncShieldsResourceWithStreamingResponse(client.shields)
        self.synthetic_data_generation = resources.AsyncSyntheticDataGenerationResourceWithStreamingResponse(
            client.synthetic_data_generation
        )
        self.telemetry = resources.AsyncTelemetryResourceWithStreamingResponse(client.telemetry)
        self.datasetio = resources.AsyncDatasetioResourceWithStreamingResponse(client.datasetio)
        self.scoring = resources.AsyncScoringResourceWithStreamingResponse(client.scoring)
        self.scoring_functions = resources.AsyncScoringFunctionsResourceWithStreamingResponse(client.scoring_functions)
        self.eval = resources.AsyncEvalResourceWithStreamingResponse(client.eval)


Client = LlamaStackClient

AsyncClient = AsyncLlamaStackClient
