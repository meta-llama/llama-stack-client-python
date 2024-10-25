# CLI Reference

You may use the `llama-stack-client` to query information about the distribution. 

#### `llama-stack-client`
```bash
$ llama-stack-client -h

usage: llama-stack-client [-h] {models,memory_banks,shields} ...

Welcome to the LlamaStackClient CLI

options:
  -h, --help            show this help message and exit

subcommands:
  {models,memory_banks,shields}
```

#### `llama-stack-client configure`
```bash
$ llama-stack-client configure
> Enter the host name of the Llama Stack distribution server: localhost
> Enter the port number of the Llama Stack distribution server: 5000
Done! You can now use the Llama Stack Client CLI with endpoint http://localhost:5000
```


#### `llama-stack-client providers`
```bash
$ llama-stack-client providers
```
```
+-----------+----------------+-----------------+
| API       | Provider ID    | Provider Type   |
+===========+================+=================+
| scoring   | meta0          | meta-reference  |
+-----------+----------------+-----------------+
| datasetio | meta0          | meta-reference  |
+-----------+----------------+-----------------+
| inference | tgi0           | remote::tgi     |
+-----------+----------------+-----------------+
| memory    | meta-reference | meta-reference  |
+-----------+----------------+-----------------+
| agents    | meta-reference | meta-reference  |
+-----------+----------------+-----------------+
| telemetry | meta-reference | meta-reference  |
+-----------+----------------+-----------------+
| safety    | meta-reference | meta-reference  |
+-----------+----------------+-----------------+
```

#### `llama-stack-client models list`
```bash
llama-stack-client models list
```
```
+----------------------+----------------------+---------------+----------------------------------------------------------+
| identifier           | llama_model          | provider_id   | metadata                                                 |
+======================+======================+===============+==========================================================+
| Llama3.1-8B-Instruct | Llama3.1-8B-Instruct | tgi0          | {'huggingface_repo': 'meta-llama/Llama-3.1-8B-Instruct'} |
+----------------------+----------------------+---------------+----------------------------------------------------------+
```

#### `llama-stack-client models get`
```bash
llama-stack-client models get Llama3.1-8B-Instruct
```

```
+----------------------+----------------------+----------------------------------------------------------+---------------+
| identifier           | llama_model          | metadata                                                 | provider_id   |
+======================+======================+==========================================================+===============+
| Llama3.1-8B-Instruct | Llama3.1-8B-Instruct | {'huggingface_repo': 'meta-llama/Llama-3.1-8B-Instruct'} | tgi0          |
+----------------------+----------------------+----------------------------------------------------------+---------------+
```


```bash
$ llama-stack-client models get Random-Model

Model RandomModel is not found at distribution endpoint host:port. Please ensure endpoint is serving specified model.
```



#### `llama-stack-client memory_banks list`
```bash
llama-stack-client memory_banks list
```
```
+--------------+----------------+--------+-------------------+------------------------+--------------------------+
| identifier   | provider_id    | type   | embedding_model   |   chunk_size_in_tokens |   overlap_size_in_tokens |
+==============+================+========+===================+========================+==========================+
| test_bank    | meta-reference | vector | all-MiniLM-L6-v2  |                    512 |                       64 |
+--------------+----------------+--------+-------------------+------------------------+--------------------------+
```

#### `llama-stack-client shields list`
```bash
llama-stack-client shields list
```

```
+--------------+----------+----------------+-------------+
| identifier   | params   | provider_id    | type        |
+==============+==========+================+=============+
| llama_guard  | {}       | meta-reference | llama_guard |
+--------------+----------+----------------+-------------+
```
