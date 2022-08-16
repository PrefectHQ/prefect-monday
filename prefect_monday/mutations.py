"""
This is a module containing:
Monday mutation tasks

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

config_dir = Path(__file__).parent.resolve() / "configs" / "mutation"
return_fields_defaults = {}
for config_path in config_dir.glob("*.json"):
    return_fields_defaults.update(initialize_return_fields_defaults(config_path))


@task
async def change_simple_column_value(
    column_id: str,
    board_id: int,
    value: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change an item's column with simple value.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        value: The new simple value of the column.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create Status/Dropdown labels if they're
            missing. (Requires permission to change board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_simple_column_value(
        **strip_kwargs(
            column_id=column_id,
            board_id=board_id,
            value=value,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    )

    op_stack = ("change_simple_column_value",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_simple_column_value"]


@task
async def change_simple_column_value_board(
    column_id: str,
    board_id: int,
    value: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change an item's column with simple value.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        value: The new simple value of the column.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create
            Status/Dropdown labels if they're missing. (Requires
            permission to change board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_simple_column_value(
        **strip_kwargs(
            column_id=column_id,
            board_id=board_id,
            value=value,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).board(**strip_kwargs())

    op_stack = (
        "change_simple_column_value",
        "board",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_simple_column_value"]["board"]


@task
async def change_simple_column_value_group(
    column_id: str,
    board_id: int,
    value: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change an item's column with simple value.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        value: The new simple value of the column.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create
            Status/Dropdown labels if they're missing. (Requires
            permission to change board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_simple_column_value(
        **strip_kwargs(
            column_id=column_id,
            board_id=board_id,
            value=value,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).group(**strip_kwargs())

    op_stack = (
        "change_simple_column_value",
        "group",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_simple_column_value"]["group"]


@task
async def change_simple_column_value_assets(
    column_id: str,
    board_id: int,
    value: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    assets_source: graphql_schema.AssetsSource = None,
    column_ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change an item's column with simple value.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        value: The new simple value of the column.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create
            Status/Dropdown labels if they're missing. (Requires
            permission to change board structure).
        assets_source: None.
        column_ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_simple_column_value(
        **strip_kwargs(
            column_id=column_id,
            board_id=board_id,
            value=value,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).assets(
        **strip_kwargs(
            assets_source=assets_source,
            column_ids=column_ids,
        )
    )

    op_stack = (
        "change_simple_column_value",
        "assets",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_simple_column_value"]["assets"]


@task
async def change_simple_column_value_creator(
    column_id: str,
    board_id: int,
    value: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change an item's column with simple value.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        value: The new simple value of the column.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create
            Status/Dropdown labels if they're missing. (Requires
            permission to change board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_simple_column_value(
        **strip_kwargs(
            column_id=column_id,
            board_id=board_id,
            value=value,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "change_simple_column_value",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_simple_column_value"]["creator"]


@task
async def change_simple_column_value_updates(
    column_id: str,
    board_id: int,
    value: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    limit: int = 25,
    page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change an item's column with simple value.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        value: The new simple value of the column.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create
            Status/Dropdown labels if they're missing. (Requires
            permission to change board structure).
        limit: None.
        page: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_simple_column_value(
        **strip_kwargs(
            column_id=column_id,
            board_id=board_id,
            value=value,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).updates(
        **strip_kwargs(
            limit=limit,
            page=page,
        )
    )

    op_stack = (
        "change_simple_column_value",
        "updates",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_simple_column_value"]["updates"]


@task
async def change_simple_column_value_subitems(
    column_id: str,
    board_id: int,
    value: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change an item's column with simple value.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        value: The new simple value of the column.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create
            Status/Dropdown labels if they're missing. (Requires
            permission to change board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_simple_column_value(
        **strip_kwargs(
            column_id=column_id,
            board_id=board_id,
            value=value,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).subitems(**strip_kwargs())

    op_stack = (
        "change_simple_column_value",
        "subitems",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_simple_column_value"]["subitems"]


@task
async def change_simple_column_value_subscribers(
    column_id: str,
    board_id: int,
    value: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change an item's column with simple value.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        value: The new simple value of the column.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create
            Status/Dropdown labels if they're missing. (Requires
            permission to change board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_simple_column_value(
        **strip_kwargs(
            column_id=column_id,
            board_id=board_id,
            value=value,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).subscribers(**strip_kwargs())

    op_stack = (
        "change_simple_column_value",
        "subscribers",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_simple_column_value"]["subscribers"]


@task
async def change_simple_column_value_column_values(
    column_id: str,
    board_id: int,
    value: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change an item's column with simple value.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        value: The new simple value of the column.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create
            Status/Dropdown labels if they're missing. (Requires
            permission to change board structure).
        ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_simple_column_value(
        **strip_kwargs(
            column_id=column_id,
            board_id=board_id,
            value=value,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).column_values(
        **strip_kwargs(
            ids=ids,
        )
    )

    op_stack = (
        "change_simple_column_value",
        "column_values",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_simple_column_value"]["column_values"]


@task
async def remove_mock_app_subscription(
    app_id: int,
    partial_signing_secret: str,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Remove mock app subscription for the current account.

    Args:
        app_id: The app id of the app to remove the mocked subscription for.
        partial_signing_secret: The last 10 characters of the app's signing
            secret.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.remove_mock_app_subscription(
        **strip_kwargs(
            app_id=app_id,
            partial_signing_secret=partial_signing_secret,
        )
    )

    op_stack = ("remove_mock_app_subscription",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["remove_mock_app_subscription"]


@task
async def change_multiple_column_values(
    board_id: int,
    column_values: datetime,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Changes the column values of a specific item.

    Args:
        board_id: The board's unique identifier.
        column_values: The column values updates.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create Status/Dropdown labels if they're
            missing. (Requires permission to change board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_multiple_column_values(
        **strip_kwargs(
            board_id=board_id,
            column_values=column_values,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    )

    op_stack = ("change_multiple_column_values",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_multiple_column_values"]


@task
async def change_multiple_column_values_board(
    board_id: int,
    column_values: datetime,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Changes the column values of a specific item.

    Args:
        board_id: The board's unique identifier.
        column_values: The column values updates.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create
            Status/Dropdown labels if they're missing. (Requires
            permission to change board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_multiple_column_values(
        **strip_kwargs(
            board_id=board_id,
            column_values=column_values,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).board(**strip_kwargs())

    op_stack = (
        "change_multiple_column_values",
        "board",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_multiple_column_values"]["board"]


@task
async def change_multiple_column_values_group(
    board_id: int,
    column_values: datetime,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Changes the column values of a specific item.

    Args:
        board_id: The board's unique identifier.
        column_values: The column values updates.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create
            Status/Dropdown labels if they're missing. (Requires
            permission to change board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_multiple_column_values(
        **strip_kwargs(
            board_id=board_id,
            column_values=column_values,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).group(**strip_kwargs())

    op_stack = (
        "change_multiple_column_values",
        "group",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_multiple_column_values"]["group"]


@task
async def change_multiple_column_values_assets(
    board_id: int,
    column_values: datetime,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    assets_source: graphql_schema.AssetsSource = None,
    column_ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Changes the column values of a specific item.

    Args:
        board_id: The board's unique identifier.
        column_values: The column values updates.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create
            Status/Dropdown labels if they're missing. (Requires
            permission to change board structure).
        assets_source: None.
        column_ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_multiple_column_values(
        **strip_kwargs(
            board_id=board_id,
            column_values=column_values,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).assets(
        **strip_kwargs(
            assets_source=assets_source,
            column_ids=column_ids,
        )
    )

    op_stack = (
        "change_multiple_column_values",
        "assets",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_multiple_column_values"]["assets"]


@task
async def change_multiple_column_values_creator(
    board_id: int,
    column_values: datetime,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Changes the column values of a specific item.

    Args:
        board_id: The board's unique identifier.
        column_values: The column values updates.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create
            Status/Dropdown labels if they're missing. (Requires
            permission to change board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_multiple_column_values(
        **strip_kwargs(
            board_id=board_id,
            column_values=column_values,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "change_multiple_column_values",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_multiple_column_values"]["creator"]


@task
async def change_multiple_column_values_updates(
    board_id: int,
    column_values: datetime,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    limit: int = 25,
    page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Changes the column values of a specific item.

    Args:
        board_id: The board's unique identifier.
        column_values: The column values updates.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create
            Status/Dropdown labels if they're missing. (Requires
            permission to change board structure).
        limit: None.
        page: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_multiple_column_values(
        **strip_kwargs(
            board_id=board_id,
            column_values=column_values,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).updates(
        **strip_kwargs(
            limit=limit,
            page=page,
        )
    )

    op_stack = (
        "change_multiple_column_values",
        "updates",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_multiple_column_values"]["updates"]


@task
async def change_multiple_column_values_subitems(
    board_id: int,
    column_values: datetime,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Changes the column values of a specific item.

    Args:
        board_id: The board's unique identifier.
        column_values: The column values updates.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create
            Status/Dropdown labels if they're missing. (Requires
            permission to change board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_multiple_column_values(
        **strip_kwargs(
            board_id=board_id,
            column_values=column_values,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).subitems(**strip_kwargs())

    op_stack = (
        "change_multiple_column_values",
        "subitems",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_multiple_column_values"]["subitems"]


@task
async def change_multiple_column_values_subscribers(
    board_id: int,
    column_values: datetime,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Changes the column values of a specific item.

    Args:
        board_id: The board's unique identifier.
        column_values: The column values updates.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create
            Status/Dropdown labels if they're missing. (Requires
            permission to change board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_multiple_column_values(
        **strip_kwargs(
            board_id=board_id,
            column_values=column_values,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).subscribers(**strip_kwargs())

    op_stack = (
        "change_multiple_column_values",
        "subscribers",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_multiple_column_values"]["subscribers"]


@task
async def change_multiple_column_values_column_values(
    board_id: int,
    column_values: datetime,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Changes the column values of a specific item.

    Args:
        board_id: The board's unique identifier.
        column_values: The column values updates.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create
            Status/Dropdown labels if they're missing. (Requires
            permission to change board structure).
        ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_multiple_column_values(
        **strip_kwargs(
            board_id=board_id,
            column_values=column_values,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).column_values(
        **strip_kwargs(
            ids=ids,
        )
    )

    op_stack = (
        "change_multiple_column_values",
        "column_values",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_multiple_column_values"]["column_values"]


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
            item_id=item_id,
            column_id=column_id,
            file=file,
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
            item_id=item_id,
            column_id=column_id,
            file=file,
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
            item_id=item_id,
        )
    )

    op_stack = ("delete_item",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_item"]


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
            item_id=item_id,
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
            item_id=item_id,
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
    op_selection = op.delete_item(**strip_kwargs(item_id=item_id,)).assets(
        **strip_kwargs(
            assets_source=assets_source,
            column_ids=column_ids,
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
            item_id=item_id,
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
    op_selection = op.delete_item(**strip_kwargs(item_id=item_id,)).updates(
        **strip_kwargs(
            limit=limit,
            page=page,
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
            item_id=item_id,
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
            item_id=item_id,
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
    op_selection = op.delete_item(**strip_kwargs(item_id=item_id,)).column_values(
        **strip_kwargs(
            ids=ids,
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
async def create_webhook(
    board_id: int,
    url: str,
    event: graphql_schema.WebhookEventType,
    monday_credentials: MondayCredentials,
    config: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new webhook.

    Args:
        board_id: The board's unique identifier.
        url: The webhook URL.
        event: The event to listen to (incoming_notification /
            change_column_value / change_status_column_value /
            change_subitem_column_value / change_specific_column_value /
            create_item / create_subitem / create_update /
            create_subitem_update / change_subitem_name / change_name /
            when_date_arrived / item_deleted / subitem_deleted /
            item_archived / subitem_archived).
        monday_credentials: Credentials to use for authentication with Monday.
        config: The webhook config.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_webhook(
        **strip_kwargs(
            board_id=board_id,
            url=url,
            event=event,
            config=config,
        )
    )

    op_stack = ("create_webhook",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_webhook"]


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
            board_id=board_id,
            title=title,
            description=description,
            column_type=column_type,
            defaults=defaults,
        )
    )

    op_stack = ("create_column",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_column"]


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
            text=text,
            user_id=user_id,
            target_id=target_id,
            target_type=target_type,
        )
    )

    op_stack = ("create_notification",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_notification"]


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
            column_id=column_id,
            board_id=board_id,
            title=title,
        )
    )

    op_stack = ("change_column_title",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_column_title"]


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
            parent_item_id=parent_item_id,
            item_name=item_name,
            column_values=column_values,
            create_labels_if_missing=create_labels_if_missing,
        )
    )

    op_stack = ("create_subitem",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_subitem"]


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
            parent_item_id=parent_item_id,
            item_name=item_name,
            column_values=column_values,
            create_labels_if_missing=create_labels_if_missing,
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
            parent_item_id=parent_item_id,
            item_name=item_name,
            column_values=column_values,
            create_labels_if_missing=create_labels_if_missing,
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
            parent_item_id=parent_item_id,
            item_name=item_name,
            column_values=column_values,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).assets(
        **strip_kwargs(
            assets_source=assets_source,
            column_ids=column_ids,
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
            parent_item_id=parent_item_id,
            item_name=item_name,
            column_values=column_values,
            create_labels_if_missing=create_labels_if_missing,
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
            parent_item_id=parent_item_id,
            item_name=item_name,
            column_values=column_values,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).updates(
        **strip_kwargs(
            limit=limit,
            page=page,
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
            parent_item_id=parent_item_id,
            item_name=item_name,
            column_values=column_values,
            create_labels_if_missing=create_labels_if_missing,
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
            parent_item_id=parent_item_id,
            item_name=item_name,
            column_values=column_values,
            create_labels_if_missing=create_labels_if_missing,
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
            parent_item_id=parent_item_id,
            item_name=item_name,
            column_values=column_values,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).column_values(
        **strip_kwargs(
            ids=ids,
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
async def delete_board(
    board_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_board(
        **strip_kwargs(
            board_id=board_id,
        )
    )

    op_stack = ("delete_board",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_board"]


@task
async def delete_board_tags(
    board_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_board(
        **strip_kwargs(
            board_id=board_id,
        )
    ).tags(**strip_kwargs())

    op_stack = (
        "delete_board",
        "tags",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_board"]["tags"]


@task
async def delete_board_items(
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
    Delete a board.

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
    op_selection = op.delete_board(**strip_kwargs(board_id=board_id,)).items(
        **strip_kwargs(
            ids=ids,
            limit=limit,
            page=page,
            newest_first=newest_first,
            exclude_nonactive=exclude_nonactive,
        )
    )

    op_stack = (
        "delete_board",
        "items",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_board"]["items"]


@task
async def delete_board_owner(
    board_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_board(
        **strip_kwargs(
            board_id=board_id,
        )
    ).owner(**strip_kwargs())

    op_stack = (
        "delete_board",
        "owner",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_board"]["owner"]


@task
async def delete_board_views(
    board_id: int,
    monday_credentials: MondayCredentials,
    ids: Iterable[int] = None,
    type: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete a board.

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
    op_selection = op.delete_board(**strip_kwargs(board_id=board_id,)).views(
        **strip_kwargs(
            ids=ids,
            type=type,
        )
    )

    op_stack = (
        "delete_board",
        "views",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_board"]["views"]


@task
async def delete_board_groups(
    board_id: int,
    monday_credentials: MondayCredentials,
    ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete a board.

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
    op_selection = op.delete_board(**strip_kwargs(board_id=board_id,)).groups(
        **strip_kwargs(
            ids=ids,
        )
    )

    op_stack = (
        "delete_board",
        "groups",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_board"]["groups"]


@task
async def delete_board_owners(
    board_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_board(
        **strip_kwargs(
            board_id=board_id,
        )
    ).owners(**strip_kwargs())

    op_stack = (
        "delete_board",
        "owners",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_board"]["owners"]


@task
async def delete_board_columns(
    board_id: int,
    monday_credentials: MondayCredentials,
    ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete a board.

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
    op_selection = op.delete_board(**strip_kwargs(board_id=board_id,)).columns(
        **strip_kwargs(
            ids=ids,
        )
    )

    op_stack = (
        "delete_board",
        "columns",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_board"]["columns"]


@task
async def delete_board_creator(
    board_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_board(
        **strip_kwargs(
            board_id=board_id,
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "delete_board",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_board"]["creator"]


@task
async def delete_board_updates(
    board_id: int,
    monday_credentials: MondayCredentials,
    limit: int = 25,
    page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete a board.

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
    op_selection = op.delete_board(**strip_kwargs(board_id=board_id,)).updates(
        **strip_kwargs(
            limit=limit,
            page=page,
        )
    )

    op_stack = (
        "delete_board",
        "updates",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_board"]["updates"]


@task
async def delete_board_top_group(
    board_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_board(
        **strip_kwargs(
            board_id=board_id,
        )
    ).top_group(**strip_kwargs())

    op_stack = (
        "delete_board",
        "top_group",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_board"]["top_group"]


@task
async def delete_board_workspace(
    board_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_board(
        **strip_kwargs(
            board_id=board_id,
        )
    ).workspace(**strip_kwargs())

    op_stack = (
        "delete_board",
        "workspace",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_board"]["workspace"]


@task
async def delete_board_subscribers(
    board_id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete a board.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_board(
        **strip_kwargs(
            board_id=board_id,
        )
    ).subscribers(**strip_kwargs())

    op_stack = (
        "delete_board",
        "subscribers",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_board"]["subscribers"]


@task
async def delete_board_activity_logs(
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
    Delete a board.

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
    op_selection = op.delete_board(**strip_kwargs(board_id=board_id,)).activity_logs(
        **strip_kwargs(
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

    op_stack = (
        "delete_board",
        "activity_logs",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_board"]["activity_logs"]


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
            board_name=board_name,
            board_kind=board_kind,
            folder_id=folder_id,
            workspace_id=workspace_id,
            template_id=template_id,
            board_owner_ids=board_owner_ids,
            board_subscriber_ids=board_subscriber_ids,
        )
    )

    op_stack = ("create_board",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_board"]


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
            board_name=board_name,
            board_kind=board_kind,
            folder_id=folder_id,
            workspace_id=workspace_id,
            template_id=template_id,
            board_owner_ids=board_owner_ids,
            board_subscriber_ids=board_subscriber_ids,
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
            board_name=board_name,
            board_kind=board_kind,
            folder_id=folder_id,
            workspace_id=workspace_id,
            template_id=template_id,
            board_owner_ids=board_owner_ids,
            board_subscriber_ids=board_subscriber_ids,
        )
    ).items(
        **strip_kwargs(
            ids=ids,
            limit=limit,
            page=page,
            newest_first=newest_first,
            exclude_nonactive=exclude_nonactive,
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
            board_name=board_name,
            board_kind=board_kind,
            folder_id=folder_id,
            workspace_id=workspace_id,
            template_id=template_id,
            board_owner_ids=board_owner_ids,
            board_subscriber_ids=board_subscriber_ids,
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
            board_name=board_name,
            board_kind=board_kind,
            folder_id=folder_id,
            workspace_id=workspace_id,
            template_id=template_id,
            board_owner_ids=board_owner_ids,
            board_subscriber_ids=board_subscriber_ids,
        )
    ).views(
        **strip_kwargs(
            ids=ids,
            type=type,
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
            board_name=board_name,
            board_kind=board_kind,
            folder_id=folder_id,
            workspace_id=workspace_id,
            template_id=template_id,
            board_owner_ids=board_owner_ids,
            board_subscriber_ids=board_subscriber_ids,
        )
    ).groups(
        **strip_kwargs(
            ids=ids,
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
            board_name=board_name,
            board_kind=board_kind,
            folder_id=folder_id,
            workspace_id=workspace_id,
            template_id=template_id,
            board_owner_ids=board_owner_ids,
            board_subscriber_ids=board_subscriber_ids,
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
            board_name=board_name,
            board_kind=board_kind,
            folder_id=folder_id,
            workspace_id=workspace_id,
            template_id=template_id,
            board_owner_ids=board_owner_ids,
            board_subscriber_ids=board_subscriber_ids,
        )
    ).columns(
        **strip_kwargs(
            ids=ids,
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
            board_name=board_name,
            board_kind=board_kind,
            folder_id=folder_id,
            workspace_id=workspace_id,
            template_id=template_id,
            board_owner_ids=board_owner_ids,
            board_subscriber_ids=board_subscriber_ids,
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
            board_name=board_name,
            board_kind=board_kind,
            folder_id=folder_id,
            workspace_id=workspace_id,
            template_id=template_id,
            board_owner_ids=board_owner_ids,
            board_subscriber_ids=board_subscriber_ids,
        )
    ).updates(
        **strip_kwargs(
            limit=limit,
            page=page,
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
            board_name=board_name,
            board_kind=board_kind,
            folder_id=folder_id,
            workspace_id=workspace_id,
            template_id=template_id,
            board_owner_ids=board_owner_ids,
            board_subscriber_ids=board_subscriber_ids,
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
            board_name=board_name,
            board_kind=board_kind,
            folder_id=folder_id,
            workspace_id=workspace_id,
            template_id=template_id,
            board_owner_ids=board_owner_ids,
            board_subscriber_ids=board_subscriber_ids,
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
            board_name=board_name,
            board_kind=board_kind,
            folder_id=folder_id,
            workspace_id=workspace_id,
            template_id=template_id,
            board_owner_ids=board_owner_ids,
            board_subscriber_ids=board_subscriber_ids,
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
            board_name=board_name,
            board_kind=board_kind,
            folder_id=folder_id,
            workspace_id=workspace_id,
            template_id=template_id,
            board_owner_ids=board_owner_ids,
            board_subscriber_ids=board_subscriber_ids,
        )
    ).activity_logs(
        **strip_kwargs(
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
async def duplicate_item(
    board_id: int,
    monday_credentials: MondayCredentials,
    with_updates: bool = None,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Duplicate an item.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        with_updates: Duplicate with the item's updates.
        item_id: The item's unique identifier. *Required.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.duplicate_item(
        **strip_kwargs(
            board_id=board_id,
            with_updates=with_updates,
            item_id=item_id,
        )
    )

    op_stack = ("duplicate_item",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["duplicate_item"]


@task
async def duplicate_item_board(
    board_id: int,
    monday_credentials: MondayCredentials,
    with_updates: bool = None,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Duplicate an item.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        with_updates: Duplicate with the item's updates.
        item_id: The item's unique identifier. *Required.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.duplicate_item(
        **strip_kwargs(
            board_id=board_id,
            with_updates=with_updates,
            item_id=item_id,
        )
    ).board(**strip_kwargs())

    op_stack = (
        "duplicate_item",
        "board",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["duplicate_item"]["board"]


@task
async def duplicate_item_group(
    board_id: int,
    monday_credentials: MondayCredentials,
    with_updates: bool = None,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Duplicate an item.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        with_updates: Duplicate with the item's updates.
        item_id: The item's unique identifier. *Required.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.duplicate_item(
        **strip_kwargs(
            board_id=board_id,
            with_updates=with_updates,
            item_id=item_id,
        )
    ).group(**strip_kwargs())

    op_stack = (
        "duplicate_item",
        "group",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["duplicate_item"]["group"]


@task
async def duplicate_item_assets(
    board_id: int,
    monday_credentials: MondayCredentials,
    with_updates: bool = None,
    item_id: int = None,
    assets_source: graphql_schema.AssetsSource = None,
    column_ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Duplicate an item.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        with_updates: Duplicate with the item's updates.
        item_id: The item's unique identifier. *Required.
        assets_source: None.
        column_ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.duplicate_item(
        **strip_kwargs(
            board_id=board_id,
            with_updates=with_updates,
            item_id=item_id,
        )
    ).assets(
        **strip_kwargs(
            assets_source=assets_source,
            column_ids=column_ids,
        )
    )

    op_stack = (
        "duplicate_item",
        "assets",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["duplicate_item"]["assets"]


@task
async def duplicate_item_creator(
    board_id: int,
    monday_credentials: MondayCredentials,
    with_updates: bool = None,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Duplicate an item.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        with_updates: Duplicate with the item's updates.
        item_id: The item's unique identifier. *Required.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.duplicate_item(
        **strip_kwargs(
            board_id=board_id,
            with_updates=with_updates,
            item_id=item_id,
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "duplicate_item",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["duplicate_item"]["creator"]


@task
async def duplicate_item_updates(
    board_id: int,
    monday_credentials: MondayCredentials,
    with_updates: bool = None,
    item_id: int = None,
    limit: int = 25,
    page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Duplicate an item.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        with_updates: Duplicate with the item's updates.
        item_id: The item's unique identifier. *Required.
        limit: None.
        page: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.duplicate_item(
        **strip_kwargs(
            board_id=board_id,
            with_updates=with_updates,
            item_id=item_id,
        )
    ).updates(
        **strip_kwargs(
            limit=limit,
            page=page,
        )
    )

    op_stack = (
        "duplicate_item",
        "updates",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["duplicate_item"]["updates"]


@task
async def duplicate_item_subitems(
    board_id: int,
    monday_credentials: MondayCredentials,
    with_updates: bool = None,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Duplicate an item.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        with_updates: Duplicate with the item's updates.
        item_id: The item's unique identifier. *Required.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.duplicate_item(
        **strip_kwargs(
            board_id=board_id,
            with_updates=with_updates,
            item_id=item_id,
        )
    ).subitems(**strip_kwargs())

    op_stack = (
        "duplicate_item",
        "subitems",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["duplicate_item"]["subitems"]


@task
async def duplicate_item_subscribers(
    board_id: int,
    monday_credentials: MondayCredentials,
    with_updates: bool = None,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Duplicate an item.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        with_updates: Duplicate with the item's updates.
        item_id: The item's unique identifier. *Required.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.duplicate_item(
        **strip_kwargs(
            board_id=board_id,
            with_updates=with_updates,
            item_id=item_id,
        )
    ).subscribers(**strip_kwargs())

    op_stack = (
        "duplicate_item",
        "subscribers",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["duplicate_item"]["subscribers"]


@task
async def duplicate_item_column_values(
    board_id: int,
    monday_credentials: MondayCredentials,
    with_updates: bool = None,
    item_id: int = None,
    ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Duplicate an item.

    Args:
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        with_updates: Duplicate with the item's updates.
        item_id: The item's unique identifier. *Required.
        ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.duplicate_item(
        **strip_kwargs(
            board_id=board_id,
            with_updates=with_updates,
            item_id=item_id,
        )
    ).column_values(
        **strip_kwargs(
            ids=ids,
        )
    )

    op_stack = (
        "duplicate_item",
        "column_values",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["duplicate_item"]["column_values"]


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
            update_id=update_id,
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
            update_id=update_id,
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
            update_id=update_id,
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
            update_id=update_id,
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
            board_id=board_id,
            group_id=group_id,
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
            board_id=board_id,
            group_id=group_id,
        )
    ).items(
        **strip_kwargs(
            ids=ids,
            limit=limit,
            page=page,
            newest_first=newest_first,
            exclude_nonactive=exclude_nonactive,
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
async def create_workspace(
    name: str,
    kind: graphql_schema.WorkspaceKind,
    monday_credentials: MondayCredentials,
    description: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new workspace.

    Args:
        name: The Workspace's name.
        kind: The workspace's kind (open / closed).
        monday_credentials: Credentials to use for authentication with Monday.
        description: The Workspace's description.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_workspace(
        **strip_kwargs(
            name=name,
            kind=kind,
            description=description,
        )
    )

    op_stack = ("create_workspace",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_workspace"]


@task
async def create_workspace_account_product(
    name: str,
    kind: graphql_schema.WorkspaceKind,
    monday_credentials: MondayCredentials,
    description: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new workspace.

    Args:
        name: The Workspace's name.
        kind: The workspace's kind (open / closed).
        monday_credentials: Credentials to use for authentication with Monday.
        description: The Workspace's description.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_workspace(
        **strip_kwargs(
            name=name,
            kind=kind,
            description=description,
        )
    ).account_product(**strip_kwargs())

    op_stack = (
        "create_workspace",
        "account_product",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_workspace"]["account_product"]


@task
async def move_item_to_group(
    group_id: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Move an item to a different group.

    Args:
        group_id: The group's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.move_item_to_group(
        **strip_kwargs(
            group_id=group_id,
            item_id=item_id,
        )
    )

    op_stack = ("move_item_to_group",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["move_item_to_group"]


@task
async def move_item_to_group_board(
    group_id: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Move an item to a different group.

    Args:
        group_id: The group's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.move_item_to_group(
        **strip_kwargs(
            group_id=group_id,
            item_id=item_id,
        )
    ).board(**strip_kwargs())

    op_stack = (
        "move_item_to_group",
        "board",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["move_item_to_group"]["board"]


@task
async def move_item_to_group_group(
    group_id: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Move an item to a different group.

    Args:
        group_id: The group's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.move_item_to_group(
        **strip_kwargs(
            group_id=group_id,
            item_id=item_id,
        )
    ).group(**strip_kwargs())

    op_stack = (
        "move_item_to_group",
        "group",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["move_item_to_group"]["group"]


@task
async def move_item_to_group_assets(
    group_id: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    assets_source: graphql_schema.AssetsSource = None,
    column_ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Move an item to a different group.

    Args:
        group_id: The group's unique identifier.
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
    op_selection = op.move_item_to_group(
        **strip_kwargs(
            group_id=group_id,
            item_id=item_id,
        )
    ).assets(
        **strip_kwargs(
            assets_source=assets_source,
            column_ids=column_ids,
        )
    )

    op_stack = (
        "move_item_to_group",
        "assets",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["move_item_to_group"]["assets"]


@task
async def move_item_to_group_creator(
    group_id: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Move an item to a different group.

    Args:
        group_id: The group's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.move_item_to_group(
        **strip_kwargs(
            group_id=group_id,
            item_id=item_id,
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "move_item_to_group",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["move_item_to_group"]["creator"]


@task
async def move_item_to_group_updates(
    group_id: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    limit: int = 25,
    page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Move an item to a different group.

    Args:
        group_id: The group's unique identifier.
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
    op_selection = op.move_item_to_group(
        **strip_kwargs(
            group_id=group_id,
            item_id=item_id,
        )
    ).updates(
        **strip_kwargs(
            limit=limit,
            page=page,
        )
    )

    op_stack = (
        "move_item_to_group",
        "updates",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["move_item_to_group"]["updates"]


@task
async def move_item_to_group_subitems(
    group_id: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Move an item to a different group.

    Args:
        group_id: The group's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.move_item_to_group(
        **strip_kwargs(
            group_id=group_id,
            item_id=item_id,
        )
    ).subitems(**strip_kwargs())

    op_stack = (
        "move_item_to_group",
        "subitems",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["move_item_to_group"]["subitems"]


@task
async def move_item_to_group_subscribers(
    group_id: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Move an item to a different group.

    Args:
        group_id: The group's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.move_item_to_group(
        **strip_kwargs(
            group_id=group_id,
            item_id=item_id,
        )
    ).subscribers(**strip_kwargs())

    op_stack = (
        "move_item_to_group",
        "subscribers",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["move_item_to_group"]["subscribers"]


@task
async def move_item_to_group_column_values(
    group_id: str,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Move an item to a different group.

    Args:
        group_id: The group's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.move_item_to_group(
        **strip_kwargs(
            group_id=group_id,
            item_id=item_id,
        )
    ).column_values(
        **strip_kwargs(
            ids=ids,
        )
    )

    op_stack = (
        "move_item_to_group",
        "column_values",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["move_item_to_group"]["column_values"]


@task
async def duplicate_group(
    board_id: int,
    group_id: str,
    monday_credentials: MondayCredentials,
    add_to_top: bool = None,
    group_title: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Duplicate a group.

    Args:
        board_id: The board's unique identifier.
        group_id: The group's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        add_to_top: Should the new group be added to the top.
        group_title: The group's title.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.duplicate_group(
        **strip_kwargs(
            board_id=board_id,
            group_id=group_id,
            add_to_top=add_to_top,
            group_title=group_title,
        )
    )

    op_stack = ("duplicate_group",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["duplicate_group"]


@task
async def duplicate_group_items(
    board_id: int,
    group_id: str,
    monday_credentials: MondayCredentials,
    add_to_top: bool = None,
    group_title: str = None,
    ids: Iterable[int] = None,
    limit: int = None,
    page: int = 1,
    newest_first: bool = None,
    exclude_nonactive: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Duplicate a group.

    Args:
        board_id: The board's unique identifier.
        group_id: The group's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        add_to_top: Should the new group be added to the top.
        group_title: The group's title.
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
    op_selection = op.duplicate_group(
        **strip_kwargs(
            board_id=board_id,
            group_id=group_id,
            add_to_top=add_to_top,
            group_title=group_title,
        )
    ).items(
        **strip_kwargs(
            ids=ids,
            limit=limit,
            page=page,
            newest_first=newest_first,
            exclude_nonactive=exclude_nonactive,
        )
    )

    op_stack = (
        "duplicate_group",
        "items",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["duplicate_group"]["items"]


@task
async def delete_users_from_workspace(
    workspace_id: int,
    user_ids: Iterable[int],
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete users from a workspace.

    Args:
        workspace_id: The workspace's unique identifier.
        user_ids: User ids to unsubscribe from a workspace.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_users_from_workspace(
        **strip_kwargs(
            workspace_id=workspace_id,
            user_ids=user_ids,
        )
    )

    op_stack = ("delete_users_from_workspace",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_users_from_workspace"]


@task
async def delete_users_from_workspace_teams(
    workspace_id: int,
    user_ids: Iterable[int],
    monday_credentials: MondayCredentials,
    ids: Iterable[int] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete users from a workspace.

    Args:
        workspace_id: The workspace's unique
            identifier.
        user_ids: User ids to unsubscribe from a
            workspace.
        monday_credentials: Credentials to use for authentication with Monday.
        ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_users_from_workspace(
        **strip_kwargs(
            workspace_id=workspace_id,
            user_ids=user_ids,
        )
    ).teams(
        **strip_kwargs(
            ids=ids,
        )
    )

    op_stack = (
        "delete_users_from_workspace",
        "teams",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_users_from_workspace"]["teams"]


@task
async def delete_users_from_workspace_account(
    workspace_id: int,
    user_ids: Iterable[int],
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete users from a workspace.

    Args:
        workspace_id: The workspace's unique
            identifier.
        user_ids: User ids to unsubscribe from a
            workspace.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_users_from_workspace(
        **strip_kwargs(
            workspace_id=workspace_id,
            user_ids=user_ids,
        )
    ).account(**strip_kwargs())

    op_stack = (
        "delete_users_from_workspace",
        "account",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_users_from_workspace"]["account"]


@task
async def delete_subscribers_from_board(
    board_id: int,
    user_ids: Iterable[int],
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Remove subscribers from the board.

    Args:
        board_id: The board's unique identifier.
        user_ids: User ids to unsubscribe from a board.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_subscribers_from_board(
        **strip_kwargs(
            board_id=board_id,
            user_ids=user_ids,
        )
    )

    op_stack = ("delete_subscribers_from_board",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_subscribers_from_board"]


@task
async def delete_subscribers_from_board_teams(
    board_id: int,
    user_ids: Iterable[int],
    monday_credentials: MondayCredentials,
    ids: Iterable[int] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Remove subscribers from the board.

    Args:
        board_id: The board's unique identifier.
        user_ids: User ids to unsubscribe from a
            board.
        monday_credentials: Credentials to use for authentication with Monday.
        ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_subscribers_from_board(
        **strip_kwargs(
            board_id=board_id,
            user_ids=user_ids,
        )
    ).teams(
        **strip_kwargs(
            ids=ids,
        )
    )

    op_stack = (
        "delete_subscribers_from_board",
        "teams",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_subscribers_from_board"]["teams"]


@task
async def delete_subscribers_from_board_account(
    board_id: int,
    user_ids: Iterable[int],
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Remove subscribers from the board.

    Args:
        board_id: The board's unique identifier.
        user_ids: User ids to unsubscribe from a
            board.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_subscribers_from_board(
        **strip_kwargs(
            board_id=board_id,
            user_ids=user_ids,
        )
    ).account(**strip_kwargs())

    op_stack = (
        "delete_subscribers_from_board",
        "account",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_subscribers_from_board"]["account"]


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
            body=body,
            item_id=item_id,
            parent_id=parent_id,
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
            body=body,
            item_id=item_id,
            parent_id=parent_id,
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
            body=body,
            item_id=item_id,
            parent_id=parent_id,
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
            body=body,
            item_id=item_id,
            parent_id=parent_id,
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
async def set_mock_app_subscription(
    app_id: int,
    partial_signing_secret: str,
    monday_credentials: MondayCredentials,
    plan_id: str = None,
    is_trial: bool = None,
    renewal_date: datetime = None,
    billing_period: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Set mock app subscription for the current account.

    Args:
        app_id: The app id of the app to mock subscription for.
        partial_signing_secret: The last 10 characters of the app's signing
            secret.
        monday_credentials: Credentials to use for authentication with Monday.
        plan_id: The plan id for the mocked plan.
        is_trial: Is the subscription a trial.
        renewal_date: The subscription renewal date.
        billing_period: Billing period [monthly/yearly].
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.set_mock_app_subscription(
        **strip_kwargs(
            app_id=app_id,
            partial_signing_secret=partial_signing_secret,
            plan_id=plan_id,
            is_trial=is_trial,
            renewal_date=renewal_date,
            billing_period=billing_period,
        )
    )

    op_stack = ("set_mock_app_subscription",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["set_mock_app_subscription"]


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
            item_id=item_id,
        )
    )

    op_stack = ("clear_item_updates",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["clear_item_updates"]


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
            item_id=item_id,
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
            item_id=item_id,
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
    op_selection = op.clear_item_updates(**strip_kwargs(item_id=item_id,)).assets(
        **strip_kwargs(
            assets_source=assets_source,
            column_ids=column_ids,
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
            item_id=item_id,
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
async def clear_item_updates_updates(
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
    op_selection = op.clear_item_updates(**strip_kwargs(item_id=item_id,)).updates(
        **strip_kwargs(
            limit=limit,
            page=page,
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
            item_id=item_id,
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
            item_id=item_id,
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
            item_id=item_id,
        )
    ).column_values(
        **strip_kwargs(
            ids=ids,
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
            update_id=update_id,
            file=file,
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
            update_id=update_id,
            file=file,
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
            id=id,
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
            id=id,
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
            id=id,
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
            id=id,
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
async def add_subscribers_to_board(
    board_id: int,
    user_ids: Iterable[int],
    monday_credentials: MondayCredentials,
    kind: graphql_schema.BoardSubscriberKind = "subscriber",
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Add subscribers to a board.

    Args:
        board_id: The board's unique identifier.
        user_ids: User ids to subscribe to a board.
        monday_credentials: Credentials to use for authentication with Monday.
        kind: Subscribers kind (subscriber / owner).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.add_subscribers_to_board(
        **strip_kwargs(
            board_id=board_id,
            user_ids=user_ids,
            kind=kind,
        )
    )

    op_stack = ("add_subscribers_to_board",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["add_subscribers_to_board"]


@task
async def add_subscribers_to_board_teams(
    board_id: int,
    user_ids: Iterable[int],
    monday_credentials: MondayCredentials,
    kind: graphql_schema.BoardSubscriberKind = "subscriber",
    ids: Iterable[int] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Add subscribers to a board.

    Args:
        board_id: The board's unique identifier.
        user_ids: User ids to subscribe to a board.
        monday_credentials: Credentials to use for authentication with Monday.
        kind: Subscribers kind (subscriber / owner).
        ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.add_subscribers_to_board(
        **strip_kwargs(
            board_id=board_id,
            user_ids=user_ids,
            kind=kind,
        )
    ).teams(
        **strip_kwargs(
            ids=ids,
        )
    )

    op_stack = (
        "add_subscribers_to_board",
        "teams",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["add_subscribers_to_board"]["teams"]


@task
async def add_subscribers_to_board_account(
    board_id: int,
    user_ids: Iterable[int],
    monday_credentials: MondayCredentials,
    kind: graphql_schema.BoardSubscriberKind = "subscriber",
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Add subscribers to a board.

    Args:
        board_id: The board's unique identifier.
        user_ids: User ids to subscribe to a board.
        monday_credentials: Credentials to use for authentication with Monday.
        kind: Subscribers kind (subscriber / owner).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.add_subscribers_to_board(
        **strip_kwargs(
            board_id=board_id,
            user_ids=user_ids,
            kind=kind,
        )
    ).account(**strip_kwargs())

    op_stack = (
        "add_subscribers_to_board",
        "account",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["add_subscribers_to_board"]["account"]


@task
async def delete_webhook(
    id: int,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete a new webhook.

    Args:
        id: The webhook's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_webhook(
        **strip_kwargs(
            id=id,
        )
    )

    op_stack = ("delete_webhook",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_webhook"]


@task
async def add_teams_to_workspace(
    workspace_id: int,
    team_ids: Iterable[int],
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
            workspace_id=workspace_id,
            team_ids=team_ids,
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
    team_ids: Iterable[int],
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
            workspace_id=workspace_id,
            team_ids=team_ids,
        )
    ).users(
        **strip_kwargs(
            ids=ids,
            kind=kind,
            newest_first=newest_first,
            limit=limit,
            emails=emails,
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
async def complexity(
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Get the complexity data of your mutations.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.complexity(**strip_kwargs())

    op_stack = ("complexity",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["complexity"]


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
            board_id=board_id,
            item_name=item_name,
            group_id=group_id,
            column_values=column_values,
            create_labels_if_missing=create_labels_if_missing,
        )
    )

    op_stack = ("create_item",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_item"]


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
            board_id=board_id,
            item_name=item_name,
            group_id=group_id,
            column_values=column_values,
            create_labels_if_missing=create_labels_if_missing,
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
            board_id=board_id,
            item_name=item_name,
            group_id=group_id,
            column_values=column_values,
            create_labels_if_missing=create_labels_if_missing,
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
            board_id=board_id,
            item_name=item_name,
            group_id=group_id,
            column_values=column_values,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).assets(
        **strip_kwargs(
            assets_source=assets_source,
            column_ids=column_ids,
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
            board_id=board_id,
            item_name=item_name,
            group_id=group_id,
            column_values=column_values,
            create_labels_if_missing=create_labels_if_missing,
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
            board_id=board_id,
            item_name=item_name,
            group_id=group_id,
            column_values=column_values,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).updates(
        **strip_kwargs(
            limit=limit,
            page=page,
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
            board_id=board_id,
            item_name=item_name,
            group_id=group_id,
            column_values=column_values,
            create_labels_if_missing=create_labels_if_missing,
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
            board_id=board_id,
            item_name=item_name,
            group_id=group_id,
            column_values=column_values,
            create_labels_if_missing=create_labels_if_missing,
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
            board_id=board_id,
            item_name=item_name,
            group_id=group_id,
            column_values=column_values,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).column_values(
        **strip_kwargs(
            ids=ids,
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
async def change_column_value(
    column_id: str,
    board_id: int,
    value: datetime,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change an item's column value.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        value: The new value of the column.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create Status/Dropdown labels if they're
            missing. (Requires permission to change board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_column_value(
        **strip_kwargs(
            column_id=column_id,
            board_id=board_id,
            value=value,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    )

    op_stack = ("change_column_value",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_column_value"]


@task
async def change_column_value_board(
    column_id: str,
    board_id: int,
    value: datetime,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change an item's column value.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        value: The new value of the column.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create Status/Dropdown
            labels if they're missing. (Requires permission to change
            board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_column_value(
        **strip_kwargs(
            column_id=column_id,
            board_id=board_id,
            value=value,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).board(**strip_kwargs())

    op_stack = (
        "change_column_value",
        "board",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_column_value"]["board"]


@task
async def change_column_value_group(
    column_id: str,
    board_id: int,
    value: datetime,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change an item's column value.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        value: The new value of the column.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create Status/Dropdown
            labels if they're missing. (Requires permission to change
            board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_column_value(
        **strip_kwargs(
            column_id=column_id,
            board_id=board_id,
            value=value,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).group(**strip_kwargs())

    op_stack = (
        "change_column_value",
        "group",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_column_value"]["group"]


@task
async def change_column_value_assets(
    column_id: str,
    board_id: int,
    value: datetime,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    assets_source: graphql_schema.AssetsSource = None,
    column_ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change an item's column value.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        value: The new value of the column.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create Status/Dropdown
            labels if they're missing. (Requires permission to change
            board structure).
        assets_source: None.
        column_ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_column_value(
        **strip_kwargs(
            column_id=column_id,
            board_id=board_id,
            value=value,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).assets(
        **strip_kwargs(
            assets_source=assets_source,
            column_ids=column_ids,
        )
    )

    op_stack = (
        "change_column_value",
        "assets",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_column_value"]["assets"]


@task
async def change_column_value_creator(
    column_id: str,
    board_id: int,
    value: datetime,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change an item's column value.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        value: The new value of the column.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create Status/Dropdown
            labels if they're missing. (Requires permission to change
            board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_column_value(
        **strip_kwargs(
            column_id=column_id,
            board_id=board_id,
            value=value,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).creator(**strip_kwargs())

    op_stack = (
        "change_column_value",
        "creator",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_column_value"]["creator"]


@task
async def change_column_value_updates(
    column_id: str,
    board_id: int,
    value: datetime,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    limit: int = 25,
    page: int = 1,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change an item's column value.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        value: The new value of the column.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create Status/Dropdown
            labels if they're missing. (Requires permission to change
            board structure).
        limit: None.
        page: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_column_value(
        **strip_kwargs(
            column_id=column_id,
            board_id=board_id,
            value=value,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).updates(
        **strip_kwargs(
            limit=limit,
            page=page,
        )
    )

    op_stack = (
        "change_column_value",
        "updates",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_column_value"]["updates"]


@task
async def change_column_value_subitems(
    column_id: str,
    board_id: int,
    value: datetime,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change an item's column value.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        value: The new value of the column.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create Status/Dropdown
            labels if they're missing. (Requires permission to change
            board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_column_value(
        **strip_kwargs(
            column_id=column_id,
            board_id=board_id,
            value=value,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).subitems(**strip_kwargs())

    op_stack = (
        "change_column_value",
        "subitems",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_column_value"]["subitems"]


@task
async def change_column_value_subscribers(
    column_id: str,
    board_id: int,
    value: datetime,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change an item's column value.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        value: The new value of the column.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create Status/Dropdown
            labels if they're missing. (Requires permission to change
            board structure).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_column_value(
        **strip_kwargs(
            column_id=column_id,
            board_id=board_id,
            value=value,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).subscribers(**strip_kwargs())

    op_stack = (
        "change_column_value",
        "subscribers",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_column_value"]["subscribers"]


@task
async def change_column_value_column_values(
    column_id: str,
    board_id: int,
    value: datetime,
    monday_credentials: MondayCredentials,
    item_id: int = None,
    create_labels_if_missing: bool = None,
    ids: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change an item's column value.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        value: The new value of the column.
        monday_credentials: Credentials to use for authentication with Monday.
        item_id: The item's unique identifier.
        create_labels_if_missing: Create Status/Dropdown
            labels if they're missing. (Requires permission to change
            board structure).
        ids: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_column_value(
        **strip_kwargs(
            column_id=column_id,
            board_id=board_id,
            value=value,
            item_id=item_id,
            create_labels_if_missing=create_labels_if_missing,
        )
    ).column_values(
        **strip_kwargs(
            ids=ids,
        )
    )

    op_stack = (
        "change_column_value",
        "column_values",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_column_value"]["column_values"]


@task
async def delete_group(
    board_id: int,
    group_id: str,
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Deletes a group in a specific board.

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
    op_selection = op.delete_group(
        **strip_kwargs(
            board_id=board_id,
            group_id=group_id,
        )
    )

    op_stack = ("delete_group",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_group"]


@task
async def delete_group_items(
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
    Deletes a group in a specific board.

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
    op_selection = op.delete_group(
        **strip_kwargs(
            board_id=board_id,
            group_id=group_id,
        )
    ).items(
        **strip_kwargs(
            ids=ids,
            limit=limit,
            page=page,
            newest_first=newest_first,
            exclude_nonactive=exclude_nonactive,
        )
    )

    op_stack = (
        "delete_group",
        "items",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_group"]["items"]


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
            item_id=item_id,
        )
    )

    op_stack = ("archive_item",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_item"]


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
            item_id=item_id,
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
            item_id=item_id,
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
    op_selection = op.archive_item(**strip_kwargs(item_id=item_id,)).assets(
        **strip_kwargs(
            assets_source=assets_source,
            column_ids=column_ids,
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
            item_id=item_id,
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
    op_selection = op.archive_item(**strip_kwargs(item_id=item_id,)).updates(
        **strip_kwargs(
            limit=limit,
            page=page,
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
            item_id=item_id,
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
            item_id=item_id,
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
    op_selection = op.archive_item(**strip_kwargs(item_id=item_id,)).column_values(
        **strip_kwargs(
            ids=ids,
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
async def add_users_to_workspace(
    workspace_id: int,
    user_ids: Iterable[int],
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
            workspace_id=workspace_id,
            user_ids=user_ids,
            kind=kind,
        )
    )

    op_stack = ("add_users_to_workspace",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["add_users_to_workspace"]


@task
async def add_users_to_workspace_teams(
    workspace_id: int,
    user_ids: Iterable[int],
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
            workspace_id=workspace_id,
            user_ids=user_ids,
            kind=kind,
        )
    ).teams(
        **strip_kwargs(
            ids=ids,
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


@task
async def add_users_to_workspace_account(
    workspace_id: int,
    user_ids: Iterable[int],
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
            workspace_id=workspace_id,
            user_ids=user_ids,
            kind=kind,
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
            board_id=board_id,
            group_name=group_name,
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
            board_id=board_id,
            group_name=group_name,
        )
    ).items(
        **strip_kwargs(
            ids=ids,
            limit=limit,
            page=page,
            newest_first=newest_first,
            exclude_nonactive=exclude_nonactive,
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
            board_id=board_id,
        )
    )

    op_stack = ("archive_board",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["archive_board"]


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
            board_id=board_id,
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
    op_selection = op.archive_board(**strip_kwargs(board_id=board_id,)).items(
        **strip_kwargs(
            ids=ids,
            limit=limit,
            page=page,
            newest_first=newest_first,
            exclude_nonactive=exclude_nonactive,
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
            board_id=board_id,
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
    op_selection = op.archive_board(**strip_kwargs(board_id=board_id,)).views(
        **strip_kwargs(
            ids=ids,
            type=type,
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
    op_selection = op.archive_board(**strip_kwargs(board_id=board_id,)).groups(
        **strip_kwargs(
            ids=ids,
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
            board_id=board_id,
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
    op_selection = op.archive_board(**strip_kwargs(board_id=board_id,)).columns(
        **strip_kwargs(
            ids=ids,
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
            board_id=board_id,
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
    op_selection = op.archive_board(**strip_kwargs(board_id=board_id,)).updates(
        **strip_kwargs(
            limit=limit,
            page=page,
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
            board_id=board_id,
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
            board_id=board_id,
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
            board_id=board_id,
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
    op_selection = op.archive_board(**strip_kwargs(board_id=board_id,)).activity_logs(
        **strip_kwargs(
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
async def delete_teams_from_workspace(
    workspace_id: int,
    team_ids: Iterable[int],
    monday_credentials: MondayCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete teams from a workspace.

    Args:
        workspace_id: The workspace's unique identifier.
        team_ids: Team ids to unsubscribe from a workspace.
        monday_credentials: Credentials to use for authentication with Monday.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.delete_teams_from_workspace(
        **strip_kwargs(
            workspace_id=workspace_id,
            team_ids=team_ids,
        )
    )

    op_stack = ("delete_teams_from_workspace",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_teams_from_workspace"]


@task
async def delete_teams_from_workspace_users(
    workspace_id: int,
    team_ids: Iterable[int],
    monday_credentials: MondayCredentials,
    ids: Iterable[int] = None,
    kind: graphql_schema.UserKind = None,
    newest_first: bool = None,
    limit: int = None,
    emails: Iterable[str] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Delete teams from a workspace.

    Args:
        workspace_id: The workspace's unique
            identifier.
        team_ids: Team ids to unsubscribe from a
            workspace.
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
    op_selection = op.delete_teams_from_workspace(
        **strip_kwargs(
            workspace_id=workspace_id,
            team_ids=team_ids,
        )
    ).users(
        **strip_kwargs(
            ids=ids,
            kind=kind,
            newest_first=newest_first,
            limit=limit,
            emails=emails,
        )
    )

    op_stack = (
        "delete_teams_from_workspace",
        "users",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["delete_teams_from_workspace"]["users"]


@task
async def change_column_metadata(
    column_id: str,
    board_id: int,
    monday_credentials: MondayCredentials,
    column_property: graphql_schema.ColumnProperty = None,
    value: str = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Change a column's properties.

    Args:
        column_id: The column's unique identifier.
        board_id: The board's unique identifier.
        monday_credentials: Credentials to use for authentication with Monday.
        column_property: The property name of the column to be changed (title /
            description).
        value: The new description of the column.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.change_column_metadata(
        **strip_kwargs(
            column_id=column_id,
            board_id=board_id,
            column_property=column_property,
            value=value,
        )
    )

    op_stack = ("change_column_metadata",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["change_column_metadata"]


@task
async def create_or_get_tag(
    monday_credentials: MondayCredentials,
    tag_name: str = None,
    board_id: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Create a new tag or get it if it already exists.

    Args:
        monday_credentials: Credentials to use for authentication with Monday.
        tag_name: The new tag's name.
        board_id: The private board id to create the tag at (not needed for
            public boards).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.create_or_get_tag(
        **strip_kwargs(
            tag_name=tag_name,
            board_id=board_id,
        )
    )

    op_stack = ("create_or_get_tag",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["create_or_get_tag"]


@task
async def duplicate_board(
    board_id: int,
    duplicate_type: graphql_schema.DuplicateBoardType,
    monday_credentials: MondayCredentials,
    board_name: str = None,
    workspace_id: int = None,
    folder_id: int = None,
    keep_subscribers: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Duplicate a board.

    Args:
        board_id: The board's unique identifier.
        duplicate_type: The duplication type.
        monday_credentials: Credentials to use for authentication with Monday.
        board_name: Optional the new board's name. If omitted then automaticlly
            generated.
        workspace_id: Optional destination workspace. Defaults to the original
            board workspace.
        folder_id: Optional destination folder in destionation workspace.
            Defaults to the original board folder.
        keep_subscribers: Duplicate the subscribers to the new board. Defaults
            to false.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.duplicate_board(
        **strip_kwargs(
            board_id=board_id,
            duplicate_type=duplicate_type,
            board_name=board_name,
            workspace_id=workspace_id,
            folder_id=folder_id,
            keep_subscribers=keep_subscribers,
        )
    )

    op_stack = ("duplicate_board",)
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["duplicate_board"]


@task
async def duplicate_board_board(
    board_id: int,
    duplicate_type: graphql_schema.DuplicateBoardType,
    monday_credentials: MondayCredentials,
    board_name: str = None,
    workspace_id: int = None,
    folder_id: int = None,
    keep_subscribers: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Duplicate a board.

    Args:
        board_id: The board's unique identifier.
        duplicate_type: The duplication type.
        monday_credentials: Credentials to use for authentication with Monday.
        board_name: Optional the new board's name. If omitted
            then automaticlly generated.
        workspace_id: Optional destination workspace. Defaults
            to the original board workspace.
        folder_id: Optional destination folder in destionation
            workspace. Defaults to the original board folder.
        keep_subscribers: Duplicate the subscribers to the new
            board. Defaults to false.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.duplicate_board(
        **strip_kwargs(
            board_id=board_id,
            duplicate_type=duplicate_type,
            board_name=board_name,
            workspace_id=workspace_id,
            folder_id=folder_id,
            keep_subscribers=keep_subscribers,
        )
    ).board(**strip_kwargs())

    op_stack = (
        "duplicate_board",
        "board",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await _execute_graphql_op(op, monday_credentials)
    return result["duplicate_board"]["board"]
