"""
This is a module containing:
Monday query_items* tasks
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

config_path = Path(__file__).parent.resolve() / "configs" / "query" / "items.json"
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_items(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    newest_first: bool = None,
    exclude_nonactive: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Get your data from monday.com.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of items unique identifiers.
        newest_first: Get the recently created items at the top of the list.
        exclude_nonactive: Excludes items that are inactive, deleted or belong
            to deleted items.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.items(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            newest_first=newest_first,
            exclude_nonactive=exclude_nonactive,
        )
    )

    op_stack = ("items",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["items"]


@task
async def query_items_board(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    newest_first: bool = None,
    exclude_nonactive: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The board that contains this item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of items unique identifiers.
        newest_first: Get the recently created items at the top of the
            list.
        exclude_nonactive: Excludes items that are inactive, deleted or
            belong to deleted items.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.items(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            newest_first=newest_first,
            exclude_nonactive=exclude_nonactive,
        )
    ).board(**strip_kwargs())

    op_stack = (
        "items",
        "board",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["items"]["board"]


@task
async def query_items_group(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    newest_first: bool = None,
    exclude_nonactive: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The group that contains this item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of items unique identifiers.
        newest_first: Get the recently created items at the top of the
            list.
        exclude_nonactive: Excludes items that are inactive, deleted or
            belong to deleted items.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.items(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            newest_first=newest_first,
            exclude_nonactive=exclude_nonactive,
        )
    ).group(**strip_kwargs())

    op_stack = (
        "items",
        "group",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["items"]["group"]


@task
async def query_items_assets(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    newest_first: bool = None,
    exclude_nonactive: bool = None,
    assets_source: graphql_schema.AssetsSource = None,
    column_ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The item's assets/files.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of items unique identifiers.
        newest_first: Get the recently created items at the top of the
            list.
        exclude_nonactive: Excludes items that are inactive, deleted or
            belong to deleted items.
        assets_source: The assets source (all / columns / gallery).
        column_ids: Ids of the columns you want to get assets from.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.items(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            newest_first=newest_first,
            exclude_nonactive=exclude_nonactive,
        )
    ).assets(
        **strip_kwargs(
            assets_source=assets_source,
            column_ids=column_ids,
        )
    )

    op_stack = (
        "items",
        "assets",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["items"]["assets"]


@task
async def query_items_creator(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    newest_first: bool = None,
    exclude_nonactive: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The item's creator.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of items unique identifiers.
        newest_first: Get the recently created items at the top of the
            list.
        exclude_nonactive: Excludes items that are inactive, deleted or
            belong to deleted items.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.items(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            newest_first=newest_first,
            exclude_nonactive=exclude_nonactive,
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "items",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["items"]["creator"]


@task
async def query_items_updates(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    newest_first: bool = None,
    exclude_nonactive: bool = None,
    updates_limit: int = 25,
    updates_page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The item's updates.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of items unique identifiers.
        newest_first: Get the recently created items at the top of the
            list.
        exclude_nonactive: Excludes items that are inactive, deleted or
            belong to deleted items.
        updates_limit: Number of items to get, the default is 25.
        updates_page: Page number to get, starting at 1.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.items(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            newest_first=newest_first,
            exclude_nonactive=exclude_nonactive,
        )
    ).updates(
        **strip_kwargs(
            limit=updates_limit,
            page=updates_page,
        )
    )

    op_stack = (
        "items",
        "updates",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["items"]["updates"]


@task
async def query_items_parent_item(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    newest_first: bool = None,
    exclude_nonactive: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The parent item of a subitem.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of items unique identifiers.
        newest_first: Get the recently created items at the top of the
            list.
        exclude_nonactive: Excludes items that are inactive, deleted or
            belong to deleted items.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.items(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            newest_first=newest_first,
            exclude_nonactive=exclude_nonactive,
        )
    ).parent_item(**strip_kwargs())

    op_stack = (
        "items",
        "parent_item",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["items"]["parent_item"]


@task
async def query_items_subscribers(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    newest_first: bool = None,
    exclude_nonactive: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The pulses's subscribers.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of items unique identifiers.
        newest_first: Get the recently created items at the top of the
            list.
        exclude_nonactive: Excludes items that are inactive, deleted or
            belong to deleted items.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.items(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            newest_first=newest_first,
            exclude_nonactive=exclude_nonactive,
        )
    ).subscribers(**strip_kwargs())

    op_stack = (
        "items",
        "subscribers",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["items"]["subscribers"]


@task
async def query_items_column_values(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    newest_first: bool = None,
    exclude_nonactive: bool = None,
    column_values_ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The item's column values.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of items unique identifiers.
        newest_first: Get the recently created items at the top of the
            list.
        exclude_nonactive: Excludes items that are inactive, deleted or
            belong to deleted items.
        column_values_ids: A list of column ids to return.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.items(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            newest_first=newest_first,
            exclude_nonactive=exclude_nonactive,
        )
    ).column_values(
        **strip_kwargs(
            ids=column_values_ids,
        )
    )

    op_stack = (
        "items",
        "column_values",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["items"]["column_values"]
