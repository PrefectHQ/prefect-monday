# prefect-monday

<p align="center">
    <a href="https://pypi.python.org/pypi/prefect-monday/" alt="PyPI version">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/prefect-monday?color=0052FF&labelColor=090422"></a>
    <a href="https://github.com/PrefectHQ/prefect-monday/" alt="Stars">
        <img src="https://img.shields.io/github/stars/PrefectHQ/prefect-monday?color=0052FF&labelColor=090422" /></a>
    <a href="https://pepy.tech/badge/prefect-monday/" alt="Downloads">
        <img src="https://img.shields.io/pypi/dm/prefect-monday?color=0052FF&labelColor=090422" /></a>
    <a href="https://github.com/PrefectHQ/prefect-monday/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/PrefectHQ/prefect-monday?color=0052FF&labelColor=090422" /></a>
    <br>
    <a href="https://prefect-community.slack.com" alt="Slack">
        <img src="https://img.shields.io/badge/slack-join_community-red.svg?color=0052FF&labelColor=090422&logo=slack" /></a>
    <a href="https://discourse.prefect.io/" alt="Discourse">
        <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?color=0052FF&labelColor=090422&logo=discourse" /></a>
</p>


## Welcome!

Prefect integrations interacting with monday.com.

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

Then, register to [view the block](https://orion-docs.prefect.io/ui/blocks/) on Prefect Cloud:

```bash
prefect block register -m prefect_monday.credentials
```

### Query personal account info

Note, to use the `load` method, you must already have a block document [saved through code](https://orion-docs.prefect.io/concepts/blocks/#saving-blocks) or [saved through the UI](https://orion-docs.prefect.io/ui/blocks/).

```python
from prefect import flow

from prefect_monday.credentials import MondayCredentials
from prefect_monday.me import query_me

@flow
def query_me_flow():
    monday_credentials = MondayCredentials.load("BLOCK_NAME")
    result = query_me(monday_credentials)
    return result

query_me_flow()
```

### Query available boards

```python
from prefect import flow

from prefect_monday.credentials import MondayCredentials
from prefect_monday.boards import query_boards

@flow
def query_boards_flow():
    monday_credentials = MondayCredentials.load("BLOCK_NAME")
    boards = query_boards(monday_credentials=monday_credentials)
    return boards

query_boards_flow()
```

### Create new workspace

```python
from prefect import flow

from prefect_monday.credentials import MondayCredentials
from prefect_monday.mutations import create_workspace
from prefect_monday.schemas import graphql_schema

@flow
def create_workspace_flow():
    monday_credentials = MondayCredentials.load("BLOCK_NAME")
    workspace = create_workspace(
        "integrations-test-workspace",
        graphql_schema.WorkspaceKind.open,
        monday_credentials=monday_credentials
    )
    return workspace

create_workspace_flow()
```

## Resources

If you encounter any bugs while using `prefect-monday`, feel free to open an issue in the [prefect-monday](https://github.com/PrefectHQ/prefect-monday) repository.

If you have any questions or issues while using `prefect-monday`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

Feel free to ⭐️ or watch [`prefect-monday`](https://github.com/PrefectHQ/prefect-monday) for updates too!

## Development

If you'd like to install a version of `prefect-monday` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-monday.git

cd prefect-monday/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
