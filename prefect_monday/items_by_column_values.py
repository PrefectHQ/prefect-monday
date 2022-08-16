"""
This is a module containing:
Monday query_items_by_column_values* tasks
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

config_path = (
    Path(__file__).parent.resolve()
    / "configs"
    / "query"
    / "items_by_column_values.json"
)
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_items_by_column_values(
    board_id: int,
    column_id: str,
    column_value: str,
    monday_credentials: MondayCredentials,
    limit: int = None,
    page: int = 1,
    column_type: str = None,
    state: graphql_schema.State = "active",
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Get your data from monday.com.

    Args:
        board_id: The board's unique identifier.
        column_id: The column's unique identifier.
        column_value: The column value to search items by.
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get.
        page: Page number to get, starting at 1.
        column_type: The column type.
        state: The state of the item (all / active / archived / deleted), the
            default is active.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.items_by_column_values(
        **strip_kwargs(
            board_id=board_id,
            column_id=column_id,
            column_value=column_value,
            limit=limit,
            page=page,
            column_type=column_type,
            state=state,
        )
    )

    op_stack = ("items_by_column_values",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["items_by_column_values"]


@task
async def query_items_by_column_values_board(
    board_id: int,
    column_id: str,
    column_value: str,
    monday_credentials: MondayCredentials,
    limit: int = None,
    page: int = 1,
    column_type: str = None,
    state: graphql_schema.State = "active",
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The board that contains this item.

    Args:
        board_id: The board's unique identifier.
        column_id: The column's unique identifier.
        column_value: The column value to search items
            by.
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get.
        page: Page number to get, starting at 1.
        column_type: The column type.
        state: The state of the item (all / active /
            archived / deleted), the default is active.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.items_by_column_values(
        **strip_kwargs(
            board_id=board_id,
            column_id=column_id,
            column_value=column_value,
            limit=limit,
            page=page,
            column_type=column_type,
            state=state,
        )
    ).board(**strip_kwargs())

    op_stack = (
        "items_by_column_values",
        "board",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["items_by_column_values"]["board"]


@task
async def query_items_by_column_values_group(
    board_id: int,
    column_id: str,
    column_value: str,
    monday_credentials: MondayCredentials,
    limit: int = None,
    page: int = 1,
    column_type: str = None,
    state: graphql_schema.State = "active",
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The group that contains this item.

    Args:
        board_id: The board's unique identifier.
        column_id: The column's unique identifier.
        column_value: The column value to search items
            by.
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get.
        page: Page number to get, starting at 1.
        column_type: The column type.
        state: The state of the item (all / active /
            archived / deleted), the default is active.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.items_by_column_values(
        **strip_kwargs(
            board_id=board_id,
            column_id=column_id,
            column_value=column_value,
            limit=limit,
            page=page,
            column_type=column_type,
            state=state,
        )
    ).group(**strip_kwargs())

    op_stack = (
        "items_by_column_values",
        "group",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["items_by_column_values"]["group"]


@task
async def query_items_by_column_values_assets(
    board_id: int,
    column_id: str,
    column_value: str,
    monday_credentials: MondayCredentials,
    limit: int = None,
    page: int = 1,
    column_type: str = None,
    state: graphql_schema.State = "active",
    assets_source: graphql_schema.AssetsSource = None,
    column_ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The item's assets/files.

    Args:
        board_id: The board's unique identifier.
        column_id: The column's unique identifier.
        column_value: The column value to search items
            by.
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get.
        page: Page number to get, starting at 1.
        column_type: The column type.
        state: The state of the item (all / active /
            archived / deleted), the default is active.
        assets_source: The assets source (all / columns / gallery).
        column_ids: Ids of the columns you want to get assets from.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.items_by_column_values(
        **strip_kwargs(
            board_id=board_id,
            column_id=column_id,
            column_value=column_value,
            limit=limit,
            page=page,
            column_type=column_type,
            state=state,
        )
    ).assets(
        **strip_kwargs(
            assets_source=assets_source,
            column_ids=column_ids,
        )
    )

    op_stack = (
        "items_by_column_values",
        "assets",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["items_by_column_values"]["assets"]


@task
async def query_items_by_column_values_creator(
    board_id: int,
    column_id: str,
    column_value: str,
    monday_credentials: MondayCredentials,
    limit: int = None,
    page: int = 1,
    column_type: str = None,
    state: graphql_schema.State = "active",
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The item's creator.

    Args:
        board_id: The board's unique identifier.
        column_id: The column's unique identifier.
        column_value: The column value to search items
            by.
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get.
        page: Page number to get, starting at 1.
        column_type: The column type.
        state: The state of the item (all / active /
            archived / deleted), the default is active.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.items_by_column_values(
        **strip_kwargs(
            board_id=board_id,
            column_id=column_id,
            column_value=column_value,
            limit=limit,
            page=page,
            column_type=column_type,
            state=state,
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "items_by_column_values",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["items_by_column_values"]["creator"]


@task
async def query_items_by_column_values_updates(
    board_id: int,
    column_id: str,
    column_value: str,
    monday_credentials: MondayCredentials,
    limit: int = None,
    page: int = 1,
    column_type: str = None,
    state: graphql_schema.State = "active",
    updates_limit: int = 25,
    updates_page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The item's updates.

    Args:
        board_id: The board's unique identifier.
        column_id: The column's unique identifier.
        column_value: The column value to search items
            by.
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get.
        page: Page number to get, starting at 1.
        column_type: The column type.
        state: The state of the item (all / active /
            archived / deleted), the default is active.
        updates_limit: Number of items to get, the default is 25.
        updates_page: Page number to get, starting at 1.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.items_by_column_values(
        **strip_kwargs(
            board_id=board_id,
            column_id=column_id,
            column_value=column_value,
            limit=limit,
            page=page,
            column_type=column_type,
            state=state,
        )
    ).updates(
        **strip_kwargs(
            limit=updates_limit,
            page=updates_page,
        )
    )

    op_stack = (
        "items_by_column_values",
        "updates",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["items_by_column_values"]["updates"]


@task
async def query_items_by_column_values_parent_item(
    board_id: int,
    column_id: str,
    column_value: str,
    monday_credentials: MondayCredentials,
    limit: int = None,
    page: int = 1,
    column_type: str = None,
    state: graphql_schema.State = "active",
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The parent item of a subitem.

    Args:
        board_id: The board's unique identifier.
        column_id: The column's unique identifier.
        column_value: The column value to search items
            by.
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get.
        page: Page number to get, starting at 1.
        column_type: The column type.
        state: The state of the item (all / active /
            archived / deleted), the default is active.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.items_by_column_values(
        **strip_kwargs(
            board_id=board_id,
            column_id=column_id,
            column_value=column_value,
            limit=limit,
            page=page,
            column_type=column_type,
            state=state,
        )
    ).parent_item(**strip_kwargs())

    op_stack = (
        "items_by_column_values",
        "parent_item",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["items_by_column_values"]["parent_item"]


@task
async def query_items_by_column_values_subscribers(
    board_id: int,
    column_id: str,
    column_value: str,
    monday_credentials: MondayCredentials,
    limit: int = None,
    page: int = 1,
    column_type: str = None,
    state: graphql_schema.State = "active",
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The pulses's subscribers.

    Args:
        board_id: The board's unique identifier.
        column_id: The column's unique identifier.
        column_value: The column value to search items
            by.
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get.
        page: Page number to get, starting at 1.
        column_type: The column type.
        state: The state of the item (all / active /
            archived / deleted), the default is active.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.items_by_column_values(
        **strip_kwargs(
            board_id=board_id,
            column_id=column_id,
            column_value=column_value,
            limit=limit,
            page=page,
            column_type=column_type,
            state=state,
        )
    ).subscribers(**strip_kwargs())

    op_stack = (
        "items_by_column_values",
        "subscribers",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["items_by_column_values"]["subscribers"]


@task
async def query_items_by_column_values_column_values(
    board_id: int,
    column_id: str,
    column_value: str,
    monday_credentials: MondayCredentials,
    limit: int = None,
    page: int = 1,
    column_type: str = None,
    state: graphql_schema.State = "active",
    ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The item's column values.

    Args:
        board_id: The board's unique identifier.
        column_id: The column's unique identifier.
        column_value: The column value to search items
            by.
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get.
        page: Page number to get, starting at 1.
        column_type: The column type.
        state: The state of the item (all / active /
            archived / deleted), the default is active.
        ids: A list of column ids to return.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.items_by_column_values(
        **strip_kwargs(
            board_id=board_id,
            column_id=column_id,
            column_value=column_value,
            limit=limit,
            page=page,
            column_type=column_type,
            state=state,
        )
    ).column_values(
        **strip_kwargs(
            ids=ids,
        )
    )

    op_stack = (
        "items_by_column_values",
        "column_values",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["items_by_column_values"]["column_values"]
