"""
This is a module for interacting with Monday Query users tasks.
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

config_path = Path(__file__).parent.resolve() / "configs" / "query" / "users.json"
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task()
async def query_users(
    monday_credentials: MondayCredentials,
    ids: Iterable[int] = None,
    kind: graphql_schema.UserKind = None,
    newest_first: bool = None,
    limit: int = None,
    emails: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Get your data from monday.com.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        ids: A list of users unique identifiers.
        kind: The kind to search users by (all / non_guests / guests /
            non_pending).
        newest_first: Get the recently created users at the top of the list.
        limit: Number of users to get.
        emails: A list of users emails.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.users(
        **strip_kwargs(
            ids=ids,
            kind=kind,
            newest_first=newest_first,
            limit=limit,
            emails=emails,
        )
    )

    if not return_fields:
        op_stack = ("users",)
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, monday_credentials)
    return result["users"]


@task()
async def query_users_account(
    monday_credentials: MondayCredentials,
    ids: Iterable[int] = None,
    kind: graphql_schema.UserKind = None,
    newest_first: bool = None,
    limit: int = None,
    emails: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The user's account.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        ids: A list of users unique identifiers.
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
    op_settings = op.users(
        **strip_kwargs(
            ids=ids,
            kind=kind,
            newest_first=newest_first,
            limit=limit,
            emails=emails,
        )
    ).account(**strip_kwargs())

    if not return_fields:
        op_stack = (
            "users",
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
    return result["users"]["account"]


@task()
async def query_users_teams(
    monday_credentials: MondayCredentials,
    ids: Iterable[int] = None,
    kind: graphql_schema.UserKind = None,
    newest_first: bool = None,
    limit: int = None,
    emails: Iterable[str] = None,
    teams_ids: Iterable[int] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The teams the user is a member in.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        ids: A list of users unique identifiers.
        kind: The kind to search users by (all / non_guests / guests /
            non_pending).
        newest_first: Get the recently created users at the top of the
            list.
        limit: Number of users to get.
        emails: A list of users emails.
        teams_ids: A list of teams unique identifiers.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.users(
        **strip_kwargs(
            ids=ids,
            kind=kind,
            newest_first=newest_first,
            limit=limit,
            emails=emails,
        )
    ).teams(
        **strip_kwargs(
            ids=teams_ids,
        )
    )

    if not return_fields:
        op_stack = (
            "users",
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
    return result["users"]["teams"]
