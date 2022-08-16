"""
This is a module containing:
Monday query_teams* tasks
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

config_path = Path(__file__).parent.resolve() / "configs" / "query" / "teams.json"
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_teams(
    monday_credentials: MondayCredentials,
    ids: Iterable[int] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Get your data from monday.com.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        ids: A list of teams unique identifiers.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.teams(
        **strip_kwargs(
            ids=ids,
        )
    )

    op_stack = ("teams",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["teams"]


@task
async def query_teams_users(
    monday_credentials: MondayCredentials,
    ids: Iterable[int] = None,
    users_ids: Iterable[int] = None,
    kind: graphql_schema.UserKind = None,
    newest_first: bool = None,
    limit: int = None,
    emails: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The users in the team.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        ids: A list of teams unique identifiers.
        users_ids: A list of users unique identifiers.
        kind: The kind to search users by (all / non_guests / guests /
            non_pending).
        newest_first: Get the recently created users at the top of the
            list.
        limit: Number of users to get.
        emails: A list of users emails.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.teams(**strip_kwargs(ids=ids,)).users(
        **strip_kwargs(
            ids=users_ids,
            kind=kind,
            newest_first=newest_first,
            limit=limit,
            emails=emails,
        )
    )

    op_stack = (
        "teams",
        "users",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["teams"]["users"]
