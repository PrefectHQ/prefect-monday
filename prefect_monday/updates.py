"""
This is a module containing:
Monday query_updates* tasks
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

config_path = Path(__file__).parent.resolve() / "configs" / "query" / "updates.json"
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_updates(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Get your data from monday.com.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.updates(
        **strip_kwargs(
            limit=limit,
            page=page,
        )
    )

    op_stack = ("updates",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["updates"]


@task
async def query_updates_assets(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The update's assets/files.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.updates(
        **strip_kwargs(
            limit=limit,
            page=page,
        )
    ).assets(**strip_kwargs())

    op_stack = (
        "updates",
        "assets",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["updates"]["assets"]


@task
async def query_updates_creator(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The update's creator.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.updates(
        **strip_kwargs(
            limit=limit,
            page=page,
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "updates",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["updates"]["creator"]


@task
async def query_updates_replies(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The update's replies.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.updates(
        **strip_kwargs(
            limit=limit,
            page=page,
        )
    ).replies(**strip_kwargs())

    op_stack = (
        "updates",
        "replies",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["updates"]["replies"]
