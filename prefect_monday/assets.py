"""
This is a module containing:
Monday query_assets* tasks
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

from pathlib import Path
from typing import Any, Dict, Iterable

from prefect import task
from sgqlc.operation import Operation

from prefect_monday import MondayCredentials
from prefect_monday.graphql import _execute_graphql_op, _subset_return_fields
from prefect_monday.schemas import graphql_schema
from prefect_monday.utils import initialize_return_fields_defaults, strip_kwargs

config_path = Path(__file__).parent.resolve() / "configs" / "query" / "assets.json"
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_assets(
    ids: Iterable[int],
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
    op_selection = op.assets(
        **strip_kwargs(
            ids=ids,
        )
    )

    op_stack = ("assets",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["assets"]


@task
async def query_assets_uploaded_by(
    ids: Iterable[int],
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
    op_selection = op.assets(
        **strip_kwargs(
            ids=ids,
        )
    ).uploaded_by(**strip_kwargs())

    op_stack = (
        "assets",
        "uploaded_by",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["assets"]["uploaded_by"]
