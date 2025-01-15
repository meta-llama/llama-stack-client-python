# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types.agents import Turn, TurnCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTurn:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_create_overload_1(self, client: LlamaStackClient) -> None:
        turn = client.agents.turn.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        )
        assert_matches_type(TurnCreateResponse, turn, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: LlamaStackClient) -> None:
        turn = client.agents.turn.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                }
            ],
            documents=[
                {
                    "content": "string",
                    "mime_type": "mime_type",
                }
            ],
            stream=False,
            toolgroups=["string"],
            x_llama_stack_client_version="X-LlamaStack-Client-Version",
            x_llama_stack_provider_data="X-LlamaStack-Provider-Data",
        )
        assert_matches_type(TurnCreateResponse, turn, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_create_overload_1(self, client: LlamaStackClient) -> None:
        response = client.agents.turn.with_raw_response.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        turn = response.parse()
        assert_matches_type(TurnCreateResponse, turn, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_create_overload_1(self, client: LlamaStackClient) -> None:
        with client.agents.turn.with_streaming_response.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            turn = response.parse()
            assert_matches_type(TurnCreateResponse, turn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_path_params_create_overload_1(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.turn.with_raw_response.create(
                session_id="session_id",
                agent_id="",
                messages=[
                    {
                        "content": "string",
                        "role": "user",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.agents.turn.with_raw_response.create(
                session_id="",
                agent_id="agent_id",
                messages=[
                    {
                        "content": "string",
                        "role": "user",
                    }
                ],
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_create_overload_2(self, client: LlamaStackClient) -> None:
        turn_stream = client.agents.turn.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            stream=True,
        )
        turn_stream.response.close()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: LlamaStackClient) -> None:
        turn_stream = client.agents.turn.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                }
            ],
            stream=True,
            documents=[
                {
                    "content": "string",
                    "mime_type": "mime_type",
                }
            ],
            toolgroups=["string"],
            x_llama_stack_client_version="X-LlamaStack-Client-Version",
            x_llama_stack_provider_data="X-LlamaStack-Provider-Data",
        )
        turn_stream.response.close()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_create_overload_2(self, client: LlamaStackClient) -> None:
        response = client.agents.turn.with_raw_response.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_create_overload_2(self, client: LlamaStackClient) -> None:
        with client.agents.turn.with_streaming_response.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_path_params_create_overload_2(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.turn.with_raw_response.create(
                session_id="session_id",
                agent_id="",
                messages=[
                    {
                        "content": "string",
                        "role": "user",
                    }
                ],
                stream=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.agents.turn.with_raw_response.create(
                session_id="",
                agent_id="agent_id",
                messages=[
                    {
                        "content": "string",
                        "role": "user",
                    }
                ],
                stream=True,
            )

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        turn = client.agents.turn.retrieve(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
        )
        assert_matches_type(Turn, turn, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: LlamaStackClient) -> None:
        turn = client.agents.turn.retrieve(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
            x_llama_stack_client_version="X-LlamaStack-Client-Version",
            x_llama_stack_provider_data="X-LlamaStack-Provider-Data",
        )
        assert_matches_type(Turn, turn, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.agents.turn.with_raw_response.retrieve(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        turn = response.parse()
        assert_matches_type(Turn, turn, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.agents.turn.with_streaming_response.retrieve(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            turn = response.parse()
            assert_matches_type(Turn, turn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.turn.with_raw_response.retrieve(
                turn_id="turn_id",
                agent_id="",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.agents.turn.with_raw_response.retrieve(
                turn_id="turn_id",
                agent_id="agent_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `turn_id` but received ''"):
            client.agents.turn.with_raw_response.retrieve(
                turn_id="",
                agent_id="agent_id",
                session_id="session_id",
            )


class TestAsyncTurn:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        turn = await async_client.agents.turn.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        )
        assert_matches_type(TurnCreateResponse, turn, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        turn = await async_client.agents.turn.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                }
            ],
            documents=[
                {
                    "content": "string",
                    "mime_type": "mime_type",
                }
            ],
            stream=False,
            toolgroups=["string"],
            x_llama_stack_client_version="X-LlamaStack-Client-Version",
            x_llama_stack_provider_data="X-LlamaStack-Provider-Data",
        )
        assert_matches_type(TurnCreateResponse, turn, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.agents.turn.with_raw_response.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        turn = await response.parse()
        assert_matches_type(TurnCreateResponse, turn, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.agents.turn.with_streaming_response.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            turn = await response.parse()
            assert_matches_type(TurnCreateResponse, turn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.turn.with_raw_response.create(
                session_id="session_id",
                agent_id="",
                messages=[
                    {
                        "content": "string",
                        "role": "user",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.agents.turn.with_raw_response.create(
                session_id="",
                agent_id="agent_id",
                messages=[
                    {
                        "content": "string",
                        "role": "user",
                    }
                ],
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        turn_stream = await async_client.agents.turn.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            stream=True,
        )
        await turn_stream.response.aclose()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        turn_stream = await async_client.agents.turn.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                }
            ],
            stream=True,
            documents=[
                {
                    "content": "string",
                    "mime_type": "mime_type",
                }
            ],
            toolgroups=["string"],
            x_llama_stack_client_version="X-LlamaStack-Client-Version",
            x_llama_stack_provider_data="X-LlamaStack-Provider-Data",
        )
        await turn_stream.response.aclose()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.agents.turn.with_raw_response.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.agents.turn.with_streaming_response.create(
            session_id="session_id",
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.turn.with_raw_response.create(
                session_id="session_id",
                agent_id="",
                messages=[
                    {
                        "content": "string",
                        "role": "user",
                    }
                ],
                stream=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.agents.turn.with_raw_response.create(
                session_id="",
                agent_id="agent_id",
                messages=[
                    {
                        "content": "string",
                        "role": "user",
                    }
                ],
                stream=True,
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        turn = await async_client.agents.turn.retrieve(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
        )
        assert_matches_type(Turn, turn, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        turn = await async_client.agents.turn.retrieve(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
            x_llama_stack_client_version="X-LlamaStack-Client-Version",
            x_llama_stack_provider_data="X-LlamaStack-Provider-Data",
        )
        assert_matches_type(Turn, turn, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.agents.turn.with_raw_response.retrieve(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        turn = await response.parse()
        assert_matches_type(Turn, turn, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.agents.turn.with_streaming_response.retrieve(
            turn_id="turn_id",
            agent_id="agent_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            turn = await response.parse()
            assert_matches_type(Turn, turn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.turn.with_raw_response.retrieve(
                turn_id="turn_id",
                agent_id="",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.agents.turn.with_raw_response.retrieve(
                turn_id="turn_id",
                agent_id="agent_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `turn_id` but received ''"):
            await async_client.agents.turn.with_raw_response.retrieve(
                turn_id="",
                agent_id="agent_id",
                session_id="session_id",
            )
