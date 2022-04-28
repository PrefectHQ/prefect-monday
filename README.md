# prefect-monday

## Welcome!

Prefect tasks and subflows for monday.com

The tasks within this collection were created by a code generator using the service's GraphQL schema.

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-monday` with `pip`:

```bash
pip install prefect-monday
```

### Write and run a flow

```python
from prefect import flow
from prefect_monday.credentials import MondayCredentials
from prefect_monday.me import query_me

@flow
def query_me_flow():
    monday_credentials = MondayCredentials("token")
    result = query_me(monday_credentials)
    return result

query_me_flow()
```

## Resources

If you encounter any bugs while using `prefect-monday`, feel free to open an issue in the [prefect-monday](https://github.com/PrefectHQ/prefect-monday) repository.

If you have any questions or issues while using `prefect-monday`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

## Development

If you'd like to install a version of `prefect-monday` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-monday.git

cd prefect-monday/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
