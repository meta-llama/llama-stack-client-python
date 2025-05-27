## Setting up the environment

### With UV

We use [UV](https://docs.astral.sh/uv/) to manage dependencies so we highly recommend [installing it](https://docs.astral.sh/uv/installation/) as it will automatically provision a Python environment with the expected Python version.

After installing UV, you'll just have to run this command:

```bash
uv sync
```



## Modifying/Adding code

Most of the SDK is generated code. Modifications to code will be persisted between generations, but may
result in merge conflicts between manual patches and changes from the generator. The generator will never
modify the contents of the `src/llama_stack_client/lib/` and `examples/` directories.

## Using the repository from source

If you’d like to use the repository from source, you can either install from git or link to a cloned repository:

To install via git:

```bash
uv pip install git+ssh://git@github.com/stainless-sdks/llama-stack-python.git
```

Alternatively, you can build from source and install the wheel file:

Building this package will create two files in the `dist/` directory, a `.tar.gz` containing the source files and a `.whl` that can be used to install the package efficiently.

To create a distributable version of the library, all you have to do is run this command:

```bash
uv build
```

Then to install:

```sh
uv pip install ./path-to-wheel-file.whl
```

## Running tests

Most tests require you to [set up a mock server](https://github.com/stoplightio/prism) against the OpenAPI spec to run the tests.

```bash
# you will need npm installed
npx prism mock path/to/your/openapi.yml
```

```bash
uv run pytest
```

## Linting and formatting

There is a pre-commit hook that will run ruff and black on the code.

To run the pre-commit hook:

```bash
uv run pre-commit
```

## Publishing and releases

Changes made to this repository via the automated release PR pipeline should publish to PyPI automatically. If
the changes aren't made through the automated pipeline, you may want to make releases manually.

### Publish with a GitHub workflow

You can release to package managers by using [the `Publish PyPI` GitHub action](https://www.github.com/stainless-sdks/llama-stack-python/actions/workflows/publish-pypi.yml). This requires a setup organization or repository secret to be set up.

### Publish manually

If you need to manually release a package, you can run the `bin/publish-pypi` script with a `PYPI_TOKEN` set on
the environment.
