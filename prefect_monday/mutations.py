"""
This is a module for interacting with Monday Mutation  tasks.
It was auto-generated using prefect-collection-generator so
manually editing this file is not recommended.
"""

from pathlib import Path
from typing import Any, Dict, Iterable

from prefect import task
from prefect_monday import MondayCredentials
from prefect_monday.graphql import _execute_graphql_op, _subset_return_fields
from prefect_monday.schemas import graphql_schema
from prefect_monday.utils import initialize_return_fields_defaults, strip_kwargs
from sgqlc.operation import Operation

config_dir = Path(__file__).parent.resolve() / "configs" / "mutation"
return_fields_defaults = {}
for config_path in config_dir.glob("*.json"):
    return_fields_defaults.update(initialize_return_fields_defaults(config_path))


@task
async def change_column_title(
    column_id: str,
    board_id: int,
    title: str,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change a column's title.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        title: The new title of the column.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_column_title(
        **strip_kwargs(
            input=dict(
                column_id=column_id,
                board_id=board_id,
                title=title,
            )
        )
    )

    op_stack = ("change_column_title",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_column_title"]
@task
async def clear_item_updates(
    item_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Clear an item's updates.

    Args:
        item_id: The item's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.clear_item_updates(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    )

    op_stack = ("clear_item_updates",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["clear_item_updates"]


@task
async def clear_item_updates_assets(
    item_id: int,
    monday_credentials: MondayCredentials,
    assets_source: graphql_schema.AssetsSource = None,
    column_ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Clear an item's updates.

    Args:
        item_id: The item's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        assets_source: None.
        column_ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.clear_item_updates(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).assets(
        **strip_kwargs(
            input=dict(
                assets_source=assets_source,
                column_ids=column_ids,
            )
        )
    )

    op_stack = (
        "clear_item_updates",
        "assets",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["clear_item_updates"]["assets"]


@task
async def clear_item_updates_board(
    item_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Clear an item's updates.

    Args:
        item_id: The item's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.clear_item_updates(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).board(**strip_kwargs())

    op_stack = (
        "clear_item_updates",
        "board",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["clear_item_updates"]["board"]


@task
async def clear_item_updates_column_values(
    item_id: int,
    monday_credentials: MondayCredentials,
    ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Clear an item's updates.

    Args:
        item_id: The item's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.clear_item_updates(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).column_values(
        **strip_kwargs(
            input=dict(
                ids=ids,
            )
        )
    )

    op_stack = (
        "clear_item_updates",
        "column_values",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["clear_item_updates"]["column_values"]


@task
async def clear_item_updates_creator(
    item_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Clear an item's updates.

    Args:
        item_id: The item's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.clear_item_updates(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "clear_item_updates",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["clear_item_updates"]["creator"]


@task
async def clear_item_updates_group(
    item_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Clear an item's updates.

    Args:
        item_id: The item's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.clear_item_updates(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).group(**strip_kwargs())

    op_stack = (
        "clear_item_updates",
        "group",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["clear_item_updates"]["group"]


@task
async def clear_item_updates_subitems(
    item_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Clear an item's updates.

    Args:
        item_id: The item's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.clear_item_updates(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).subitems(**strip_kwargs())

    op_stack = (
        "clear_item_updates",
        "subitems",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["clear_item_updates"]["subitems"]


@task
async def clear_item_updates_subscribers(
    item_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Clear an item's updates.

    Args:
        item_id: The item's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.clear_item_updates(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).subscribers(**strip_kwargs())

    op_stack = (
        "clear_item_updates",
        "subscribers",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["clear_item_updates"]["subscribers"]


@task
async def clear_item_updates(
    item_id: int,
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Clear an item's updates.

    Args:
        item_id: The item's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        limit: None.
        page: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.clear_item_updates(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).updates(
        **strip_kwargs(
            input=dict(
                limit=limit,
                page=page,
            )
        )
    )

    op_stack = (
        "clear_item_updates",
        "updates",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["clear_item_updates"]["updates"]
@task
async def create_board(
    board_name: str,
    board_kind: graphql_schema.BoardKind,
    monday_credentials: MondayCredentials,
    folder_id: int = None,
    workspace_id: int = None,
    template_id: int = None,
    board_owner_ids: Iterable[int] = None,
    board_subscriber_ids: Iterable[int] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new board.

    Args:
        board_name: The board's name.
        board_kind: The board's kind (public / private / share).
        monday_credentials: Credentials to use for authentication with Monday.
        folder_id: Optional board folder id.
        workspace_id: Optional workspace id.
        template_id: Optional board template id.
        board_owner_ids: Optional board owner ids.
        board_subscriber_ids: Optional board subscriber ids.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_board(
        **strip_kwargs(
            input=dict(
                board_name=board_name,
                board_kind=board_kind,
                folder_id=folder_id,
                workspace_id=workspace_id,
                template_id=template_id,
                board_owner_ids=board_owner_ids,
                board_subscriber_ids=board_subscriber_ids,
            )
        )
    )

    op_stack = ("create_board",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_board"]


@task
async def create_board_activity_logs(
    board_name: str,
    board_kind: graphql_schema.BoardKind,
    monday_credentials: MondayCredentials,
    folder_id: int = None,
    workspace_id: int = None,
    template_id: int = None,
    board_owner_ids: Iterable[int] = None,
    board_subscriber_ids: Iterable[int] = None,
    limit: int = 25,
    page: int = 1,
    user_ids: Iterable[int] = None,
    column_ids: Iterable[str] = None,
    group_ids: Iterable[str] = None,
    item_ids: Iterable[int] = None,
    from_: datetime = None,
    to: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new board.

    Args:
        board_name: The board's name.
        board_kind: The board's kind (public / private / share).
        monday_credentials: Credentials to use for authentication with Monday.
        folder_id: Optional board folder id.
        workspace_id: Optional workspace id.
        template_id: Optional board template id.
        board_owner_ids: Optional board owner ids.
        board_subscriber_ids: Optional board subscriber ids.
        limit: None.
        page: None.
        user_ids: None.
        column_ids: None.
        group_ids: None.
        item_ids: None.
        from_: None.
        to: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_board(
        **strip_kwargs(
            input=dict(
                board_name=board_name,
                board_kind=board_kind,
                folder_id=folder_id,
                workspace_id=workspace_id,
                template_id=template_id,
                board_owner_ids=board_owner_ids,
                board_subscriber_ids=board_subscriber_ids,
            )
        )
    ).activity_logs(
        **strip_kwargs(
            input=dict(
                limit=limit,
                page=page,
                user_ids=user_ids,
                column_ids=column_ids,
                group_ids=group_ids,
                item_ids=item_ids,
                from_=from_,
                to=to,
            )
        )
    )

    op_stack = (
        "create_board",
        "activity_logs",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_board"]["activity_logs"]


@task
async def create_board_columns(
    board_name: str,
    board_kind: graphql_schema.BoardKind,
    monday_credentials: MondayCredentials,
    folder_id: int = None,
    workspace_id: int = None,
    template_id: int = None,
    board_owner_ids: Iterable[int] = None,
    board_subscriber_ids: Iterable[int] = None,
    ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new board.

    Args:
        board_name: The board's name.
        board_kind: The board's kind (public / private / share).
        monday_credentials: Credentials to use for authentication with Monday.
        folder_id: Optional board folder id.
        workspace_id: Optional workspace id.
        template_id: Optional board template id.
        board_owner_ids: Optional board owner ids.
        board_subscriber_ids: Optional board subscriber ids.
        ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_board(
        **strip_kwargs(
            input=dict(
                board_name=board_name,
                board_kind=board_kind,
                folder_id=folder_id,
                workspace_id=workspace_id,
                template_id=template_id,
                board_owner_ids=board_owner_ids,
                board_subscriber_ids=board_subscriber_ids,
            )
        )
    ).columns(
        **strip_kwargs(
            input=dict(
                ids=ids,
            )
        )
    )

    op_stack = (
        "create_board",
        "columns",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_board"]["columns"]


@task
async def create_board_creator(
    board_name: str,
    board_kind: graphql_schema.BoardKind,
    monday_credentials: MondayCredentials,
    folder_id: int = None,
    workspace_id: int = None,
    template_id: int = None,
    board_owner_ids: Iterable[int] = None,
    board_subscriber_ids: Iterable[int] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new board.

    Args:
        board_name: The board's name.
        board_kind: The board's kind (public / private / share).
        monday_credentials: Credentials to use for authentication with Monday.
        folder_id: Optional board folder id.
        workspace_id: Optional workspace id.
        template_id: Optional board template id.
        board_owner_ids: Optional board owner ids.
        board_subscriber_ids: Optional board subscriber ids.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_board(
        **strip_kwargs(
            input=dict(
                board_name=board_name,
                board_kind=board_kind,
                folder_id=folder_id,
                workspace_id=workspace_id,
                template_id=template_id,
                board_owner_ids=board_owner_ids,
                board_subscriber_ids=board_subscriber_ids,
            )
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "create_board",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_board"]["creator"]


@task
async def create_board_groups(
    board_name: str,
    board_kind: graphql_schema.BoardKind,
    monday_credentials: MondayCredentials,
    folder_id: int = None,
    workspace_id: int = None,
    template_id: int = None,
    board_owner_ids: Iterable[int] = None,
    board_subscriber_ids: Iterable[int] = None,
    ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new board.

    Args:
        board_name: The board's name.
        board_kind: The board's kind (public / private / share).
        monday_credentials: Credentials to use for authentication with Monday.
        folder_id: Optional board folder id.
        workspace_id: Optional workspace id.
        template_id: Optional board template id.
        board_owner_ids: Optional board owner ids.
        board_subscriber_ids: Optional board subscriber ids.
        ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_board(
        **strip_kwargs(
            input=dict(
                board_name=board_name,
                board_kind=board_kind,
                folder_id=folder_id,
                workspace_id=workspace_id,
                template_id=template_id,
                board_owner_ids=board_owner_ids,
                board_subscriber_ids=board_subscriber_ids,
            )
        )
    ).groups(
        **strip_kwargs(
            input=dict(
                ids=ids,
            )
        )
    )

    op_stack = (
        "create_board",
        "groups",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_board"]["groups"]


@task
async def create_board_items(
    board_name: str,
    board_kind: graphql_schema.BoardKind,
    monday_credentials: MondayCredentials,
    folder_id: int = None,
    workspace_id: int = None,
    template_id: int = None,
    board_owner_ids: Iterable[int] = None,
    board_subscriber_ids: Iterable[int] = None,
    ids: Iterable[int] = None,
    limit: int = None,
    page: int = 1,
    newest_first: bool = None,
    exclude_nonactive: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new board.

    Args:
        board_name: The board's name.
        board_kind: The board's kind (public / private / share).
        monday_credentials: Credentials to use for authentication with Monday.
        folder_id: Optional board folder id.
        workspace_id: Optional workspace id.
        template_id: Optional board template id.
        board_owner_ids: Optional board owner ids.
        board_subscriber_ids: Optional board subscriber ids.
        ids: None.
        limit: None.
        page: None.
        newest_first: None.
        exclude_nonactive: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_board(
        **strip_kwargs(
            input=dict(
                board_name=board_name,
                board_kind=board_kind,
                folder_id=folder_id,
                workspace_id=workspace_id,
                template_id=template_id,
                board_owner_ids=board_owner_ids,
                board_subscriber_ids=board_subscriber_ids,
            )
        )
    ).items(
        **strip_kwargs(
            input=dict(
                ids=ids,
                limit=limit,
                page=page,
                newest_first=newest_first,
                exclude_nonactive=exclude_nonactive,
            )
        )
    )

    op_stack = (
        "create_board",
        "items",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_board"]["items"]


@task
async def create_board_owner(
    board_name: str,
    board_kind: graphql_schema.BoardKind,
    monday_credentials: MondayCredentials,
    folder_id: int = None,
    workspace_id: int = None,
    template_id: int = None,
    board_owner_ids: Iterable[int] = None,
    board_subscriber_ids: Iterable[int] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new board.

    Args:
        board_name: The board's name.
        board_kind: The board's kind (public / private / share).
        monday_credentials: Credentials to use for authentication with Monday.
        folder_id: Optional board folder id.
        workspace_id: Optional workspace id.
        template_id: Optional board template id.
        board_owner_ids: Optional board owner ids.
        board_subscriber_ids: Optional board subscriber ids.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_board(
        **strip_kwargs(
            input=dict(
                board_name=board_name,
                board_kind=board_kind,
                folder_id=folder_id,
                workspace_id=workspace_id,
                template_id=template_id,
                board_owner_ids=board_owner_ids,
                board_subscriber_ids=board_subscriber_ids,
            )
        )
    ).owner(**strip_kwargs())

    op_stack = (
        "create_board",
        "owner",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_board"]["owner"]


@task
async def create_board_owners(
    board_name: str,
    board_kind: graphql_schema.BoardKind,
    monday_credentials: MondayCredentials,
    folder_id: int = None,
    workspace_id: int = None,
    template_id: int = None,
    board_owner_ids: Iterable[int] = None,
    board_subscriber_ids: Iterable[int] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new board.

    Args:
        board_name: The board's name.
        board_kind: The board's kind (public / private / share).
        monday_credentials: Credentials to use for authentication with Monday.
        folder_id: Optional board folder id.
        workspace_id: Optional workspace id.
        template_id: Optional board template id.
        board_owner_ids: Optional board owner ids.
        board_subscriber_ids: Optional board subscriber ids.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_board(
        **strip_kwargs(
            input=dict(
                board_name=board_name,
                board_kind=board_kind,
                folder_id=folder_id,
                workspace_id=workspace_id,
                template_id=template_id,
                board_owner_ids=board_owner_ids,
                board_subscriber_ids=board_subscriber_ids,
            )
        )
    ).owners(**strip_kwargs())

    op_stack = (
        "create_board",
        "owners",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_board"]["owners"]


@task
async def create_board_subscribers(
    board_name: str,
    board_kind: graphql_schema.BoardKind,
    monday_credentials: MondayCredentials,
    folder_id: int = None,
    workspace_id: int = None,
    template_id: int = None,
    board_owner_ids: Iterable[int] = None,
    board_subscriber_ids: Iterable[int] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new board.

    Args:
        board_name: The board's name.
        board_kind: The board's kind (public / private / share).
        monday_credentials: Credentials to use for authentication with Monday.
        folder_id: Optional board folder id.
        workspace_id: Optional workspace id.
        template_id: Optional board template id.
        board_owner_ids: Optional board owner ids.
        board_subscriber_ids: Optional board subscriber ids.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_board(
        **strip_kwargs(
            input=dict(
                board_name=board_name,
                board_kind=board_kind,
                folder_id=folder_id,
                workspace_id=workspace_id,
                template_id=template_id,
                board_owner_ids=board_owner_ids,
                board_subscriber_ids=board_subscriber_ids,
            )
        )
    ).subscribers(**strip_kwargs())

    op_stack = (
        "create_board",
        "subscribers",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_board"]["subscribers"]


@task
async def create_board_tags(
    board_name: str,
    board_kind: graphql_schema.BoardKind,
    monday_credentials: MondayCredentials,
    folder_id: int = None,
    workspace_id: int = None,
    template_id: int = None,
    board_owner_ids: Iterable[int] = None,
    board_subscriber_ids: Iterable[int] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new board.

    Args:
        board_name: The board's name.
        board_kind: The board's kind (public / private / share).
        monday_credentials: Credentials to use for authentication with Monday.
        folder_id: Optional board folder id.
        workspace_id: Optional workspace id.
        template_id: Optional board template id.
        board_owner_ids: Optional board owner ids.
        board_subscriber_ids: Optional board subscriber ids.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_board(
        **strip_kwargs(
            input=dict(
                board_name=board_name,
                board_kind=board_kind,
                folder_id=folder_id,
                workspace_id=workspace_id,
                template_id=template_id,
                board_owner_ids=board_owner_ids,
                board_subscriber_ids=board_subscriber_ids,
            )
        )
    ).tags(**strip_kwargs())

    op_stack = (
        "create_board",
        "tags",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_board"]["tags"]


@task
async def create_board_top_group(
    board_name: str,
    board_kind: graphql_schema.BoardKind,
    monday_credentials: MondayCredentials,
    folder_id: int = None,
    workspace_id: int = None,
    template_id: int = None,
    board_owner_ids: Iterable[int] = None,
    board_subscriber_ids: Iterable[int] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new board.

    Args:
        board_name: The board's name.
        board_kind: The board's kind (public / private / share).
        monday_credentials: Credentials to use for authentication with Monday.
        folder_id: Optional board folder id.
        workspace_id: Optional workspace id.
        template_id: Optional board template id.
        board_owner_ids: Optional board owner ids.
        board_subscriber_ids: Optional board subscriber ids.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_board(
        **strip_kwargs(
            input=dict(
                board_name=board_name,
                board_kind=board_kind,
                folder_id=folder_id,
                workspace_id=workspace_id,
                template_id=template_id,
                board_owner_ids=board_owner_ids,
                board_subscriber_ids=board_subscriber_ids,
            )
        )
    ).top_group(**strip_kwargs())

    op_stack = (
        "create_board",
        "top_group",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_board"]["top_group"]


@task
async def create_board_updates(
    board_name: str,
    board_kind: graphql_schema.BoardKind,
    monday_credentials: MondayCredentials,
    folder_id: int = None,
    workspace_id: int = None,
    template_id: int = None,
    board_owner_ids: Iterable[int] = None,
    board_subscriber_ids: Iterable[int] = None,
    limit: int = 25,
    page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new board.

    Args:
        board_name: The board's name.
        board_kind: The board's kind (public / private / share).
        monday_credentials: Credentials to use for authentication with Monday.
        folder_id: Optional board folder id.
        workspace_id: Optional workspace id.
        template_id: Optional board template id.
        board_owner_ids: Optional board owner ids.
        board_subscriber_ids: Optional board subscriber ids.
        limit: None.
        page: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_board(
        **strip_kwargs(
            input=dict(
                board_name=board_name,
                board_kind=board_kind,
                folder_id=folder_id,
                workspace_id=workspace_id,
                template_id=template_id,
                board_owner_ids=board_owner_ids,
                board_subscriber_ids=board_subscriber_ids,
            )
        )
    ).updates(
        **strip_kwargs(
            input=dict(
                limit=limit,
                page=page,
            )
        )
    )

    op_stack = (
        "create_board",
        "updates",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_board"]["updates"]


@task
async def create_board_views(
    board_name: str,
    board_kind: graphql_schema.BoardKind,
    monday_credentials: MondayCredentials,
    folder_id: int = None,
    workspace_id: int = None,
    template_id: int = None,
    board_owner_ids: Iterable[int] = None,
    board_subscriber_ids: Iterable[int] = None,
    ids: Iterable[int] = None,
    type: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new board.

    Args:
        board_name: The board's name.
        board_kind: The board's kind (public / private / share).
        monday_credentials: Credentials to use for authentication with Monday.
        folder_id: Optional board folder id.
        workspace_id: Optional workspace id.
        template_id: Optional board template id.
        board_owner_ids: Optional board owner ids.
        board_subscriber_ids: Optional board subscriber ids.
        ids: None.
        type: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_board(
        **strip_kwargs(
            input=dict(
                board_name=board_name,
                board_kind=board_kind,
                folder_id=folder_id,
                workspace_id=workspace_id,
                template_id=template_id,
                board_owner_ids=board_owner_ids,
                board_subscriber_ids=board_subscriber_ids,
            )
        )
    ).views(
        **strip_kwargs(
            input=dict(
                ids=ids,
                type=type,
            )
        )
    )

    op_stack = (
        "create_board",
        "views",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_board"]["views"]


@task
async def create_board_workspace(
    board_name: str,
    board_kind: graphql_schema.BoardKind,
    monday_credentials: MondayCredentials,
    folder_id: int = None,
    workspace_id: int = None,
    template_id: int = None,
    board_owner_ids: Iterable[int] = None,
    board_subscriber_ids: Iterable[int] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new board.

    Args:
        board_name: The board's name.
        board_kind: The board's kind (public / private / share).
        monday_credentials: Credentials to use for authentication with Monday.
        folder_id: Optional board folder id.
        workspace_id: Optional workspace id.
        template_id: Optional board template id.
        board_owner_ids: Optional board owner ids.
        board_subscriber_ids: Optional board subscriber ids.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_board(
        **strip_kwargs(
            input=dict(
                board_name=board_name,
                board_kind=board_kind,
                folder_id=folder_id,
                workspace_id=workspace_id,
                template_id=template_id,
                board_owner_ids=board_owner_ids,
                board_subscriber_ids=board_subscriber_ids,
            )
        )
    ).workspace(**strip_kwargs())

    op_stack = (
        "create_board",
        "workspace",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_board"]["workspace"]
@task
async def create_column(
    board_id: int,
    title: str,
    monday_credentials: MondayCredentials,
    description: str = None,
    column_type: graphql_schema.ColumnType = None,
    defaults: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new column in board.

    Args:
        board_id: The board's unique identifier.
        title: The new column's title.
        monday_credentials: Credentials to use for authentication with Monday.
        description: The new column's description.
        column_type: The type of column to create.
        defaults: The new column's defaults.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_column(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
                title=title,
                description=description,
                column_type=column_type,
                defaults=defaults,
            )
        )
    )

    op_stack = ("create_column",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_column"]
@task
async def create_group(
    board_id: int,
    group_name: str,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Creates a new group in a specific board.

    Args:
        board_id: The board's unique identifier.
        group_name: The name of the new group.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_group(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
                group_name=group_name,
            )
        )
    )

    op_stack = ("create_group",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_group"]


@task
async def create_group_items(
    board_id: int,
    group_name: str,
    monday_credentials: MondayCredentials,
    ids: Iterable[int] = None,
    limit: int = None,
    page: int = 1,
    newest_first: bool = None,
    exclude_nonactive: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Creates a new group in a specific board.

    Args:
        board_id: The board's unique identifier.
        group_name: The name of the new group.
        monday_credentials: Credentials to use for authentication with Monday.
        ids: None.
        limit: None.
        page: None.
        newest_first: None.
        exclude_nonactive: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_group(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
                group_name=group_name,
            )
        )
    ).items(
        **strip_kwargs(
            input=dict(
                ids=ids,
                limit=limit,
                page=page,
                newest_first=newest_first,
                exclude_nonactive=exclude_nonactive,
            )
        )
    )

    op_stack = (
        "create_group",
        "items",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_group"]["items"]
@task
async def create_item(
    board_id: int,
    monday_credentials: MondayCredentials,
    item_name: str = None,
    group_id: str = None,
    column_values: datetime = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new item.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        item_name: The new item's name.
        group_id: The group's unique identifier.
        column_values: The column values of the new item.
        create_labels_if_missing: Create Status/Dropdown labels if they're
            missing. (Requires permission to change board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_item(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
                item_name=item_name,
                group_id=group_id,
                column_values=column_values,
                create_labels_if_missing=create_labels_if_missing,
            )
        )
    )

    op_stack = ("create_item",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_item"]


@task
async def create_item_assets(
    board_id: int,
    monday_credentials: MondayCredentials,
    item_name: str = None,
    group_id: str = None,
    column_values: datetime = None,
    create_labels_if_missing: bool = None,
    assets_source: graphql_schema.AssetsSource = None,
    column_ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new item.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        item_name: The new item's name.
        group_id: The group's unique identifier.
        column_values: The column values of the new item.
        create_labels_if_missing: Create Status/Dropdown labels if
            they're missing. (Requires permission to change board
            structure).
        assets_source: None.
        column_ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_item(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
                item_name=item_name,
                group_id=group_id,
                column_values=column_values,
                create_labels_if_missing=create_labels_if_missing,
            )
        )
    ).assets(
        **strip_kwargs(
            input=dict(
                assets_source=assets_source,
                column_ids=column_ids,
            )
        )
    )

    op_stack = (
        "create_item",
        "assets",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_item"]["assets"]


@task
async def create_item_board(
    board_id: int,
    monday_credentials: MondayCredentials,
    item_name: str = None,
    group_id: str = None,
    column_values: datetime = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new item.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        item_name: The new item's name.
        group_id: The group's unique identifier.
        column_values: The column values of the new item.
        create_labels_if_missing: Create Status/Dropdown labels if
            they're missing. (Requires permission to change board
            structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_item(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
                item_name=item_name,
                group_id=group_id,
                column_values=column_values,
                create_labels_if_missing=create_labels_if_missing,
            )
        )
    ).board(**strip_kwargs())

    op_stack = (
        "create_item",
        "board",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_item"]["board"]


@task
async def create_item_column_values(
    board_id: int,
    monday_credentials: MondayCredentials,
    item_name: str = None,
    group_id: str = None,
    column_values: datetime = None,
    create_labels_if_missing: bool = None,
    ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new item.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        item_name: The new item's name.
        group_id: The group's unique identifier.
        column_values: The column values of the new item.
        create_labels_if_missing: Create Status/Dropdown labels if
            they're missing. (Requires permission to change board
            structure).
        ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_item(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
                item_name=item_name,
                group_id=group_id,
                column_values=column_values,
                create_labels_if_missing=create_labels_if_missing,
            )
        )
    ).column_values(
        **strip_kwargs(
            input=dict(
                ids=ids,
            )
        )
    )

    op_stack = (
        "create_item",
        "column_values",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_item"]["column_values"]


@task
async def create_item_creator(
    board_id: int,
    monday_credentials: MondayCredentials,
    item_name: str = None,
    group_id: str = None,
    column_values: datetime = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new item.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        item_name: The new item's name.
        group_id: The group's unique identifier.
        column_values: The column values of the new item.
        create_labels_if_missing: Create Status/Dropdown labels if
            they're missing. (Requires permission to change board
            structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_item(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
                item_name=item_name,
                group_id=group_id,
                column_values=column_values,
                create_labels_if_missing=create_labels_if_missing,
            )
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "create_item",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_item"]["creator"]


@task
async def create_item_group(
    board_id: int,
    monday_credentials: MondayCredentials,
    item_name: str = None,
    group_id: str = None,
    column_values: datetime = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new item.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        item_name: The new item's name.
        group_id: The group's unique identifier.
        column_values: The column values of the new item.
        create_labels_if_missing: Create Status/Dropdown labels if
            they're missing. (Requires permission to change board
            structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_item(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
                item_name=item_name,
                group_id=group_id,
                column_values=column_values,
                create_labels_if_missing=create_labels_if_missing,
            )
        )
    ).group(**strip_kwargs())

    op_stack = (
        "create_item",
        "group",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_item"]["group"]


@task
async def create_item_subitems(
    board_id: int,
    monday_credentials: MondayCredentials,
    item_name: str = None,
    group_id: str = None,
    column_values: datetime = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new item.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        item_name: The new item's name.
        group_id: The group's unique identifier.
        column_values: The column values of the new item.
        create_labels_if_missing: Create Status/Dropdown labels if
            they're missing. (Requires permission to change board
            structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_item(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
                item_name=item_name,
                group_id=group_id,
                column_values=column_values,
                create_labels_if_missing=create_labels_if_missing,
            )
        )
    ).subitems(**strip_kwargs())

    op_stack = (
        "create_item",
        "subitems",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_item"]["subitems"]


@task
async def create_item_subscribers(
    board_id: int,
    monday_credentials: MondayCredentials,
    item_name: str = None,
    group_id: str = None,
    column_values: datetime = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new item.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        item_name: The new item's name.
        group_id: The group's unique identifier.
        column_values: The column values of the new item.
        create_labels_if_missing: Create Status/Dropdown labels if
            they're missing. (Requires permission to change board
            structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_item(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
                item_name=item_name,
                group_id=group_id,
                column_values=column_values,
                create_labels_if_missing=create_labels_if_missing,
            )
        )
    ).subscribers(**strip_kwargs())

    op_stack = (
        "create_item",
        "subscribers",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_item"]["subscribers"]


@task
async def create_item_updates(
    board_id: int,
    monday_credentials: MondayCredentials,
    item_name: str = None,
    group_id: str = None,
    column_values: datetime = None,
    create_labels_if_missing: bool = None,
    limit: int = 25,
    page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new item.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        item_name: The new item's name.
        group_id: The group's unique identifier.
        column_values: The column values of the new item.
        create_labels_if_missing: Create Status/Dropdown labels if
            they're missing. (Requires permission to change board
            structure).
        limit: None.
        page: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_item(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
                item_name=item_name,
                group_id=group_id,
                column_values=column_values,
                create_labels_if_missing=create_labels_if_missing,
            )
        )
    ).updates(
        **strip_kwargs(
            input=dict(
                limit=limit,
                page=page,
            )
        )
    )

    op_stack = (
        "create_item",
        "updates",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_item"]["updates"]
@task
async def create_notification(
    text: str,
    user_id: int,
    target_id: int,
    target_type: graphql_schema.NotificationTargetType,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new notification.

    Args:
        text: The notification text.
        user_id: The user's unique identifier.
        target_id: The target's unique identifier.
        target_type: The target's type (Project / Post).
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_notification(
        **strip_kwargs(
            input=dict(
                text=text,
                user_id=user_id,
                target_id=target_id,
                target_type=target_type,
            )
        )
    )

    op_stack = ("create_notification",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_notification"]
@task
async def create_update(
    body: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    parent_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new update.

    Args:
        body: The update text.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        parent_id: The parent post identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_update(
        **strip_kwargs(
            input=dict(
                body=body,
                item_id=item_id,
                parent_id=parent_id,
            )
        )
    )

    op_stack = ("create_update",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_update"]


@task
async def create_update_assets(
    body: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    parent_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new update.

    Args:
        body: The update text.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        parent_id: The parent post identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_update(
        **strip_kwargs(
            input=dict(
                body=body,
                item_id=item_id,
                parent_id=parent_id,
            )
        )
    ).assets(**strip_kwargs())

    op_stack = (
        "create_update",
        "assets",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_update"]["assets"]


@task
async def create_update_creator(
    body: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    parent_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new update.

    Args:
        body: The update text.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        parent_id: The parent post identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_update(
        **strip_kwargs(
            input=dict(
                body=body,
                item_id=item_id,
                parent_id=parent_id,
            )
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "create_update",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_update"]["creator"]


@task
async def create_update_replies(
    body: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    parent_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new update.

    Args:
        body: The update text.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        parent_id: The parent post identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_update(
        **strip_kwargs(
            input=dict(
                body=body,
                item_id=item_id,
                parent_id=parent_id,
            )
        )
    ).replies(**strip_kwargs())

    op_stack = (
        "create_update",
        "replies",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_update"]["replies"]
@task
async def create_subitem(
    monday_credentials: MondayCredentials,
    parent_item_id: int = None,
    item_name: str = None,
    column_values: datetime = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create subitem.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        parent_item_id: The parent item's unique identifier.
        item_name: The new item's name.
        column_values: The column values of the new item.
        create_labels_if_missing: Create Status/Dropdown labels if they're
            missing. (Requires permission to change board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_subitem(
        **strip_kwargs(
            input=dict(
                parent_item_id=parent_item_id,
                item_name=item_name,
                column_values=column_values,
                create_labels_if_missing=create_labels_if_missing,
            )
        )
    )

    op_stack = ("create_subitem",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_subitem"]


@task
async def create_subitem_assets(
    monday_credentials: MondayCredentials,
    parent_item_id: int = None,
    item_name: str = None,
    column_values: datetime = None,
    create_labels_if_missing: bool = None,
    assets_source: graphql_schema.AssetsSource = None,
    column_ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create subitem.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        parent_item_id: The parent item's unique identifier.
        item_name: The new item's name.
        column_values: The column values of the new item.
        create_labels_if_missing: Create Status/Dropdown labels
            if they're missing. (Requires permission to change board
            structure).
        assets_source: None.
        column_ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_subitem(
        **strip_kwargs(
            input=dict(
                parent_item_id=parent_item_id,
                item_name=item_name,
                column_values=column_values,
                create_labels_if_missing=create_labels_if_missing,
            )
        )
    ).assets(
        **strip_kwargs(
            input=dict(
                assets_source=assets_source,
                column_ids=column_ids,
            )
        )
    )

    op_stack = (
        "create_subitem",
        "assets",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_subitem"]["assets"]


@task
async def create_subitem_board(
    monday_credentials: MondayCredentials,
    parent_item_id: int = None,
    item_name: str = None,
    column_values: datetime = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create subitem.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        parent_item_id: The parent item's unique identifier.
        item_name: The new item's name.
        column_values: The column values of the new item.
        create_labels_if_missing: Create Status/Dropdown labels
            if they're missing. (Requires permission to change board
            structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_subitem(
        **strip_kwargs(
            input=dict(
                parent_item_id=parent_item_id,
                item_name=item_name,
                column_values=column_values,
                create_labels_if_missing=create_labels_if_missing,
            )
        )
    ).board(**strip_kwargs())

    op_stack = (
        "create_subitem",
        "board",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_subitem"]["board"]


@task
async def create_subitem_column_values(
    monday_credentials: MondayCredentials,
    parent_item_id: int = None,
    item_name: str = None,
    column_values: datetime = None,
    create_labels_if_missing: bool = None,
    ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create subitem.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        parent_item_id: The parent item's unique identifier.
        item_name: The new item's name.
        column_values: The column values of the new item.
        create_labels_if_missing: Create Status/Dropdown labels
            if they're missing. (Requires permission to change board
            structure).
        ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_subitem(
        **strip_kwargs(
            input=dict(
                parent_item_id=parent_item_id,
                item_name=item_name,
                column_values=column_values,
                create_labels_if_missing=create_labels_if_missing,
            )
        )
    ).column_values(
        **strip_kwargs(
            input=dict(
                ids=ids,
            )
        )
    )

    op_stack = (
        "create_subitem",
        "column_values",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_subitem"]["column_values"]


@task
async def create_subitem_creator(
    monday_credentials: MondayCredentials,
    parent_item_id: int = None,
    item_name: str = None,
    column_values: datetime = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create subitem.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        parent_item_id: The parent item's unique identifier.
        item_name: The new item's name.
        column_values: The column values of the new item.
        create_labels_if_missing: Create Status/Dropdown labels
            if they're missing. (Requires permission to change board
            structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_subitem(
        **strip_kwargs(
            input=dict(
                parent_item_id=parent_item_id,
                item_name=item_name,
                column_values=column_values,
                create_labels_if_missing=create_labels_if_missing,
            )
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "create_subitem",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_subitem"]["creator"]


@task
async def create_subitem_group(
    monday_credentials: MondayCredentials,
    parent_item_id: int = None,
    item_name: str = None,
    column_values: datetime = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create subitem.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        parent_item_id: The parent item's unique identifier.
        item_name: The new item's name.
        column_values: The column values of the new item.
        create_labels_if_missing: Create Status/Dropdown labels
            if they're missing. (Requires permission to change board
            structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_subitem(
        **strip_kwargs(
            input=dict(
                parent_item_id=parent_item_id,
                item_name=item_name,
                column_values=column_values,
                create_labels_if_missing=create_labels_if_missing,
            )
        )
    ).group(**strip_kwargs())

    op_stack = (
        "create_subitem",
        "group",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_subitem"]["group"]


@task
async def create_subitem_subitems(
    monday_credentials: MondayCredentials,
    parent_item_id: int = None,
    item_name: str = None,
    column_values: datetime = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create subitem.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        parent_item_id: The parent item's unique identifier.
        item_name: The new item's name.
        column_values: The column values of the new item.
        create_labels_if_missing: Create Status/Dropdown labels
            if they're missing. (Requires permission to change board
            structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_subitem(
        **strip_kwargs(
            input=dict(
                parent_item_id=parent_item_id,
                item_name=item_name,
                column_values=column_values,
                create_labels_if_missing=create_labels_if_missing,
            )
        )
    ).subitems(**strip_kwargs())

    op_stack = (
        "create_subitem",
        "subitems",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_subitem"]["subitems"]


@task
async def create_subitem_subscribers(
    monday_credentials: MondayCredentials,
    parent_item_id: int = None,
    item_name: str = None,
    column_values: datetime = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create subitem.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        parent_item_id: The parent item's unique identifier.
        item_name: The new item's name.
        column_values: The column values of the new item.
        create_labels_if_missing: Create Status/Dropdown labels
            if they're missing. (Requires permission to change board
            structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_subitem(
        **strip_kwargs(
            input=dict(
                parent_item_id=parent_item_id,
                item_name=item_name,
                column_values=column_values,
                create_labels_if_missing=create_labels_if_missing,
            )
        )
    ).subscribers(**strip_kwargs())

    op_stack = (
        "create_subitem",
        "subscribers",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_subitem"]["subscribers"]


@task
async def create_subitem_updates(
    monday_credentials: MondayCredentials,
    parent_item_id: int = None,
    item_name: str = None,
    column_values: datetime = None,
    create_labels_if_missing: bool = None,
    limit: int = 25,
    page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create subitem.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        parent_item_id: The parent item's unique identifier.
        item_name: The new item's name.
        column_values: The column values of the new item.
        create_labels_if_missing: Create Status/Dropdown labels
            if they're missing. (Requires permission to change board
            structure).
        limit: None.
        page: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_subitem(
        **strip_kwargs(
            input=dict(
                parent_item_id=parent_item_id,
                item_name=item_name,
                column_values=column_values,
                create_labels_if_missing=create_labels_if_missing,
            )
        )
    ).updates(
        **strip_kwargs(
            input=dict(
                limit=limit,
                page=page,
            )
        )
    )

    op_stack = (
        "create_subitem",
        "updates",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_subitem"]["updates"]
@task
async def delete_item(
    monday_credentials: MondayCredentials,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete an item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_item(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    )

    op_stack = ("delete_item",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_item"]


@task
async def delete_item_assets(
    monday_credentials: MondayCredentials,
    item_id: int = None,
    assets_source: graphql_schema.AssetsSource = None,
    column_ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete an item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        assets_source: None.
        column_ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_item(**strip_kwargs(input=dict(item_id=item_id,))).assets(
        **strip_kwargs(
            input=dict(
                assets_source=assets_source,
                column_ids=column_ids,
            )
        )
    )

    op_stack = (
        "delete_item",
        "assets",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_item"]["assets"]


@task
async def delete_item_board(
    monday_credentials: MondayCredentials,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete an item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_item(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).board(**strip_kwargs())

    op_stack = (
        "delete_item",
        "board",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_item"]["board"]


@task
async def delete_item_column_values(
    monday_credentials: MondayCredentials,
    item_id: int = None,
    ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete an item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_item(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).column_values(
        **strip_kwargs(
            input=dict(
                ids=ids,
            )
        )
    )

    op_stack = (
        "delete_item",
        "column_values",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_item"]["column_values"]


@task
async def delete_item_creator(
    monday_credentials: MondayCredentials,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete an item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_item(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "delete_item",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_item"]["creator"]


@task
async def delete_item_group(
    monday_credentials: MondayCredentials,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete an item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_item(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).group(**strip_kwargs())

    op_stack = (
        "delete_item",
        "group",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_item"]["group"]


@task
async def delete_item_subitems(
    monday_credentials: MondayCredentials,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete an item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_item(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).subitems(**strip_kwargs())

    op_stack = (
        "delete_item",
        "subitems",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_item"]["subitems"]


@task
async def delete_item_subscribers(
    monday_credentials: MondayCredentials,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete an item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_item(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).subscribers(**strip_kwargs())

    op_stack = (
        "delete_item",
        "subscribers",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_item"]["subscribers"]


@task
async def delete_item_updates(
    monday_credentials: MondayCredentials,
    item_id: int = None,
    limit: int = 25,
    page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete an item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        limit: None.
        page: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_item(**strip_kwargs(input=dict(item_id=item_id,))).updates(
        **strip_kwargs(
            input=dict(
                limit=limit,
                page=page,
            )
        )
    )

    op_stack = (
        "delete_item",
        "updates",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_item"]["updates"]
@task
async def delete_update(
    id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete an update.

    Args:
        id: The update's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_update(
        **strip_kwargs(
            input=dict(
                id=id,
            )
        )
    )

    op_stack = ("delete_update",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_update"]


@task
async def delete_update_assets(
    id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete an update.

    Args:
        id: The update's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_update(
        **strip_kwargs(
            input=dict(
                id=id,
            )
        )
    ).assets(**strip_kwargs())

    op_stack = (
        "delete_update",
        "assets",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_update"]["assets"]


@task
async def delete_update_creator(
    id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete an update.

    Args:
        id: The update's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_update(
        **strip_kwargs(
            input=dict(
                id=id,
            )
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "delete_update",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_update"]["creator"]


@task
async def delete_update_replies(
    id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete an update.

    Args:
        id: The update's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_update(
        **strip_kwargs(
            input=dict(
                id=id,
            )
        )
    ).replies(**strip_kwargs())

    op_stack = (
        "delete_update",
        "replies",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_update"]["replies"]
@task
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
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.like_update(
        **strip_kwargs(
            input=dict(
                update_id=update_id,
            )
        )
    )

    op_stack = ("like_update",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["like_update"]


@task
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
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.like_update(
        **strip_kwargs(
            input=dict(
                update_id=update_id,
            )
        )
    ).assets(**strip_kwargs())

    op_stack = (
        "like_update",
        "assets",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["like_update"]["assets"]


@task
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
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.like_update(
        **strip_kwargs(
            input=dict(
                update_id=update_id,
            )
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "like_update",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["like_update"]["creator"]


@task
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
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.like_update(
        **strip_kwargs(
            input=dict(
                update_id=update_id,
            )
        )
    ).replies(**strip_kwargs())

    op_stack = (
        "like_update",
        "replies",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["like_update"]["replies"]
@task
async def add_file_to_column(
    item_id: int,
    column_id: str,
    file: datetime,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Add a file to a column value.

    Args:
        item_id: The item to add the file to.
        column_id: The column to add the file to.
        file: The file to upload.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.add_file_to_column(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
                column_id=column_id,
                file=file,
            )
        )
    )

    op_stack = ("add_file_to_column",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["add_file_to_column"]


@task
async def add_file_to_column_uploaded_by(
    item_id: int,
    column_id: str,
    file: datetime,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Add a file to a column value.

    Args:
        item_id: The item to add the file to.
        column_id: The column to add the file to.
        file: The file to upload.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.add_file_to_column(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
                column_id=column_id,
                file=file,
            )
        )
    ).uploaded_by(**strip_kwargs())

    op_stack = (
        "add_file_to_column",
        "uploaded_by",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["add_file_to_column"]["uploaded_by"]
@task
async def add_file_to_update(
    update_id: int,
    file: datetime,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Add a file to an update.

    Args:
        update_id: The update to add the file to.
        file: The file to upload.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.add_file_to_update(
        **strip_kwargs(
            input=dict(
                update_id=update_id,
                file=file,
            )
        )
    )

    op_stack = ("add_file_to_update",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["add_file_to_update"]


@task
async def add_file_to_update_uploaded_by(
    update_id: int,
    file: datetime,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Add a file to an update.

    Args:
        update_id: The update to add the file to.
        file: The file to upload.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.add_file_to_update(
        **strip_kwargs(
            input=dict(
                update_id=update_id,
                file=file,
            )
        )
    ).uploaded_by(**strip_kwargs())

    op_stack = (
        "add_file_to_update",
        "uploaded_by",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["add_file_to_update"]["uploaded_by"]
@task
async def archive_board(
    board_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_board(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
            )
        )
    )

    op_stack = ("archive_board",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_board"]


@task
async def archive_board_activity_logs(
    board_id: int,
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    user_ids: Iterable[int] = None,
    column_ids: Iterable[str] = None,
    group_ids: Iterable[str] = None,
    item_ids: Iterable[int] = None,
    from_: datetime = None,
    to: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        limit: None.
        page: None.
        user_ids: None.
        column_ids: None.
        group_ids: None.
        item_ids: None.
        from_: None.
        to: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_board(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
            )
        )
    ).activity_logs(
        **strip_kwargs(
            input=dict(
                limit=limit,
                page=page,
                user_ids=user_ids,
                column_ids=column_ids,
                group_ids=group_ids,
                item_ids=item_ids,
                from_=from_,
                to=to,
            )
        )
    )

    op_stack = (
        "archive_board",
        "activity_logs",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_board"]["activity_logs"]


@task
async def archive_board_columns(
    board_id: int,
    monday_credentials: MondayCredentials,
    ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_board(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
            )
        )
    ).columns(
        **strip_kwargs(
            input=dict(
                ids=ids,
            )
        )
    )

    op_stack = (
        "archive_board",
        "columns",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_board"]["columns"]


@task
async def archive_board_creator(
    board_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_board(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
            )
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "archive_board",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_board"]["creator"]


@task
async def archive_board_groups(
    board_id: int,
    monday_credentials: MondayCredentials,
    ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_board(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
            )
        )
    ).groups(
        **strip_kwargs(
            input=dict(
                ids=ids,
            )
        )
    )

    op_stack = (
        "archive_board",
        "groups",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_board"]["groups"]


@task
async def archive_board_items(
    board_id: int,
    monday_credentials: MondayCredentials,
    ids: Iterable[int] = None,
    limit: int = None,
    page: int = 1,
    newest_first: bool = None,
    exclude_nonactive: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        ids: None.
        limit: None.
        page: None.
        newest_first: None.
        exclude_nonactive: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_board(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
            )
        )
    ).items(
        **strip_kwargs(
            input=dict(
                ids=ids,
                limit=limit,
                page=page,
                newest_first=newest_first,
                exclude_nonactive=exclude_nonactive,
            )
        )
    )

    op_stack = (
        "archive_board",
        "items",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_board"]["items"]


@task
async def archive_board_owner(
    board_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_board(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
            )
        )
    ).owner(**strip_kwargs())

    op_stack = (
        "archive_board",
        "owner",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_board"]["owner"]


@task
async def archive_board_owners(
    board_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_board(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
            )
        )
    ).owners(**strip_kwargs())

    op_stack = (
        "archive_board",
        "owners",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_board"]["owners"]


@task
async def archive_board_subscribers(
    board_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_board(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
            )
        )
    ).subscribers(**strip_kwargs())

    op_stack = (
        "archive_board",
        "subscribers",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_board"]["subscribers"]


@task
async def archive_board_tags(
    board_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_board(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
            )
        )
    ).tags(**strip_kwargs())

    op_stack = (
        "archive_board",
        "tags",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_board"]["tags"]


@task
async def archive_board_top_group(
    board_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_board(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
            )
        )
    ).top_group(**strip_kwargs())

    op_stack = (
        "archive_board",
        "top_group",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_board"]["top_group"]


@task
async def archive_board_updates(
    board_id: int,
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        limit: None.
        page: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_board(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
            )
        )
    ).updates(
        **strip_kwargs(
            input=dict(
                limit=limit,
                page=page,
            )
        )
    )

    op_stack = (
        "archive_board",
        "updates",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_board"]["updates"]


@task
async def archive_board_views(
    board_id: int,
    monday_credentials: MondayCredentials,
    ids: Iterable[int] = None,
    type: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        ids: None.
        type: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_board(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
            )
        )
    ).views(
        **strip_kwargs(
            input=dict(
                ids=ids,
                type=type,
            )
        )
    )

    op_stack = (
        "archive_board",
        "views",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_board"]["views"]


@task
async def archive_board_workspace(
    board_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_board(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
            )
        )
    ).workspace(**strip_kwargs())

    op_stack = (
        "archive_board",
        "workspace",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_board"]["workspace"]
@task
async def archive_group(
    board_id: int,
    group_id: str,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archives a group in a specific board.

    Args:
        board_id: The board's unique identifier.
        group_id: The group's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_group(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
                group_id=group_id,
            )
        )
    )

    op_stack = ("archive_group",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_group"]


@task
async def archive_group_items(
    board_id: int,
    group_id: str,
    monday_credentials: MondayCredentials,
    ids: Iterable[int] = None,
    limit: int = None,
    page: int = 1,
    newest_first: bool = None,
    exclude_nonactive: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archives a group in a specific board.

    Args:
        board_id: The board's unique identifier.
        group_id: The group's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        ids: None.
        limit: None.
        page: None.
        newest_first: None.
        exclude_nonactive: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_group(
        **strip_kwargs(
            input=dict(
                board_id=board_id,
                group_id=group_id,
            )
        )
    ).items(
        **strip_kwargs(
            input=dict(
                ids=ids,
                limit=limit,
                page=page,
                newest_first=newest_first,
                exclude_nonactive=exclude_nonactive,
            )
        )
    )

    op_stack = (
        "archive_group",
        "items",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_group"]["items"]
@task
async def archive_item(
    monday_credentials: MondayCredentials,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive an item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_item(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    )

    op_stack = ("archive_item",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_item"]


@task
async def archive_item_assets(
    monday_credentials: MondayCredentials,
    item_id: int = None,
    assets_source: graphql_schema.AssetsSource = None,
    column_ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive an item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        assets_source: None.
        column_ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_item(**strip_kwargs(input=dict(item_id=item_id,))).assets(
        **strip_kwargs(
            input=dict(
                assets_source=assets_source,
                column_ids=column_ids,
            )
        )
    )

    op_stack = (
        "archive_item",
        "assets",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_item"]["assets"]


@task
async def archive_item_board(
    monday_credentials: MondayCredentials,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive an item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_item(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).board(**strip_kwargs())

    op_stack = (
        "archive_item",
        "board",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_item"]["board"]


@task
async def archive_item_column_values(
    monday_credentials: MondayCredentials,
    item_id: int = None,
    ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive an item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_item(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).column_values(
        **strip_kwargs(
            input=dict(
                ids=ids,
            )
        )
    )

    op_stack = (
        "archive_item",
        "column_values",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_item"]["column_values"]


@task
async def archive_item_creator(
    monday_credentials: MondayCredentials,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive an item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_item(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "archive_item",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_item"]["creator"]


@task
async def archive_item_group(
    monday_credentials: MondayCredentials,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive an item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_item(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).group(**strip_kwargs())

    op_stack = (
        "archive_item",
        "group",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_item"]["group"]


@task
async def archive_item_subitems(
    monday_credentials: MondayCredentials,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive an item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_item(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).subitems(**strip_kwargs())

    op_stack = (
        "archive_item",
        "subitems",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_item"]["subitems"]


@task
async def archive_item_subscribers(
    monday_credentials: MondayCredentials,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive an item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_item(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).subscribers(**strip_kwargs())

    op_stack = (
        "archive_item",
        "subscribers",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_item"]["subscribers"]


@task
async def archive_item_updates(
    monday_credentials: MondayCredentials,
    item_id: int = None,
    limit: int = 25,
    page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Archive an item.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        limit: None.
        page: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.archive_item(
        **strip_kwargs(
            input=dict(
                item_id=item_id,
            )
        )
    ).updates(
        **strip_kwargs(
            input=dict(
                limit=limit,
                page=page,
            )
        )
    )

    op_stack = (
        "archive_item",
        "updates",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_item"]["updates"]
@task
async def add_teams_to_workspace(
    workspace_id: int,
    team_ids: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Add teams to a workspace.

    Args:
        workspace_id: The workspace's unique identifier.
        team_ids: Team ids to subscribe to a workspace.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.add_teams_to_workspace(
        **strip_kwargs(
            input=dict(
                workspace_id=workspace_id,
                team_ids=team_ids,
            )
        )
    )

    op_stack = ("add_teams_to_workspace",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["add_teams_to_workspace"]


@task
async def add_teams_to_workspace_users(
    workspace_id: int,
    team_ids: int,
    monday_credentials: MondayCredentials,
    ids: Iterable[int] = None,
    kind: graphql_schema.UserKind = None,
    newest_first: bool = None,
    limit: int = None,
    emails: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Add teams to a workspace.

    Args:
        workspace_id: The workspace's unique identifier.
        team_ids: Team ids to subscribe to a workspace.
        monday_credentials: Credentials to use for authentication with Monday.
        ids: None.
        kind: None.
        newest_first: None.
        limit: None.
        emails: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.add_teams_to_workspace(
        **strip_kwargs(
            input=dict(
                workspace_id=workspace_id,
                team_ids=team_ids,
            )
        )
    ).users(
        **strip_kwargs(
            input=dict(
                ids=ids,
                kind=kind,
                newest_first=newest_first,
                limit=limit,
                emails=emails,
            )
        )
    )

    op_stack = (
        "add_teams_to_workspace",
        "users",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["add_teams_to_workspace"]["users"]
@task
async def add_users_to_workspace(
    workspace_id: int,
    user_ids: int,
    monday_credentials: MondayCredentials,
    kind: graphql_schema.WorkspaceSubscriberKind = "subscriber",
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Add users to a workspace.

    Args:
        workspace_id: The workspace's unique identifier.
        user_ids: User ids to subscribe to a workspace.
        monday_credentials: Credentials to use for authentication with Monday.
        kind: Subscribers kind (subscriber / owner).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.add_users_to_workspace(
        **strip_kwargs(
            input=dict(
                workspace_id=workspace_id,
                user_ids=user_ids,
                kind=kind,
            )
        )
    )

    op_stack = ("add_users_to_workspace",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["add_users_to_workspace"]


@task
async def add_users_to_workspace_account(
    workspace_id: int,
    user_ids: int,
    monday_credentials: MondayCredentials,
    kind: graphql_schema.WorkspaceSubscriberKind = "subscriber",
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Add users to a workspace.

    Args:
        workspace_id: The workspace's unique identifier.
        user_ids: User ids to subscribe to a workspace.
        monday_credentials: Credentials to use for authentication with Monday.
        kind: Subscribers kind (subscriber / owner).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.add_users_to_workspace(
        **strip_kwargs(
            input=dict(
                workspace_id=workspace_id,
                user_ids=user_ids,
                kind=kind,
            )
        )
    ).account(**strip_kwargs())

    op_stack = (
        "add_users_to_workspace",
        "account",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["add_users_to_workspace"]["account"]


@task
async def add_users_to_workspace_teams(
    workspace_id: int,
    user_ids: int,
    monday_credentials: MondayCredentials,
    kind: graphql_schema.WorkspaceSubscriberKind = "subscriber",
    ids: Iterable[int] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Add users to a workspace.

    Args:
        workspace_id: The workspace's unique identifier.
        user_ids: User ids to subscribe to a workspace.
        monday_credentials: Credentials to use for authentication with Monday.
        kind: Subscribers kind (subscriber / owner).
        ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.add_users_to_workspace(
        **strip_kwargs(
            input=dict(
                workspace_id=workspace_id,
                user_ids=user_ids,
                kind=kind,
            )
        )
    ).teams(
        **strip_kwargs(
            input=dict(
                ids=ids,
            )
        )
    )

    op_stack = (
        "add_users_to_workspace",
        "teams",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["add_users_to_workspace"]["teams"]
