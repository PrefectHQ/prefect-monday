"""
This is a module for interacting with Monday Queryme tasks.
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

config_path = Path(__file__).parent.resolve() / "configs" / "query" / "me.json"
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task()
async def query_me(
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Get your data from monday.com.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returneds fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.me(**strip_kwargs())
    if not return_fields:
        op_stack = ("me",)
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, monday_credentials)
    return result["me"]


@task()
async def query_me_account(
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The user's account.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returneds fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.me(**strip_kwargs()).account(**strip_kwargs())
    if not return_fields:
        op_stack = (
            "me",
            "account",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, monday_credentials)
    return result["me"]["account"]


@task()
async def query_me_teams(
    monday_credentials: MondayCredentials,
    ids: Iterable[int] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The teams the user is a member in.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        ids: A list of teams unique identifiers.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returneds fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.me(**strip_kwargs()).teams(
        **strip_kwargs(
            ids=ids,
        )
    )
    if not return_fields:
        op_stack = (
            "me",
            "teams",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, monday_credentials)
    return result["me"]["teams"]
