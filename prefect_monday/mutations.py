"""
This is a module for interacting with Monday Mutation tasks.
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

config_dir = Path(__file__).parent.resolve() / "configs" / "mutation"
return_fields_defaults = {}
for config_path in config_dir.glob("*.json"):
    return_fields_defaults.update(initialize_return_fields_defaults(config_path))


@task()
async def like_update(
    monday_credentials: MondayCredentials,
    update_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Like an update.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        update_id: The update identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returneds fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_settings = op.like_update(
        **strip_kwargs(
            input=dict(
                update_id=update_id,
            )
        )
    )
    if not return_fields:
        op_stack = ("like_update",)
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, monday_credentials)
    return result["like_update"]


@task()
async def like_update_assets(
    monday_credentials: MondayCredentials,
    update_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Like an update.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        update_id: The update identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returneds fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_settings = op.like_update(
        **strip_kwargs(
            input=dict(
                update_id=update_id,
            )
        )
    ).assets(**strip_kwargs())
    if not return_fields:
        op_stack = (
            "like_update",
            "assets",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, monday_credentials)
    return result["like_update"]["assets"]


@task()
async def like_update_creator(
    monday_credentials: MondayCredentials,
    update_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Like an update.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        update_id: The update identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returneds fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_settings = op.like_update(
        **strip_kwargs(
            input=dict(
                update_id=update_id,
            )
        )
    ).creator(**strip_kwargs())
    if not return_fields:
        op_stack = (
            "like_update",
            "creator",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, monday_credentials)
    return result["like_update"]["creator"]


@task()
async def like_update_replies(
    monday_credentials: MondayCredentials,
    update_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Like an update.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        update_id: The update identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returneds fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_settings = op.like_update(
        **strip_kwargs(
            input=dict(
                update_id=update_id,
            )
        )
    ).replies(**strip_kwargs())
    if not return_fields:
        op_stack = (
            "like_update",
            "replies",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, monday_credentials)
    return result["like_update"]["replies"]
