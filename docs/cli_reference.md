# CLI Reference

Welcome to the llama-stack-client CLI - a command-line interface for interacting with Llama Stack

### Usage

```
Usage: llama-stack-client [OPTIONS] COMMAND [ARGS]...
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

* **--version**: Show the version and exit. [default: False]

* **--endpoint**: Llama Stack distribution endpoint [default: ]

* **--api-key**: Llama Stack distribution API key [default: ]

* **--config**: Path to config file

### Commands

* **configure**: Configure Llama Stack Client CLI.

* **datasets**: Manage datasets.

* **eval**: Run evaluation tasks.

* **eval_tasks**: Manage evaluation tasks.

* **inference**: Inference (chat).

* **inspect**: Inspect server configuration.

* **models**: Manage GenAI models.

* **post_training**: Post-training.

* **providers**: Manage API providers.

* **scoring_functions**: Manage scoring functions.

* **shields**: Manage safety shield services.

* **toolgroups**: Manage available tool groups.

* **vector_dbs**: Manage vector databases.



## configure

Configure Llama Stack Client CLI.

### Usage

```
Usage: llama-stack-client configure [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

* **--endpoint**: Llama Stack distribution endpoint [default: ]

* **--api-key**: Llama Stack distribution API key [default: ]



## datasets

Manage datasets.

### Usage

```
Usage: llama-stack-client datasets [OPTIONS] COMMAND [ARGS]...
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

### Commands

* **list**: Show available datasets on distribution...

* **register**: Create a new dataset



### list

Show available datasets on distribution endpoint

### Usage

```
Usage: llama-stack-client datasets list [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]



### register

Create a new dataset

### Usage

```
Usage: llama-stack-client datasets register [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

* **--dataset-id**: Id of the dataset

* **--provider-id**: Provider ID for the dataset

* **--provider-dataset-id**: Provider's dataset ID

* **--metadata**: Metadata of the dataset

* **--url**: URL of the dataset

* **--dataset-path**: Local file path to the dataset. If specified, upload dataset via URL

* **--schema**: JSON schema of the dataset



## eval

Run evaluation tasks.

### Usage

```
Usage: llama-stack-client eval [OPTIONS] COMMAND [ARGS]...
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

### Commands

* **run-benchmark**: Run a evaluation benchmark task

* **run-scoring**: Run scoring from application datasets



### run-benchmark

Run a evaluation benchmark task

### Usage

```
Usage: llama-stack-client eval run-benchmark [OPTIONS] BENCHMARK_IDS...
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

* **--model-id**: model id to run the benchmark eval on

* **--output-dir**: Path to the dump eval results output directory

* **--num-examples**: Number of examples to evaluate on, useful for debugging

* **--temperature**: temperature in the sampling params to run generation [default: 0.0]

* **--max-tokens**: max-tokens in the sampling params to run generation [default: 4096]

* **--top-p**: top-p in the sampling params to run generation [default: 0.9]

* **--repeat-penalty**: repeat-penalty in the sampling params to run generation [default: 1.0]

* **--visualize**: Visualize evaluation results after completion [default: False]

### Arguments

* **BENCHMARK_IDS**



### run-scoring

Run scoring from application datasets

### Usage

```
Usage: llama-stack-client eval run-scoring [OPTIONS] SCORING_FUNCTION_IDS...
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

* **--dataset-id**: Pre-registered dataset_id to score (from llama-stack-client datasets list)

* **--dataset-path**: Path to the dataset file to score

* **--scoring-params-config**: Path to the scoring params config file in JSON format

* **--num-examples**: Number of examples to evaluate on, useful for debugging

* **--output-dir**: Path to the dump eval results output directory

* **--visualize**: Visualize evaluation results after completion [default: False]

### Arguments

* **SCORING_FUNCTION_IDS**



## eval-tasks

Manage evaluation tasks.

### Usage

```
Usage: llama-stack-client eval-tasks [OPTIONS] COMMAND [ARGS]...
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

### Commands

* **list**: Show available eval tasks on distribution...

* **register**: Register a new eval task



### list

Show available eval tasks on distribution endpoint

### Usage

```
Usage: llama-stack-client eval-tasks list [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]



### register

Register a new eval task

### Usage

```
Usage: llama-stack-client eval-tasks register [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

* **--eval-task-id**: ID of the eval task

* **--dataset-id**: ID of the dataset to evaluate

* **--scoring-functions**: Scoring functions to use for evaluation

* **--provider-id**: Provider ID for the eval task

* **--provider-eval-task-id**: Provider's eval task ID

* **--metadata**: Metadata for the eval task in JSON format



## inference

Inference (chat).

### Usage

```
Usage: llama-stack-client inference [OPTIONS] COMMAND [ARGS]...
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

### Commands

* **chat-completion**: Show available inference chat completion...



### chat-completion

Show available inference chat completion endpoints on distribution endpoint

### Usage

```
Usage: llama-stack-client inference chat-completion [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

* **--message**: Message

* **--stream**: Streaming [default: False]

* **--session**: Start a Chat Session [default: False]

* **--model-id**: Model ID



## inspect

Inspect server configuration.

### Usage

```
Usage: llama-stack-client inspect [OPTIONS] COMMAND [ARGS]...
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

### Commands

* **version**: Show available providers on distribution...



### version

Show available providers on distribution endpoint

### Usage

```
Usage: llama-stack-client inspect version [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]



## models

Manage GenAI models.

### Usage

```
Usage: llama-stack-client models [OPTIONS] COMMAND [ARGS]...
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

### Commands

* **get**: Show available llama models at distribution...

* **list**: Show available llama models at distribution...

* **register**: Register a new model at distribution endpoint

* **unregister**: Unregister a model from distribution endpoint



### get

Show available llama models at distribution endpoint

### Usage

```
Usage: llama-stack-client models get [OPTIONS] MODEL_ID
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

### Arguments

* **MODEL_ID**



### list

Show available llama models at distribution endpoint

### Usage

```
Usage: llama-stack-client models list [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]



### register

Register a new model at distribution endpoint

### Usage

```
Usage: llama-stack-client models register [OPTIONS] MODEL_ID
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

* **--provider-id**: Provider ID for the model

* **--provider-model-id**: Provider's model ID

* **--metadata**: JSON metadata for the model

### Arguments

* **MODEL_ID**



### unregister

Unregister a model from distribution endpoint

### Usage

```
Usage: llama-stack-client models unregister [OPTIONS] MODEL_ID
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

### Arguments

* **MODEL_ID**



## post-training

Post-training.

### Usage

```
Usage: llama-stack-client post-training [OPTIONS] COMMAND [ARGS]...
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

### Commands

* **artifacts**: Get the training artifacts of a specific post...

* **cancel**: Cancel the training job

* **list**: Show the list of available post training jobs

* **status**: Show the status of a specific post training...

* **supervised_fine_tune**: Kick off a supervised fine tune job



### artifacts

Get the training artifacts of a specific post training job

### Usage

```
Usage: llama-stack-client post-training artifacts [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

* **--job-uuid**: Job UUID



### cancel

Cancel the training job

### Usage

```
Usage: llama-stack-client post-training cancel [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

* **--job-uuid**: Job UUID



### list

Show the list of available post training jobs

### Usage

```
Usage: llama-stack-client post-training list [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]



### status

Show the status of a specific post training job

### Usage

```
Usage: llama-stack-client post-training status [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

* **--job-uuid**: Job UUID



### supervised_fine_tune

Kick off a supervised fine tune job

### Usage

```
Usage: llama-stack-client post-training supervised_fine_tune 
           [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

* **--job-uuid**: Job UUID

* **--model**: Model ID

* **--algorithm-config**: Algorithm Config

* **--training-config**: Training Config

* **--checkpoint-dir**: Checkpoint Config



## providers

Manage API providers.

### Usage

```
Usage: llama-stack-client providers [OPTIONS] COMMAND [ARGS]...
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

### Commands

* **list**: Show available providers on distribution...



### list

Show available providers on distribution endpoint

### Usage

```
Usage: llama-stack-client providers list [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]



## scoring-functions

Manage scoring functions.

### Usage

```
Usage: llama-stack-client scoring-functions [OPTIONS] COMMAND [ARGS]...
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

### Commands

* **list**: Show available scoring functions on...

* **register**: Register a new scoring function



### list

Show available scoring functions on distribution endpoint

### Usage

```
Usage: llama-stack-client scoring-functions list [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]



### register

Register a new scoring function

### Usage

```
Usage: llama-stack-client scoring-functions register [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

* **--scoring-fn-id**: Id of the scoring function

* **--description**: Description of the scoring function

* **--return-type**: Return type of the scoring function

* **--provider-id**: Provider ID for the scoring function

* **--provider-scoring-fn-id**: Provider's scoring function ID

* **--params**: Parameters for the scoring function in JSON format



## shields

Manage safety shield services.

### Usage

```
Usage: llama-stack-client shields [OPTIONS] COMMAND [ARGS]...
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

### Commands

* **list**: Show available safety shields on distribution...

* **register**: Register a new safety shield



### list

Show available safety shields on distribution endpoint

### Usage

```
Usage: llama-stack-client shields list [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]



### register

Register a new safety shield

### Usage

```
Usage: llama-stack-client shields register [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

* **--shield-id**: Id of the shield

* **--provider-id**: Provider ID for the shield

* **--provider-shield-id**: Provider's shield ID

* **--params**: JSON configuration parameters for the shield



## toolgroups

Manage available tool groups.

### Usage

```
Usage: llama-stack-client toolgroups [OPTIONS] COMMAND [ARGS]...
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

### Commands

* **get**: Show available llama toolgroups at...

* **list**: Show available llama toolgroups at...

* **register**: Register a new toolgroup at distribution...

* **unregister**: Unregister a toolgroup from distribution...



### get

Show available llama toolgroups at distribution endpoint

### Usage

```
Usage: llama-stack-client toolgroups get [OPTIONS] TOOLGROUP_ID
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

### Arguments

* **TOOLGROUP_ID**



### list

Show available llama toolgroups at distribution endpoint

### Usage

```
Usage: llama-stack-client toolgroups list [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]



### register

Register a new toolgroup at distribution endpoint

### Usage

```
Usage: llama-stack-client toolgroups register [OPTIONS] TOOLGROUP_ID
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

* **--provider-id**: Provider ID for the toolgroup

* **--provider-toolgroup-id**: Provider's toolgroup ID

* **--mcp-config**: JSON mcp_config for the toolgroup

* **--args**: JSON args for the toolgroup

### Arguments

* **TOOLGROUP_ID**



### unregister

Unregister a toolgroup from distribution endpoint

### Usage

```
Usage: llama-stack-client toolgroups unregister [OPTIONS] TOOLGROUP_ID
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

### Arguments

* **TOOLGROUP_ID**



## vector-dbs

Manage vector databases.

### Usage

```
Usage: llama-stack-client vector-dbs [OPTIONS] COMMAND [ARGS]...
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

### Commands

* **list**: Show available vector dbs on distribution...

* **register**: Create a new vector db

* **unregister**: Delete a vector db



### list

Show available vector dbs on distribution endpoint

### Usage

```
Usage: llama-stack-client vector-dbs list [OPTIONS]
```

### Options

* **-h, --help**: Show this message and exit. [default: False]



### register

Create a new vector db

### Usage

```
Usage: llama-stack-client vector-dbs register [OPTIONS] VECTOR_DB_ID
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

* **--provider-id**: Provider ID for the vector db

* **--provider-vector-db-id**: Provider's vector db ID

* **--embedding-model**: Embedding model (for vector type) [default: all-MiniLM-L6-v2]

* **--embedding-dimension**: Embedding dimension (for vector type) [default: 384]

### Arguments

* **VECTOR_DB_ID**



### unregister

Delete a vector db

### Usage

```
Usage: llama-stack-client vector-dbs unregister [OPTIONS] VECTOR_DB_ID
```

### Options

* **-h, --help**: Show this message and exit. [default: False]

### Arguments

* **VECTOR_DB_ID**
