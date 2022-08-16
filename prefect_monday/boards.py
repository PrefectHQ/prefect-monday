"""
This is a module containing:
Monday query_boards* tasks
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable

from prefect import task
from sgqlc.operation import Operation

from prefect_monday import MondayCredentials
from prefect_monday.graphql import _execute_graphql_op, _subset_return_fields
from prefect_monday.schemas import graphql_schema
from prefect_monday.utils import initialize_return_fields_defaults, strip_kwargs

config_path = Path(__file__).parent.resolve() / "configs" / "query" / "boards.json"
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
async def query_boards(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    board_kind: graphql_schema.BoardKind = None,
    state: graphql_schema.State = "active",
    newest_first: bool = None,
    order_by: graphql_schema.BoardsOrderBy = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Get your data from monday.com.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of boards unique identifiers.
        board_kind: The board's kind (public / private / share).
        state: The state of the board (all / active / archived / deleted), the
            default is active.
        newest_first: Get the recently created boards at the top of the list,
            (Deprecated, use order_by:created_at).
        order_by: Property to order by (created_at / used_at).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.boards(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            board_kind=board_kind,
            state=state,
            newest_first=newest_first,
            order_by=order_by,
        )
    )

    op_stack = ("boards",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["boards"]


@task
async def query_boards_tags(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    board_kind: graphql_schema.BoardKind = None,
    state: graphql_schema.State = "active",
    newest_first: bool = None,
    order_by: graphql_schema.BoardsOrderBy = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The board's specific tags.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of boards unique identifiers.
        board_kind: The board's kind (public / private / share).
        state: The state of the board (all / active / archived /
            deleted), the default is active.
        newest_first: Get the recently created boards at the top of the
            list, (Deprecated, use order_by:created_at).
        order_by: Property to order by (created_at / used_at).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.boards(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            board_kind=board_kind,
            state=state,
            newest_first=newest_first,
            order_by=order_by,
        )
    ).tags(**strip_kwargs())

    op_stack = (
        "boards",
        "tags",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["boards"]["tags"]


@task
async def query_boards_items(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    board_kind: graphql_schema.BoardKind = None,
    state: graphql_schema.State = "active",
    newest_first: bool = None,
    order_by: graphql_schema.BoardsOrderBy = None,
    items_ids: Iterable[int] = None,
    items_limit: int = None,
    items_page: int = 1,
    items_newest_first: bool = None,
    exclude_nonactive: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The board's items (rows).

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of boards unique identifiers.
        board_kind: The board's kind (public / private / share).
        state: The state of the board (all / active / archived /
            deleted), the default is active.
        newest_first: Get the recently created boards at the top of the
            list, (Deprecated, use order_by:created_at).
        order_by: Property to order by (created_at / used_at).
        items_ids: A list of items unique identifiers.
        items_limit: Number of items to get.
        items_page: Page number to get, starting at 1.
        items_newest_first: Get the recently created items at the top of the
            list.
        exclude_nonactive: When providing a list of item IDs, this flag
            will exclude items that are archived, deleted or belong to
            deleted items.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.boards(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            board_kind=board_kind,
            state=state,
            newest_first=newest_first,
            order_by=order_by,
        )
    ).items(
        **strip_kwargs(
            ids=items_ids,
            limit=items_limit,
            page=items_page,
            newest_first=items_newest_first,
            exclude_nonactive=exclude_nonactive,
        )
    )

    op_stack = (
        "boards",
        "items",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["boards"]["items"]


@task
async def query_boards_owner(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    board_kind: graphql_schema.BoardKind = None,
    state: graphql_schema.State = "active",
    newest_first: bool = None,
    order_by: graphql_schema.BoardsOrderBy = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The owner of the board.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of boards unique identifiers.
        board_kind: The board's kind (public / private / share).
        state: The state of the board (all / active / archived /
            deleted), the default is active.
        newest_first: Get the recently created boards at the top of the
            list, (Deprecated, use order_by:created_at).
        order_by: Property to order by (created_at / used_at).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.boards(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            board_kind=board_kind,
            state=state,
            newest_first=newest_first,
            order_by=order_by,
        )
    ).owner(**strip_kwargs())

    op_stack = (
        "boards",
        "owner",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["boards"]["owner"]


@task
async def query_boards_views(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    board_kind: graphql_schema.BoardKind = None,
    state: graphql_schema.State = "active",
    newest_first: bool = None,
    order_by: graphql_schema.BoardsOrderBy = None,
    views_ids: Iterable[int] = None,
    type: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The board's views.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of boards unique identifiers.
        board_kind: The board's kind (public / private / share).
        state: The state of the board (all / active / archived /
            deleted), the default is active.
        newest_first: Get the recently created boards at the top of the
            list, (Deprecated, use order_by:created_at).
        order_by: Property to order by (created_at / used_at).
        views_ids: A list of view unique identifiers.
        type: The view's type.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.boards(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            board_kind=board_kind,
            state=state,
            newest_first=newest_first,
            order_by=order_by,
        )
    ).views(
        **strip_kwargs(
            ids=views_ids,
            type=type,
        )
    )

    op_stack = (
        "boards",
        "views",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["boards"]["views"]


@task
async def query_boards_groups(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    board_kind: graphql_schema.BoardKind = None,
    state: graphql_schema.State = "active",
    newest_first: bool = None,
    order_by: graphql_schema.BoardsOrderBy = None,
    groups_ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The board's visible groups.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of boards unique identifiers.
        board_kind: The board's kind (public / private / share).
        state: The state of the board (all / active / archived /
            deleted), the default is active.
        newest_first: Get the recently created boards at the top of the
            list, (Deprecated, use order_by:created_at).
        order_by: Property to order by (created_at / used_at).
        groups_ids: A list of group unique identifiers.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.boards(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            board_kind=board_kind,
            state=state,
            newest_first=newest_first,
            order_by=order_by,
        )
    ).groups(
        **strip_kwargs(
            ids=groups_ids,
        )
    )

    op_stack = (
        "boards",
        "groups",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["boards"]["groups"]


@task
async def query_boards_owners(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    board_kind: graphql_schema.BoardKind = None,
    state: graphql_schema.State = "active",
    newest_first: bool = None,
    order_by: graphql_schema.BoardsOrderBy = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    List of board owners.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of boards unique identifiers.
        board_kind: The board's kind (public / private / share).
        state: The state of the board (all / active / archived /
            deleted), the default is active.
        newest_first: Get the recently created boards at the top of the
            list, (Deprecated, use order_by:created_at).
        order_by: Property to order by (created_at / used_at).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.boards(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            board_kind=board_kind,
            state=state,
            newest_first=newest_first,
            order_by=order_by,
        )
    ).owners(**strip_kwargs())

    op_stack = (
        "boards",
        "owners",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["boards"]["owners"]


@task
async def query_boards_columns(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    board_kind: graphql_schema.BoardKind = None,
    state: graphql_schema.State = "active",
    newest_first: bool = None,
    order_by: graphql_schema.BoardsOrderBy = None,
    columns_ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The board's visible columns.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of boards unique identifiers.
        board_kind: The board's kind (public / private / share).
        state: The state of the board (all / active / archived /
            deleted), the default is active.
        newest_first: Get the recently created boards at the top of the
            list, (Deprecated, use order_by:created_at).
        order_by: Property to order by (created_at / used_at).
        columns_ids: A list of column unique identifiers.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.boards(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            board_kind=board_kind,
            state=state,
            newest_first=newest_first,
            order_by=order_by,
        )
    ).columns(
        **strip_kwargs(
            ids=columns_ids,
        )
    )

    op_stack = (
        "boards",
        "columns",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["boards"]["columns"]


@task
async def query_boards_creator(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    board_kind: graphql_schema.BoardKind = None,
    state: graphql_schema.State = "active",
    newest_first: bool = None,
    order_by: graphql_schema.BoardsOrderBy = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The creator of the board.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of boards unique identifiers.
        board_kind: The board's kind (public / private / share).
        state: The state of the board (all / active / archived /
            deleted), the default is active.
        newest_first: Get the recently created boards at the top of the
            list, (Deprecated, use order_by:created_at).
        order_by: Property to order by (created_at / used_at).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.boards(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            board_kind=board_kind,
            state=state,
            newest_first=newest_first,
            order_by=order_by,
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "boards",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["boards"]["creator"]


@task
async def query_boards_updates(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    board_kind: graphql_schema.BoardKind = None,
    state: graphql_schema.State = "active",
    newest_first: bool = None,
    order_by: graphql_schema.BoardsOrderBy = None,
    updates_limit: int = 25,
    updates_page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The board's updates.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of boards unique identifiers.
        board_kind: The board's kind (public / private / share).
        state: The state of the board (all / active / archived /
            deleted), the default is active.
        newest_first: Get the recently created boards at the top of the
            list, (Deprecated, use order_by:created_at).
        order_by: Property to order by (created_at / used_at).
        updates_limit: Number of items to get, the default is 25.
        updates_page: Page number to get, starting at 1.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.boards(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            board_kind=board_kind,
            state=state,
            newest_first=newest_first,
            order_by=order_by,
        )
    ).updates(
        **strip_kwargs(
            limit=updates_limit,
            page=updates_page,
        )
    )

    op_stack = (
        "boards",
        "updates",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["boards"]["updates"]


@task
async def query_boards_top_group(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    board_kind: graphql_schema.BoardKind = None,
    state: graphql_schema.State = "active",
    newest_first: bool = None,
    order_by: graphql_schema.BoardsOrderBy = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The top group at this board.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of boards unique identifiers.
        board_kind: The board's kind (public / private / share).
        state: The state of the board (all / active / archived /
            deleted), the default is active.
        newest_first: Get the recently created boards at the top of the
            list, (Deprecated, use order_by:created_at).
        order_by: Property to order by (created_at / used_at).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.boards(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            board_kind=board_kind,
            state=state,
            newest_first=newest_first,
            order_by=order_by,
        )
    ).top_group(**strip_kwargs())

    op_stack = (
        "boards",
        "top_group",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["boards"]["top_group"]


@task
async def query_boards_workspace(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    board_kind: graphql_schema.BoardKind = None,
    state: graphql_schema.State = "active",
    newest_first: bool = None,
    order_by: graphql_schema.BoardsOrderBy = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The workspace that contains this board (null for main workspace).

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of boards unique identifiers.
        board_kind: The board's kind (public / private / share).
        state: The state of the board (all / active / archived /
            deleted), the default is active.
        newest_first: Get the recently created boards at the top of the
            list, (Deprecated, use order_by:created_at).
        order_by: Property to order by (created_at / used_at).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.boards(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            board_kind=board_kind,
            state=state,
            newest_first=newest_first,
            order_by=order_by,
        )
    ).workspace(**strip_kwargs())

    op_stack = (
        "boards",
        "workspace",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["boards"]["workspace"]


@task
async def query_boards_subscribers(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    board_kind: graphql_schema.BoardKind = None,
    state: graphql_schema.State = "active",
    newest_first: bool = None,
    order_by: graphql_schema.BoardsOrderBy = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The board's subscribers.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of boards unique identifiers.
        board_kind: The board's kind (public / private / share).
        state: The state of the board (all / active / archived /
            deleted), the default is active.
        newest_first: Get the recently created boards at the top of the
            list, (Deprecated, use order_by:created_at).
        order_by: Property to order by (created_at / used_at).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.boards(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            board_kind=board_kind,
            state=state,
            newest_first=newest_first,
            order_by=order_by,
        )
    ).subscribers(**strip_kwargs())

    op_stack = (
        "boards",
        "subscribers",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["boards"]["subscribers"]


@task
async def query_boards_activity_logs(
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    ids: Iterable[int] = None,
    board_kind: graphql_schema.BoardKind = None,
    state: graphql_schema.State = "active",
    newest_first: bool = None,
    order_by: graphql_schema.BoardsOrderBy = None,
    activity_logs_limit: int = 25,
    activity_logs_page: int = 1,
    user_ids: Iterable[int] = None,
    column_ids: Iterable[str] = None,
    group_ids: Iterable[str] = None,
    item_ids: Iterable[int] = None,
    from_: datetime = None,
    to: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The board log events.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        limit: Number of items to get, the default is 25.
        page: Page number to get, starting at 1.
        ids: A list of boards unique identifiers.
        board_kind: The board's kind (public / private / share).
        state: The state of the board (all / active / archived /
            deleted), the default is active.
        newest_first: Get the recently created boards at the top of the
            list, (Deprecated, use order_by:created_at).
        order_by: Property to order by (created_at / used_at).
        activity_logs_limit: Number of items to get, the default is 25.
        activity_logs_page: Page number to get, starting at 1.
        user_ids: User ids to filter.
        column_ids: Column ids to filter.
        group_ids: Group ids to filter.
        item_ids: Item id to filter.
        from_: From timestamp (ISO8601).
        to: To timestamp (ISO8601).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_selection = op.boards(
        **strip_kwargs(
            limit=limit,
            page=page,
            ids=ids,
            board_kind=board_kind,
            state=state,
            newest_first=newest_first,
            order_by=order_by,
        )
    ).activity_logs(
        **strip_kwargs(
            limit=activity_logs_limit,
            page=activity_logs_page,
            user_ids=user_ids,
            column_ids=column_ids,
            group_ids=group_ids,
            item_ids=item_ids,
            from_=from_,
            to=to,
        )
    )

    op_stack = (
        "boards",
        "activity_logs",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["boards"]["activity_logs"]
