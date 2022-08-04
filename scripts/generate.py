"""
Used for generating the repository from scratch.
"""
from pathlib import Path

from cookiecutter.main import cookiecutter
from prefect_collection_generator.gql import populate_collection_repo

THIS_DIRECTORY = Path(__file__).parent.absolute()
REPO_DIRECTORY = THIS_DIRECTORY.parent

# USE THIS IF NEED TO REGENERATE FROM SCRATCH; IF NOT SKIP TO NEXT SECTION
extra_context = {
    "full_name": "Prefect Technologies, Inc.",
    "email": "help@prefect.io",
    "github_organization": "PrefectHQ",
    "collection_name": "prefect-monday",
    "collection_short_description": "Prefect integrations interacting with Monday",  # noqa
}

collection_template_url = "https://github.com/PrefectHQ/prefect-collection-template"
cookiecutter(
    collection_template_url,
    no_input=True,
    checkout="generated_graphql",
    extra_context=extra_context,
    overwrite_if_exists=True,
)
REPO_DIRECTORY = THIS_DIRECTORY / "prefect-monday"  # redirects repo_directory

# UPDATE THESE AS DESIRED

service_name = "Monday"  # e.g. GitHub
service_url = "https://api.monday.com/v2"  # e.g. https://api.github.com/graphql
token_path = Path("~/.secrets/monday").expanduser()
with open(token_path, "r") as f:
    token = f.read().strip()
root_to_op_types = {"query": None, "mutation": None}
overwrite = True

populate_collection_repo(
    service_name, service_url, token, root_to_op_types, repo_directory=REPO_DIRECTORY
)
