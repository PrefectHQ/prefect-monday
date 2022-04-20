"""
This is a module for interacting with Monday Query assets tasks.
It was auto-generated using prefect-collection-generator so
manually editing this file is not recommended.
"""

from pathlib import Path
from typing import Any, Dict, Iterable

from prefect import task
from prefect_monday import MondayCredentials
from prefect_monday.graphql import _execute_graphql_op
from prefect_monday.schemas import graphql_schema
from prefect_monday.utils import initialize_return_fields_defaults, strip_kwargs
from sgqlc.operation import Operation

config_path = Path(__file__).parent.resolve() / "configs" / "query" / "assets.json"
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task()
async def query_assets(
    ids: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Get your data from monday.com.

    Args:
        ids: Ids of the assets/files you want to get.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.assets(
        **strip_kwargs(
            ids=ids,
        )
    )

    if not return_fields:
        op_stack = ("assets",)
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, monday_credentials)
    return result["assets"]


@task()
async def query_assets_uploaded_by(
    ids: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The user who uploaded the file.

    Args:
        ids: Ids of the assets/files you want to get.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.assets(
        **strip_kwargs(
            ids=ids,
        )
    ).uploaded_by(**strip_kwargs())

    if not return_fields:
        op_stack = (
            "assets",
            "uploaded_by",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, monday_credentials)
    return result["assets"]["uploaded_by"]
