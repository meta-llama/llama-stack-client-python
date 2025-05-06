# Datasetio

Types:

```python
from llama_stack_client.types import DatasetioIterateRowsResponse
```

Methods:

- <code title="post /v1/datasetio/append-rows/{dataset_id}">client.datasetio.<a href="./src/llama_stack_client/resources/datasetio.py">append_rows</a>(dataset_id, \*\*<a href="src/llama_stack_client/types/datasetio_append_rows_params.py">params</a>) -> None</code>
- <code title="get /v1/datasetio/iterrows/{dataset_id}">client.datasetio.<a href="./src/llama_stack_client/resources/datasetio.py">iterate_rows</a>(dataset_id, \*\*<a href="src/llama_stack_client/types/datasetio_iterate_rows_params.py">params</a>) -> <a href="./src/llama_stack_client/types/datasetio_iterate_rows_response.py">DatasetioIterateRowsResponse</a></code>

# Inference

Types:

```python
from llama_stack_client.types import (
    ChatCompletionResponse,
    CompletionMessage,
    CompletionResponse,
    InterleavedContent,
    InterleavedContentItem,
    Message,
    MetricInResponse,
    ResponseFormat,
    SamplingParams,
    SystemMessage,
    TokenLogProbs,
    ToolCall,
    ToolConfig,
    ToolDefinition,
    InferenceBatchChatCompletionResponse,
    InferenceBatchCompletionResponse,
    InferenceEmbeddingsResponse,
)
```

Methods:

- <code title="post /v1/inference/batch-chat-completion">client.inference.<a href="./src/llama_stack_client/resources/inference.py">batch_chat_completion</a>(\*\*<a href="src/llama_stack_client/types/inference_batch_chat_completion_params.py">params</a>) -> <a href="./src/llama_stack_client/types/inference_batch_chat_completion_response.py">InferenceBatchChatCompletionResponse</a></code>
- <code title="post /v1/inference/batch-completion">client.inference.<a href="./src/llama_stack_client/resources/inference.py">batch_completion</a>(\*\*<a href="src/llama_stack_client/types/inference_batch_completion_params.py">params</a>) -> <a href="./src/llama_stack_client/types/inference_batch_completion_response.py">InferenceBatchCompletionResponse</a></code>
- <code title="post /v1/inference/chat-completion">client.inference.<a href="./src/llama_stack_client/resources/inference.py">chat_completion</a>(\*\*<a href="src/llama_stack_client/types/inference_chat_completion_params.py">params</a>) -> <a href="./src/llama_stack_client/types/chat_completion_response.py">ChatCompletionResponse</a></code>
- <code title="post /v1/inference/completion">client.inference.<a href="./src/llama_stack_client/resources/inference.py">completion</a>(\*\*<a href="src/llama_stack_client/types/inference_completion_params.py">params</a>) -> <a href="./src/llama_stack_client/types/completion_response.py">CompletionResponse</a></code>
- <code title="post /v1/inference/embeddings">client.inference.<a href="./src/llama_stack_client/resources/inference.py">embeddings</a>(\*\*<a href="src/llama_stack_client/types/inference_embeddings_params.py">params</a>) -> <a href="./src/llama_stack_client/types/inference_embeddings_response.py">InferenceEmbeddingsResponse</a></code>

# PostTraining

Types:

```python
from llama_stack_client.types import PostTrainingJob, TrainingConfig, PostTrainingListJobsResponse
```

Methods:

- <code title="post /v1/post-training/supervised-fine-tune">client.post_training.<a href="./src/llama_stack_client/resources/post_training/post_training.py">fine_tune_supervised</a>(\*\*<a href="src/llama_stack_client/types/post_training_fine_tune_supervised_params.py">params</a>) -> <a href="./src/llama_stack_client/types/post_training_job.py">PostTrainingJob</a></code>
- <code title="get /v1/post-training/jobs">client.post_training.<a href="./src/llama_stack_client/resources/post_training/post_training.py">list_jobs</a>() -> <a href="./src/llama_stack_client/types/post_training_list_jobs_response.py">PostTrainingListJobsResponse</a></code>
- <code title="post /v1/post-training/preference-optimize">client.post_training.<a href="./src/llama_stack_client/resources/post_training/post_training.py">optimize_preferences</a>(\*\*<a href="src/llama_stack_client/types/post_training_optimize_preferences_params.py">params</a>) -> <a href="./src/llama_stack_client/types/post_training_job.py">PostTrainingJob</a></code>

## Job

Types:

```python
from llama_stack_client.types.post_training import (
    JobRetrieveArtifactsResponse,
    JobRetrieveStatusResponse,
)
```

Methods:

- <code title="post /v1/post-training/job/cancel">client.post_training.job.<a href="./src/llama_stack_client/resources/post_training/job.py">cancel</a>(\*\*<a href="src/llama_stack_client/types/post_training/job_cancel_params.py">params</a>) -> None</code>
- <code title="get /v1/post-training/job/artifacts">client.post_training.job.<a href="./src/llama_stack_client/resources/post_training/job.py">retrieve_artifacts</a>(\*\*<a href="src/llama_stack_client/types/post_training/job_retrieve_artifacts_params.py">params</a>) -> <a href="./src/llama_stack_client/types/post_training/job_retrieve_artifacts_response.py">JobRetrieveArtifactsResponse</a></code>
- <code title="get /v1/post-training/job/status">client.post_training.job.<a href="./src/llama_stack_client/resources/post_training/job.py">retrieve_status</a>(\*\*<a href="src/llama_stack_client/types/post_training/job_retrieve_status_params.py">params</a>) -> <a href="./src/llama_stack_client/types/post_training/job_retrieve_status_response.py">JobRetrieveStatusResponse</a></code>

# Agents

Types:

```python
from llama_stack_client.types import (
    Agent,
    AgentConfig,
    AgentCreateResponse,
    AgentListResponse,
    AgentListSessionsResponse,
)
```

Methods:

- <code title="post /v1/agents">client.agents.<a href="./src/llama_stack_client/resources/agents/agents.py">create</a>(\*\*<a href="src/llama_stack_client/types/agent_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/agent_create_response.py">AgentCreateResponse</a></code>
- <code title="get /v1/agents/{agent_id}">client.agents.<a href="./src/llama_stack_client/resources/agents/agents.py">retrieve</a>(agent_id) -> <a href="./src/llama_stack_client/types/agent.py">Agent</a></code>
- <code title="get /v1/agents">client.agents.<a href="./src/llama_stack_client/resources/agents/agents.py">list</a>() -> <a href="./src/llama_stack_client/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /v1/agents/{agent_id}">client.agents.<a href="./src/llama_stack_client/resources/agents/agents.py">delete</a>(agent_id) -> None</code>
- <code title="get /v1/agents/{agent_id}/sessions">client.agents.<a href="./src/llama_stack_client/resources/agents/agents.py">list_sessions</a>(agent_id) -> <a href="./src/llama_stack_client/types/agent_list_sessions_response.py">AgentListSessionsResponse</a></code>

## Session

Types:

```python
from llama_stack_client.types.agents import Session, SessionCreateResponse
```

Methods:

- <code title="post /v1/agents/{agent_id}/session">client.agents.session.<a href="./src/llama_stack_client/resources/agents/session/session.py">create</a>(agent_id, \*\*<a href="src/llama_stack_client/types/agents/session_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/agents/session_create_response.py">SessionCreateResponse</a></code>
- <code title="get /v1/agents/{agent_id}/session/{session_id}">client.agents.session.<a href="./src/llama_stack_client/resources/agents/session/session.py">retrieve</a>(session_id, \*, agent_id, \*\*<a href="src/llama_stack_client/types/agents/session_retrieve_params.py">params</a>) -> <a href="./src/llama_stack_client/types/agents/session/session.py">Session</a></code>
- <code title="delete /v1/agents/{agent_id}/session/{session_id}">client.agents.session.<a href="./src/llama_stack_client/resources/agents/session/session.py">delete</a>(session_id, \*, agent_id) -> None</code>

### Turn

Types:

```python
from llama_stack_client.types.agents.session import (
    AgentTool,
    InferenceStep,
    MemoryRetrievalStep,
    ShieldCallStep,
    ToolExecutionStep,
    ToolResponse,
    ToolResponseMessage,
    Turn,
    UserMessage,
)
```

Methods:

- <code title="post /v1/agents/{agent_id}/session/{session_id}/turn">client.agents.session.turn.<a href="./src/llama_stack_client/resources/agents/session/turn/turn.py">create</a>(session_id, \*, agent_id, \*\*<a href="src/llama_stack_client/types/agents/session/turn_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/agents/session/turn/turn.py">Turn</a></code>
- <code title="get /v1/agents/{agent_id}/session/{session_id}/turn/{turn_id}">client.agents.session.turn.<a href="./src/llama_stack_client/resources/agents/session/turn/turn.py">retrieve</a>(turn_id, \*, agent_id, session_id) -> <a href="./src/llama_stack_client/types/agents/session/turn/turn.py">Turn</a></code>
- <code title="post /v1/agents/{agent_id}/session/{session_id}/turn/{turn_id}/resume">client.agents.session.turn.<a href="./src/llama_stack_client/resources/agents/session/turn/turn.py">resume</a>(turn_id, \*, agent_id, session_id, \*\*<a href="src/llama_stack_client/types/agents/session/turn_resume_params.py">params</a>) -> <a href="./src/llama_stack_client/types/agents/session/turn/turn.py">Turn</a></code>

#### Step

Types:

```python
from llama_stack_client.types.agents.session.turn import StepRetrieveResponse
```

Methods:

- <code title="get /v1/agents/{agent_id}/session/{session_id}/turn/{turn_id}/step/{step_id}">client.agents.session.turn.step.<a href="./src/llama_stack_client/resources/agents/session/turn/step.py">retrieve</a>(step_id, \*, agent_id, session_id, turn_id) -> <a href="./src/llama_stack_client/types/agents/session/turn/step_retrieve_response.py">StepRetrieveResponse</a></code>

# OpenAI

## V1

Types:

```python
from llama_stack_client.types.openai import (
    ChoiceLogprobs,
    TokenLogProb,
    V1GenerateCompletionResponse,
    V1ListModelsResponse,
)
```

Methods:

- <code title="post /v1/openai/v1/completions">client.openai.v1.<a href="./src/llama_stack_client/resources/openai/v1/v1.py">generate_completion</a>(\*\*<a href="src/llama_stack_client/types/openai/v1_generate_completion_params.py">params</a>) -> <a href="./src/llama_stack_client/types/openai/v1_generate_completion_response.py">V1GenerateCompletionResponse</a></code>
- <code title="get /v1/openai/v1/models">client.openai.v1.<a href="./src/llama_stack_client/resources/openai/v1/v1.py">list_models</a>() -> <a href="./src/llama_stack_client/types/openai/v1_list_models_response.py">V1ListModelsResponse</a></code>

### Responses

Types:

```python
from llama_stack_client.types.openai.v1 import OpenAIResponse
```

Methods:

- <code title="post /v1/openai/v1/responses">client.openai.v1.responses.<a href="./src/llama_stack_client/resources/openai/v1/responses.py">create</a>(\*\*<a href="src/llama_stack_client/types/openai/v1/response_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/openai/v1/openai_response.py">OpenAIResponse</a></code>
- <code title="get /v1/openai/v1/responses/{id}">client.openai.v1.responses.<a href="./src/llama_stack_client/resources/openai/v1/responses.py">retrieve</a>(id) -> <a href="./src/llama_stack_client/types/openai/v1/openai_response.py">OpenAIResponse</a></code>

### Chat

Types:

```python
from llama_stack_client.types.openai.v1 import (
    ChatCompletionContentPart,
    ChatCompletionToolCall,
    MessageParam,
    ChatGenerateCompletionResponse,
)
```

Methods:

- <code title="post /v1/openai/v1/chat/completions">client.openai.v1.chat.<a href="./src/llama_stack_client/resources/openai/v1/chat.py">generate_completion</a>(\*\*<a href="src/llama_stack_client/types/openai/v1/chat_generate_completion_params.py">params</a>) -> <a href="./src/llama_stack_client/types/openai/v1/chat_generate_completion_response.py">ChatGenerateCompletionResponse</a></code>

# Files

Types:

```python
from llama_stack_client.types import File, FileUpload, FileListResponse, FileListInBucketResponse
```

Methods:

- <code title="get /v1/files/{bucket}/{key}">client.files.<a href="./src/llama_stack_client/resources/files/files.py">retrieve</a>(key, \*, bucket) -> <a href="./src/llama_stack_client/types/file.py">File</a></code>
- <code title="get /v1/files">client.files.<a href="./src/llama_stack_client/resources/files/files.py">list</a>(\*\*<a href="src/llama_stack_client/types/file_list_params.py">params</a>) -> <a href="./src/llama_stack_client/types/file_list_response.py">FileListResponse</a></code>
- <code title="delete /v1/files/{bucket}/{key}">client.files.<a href="./src/llama_stack_client/resources/files/files.py">delete</a>(key, \*, bucket) -> None</code>
- <code title="post /v1/files">client.files.<a href="./src/llama_stack_client/resources/files/files.py">create_upload_session</a>(\*\*<a href="src/llama_stack_client/types/file_create_upload_session_params.py">params</a>) -> <a href="./src/llama_stack_client/types/file_upload.py">FileUpload</a></code>
- <code title="get /v1/files/{bucket}">client.files.<a href="./src/llama_stack_client/resources/files/files.py">list_in_bucket</a>(bucket) -> <a href="./src/llama_stack_client/types/file_list_in_bucket_response.py">FileListInBucketResponse</a></code>

## Session

Methods:

- <code title="get /v1/files/session:{upload_id}">client.files.session.<a href="./src/llama_stack_client/resources/files/session.py">retrieve</a>(upload_id) -> <a href="./src/llama_stack_client/types/file_upload.py">FileUpload</a></code>
- <code title="post /v1/files/session:{upload_id}">client.files.session.<a href="./src/llama_stack_client/resources/files/session.py">upload_content</a>(upload_id, \*\*<a href="src/llama_stack_client/types/files/session_upload_content_params.py">params</a>) -> <a href="./src/llama_stack_client/types/file.py">Optional[File]</a></code>

# Eval

## Benchmarks

Types:

```python
from llama_stack_client.types.eval import (
    Benchmark,
    BenchmarkConfig,
    EvaluateResponse,
    BenchmarkListResponse,
)
```

Methods:

- <code title="post /v1/eval/benchmarks">client.eval.benchmarks.<a href="./src/llama_stack_client/resources/eval/benchmarks/benchmarks.py">create</a>(\*\*<a href="src/llama_stack_client/types/eval/benchmark_create_params.py">params</a>) -> None</code>
- <code title="get /v1/eval/benchmarks/{benchmark_id}">client.eval.benchmarks.<a href="./src/llama_stack_client/resources/eval/benchmarks/benchmarks.py">retrieve</a>(benchmark_id) -> <a href="./src/llama_stack_client/types/eval/benchmark.py">Benchmark</a></code>
- <code title="get /v1/eval/benchmarks">client.eval.benchmarks.<a href="./src/llama_stack_client/resources/eval/benchmarks/benchmarks.py">list</a>() -> <a href="./src/llama_stack_client/types/eval/benchmark_list_response.py">BenchmarkListResponse</a></code>
- <code title="post /v1/eval/benchmarks/{benchmark_id}/evaluations">client.eval.benchmarks.<a href="./src/llama_stack_client/resources/eval/benchmarks/benchmarks.py">evaluate</a>(benchmark_id, \*\*<a href="src/llama_stack_client/types/eval/benchmark_evaluate_params.py">params</a>) -> <a href="./src/llama_stack_client/types/eval/evaluate_response.py">EvaluateResponse</a></code>

### Jobs

Types:

```python
from llama_stack_client.types.eval.benchmarks import Job
```

Methods:

- <code title="get /v1/eval/benchmarks/{benchmark_id}/jobs/{job_id}">client.eval.benchmarks.jobs.<a href="./src/llama_stack_client/resources/eval/benchmarks/jobs.py">retrieve</a>(job_id, \*, benchmark_id) -> <a href="./src/llama_stack_client/types/eval/benchmarks/job.py">Job</a></code>
- <code title="delete /v1/eval/benchmarks/{benchmark_id}/jobs/{job_id}">client.eval.benchmarks.jobs.<a href="./src/llama_stack_client/resources/eval/benchmarks/jobs.py">cancel</a>(job_id, \*, benchmark_id) -> None</code>
- <code title="get /v1/eval/benchmarks/{benchmark_id}/jobs/{job_id}/result">client.eval.benchmarks.jobs.<a href="./src/llama_stack_client/resources/eval/benchmarks/jobs.py">result</a>(job_id, \*, benchmark_id) -> <a href="./src/llama_stack_client/types/eval/evaluate_response.py">EvaluateResponse</a></code>
- <code title="post /v1/eval/benchmarks/{benchmark_id}/jobs">client.eval.benchmarks.jobs.<a href="./src/llama_stack_client/resources/eval/benchmarks/jobs.py">run</a>(benchmark_id, \*\*<a href="src/llama_stack_client/types/eval/benchmarks/job_run_params.py">params</a>) -> <a href="./src/llama_stack_client/types/eval/benchmarks/job.py">Job</a></code>

# Datasets

Types:

```python
from llama_stack_client.types import DataSource, Dataset, DatasetListResponse
```

Methods:

- <code title="post /v1/datasets">client.datasets.<a href="./src/llama_stack_client/resources/datasets.py">create</a>(\*\*<a href="src/llama_stack_client/types/dataset_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/dataset.py">Dataset</a></code>
- <code title="get /v1/datasets/{dataset_id}">client.datasets.<a href="./src/llama_stack_client/resources/datasets.py">retrieve</a>(dataset_id) -> <a href="./src/llama_stack_client/types/dataset.py">Dataset</a></code>
- <code title="get /v1/datasets">client.datasets.<a href="./src/llama_stack_client/resources/datasets.py">list</a>() -> <a href="./src/llama_stack_client/types/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="delete /v1/datasets/{dataset_id}">client.datasets.<a href="./src/llama_stack_client/resources/datasets.py">delete</a>(dataset_id) -> None</code>

# Models

Types:

```python
from llama_stack_client.types import Model, ModelType, ModelListResponse
```

Methods:

- <code title="post /v1/models">client.models.<a href="./src/llama_stack_client/resources/models.py">create</a>(\*\*<a href="src/llama_stack_client/types/model_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/model.py">Model</a></code>
- <code title="get /v1/models/{model_id}">client.models.<a href="./src/llama_stack_client/resources/models.py">retrieve</a>(model_id) -> <a href="./src/llama_stack_client/types/model.py">Model</a></code>
- <code title="get /v1/models">client.models.<a href="./src/llama_stack_client/resources/models.py">list</a>() -> <a href="./src/llama_stack_client/types/model_list_response.py">ModelListResponse</a></code>
- <code title="delete /v1/models/{model_id}">client.models.<a href="./src/llama_stack_client/resources/models.py">delete</a>(model_id) -> None</code>

# ScoringFunctions

Types:

```python
from llama_stack_client.types import (
    AggregationFunctionType,
    ParamType,
    ScoringFn,
    ScoringFnParams,
    ScoringFnParamsType,
    ScoringFunctionListResponse,
)
```

Methods:

- <code title="post /v1/scoring-functions">client.scoring_functions.<a href="./src/llama_stack_client/resources/scoring_functions.py">create</a>(\*\*<a href="src/llama_stack_client/types/scoring_function_create_params.py">params</a>) -> None</code>
- <code title="get /v1/scoring-functions/{scoring_fn_id}">client.scoring_functions.<a href="./src/llama_stack_client/resources/scoring_functions.py">retrieve</a>(scoring_fn_id) -> <a href="./src/llama_stack_client/types/scoring_fn.py">ScoringFn</a></code>
- <code title="get /v1/scoring-functions">client.scoring_functions.<a href="./src/llama_stack_client/resources/scoring_functions.py">list</a>() -> <a href="./src/llama_stack_client/types/scoring_function_list_response.py">ScoringFunctionListResponse</a></code>

# Shields

Types:

```python
from llama_stack_client.types import Shield, ShieldListResponse
```

Methods:

- <code title="post /v1/shields">client.shields.<a href="./src/llama_stack_client/resources/shields.py">create</a>(\*\*<a href="src/llama_stack_client/types/shield_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/shield.py">Shield</a></code>
- <code title="get /v1/shields/{identifier}">client.shields.<a href="./src/llama_stack_client/resources/shields.py">retrieve</a>(identifier) -> <a href="./src/llama_stack_client/types/shield.py">Shield</a></code>
- <code title="get /v1/shields">client.shields.<a href="./src/llama_stack_client/resources/shields.py">list</a>() -> <a href="./src/llama_stack_client/types/shield_list_response.py">ShieldListResponse</a></code>

# Telemetry

Types:

```python
from llama_stack_client.types import EventType, StructuredLogType
```

Methods:

- <code title="post /v1/telemetry/events">client.telemetry.<a href="./src/llama_stack_client/resources/telemetry/telemetry.py">create_event</a>(\*\*<a href="src/llama_stack_client/types/telemetry_create_event_params.py">params</a>) -> None</code>

## Traces

Types:

```python
from llama_stack_client.types.telemetry import Span, Trace, TraceCreateResponse
```

Methods:

- <code title="post /v1/telemetry/traces">client.telemetry.traces.<a href="./src/llama_stack_client/resources/telemetry/traces.py">create</a>(\*\*<a href="src/llama_stack_client/types/telemetry/trace_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/telemetry/trace_create_response.py">TraceCreateResponse</a></code>
- <code title="get /v1/telemetry/traces/{trace_id}/spans/{span_id}">client.telemetry.traces.<a href="./src/llama_stack_client/resources/telemetry/traces.py">retrieve_span</a>(span_id, \*, trace_id) -> <a href="./src/llama_stack_client/types/telemetry/span.py">Span</a></code>
- <code title="get /v1/telemetry/traces/{trace_id}">client.telemetry.traces.<a href="./src/llama_stack_client/resources/telemetry/traces.py">retrieve_trace</a>(trace_id) -> <a href="./src/llama_stack_client/types/telemetry/trace.py">Trace</a></code>

## Spans

Types:

```python
from llama_stack_client.types.telemetry import (
    QueryCondition,
    SpanCreateResponse,
    SpanBuildTreeResponse,
)
```

Methods:

- <code title="post /v1/telemetry/spans">client.telemetry.spans.<a href="./src/llama_stack_client/resources/telemetry/spans.py">create</a>(\*\*<a href="src/llama_stack_client/types/telemetry/span_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/telemetry/span_create_response.py">SpanCreateResponse</a></code>
- <code title="post /v1/telemetry/spans/{span_id}/tree">client.telemetry.spans.<a href="./src/llama_stack_client/resources/telemetry/spans.py">build_tree</a>(span_id, \*\*<a href="src/llama_stack_client/types/telemetry/span_build_tree_params.py">params</a>) -> <a href="./src/llama_stack_client/types/telemetry/span_build_tree_response.py">SpanBuildTreeResponse</a></code>
- <code title="post /v1/telemetry/spans/export">client.telemetry.spans.<a href="./src/llama_stack_client/resources/telemetry/spans.py">export</a>(\*\*<a href="src/llama_stack_client/types/telemetry/span_export_params.py">params</a>) -> None</code>

# Tools

Types:

```python
from llama_stack_client.types import Tool, ToolParameter, ToolListResponse
```

Methods:

- <code title="get /v1/tools/{tool_name}">client.tools.<a href="./src/llama_stack_client/resources/tools.py">retrieve</a>(tool_name) -> <a href="./src/llama_stack_client/types/tool.py">Tool</a></code>
- <code title="get /v1/tools">client.tools.<a href="./src/llama_stack_client/resources/tools.py">list</a>(\*\*<a href="src/llama_stack_client/types/tool_list_params.py">params</a>) -> <a href="./src/llama_stack_client/types/tool_list_response.py">ToolListResponse</a></code>

# Toolgroups

Types:

```python
from llama_stack_client.types import ToolGroup, ToolgroupListResponse
```

Methods:

- <code title="get /v1/toolgroups/{toolgroup_id}">client.toolgroups.<a href="./src/llama_stack_client/resources/toolgroups.py">retrieve</a>(toolgroup_id) -> <a href="./src/llama_stack_client/types/tool_group.py">ToolGroup</a></code>
- <code title="get /v1/toolgroups">client.toolgroups.<a href="./src/llama_stack_client/resources/toolgroups.py">list</a>() -> <a href="./src/llama_stack_client/types/toolgroup_list_response.py">ToolgroupListResponse</a></code>
- <code title="post /v1/toolgroups">client.toolgroups.<a href="./src/llama_stack_client/resources/toolgroups.py">register</a>(\*\*<a href="src/llama_stack_client/types/toolgroup_register_params.py">params</a>) -> None</code>
- <code title="delete /v1/toolgroups/{toolgroup_id}">client.toolgroups.<a href="./src/llama_stack_client/resources/toolgroups.py">unregister</a>(toolgroup_id) -> None</code>

# VectorDBs

Types:

```python
from llama_stack_client.types import VectorDB, VectorDBListResponse
```

Methods:

- <code title="post /v1/vector-dbs">client.vector_dbs.<a href="./src/llama_stack_client/resources/vector_dbs.py">create</a>(\*\*<a href="src/llama_stack_client/types/vector_db_create_params.py">params</a>) -> <a href="./src/llama_stack_client/types/vector_db.py">VectorDB</a></code>
- <code title="get /v1/vector-dbs/{vector_db_id}">client.vector_dbs.<a href="./src/llama_stack_client/resources/vector_dbs.py">retrieve</a>(vector_db_id) -> <a href="./src/llama_stack_client/types/vector_db.py">VectorDB</a></code>
- <code title="get /v1/vector-dbs">client.vector_dbs.<a href="./src/llama_stack_client/resources/vector_dbs.py">list</a>() -> <a href="./src/llama_stack_client/types/vector_db_list_response.py">VectorDBListResponse</a></code>
- <code title="delete /v1/vector-dbs/{vector_db_id}">client.vector_dbs.<a href="./src/llama_stack_client/resources/vector_dbs.py">delete</a>(vector_db_id) -> None</code>

# Health

Types:

```python
from llama_stack_client.types import HealthCheckResponse
```

Methods:

- <code title="get /v1/health">client.health.<a href="./src/llama_stack_client/resources/health.py">check</a>() -> <a href="./src/llama_stack_client/types/health_check_response.py">HealthCheckResponse</a></code>

# ToolRuntime

Types:

```python
from llama_stack_client.types import (
    ToolDef,
    URL,
    ToolRuntimeInvokeToolResponse,
    ToolRuntimeListToolsResponse,
)
```

Methods:

- <code title="post /v1/tool-runtime/invoke">client.tool_runtime.<a href="./src/llama_stack_client/resources/tool_runtime/tool_runtime.py">invoke_tool</a>(\*\*<a href="src/llama_stack_client/types/tool_runtime_invoke_tool_params.py">params</a>) -> <a href="./src/llama_stack_client/types/tool_runtime_invoke_tool_response.py">ToolRuntimeInvokeToolResponse</a></code>
- <code title="get /v1/tool-runtime/list-tools">client.tool_runtime.<a href="./src/llama_stack_client/resources/tool_runtime/tool_runtime.py">list_tools</a>(\*\*<a href="src/llama_stack_client/types/tool_runtime_list_tools_params.py">params</a>) -> <a href="./src/llama_stack_client/types/tool_runtime_list_tools_response.py">ToolRuntimeListToolsResponse</a></code>

## RagTool

Types:

```python
from llama_stack_client.types.tool_runtime import RagToolQueryContextResponse
```

Methods:

- <code title="post /v1/tool-runtime/rag-tool/insert">client.tool_runtime.rag_tool.<a href="./src/llama_stack_client/resources/tool_runtime/rag_tool.py">insert_documents</a>(\*\*<a href="src/llama_stack_client/types/tool_runtime/rag_tool_insert_documents_params.py">params</a>) -> None</code>
- <code title="post /v1/tool-runtime/rag-tool/query">client.tool_runtime.rag_tool.<a href="./src/llama_stack_client/resources/tool_runtime/rag_tool.py">query_context</a>(\*\*<a href="src/llama_stack_client/types/tool_runtime/rag_tool_query_context_params.py">params</a>) -> <a href="./src/llama_stack_client/types/tool_runtime/rag_tool_query_context_response.py">RagToolQueryContextResponse</a></code>

# VectorIo

Types:

```python
from llama_stack_client.types import VectorIoQueryResponse
```

Methods:

- <code title="post /v1/vector-io/insert">client.vector_io.<a href="./src/llama_stack_client/resources/vector_io.py">insert</a>(\*\*<a href="src/llama_stack_client/types/vector_io_insert_params.py">params</a>) -> None</code>
- <code title="post /v1/vector-io/query">client.vector_io.<a href="./src/llama_stack_client/resources/vector_io.py">query</a>(\*\*<a href="src/llama_stack_client/types/vector_io_query_params.py">params</a>) -> <a href="./src/llama_stack_client/types/vector_io_query_response.py">VectorIoQueryResponse</a></code>

# Providers

Types:

```python
from llama_stack_client.types import ProviderInfo, ProviderListResponse
```

Methods:

- <code title="get /v1/providers/{provider_id}">client.providers.<a href="./src/llama_stack_client/resources/providers.py">retrieve</a>(provider_id) -> <a href="./src/llama_stack_client/types/provider_info.py">ProviderInfo</a></code>
- <code title="get /v1/providers">client.providers.<a href="./src/llama_stack_client/resources/providers.py">list</a>() -> <a href="./src/llama_stack_client/types/provider_list_response.py">ProviderListResponse</a></code>

# Inspect

Types:

```python
from llama_stack_client.types import InspectListRoutesResponse
```

Methods:

- <code title="get /v1/inspect/routes">client.inspect.<a href="./src/llama_stack_client/resources/inspect.py">list_routes</a>() -> <a href="./src/llama_stack_client/types/inspect_list_routes_response.py">InspectListRoutesResponse</a></code>

# Safety

Types:

```python
from llama_stack_client.types import SafetyViolation, SafetyRunShieldResponse
```

Methods:

- <code title="post /v1/safety/run-shield">client.safety.<a href="./src/llama_stack_client/resources/safety.py">run_shield</a>(\*\*<a href="src/llama_stack_client/types/safety_run_shield_params.py">params</a>) -> <a href="./src/llama_stack_client/types/safety_run_shield_response.py">SafetyRunShieldResponse</a></code>

# Scoring

Types:

```python
from llama_stack_client.types import ScoringScoreResponse, ScoringScoreBatchResponse
```

Methods:

- <code title="post /v1/scoring/score">client.scoring.<a href="./src/llama_stack_client/resources/scoring.py">score</a>(\*\*<a href="src/llama_stack_client/types/scoring_score_params.py">params</a>) -> <a href="./src/llama_stack_client/types/scoring_score_response.py">ScoringScoreResponse</a></code>
- <code title="post /v1/scoring/score-batch">client.scoring.<a href="./src/llama_stack_client/resources/scoring.py">score_batch</a>(\*\*<a href="src/llama_stack_client/types/scoring_score_batch_params.py">params</a>) -> <a href="./src/llama_stack_client/types/scoring_score_batch_response.py">ScoringScoreBatchResponse</a></code>

# SyntheticDataGeneration

Types:

```python
from llama_stack_client.types import SyntheticDataGenerationGenerateResponse
```

Methods:

- <code title="post /v1/synthetic-data-generation/generate">client.synthetic_data_generation.<a href="./src/llama_stack_client/resources/synthetic_data_generation.py">generate</a>(\*\*<a href="src/llama_stack_client/types/synthetic_data_generation_generate_params.py">params</a>) -> <a href="./src/llama_stack_client/types/synthetic_data_generation_generate_response.py">SyntheticDataGenerationGenerateResponse</a></code>

# Version

Types:

```python
from llama_stack_client.types import VersionRetrieveResponse
```

Methods:

- <code title="get /v1/version">client.version.<a href="./src/llama_stack_client/resources/version.py">retrieve</a>() -> <a href="./src/llama_stack_client/types/version_retrieve_response.py">VersionRetrieveResponse</a></code>
