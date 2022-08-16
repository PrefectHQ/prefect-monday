import sgqlc.types
import sgqlc.types.datetime

graphql_schema = sgqlc.types.Schema()


########################################################################
# Scalars and Enumerations
########################################################################
class AccountProductKind(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = (
        "core",
        "crm",
        "forms",
        "marketing",
        "projectManagement",
        "software",
        "whiteboard",
    )


class AssetsSource(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = ("all", "columns", "gallery")


class BoardAttributes(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = ("communication", "description", "name")


class BoardKind(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = ("private", "public", "share")


class BoardObjectType(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = ("board", "document", "sub_items_board")


class BoardSubscriberKind(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = ("owner", "subscriber")


class BoardsOrderBy(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = ("created_at", "used_at")


Boolean = sgqlc.types.Boolean


class ColumnProperty(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = ("description", "title")


class ColumnType(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = (
        "auto_number",
        "checkbox",
        "color_picker",
        "country",
        "creation_log",
        "date",
        "dependency",
        "dropdown",
        "email",
        "file",
        "hour",
        "integration",
        "item_id",
        "last_updated",
        "link",
        "location",
        "long_text",
        "numbers",
        "people",
        "phone",
        "progress",
        "rating",
        "status",
        "tags",
        "team",
        "text",
        "time_tracking",
        "timeline",
        "vote",
        "week",
        "world_clock",
    )


Date = sgqlc.types.datetime.Date


class DuplicateBoardType(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = (
        "duplicate_board_with_pulses",
        "duplicate_board_with_pulses_and_updates",
        "duplicate_board_with_structure",
    )


class File(sgqlc.types.Scalar):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema


class FirstDayOfTheWeek(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = ("monday", "sunday")


ID = sgqlc.types.ID


class ISO8601DateTime(sgqlc.types.Scalar):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema


Int = sgqlc.types.Int


class InvitedUserKind(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = ("guest", "member", "view_only")


class JSON(sgqlc.types.Scalar):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema


class LinkageType(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = ("connection", "reflection")


class MentionType(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = ("Board", "Project", "Team", "User")


class NotificationTargetType(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = ("Post", "Project")


class ProductKind(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = (
        "core",
        "crm",
        "forms",
        "knowledge",
        "marketing",
        "project_management",
        "software",
        "whiteboard",
        "workflows",
    )


class State(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = ("active", "all", "archived", "deleted")


String = sgqlc.types.String


class UserKind(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = ("all", "guests", "non_guests", "non_pending")


class WebhookEventType(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = (
        "change_column_value",
        "change_name",
        "change_specific_column_value",
        "change_status_column_value",
        "change_subitem_column_value",
        "change_subitem_name",
        "create_item",
        "create_subitem",
        "create_subitem_update",
        "create_update",
        "item_archived",
        "item_deleted",
        "subitem_archived",
        "subitem_deleted",
        "when_date_arrived",
    )


class WorkspaceKind(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = ("closed", "open")


class WorkspaceSubscriberKind(sgqlc.types.Enum):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __choices__ = ("owner", "subscriber")


########################################################################
# Input Objects
########################################################################

########################################################################
# Output Objects and Interfaces
########################################################################
class Account(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = (
        "first_day_of_the_week",
        "id",
        "logo",
        "name",
        "plan",
        "show_timeline_weekends",
        "sign_up_product_kind",
        "slug",
        "tier",
    )
    first_day_of_the_week = sgqlc.types.Field(
        sgqlc.types.non_null(FirstDayOfTheWeek), graphql_name="first_day_of_the_week"
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="id")
    logo = sgqlc.types.Field(String, graphql_name="logo")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")
    plan = sgqlc.types.Field("Plan", graphql_name="plan")
    show_timeline_weekends = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="show_timeline_weekends"
    )
    sign_up_product_kind = sgqlc.types.Field(
        String, graphql_name="sign_up_product_kind"
    )
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="slug")
    tier = sgqlc.types.Field(String, graphql_name="tier")


class AccountProduct(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = ("id", "kind")
    id = sgqlc.types.Field(Int, graphql_name="id")
    kind = sgqlc.types.Field(AccountProductKind, graphql_name="kind")


class ActivityLogType(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = (
        "account_id",
        "created_at",
        "data",
        "entity",
        "event",
        "id",
        "user_id",
    )
    account_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="account_id"
    )
    created_at = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="created_at"
    )
    data = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="data")
    entity = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="entity")
    event = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="event")
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="user_id")


class AppFeature(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = (
        "app_id",
        "created_at",
        "data",
        "id",
        "name",
        "type",
        "updated_at",
    )
    app_id = sgqlc.types.Field(Int, graphql_name="app_id")
    created_at = sgqlc.types.Field(Date, graphql_name="created_at")
    data = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name="data")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="type")
    updated_at = sgqlc.types.Field(Date, graphql_name="updated_at")


class AppMonetizationStatus(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = ("is_supported",)
    is_supported = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="is_supported"
    )


class AppSubscription(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = (
        "billing_period",
        "days_left",
        "is_trial",
        "plan_id",
        "renewal_date",
    )
    billing_period = sgqlc.types.Field(String, graphql_name="billing_period")
    days_left = sgqlc.types.Field(Int, graphql_name="days_left")
    is_trial = sgqlc.types.Field(Boolean, graphql_name="is_trial")
    plan_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="plan_id")
    renewal_date = sgqlc.types.Field(
        sgqlc.types.non_null(Date), graphql_name="renewal_date"
    )


class Asset(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = (
        "created_at",
        "file_extension",
        "file_size",
        "id",
        "name",
        "original_geometry",
        "public_url",
        "uploaded_by",
        "url",
        "url_thumbnail",
    )
    created_at = sgqlc.types.Field(Date, graphql_name="created_at")
    file_extension = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="file_extension"
    )
    file_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="file_size")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")
    original_geometry = sgqlc.types.Field(String, graphql_name="original_geometry")
    public_url = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="public_url"
    )
    uploaded_by = sgqlc.types.Field(
        sgqlc.types.non_null("User"), graphql_name="uploaded_by"
    )
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="url")
    url_thumbnail = sgqlc.types.Field(String, graphql_name="url_thumbnail")


class Board(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = (
        "activity_logs",
        "board_folder_id",
        "board_kind",
        "columns",
        "communication",
        "creator",
        "description",
        "groups",
        "id",
        "items",
        "name",
        "owner",
        "owners",
        "permissions",
        "pos",
        "state",
        "subscribers",
        "tags",
        "top_group",
        "type",
        "updated_at",
        "updates",
        "views",
        "workspace",
        "workspace_id",
    )
    activity_logs = sgqlc.types.Field(
        sgqlc.types.list_of(ActivityLogType),
        graphql_name="activity_logs",
        args=sgqlc.types.ArgDict(
            (
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=25)),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=1)),
                (
                    "user_ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(Int), graphql_name="user_ids", default=None
                    ),
                ),
                (
                    "column_ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(String),
                        graphql_name="column_ids",
                        default=None,
                    ),
                ),
                (
                    "group_ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(String),
                        graphql_name="group_ids",
                        default=None,
                    ),
                ),
                (
                    "item_ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(Int), graphql_name="item_ids", default=None
                    ),
                ),
                (
                    "from_",
                    sgqlc.types.Arg(ISO8601DateTime, graphql_name="from", default=None),
                ),
                (
                    "to",
                    sgqlc.types.Arg(ISO8601DateTime, graphql_name="to", default=None),
                ),
            )
        ),
    )
    board_folder_id = sgqlc.types.Field(Int, graphql_name="board_folder_id")
    board_kind = sgqlc.types.Field(
        sgqlc.types.non_null(BoardKind), graphql_name="board_kind"
    )
    columns = sgqlc.types.Field(
        sgqlc.types.list_of("Column"),
        graphql_name="columns",
        args=sgqlc.types.ArgDict(
            (
                (
                    "ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(String), graphql_name="ids", default=None
                    ),
                ),
            )
        ),
    )
    communication = sgqlc.types.Field(JSON, graphql_name="communication")
    creator = sgqlc.types.Field(sgqlc.types.non_null("User"), graphql_name="creator")
    description = sgqlc.types.Field(String, graphql_name="description")
    groups = sgqlc.types.Field(
        sgqlc.types.list_of("Group"),
        graphql_name="groups",
        args=sgqlc.types.ArgDict(
            (
                (
                    "ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(String), graphql_name="ids", default=None
                    ),
                ),
            )
        ),
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    items = sgqlc.types.Field(
        sgqlc.types.list_of("Item"),
        graphql_name="items",
        args=sgqlc.types.ArgDict(
            (
                (
                    "ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(Int), graphql_name="ids", default=None
                    ),
                ),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=1)),
                (
                    "newest_first",
                    sgqlc.types.Arg(Boolean, graphql_name="newest_first", default=None),
                ),
                (
                    "exclude_nonactive",
                    sgqlc.types.Arg(
                        Boolean, graphql_name="exclude_nonactive", default=None
                    ),
                ),
            )
        ),
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")
    owner = sgqlc.types.Field(sgqlc.types.non_null("User"), graphql_name="owner")
    owners = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of("User")), graphql_name="owners"
    )
    permissions = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="permissions"
    )
    pos = sgqlc.types.Field(String, graphql_name="pos")
    state = sgqlc.types.Field(sgqlc.types.non_null(State), graphql_name="state")
    subscribers = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of("User")), graphql_name="subscribers"
    )
    tags = sgqlc.types.Field(sgqlc.types.list_of("Tag"), graphql_name="tags")
    top_group = sgqlc.types.Field(
        sgqlc.types.non_null("Group"), graphql_name="top_group"
    )
    type = sgqlc.types.Field(BoardObjectType, graphql_name="type")
    updated_at = sgqlc.types.Field(ISO8601DateTime, graphql_name="updated_at")
    updates = sgqlc.types.Field(
        sgqlc.types.list_of("Update"),
        graphql_name="updates",
        args=sgqlc.types.ArgDict(
            (
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=25)),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=1)),
            )
        ),
    )
    views = sgqlc.types.Field(
        sgqlc.types.list_of("BoardView"),
        graphql_name="views",
        args=sgqlc.types.ArgDict(
            (
                (
                    "ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(Int), graphql_name="ids", default=None
                    ),
                ),
                ("type", sgqlc.types.Arg(String, graphql_name="type", default=None)),
            )
        ),
    )
    workspace = sgqlc.types.Field("Workspace", graphql_name="workspace")
    workspace_id = sgqlc.types.Field(Int, graphql_name="workspace_id")


class BoardDuplication(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = ("board", "is_async")
    board = sgqlc.types.Field(sgqlc.types.non_null(Board), graphql_name="board")
    is_async = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="is_async")


class BoardView(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = ("id", "name", "settings_str", "type", "view_specific_data_str")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")
    settings_str = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="settings_str"
    )
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="type")
    view_specific_data_str = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="view_specific_data_str"
    )


class Column(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = (
        "archived",
        "description",
        "id",
        "pos",
        "settings_str",
        "title",
        "type",
        "width",
    )
    archived = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="archived")
    description = sgqlc.types.Field(String, graphql_name="description")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    pos = sgqlc.types.Field(String, graphql_name="pos")
    settings_str = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="settings_str"
    )
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="title")
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="type")
    width = sgqlc.types.Field(Int, graphql_name="width")


class ColumnValue(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = (
        "additional_info",
        "description",
        "id",
        "text",
        "title",
        "type",
        "value",
    )
    additional_info = sgqlc.types.Field(JSON, graphql_name="additional_info")
    description = sgqlc.types.Field(String, graphql_name="description")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    text = sgqlc.types.Field(String, graphql_name="text")
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="title")
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="type")
    value = sgqlc.types.Field(JSON, graphql_name="value")


class Complexity(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = ("after", "before", "query", "reset_in_x_seconds")
    after = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="after")
    before = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="before")
    query = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="query")
    reset_in_x_seconds = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="reset_in_x_seconds"
    )


class Group(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = (
        "archived",
        "color",
        "deleted",
        "id",
        "items",
        "position",
        "title",
    )
    archived = sgqlc.types.Field(Boolean, graphql_name="archived")
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="color")
    deleted = sgqlc.types.Field(Boolean, graphql_name="deleted")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    items = sgqlc.types.Field(
        sgqlc.types.list_of("Item"),
        graphql_name="items",
        args=sgqlc.types.ArgDict(
            (
                (
                    "ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(Int), graphql_name="ids", default=None
                    ),
                ),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=1)),
                (
                    "newest_first",
                    sgqlc.types.Arg(Boolean, graphql_name="newest_first", default=None),
                ),
                (
                    "exclude_nonactive",
                    sgqlc.types.Arg(
                        Boolean, graphql_name="exclude_nonactive", default=None
                    ),
                ),
            )
        ),
    )
    position = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="position")
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="title")


class Item(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = (
        "assets",
        "board",
        "column_values",
        "created_at",
        "creator",
        "creator_id",
        "email",
        "group",
        "id",
        "name",
        "parent_item",
        "state",
        "subitems",
        "subscribers",
        "updated_at",
        "updates",
    )
    assets = sgqlc.types.Field(
        sgqlc.types.list_of(Asset),
        graphql_name="assets",
        args=sgqlc.types.ArgDict(
            (
                (
                    "assets_source",
                    sgqlc.types.Arg(
                        AssetsSource, graphql_name="assets_source", default=None
                    ),
                ),
                (
                    "column_ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(String),
                        graphql_name="column_ids",
                        default=None,
                    ),
                ),
            )
        ),
    )
    board = sgqlc.types.Field(Board, graphql_name="board")
    column_values = sgqlc.types.Field(
        sgqlc.types.list_of(ColumnValue),
        graphql_name="column_values",
        args=sgqlc.types.ArgDict(
            (
                (
                    "ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(String), graphql_name="ids", default=None
                    ),
                ),
            )
        ),
    )
    created_at = sgqlc.types.Field(Date, graphql_name="created_at")
    creator = sgqlc.types.Field("User", graphql_name="creator")
    creator_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="creator_id"
    )
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="email")
    group = sgqlc.types.Field(Group, graphql_name="group")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")
    parent_item = sgqlc.types.Field("Item", graphql_name="parent_item")
    state = sgqlc.types.Field(State, graphql_name="state")
    subitems = sgqlc.types.Field(sgqlc.types.list_of("Item"), graphql_name="subitems")
    subscribers = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of("User")), graphql_name="subscribers"
    )
    updated_at = sgqlc.types.Field(Date, graphql_name="updated_at")
    updates = sgqlc.types.Field(
        sgqlc.types.list_of("Update"),
        graphql_name="updates",
        args=sgqlc.types.ArgDict(
            (
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=25)),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=1)),
            )
        ),
    )


class Mutation(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = (
        "add_file_to_column",
        "add_file_to_update",
        "add_subscribers_to_board",
        "add_teams_to_workspace",
        "add_users_to_workspace",
        "archive_board",
        "archive_group",
        "archive_item",
        "change_column_metadata",
        "change_column_title",
        "change_column_value",
        "change_multiple_column_values",
        "change_simple_column_value",
        "clear_item_updates",
        "complexity",
        "create_board",
        "create_column",
        "create_group",
        "create_item",
        "create_notification",
        "create_or_get_tag",
        "create_subitem",
        "create_update",
        "create_webhook",
        "create_workspace",
        "delete_board",
        "delete_group",
        "delete_item",
        "delete_subscribers_from_board",
        "delete_teams_from_workspace",
        "delete_update",
        "delete_users_from_workspace",
        "delete_webhook",
        "duplicate_board",
        "duplicate_group",
        "duplicate_item",
        "like_update",
        "move_item_to_group",
        "remove_mock_app_subscription",
        "set_mock_app_subscription",
        "update_board",
    )
    add_file_to_column = sgqlc.types.Field(
        Asset,
        graphql_name="add_file_to_column",
        args=sgqlc.types.ArgDict(
            (
                (
                    "item_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="item_id", default=None
                    ),
                ),
                (
                    "column_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="column_id",
                        default=None,
                    ),
                ),
                (
                    "file",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(File), graphql_name="file", default=None
                    ),
                ),
            )
        ),
    )
    add_file_to_update = sgqlc.types.Field(
        Asset,
        graphql_name="add_file_to_update",
        args=sgqlc.types.ArgDict(
            (
                (
                    "update_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int),
                        graphql_name="update_id",
                        default=None,
                    ),
                ),
                (
                    "file",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(File), graphql_name="file", default=None
                    ),
                ),
            )
        ),
    )
    add_subscribers_to_board = sgqlc.types.Field(
        sgqlc.types.list_of("User"),
        graphql_name="add_subscribers_to_board",
        args=sgqlc.types.ArgDict(
            (
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
                (
                    "user_ids",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(sgqlc.types.list_of(Int)),
                        graphql_name="user_ids",
                        default=None,
                    ),
                ),
                (
                    "kind",
                    sgqlc.types.Arg(
                        BoardSubscriberKind, graphql_name="kind", default="subscriber"
                    ),
                ),
            )
        ),
    )
    add_teams_to_workspace = sgqlc.types.Field(
        sgqlc.types.list_of("Team"),
        graphql_name="add_teams_to_workspace",
        args=sgqlc.types.ArgDict(
            (
                (
                    "workspace_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int),
                        graphql_name="workspace_id",
                        default=None,
                    ),
                ),
                (
                    "team_ids",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(sgqlc.types.list_of(Int)),
                        graphql_name="team_ids",
                        default=None,
                    ),
                ),
            )
        ),
    )
    add_users_to_workspace = sgqlc.types.Field(
        sgqlc.types.list_of("User"),
        graphql_name="add_users_to_workspace",
        args=sgqlc.types.ArgDict(
            (
                (
                    "workspace_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int),
                        graphql_name="workspace_id",
                        default=None,
                    ),
                ),
                (
                    "user_ids",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(sgqlc.types.list_of(Int)),
                        graphql_name="user_ids",
                        default=None,
                    ),
                ),
                (
                    "kind",
                    sgqlc.types.Arg(
                        WorkspaceSubscriberKind,
                        graphql_name="kind",
                        default="subscriber",
                    ),
                ),
            )
        ),
    )
    archive_board = sgqlc.types.Field(
        Board,
        graphql_name="archive_board",
        args=sgqlc.types.ArgDict(
            (
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
            )
        ),
    )
    archive_group = sgqlc.types.Field(
        Group,
        graphql_name="archive_group",
        args=sgqlc.types.ArgDict(
            (
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
                (
                    "group_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="group_id",
                        default=None,
                    ),
                ),
            )
        ),
    )
    archive_item = sgqlc.types.Field(
        Item,
        graphql_name="archive_item",
        args=sgqlc.types.ArgDict(
            (("item_id", sgqlc.types.Arg(Int, graphql_name="item_id", default=None)),)
        ),
    )
    change_column_metadata = sgqlc.types.Field(
        Column,
        graphql_name="change_column_metadata",
        args=sgqlc.types.ArgDict(
            (
                (
                    "column_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="column_id",
                        default=None,
                    ),
                ),
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
                (
                    "column_property",
                    sgqlc.types.Arg(
                        ColumnProperty, graphql_name="column_property", default=None
                    ),
                ),
                ("value", sgqlc.types.Arg(String, graphql_name="value", default=None)),
            )
        ),
    )
    change_column_title = sgqlc.types.Field(
        Column,
        graphql_name="change_column_title",
        args=sgqlc.types.ArgDict(
            (
                (
                    "column_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="column_id",
                        default=None,
                    ),
                ),
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
                (
                    "title",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="title", default=None
                    ),
                ),
            )
        ),
    )
    change_column_value = sgqlc.types.Field(
        Item,
        graphql_name="change_column_value",
        args=sgqlc.types.ArgDict(
            (
                ("item_id", sgqlc.types.Arg(Int, graphql_name="item_id", default=None)),
                (
                    "column_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="column_id",
                        default=None,
                    ),
                ),
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
                (
                    "value",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(JSON), graphql_name="value", default=None
                    ),
                ),
                (
                    "create_labels_if_missing",
                    sgqlc.types.Arg(
                        Boolean, graphql_name="create_labels_if_missing", default=None
                    ),
                ),
            )
        ),
    )
    change_multiple_column_values = sgqlc.types.Field(
        Item,
        graphql_name="change_multiple_column_values",
        args=sgqlc.types.ArgDict(
            (
                ("item_id", sgqlc.types.Arg(Int, graphql_name="item_id", default=None)),
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
                (
                    "column_values",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(JSON),
                        graphql_name="column_values",
                        default=None,
                    ),
                ),
                (
                    "create_labels_if_missing",
                    sgqlc.types.Arg(
                        Boolean, graphql_name="create_labels_if_missing", default=None
                    ),
                ),
            )
        ),
    )
    change_simple_column_value = sgqlc.types.Field(
        Item,
        graphql_name="change_simple_column_value",
        args=sgqlc.types.ArgDict(
            (
                ("item_id", sgqlc.types.Arg(Int, graphql_name="item_id", default=None)),
                (
                    "column_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="column_id",
                        default=None,
                    ),
                ),
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
                (
                    "value",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="value", default=None
                    ),
                ),
                (
                    "create_labels_if_missing",
                    sgqlc.types.Arg(
                        Boolean, graphql_name="create_labels_if_missing", default=None
                    ),
                ),
            )
        ),
    )
    clear_item_updates = sgqlc.types.Field(
        Item,
        graphql_name="clear_item_updates",
        args=sgqlc.types.ArgDict(
            (
                (
                    "item_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="item_id", default=None
                    ),
                ),
            )
        ),
    )
    complexity = sgqlc.types.Field(Complexity, graphql_name="complexity")
    create_board = sgqlc.types.Field(
        Board,
        graphql_name="create_board",
        args=sgqlc.types.ArgDict(
            (
                (
                    "board_name",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="board_name",
                        default=None,
                    ),
                ),
                (
                    "board_kind",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(BoardKind),
                        graphql_name="board_kind",
                        default=None,
                    ),
                ),
                (
                    "folder_id",
                    sgqlc.types.Arg(Int, graphql_name="folder_id", default=None),
                ),
                (
                    "workspace_id",
                    sgqlc.types.Arg(Int, graphql_name="workspace_id", default=None),
                ),
                (
                    "template_id",
                    sgqlc.types.Arg(Int, graphql_name="template_id", default=None),
                ),
                (
                    "board_owner_ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(Int),
                        graphql_name="board_owner_ids",
                        default=None,
                    ),
                ),
                (
                    "board_subscriber_ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(Int),
                        graphql_name="board_subscriber_ids",
                        default=None,
                    ),
                ),
            )
        ),
    )
    create_column = sgqlc.types.Field(
        Column,
        graphql_name="create_column",
        args=sgqlc.types.ArgDict(
            (
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
                (
                    "title",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="title", default=None
                    ),
                ),
                (
                    "description",
                    sgqlc.types.Arg(String, graphql_name="description", default=None),
                ),
                (
                    "column_type",
                    sgqlc.types.Arg(
                        ColumnType, graphql_name="column_type", default=None
                    ),
                ),
                (
                    "defaults",
                    sgqlc.types.Arg(JSON, graphql_name="defaults", default=None),
                ),
            )
        ),
    )
    create_group = sgqlc.types.Field(
        Group,
        graphql_name="create_group",
        args=sgqlc.types.ArgDict(
            (
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
                (
                    "group_name",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="group_name",
                        default=None,
                    ),
                ),
            )
        ),
    )
    create_item = sgqlc.types.Field(
        Item,
        graphql_name="create_item",
        args=sgqlc.types.ArgDict(
            (
                (
                    "item_name",
                    sgqlc.types.Arg(String, graphql_name="item_name", default=None),
                ),
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
                (
                    "group_id",
                    sgqlc.types.Arg(String, graphql_name="group_id", default=None),
                ),
                (
                    "column_values",
                    sgqlc.types.Arg(JSON, graphql_name="column_values", default=None),
                ),
                (
                    "create_labels_if_missing",
                    sgqlc.types.Arg(
                        Boolean, graphql_name="create_labels_if_missing", default=None
                    ),
                ),
            )
        ),
    )
    create_notification = sgqlc.types.Field(
        "Notification",
        graphql_name="create_notification",
        args=sgqlc.types.ArgDict(
            (
                (
                    "text",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="text", default=None
                    ),
                ),
                (
                    "user_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="user_id", default=None
                    ),
                ),
                (
                    "target_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int),
                        graphql_name="target_id",
                        default=None,
                    ),
                ),
                (
                    "target_type",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(NotificationTargetType),
                        graphql_name="target_type",
                        default=None,
                    ),
                ),
            )
        ),
    )
    create_or_get_tag = sgqlc.types.Field(
        "Tag",
        graphql_name="create_or_get_tag",
        args=sgqlc.types.ArgDict(
            (
                (
                    "tag_name",
                    sgqlc.types.Arg(String, graphql_name="tag_name", default=None),
                ),
                (
                    "board_id",
                    sgqlc.types.Arg(Int, graphql_name="board_id", default=None),
                ),
            )
        ),
    )
    create_subitem = sgqlc.types.Field(
        Item,
        graphql_name="create_subitem",
        args=sgqlc.types.ArgDict(
            (
                (
                    "parent_item_id",
                    sgqlc.types.Arg(Int, graphql_name="parent_item_id", default=None),
                ),
                (
                    "item_name",
                    sgqlc.types.Arg(String, graphql_name="item_name", default=None),
                ),
                (
                    "column_values",
                    sgqlc.types.Arg(JSON, graphql_name="column_values", default=None),
                ),
                (
                    "create_labels_if_missing",
                    sgqlc.types.Arg(
                        Boolean, graphql_name="create_labels_if_missing", default=None
                    ),
                ),
            )
        ),
    )
    create_update = sgqlc.types.Field(
        "Update",
        graphql_name="create_update",
        args=sgqlc.types.ArgDict(
            (
                (
                    "body",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="body", default=None
                    ),
                ),
                ("item_id", sgqlc.types.Arg(Int, graphql_name="item_id", default=None)),
                (
                    "parent_id",
                    sgqlc.types.Arg(Int, graphql_name="parent_id", default=None),
                ),
            )
        ),
    )
    create_webhook = sgqlc.types.Field(
        "Webhook",
        graphql_name="create_webhook",
        args=sgqlc.types.ArgDict(
            (
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
                (
                    "url",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="url", default=None
                    ),
                ),
                (
                    "event",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(WebhookEventType),
                        graphql_name="event",
                        default=None,
                    ),
                ),
                ("config", sgqlc.types.Arg(JSON, graphql_name="config", default=None)),
            )
        ),
    )
    create_workspace = sgqlc.types.Field(
        "Workspace",
        graphql_name="create_workspace",
        args=sgqlc.types.ArgDict(
            (
                (
                    "name",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="name", default=None
                    ),
                ),
                (
                    "kind",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(WorkspaceKind),
                        graphql_name="kind",
                        default=None,
                    ),
                ),
                (
                    "description",
                    sgqlc.types.Arg(String, graphql_name="description", default=None),
                ),
            )
        ),
    )
    delete_board = sgqlc.types.Field(
        Board,
        graphql_name="delete_board",
        args=sgqlc.types.ArgDict(
            (
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
            )
        ),
    )
    delete_group = sgqlc.types.Field(
        Group,
        graphql_name="delete_group",
        args=sgqlc.types.ArgDict(
            (
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
                (
                    "group_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="group_id",
                        default=None,
                    ),
                ),
            )
        ),
    )
    delete_item = sgqlc.types.Field(
        Item,
        graphql_name="delete_item",
        args=sgqlc.types.ArgDict(
            (("item_id", sgqlc.types.Arg(Int, graphql_name="item_id", default=None)),)
        ),
    )
    delete_subscribers_from_board = sgqlc.types.Field(
        sgqlc.types.list_of("User"),
        graphql_name="delete_subscribers_from_board",
        args=sgqlc.types.ArgDict(
            (
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
                (
                    "user_ids",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(sgqlc.types.list_of(Int)),
                        graphql_name="user_ids",
                        default=None,
                    ),
                ),
            )
        ),
    )
    delete_teams_from_workspace = sgqlc.types.Field(
        sgqlc.types.list_of("Team"),
        graphql_name="delete_teams_from_workspace",
        args=sgqlc.types.ArgDict(
            (
                (
                    "workspace_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int),
                        graphql_name="workspace_id",
                        default=None,
                    ),
                ),
                (
                    "team_ids",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(sgqlc.types.list_of(Int)),
                        graphql_name="team_ids",
                        default=None,
                    ),
                ),
            )
        ),
    )
    delete_update = sgqlc.types.Field(
        "Update",
        graphql_name="delete_update",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    delete_users_from_workspace = sgqlc.types.Field(
        sgqlc.types.list_of("User"),
        graphql_name="delete_users_from_workspace",
        args=sgqlc.types.ArgDict(
            (
                (
                    "workspace_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int),
                        graphql_name="workspace_id",
                        default=None,
                    ),
                ),
                (
                    "user_ids",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(sgqlc.types.list_of(Int)),
                        graphql_name="user_ids",
                        default=None,
                    ),
                ),
            )
        ),
    )
    delete_webhook = sgqlc.types.Field(
        "Webhook",
        graphql_name="delete_webhook",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    duplicate_board = sgqlc.types.Field(
        BoardDuplication,
        graphql_name="duplicate_board",
        args=sgqlc.types.ArgDict(
            (
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
                (
                    "duplicate_type",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(DuplicateBoardType),
                        graphql_name="duplicate_type",
                        default=None,
                    ),
                ),
                (
                    "board_name",
                    sgqlc.types.Arg(String, graphql_name="board_name", default=None),
                ),
                (
                    "workspace_id",
                    sgqlc.types.Arg(Int, graphql_name="workspace_id", default=None),
                ),
                (
                    "folder_id",
                    sgqlc.types.Arg(Int, graphql_name="folder_id", default=None),
                ),
                (
                    "keep_subscribers",
                    sgqlc.types.Arg(
                        Boolean, graphql_name="keep_subscribers", default=None
                    ),
                ),
            )
        ),
    )
    duplicate_group = sgqlc.types.Field(
        Group,
        graphql_name="duplicate_group",
        args=sgqlc.types.ArgDict(
            (
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
                (
                    "group_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="group_id",
                        default=None,
                    ),
                ),
                (
                    "add_to_top",
                    sgqlc.types.Arg(Boolean, graphql_name="add_to_top", default=None),
                ),
                (
                    "group_title",
                    sgqlc.types.Arg(String, graphql_name="group_title", default=None),
                ),
            )
        ),
    )
    duplicate_item = sgqlc.types.Field(
        Item,
        graphql_name="duplicate_item",
        args=sgqlc.types.ArgDict(
            (
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
                (
                    "with_updates",
                    sgqlc.types.Arg(Boolean, graphql_name="with_updates", default=None),
                ),
                ("item_id", sgqlc.types.Arg(Int, graphql_name="item_id", default=None)),
            )
        ),
    )
    like_update = sgqlc.types.Field(
        "Update",
        graphql_name="like_update",
        args=sgqlc.types.ArgDict(
            (
                (
                    "update_id",
                    sgqlc.types.Arg(Int, graphql_name="update_id", default=None),
                ),
            )
        ),
    )
    move_item_to_group = sgqlc.types.Field(
        Item,
        graphql_name="move_item_to_group",
        args=sgqlc.types.ArgDict(
            (
                ("item_id", sgqlc.types.Arg(Int, graphql_name="item_id", default=None)),
                (
                    "group_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="group_id",
                        default=None,
                    ),
                ),
            )
        ),
    )
    remove_mock_app_subscription = sgqlc.types.Field(
        AppSubscription,
        graphql_name="remove_mock_app_subscription",
        args=sgqlc.types.ArgDict(
            (
                (
                    "app_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="app_id", default=None
                    ),
                ),
                (
                    "partial_signing_secret",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="partial_signing_secret",
                        default=None,
                    ),
                ),
            )
        ),
    )
    set_mock_app_subscription = sgqlc.types.Field(
        AppSubscription,
        graphql_name="set_mock_app_subscription",
        args=sgqlc.types.ArgDict(
            (
                (
                    "app_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="app_id", default=None
                    ),
                ),
                (
                    "partial_signing_secret",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="partial_signing_secret",
                        default=None,
                    ),
                ),
                (
                    "plan_id",
                    sgqlc.types.Arg(String, graphql_name="plan_id", default=None),
                ),
                (
                    "is_trial",
                    sgqlc.types.Arg(Boolean, graphql_name="is_trial", default=None),
                ),
                (
                    "renewal_date",
                    sgqlc.types.Arg(Date, graphql_name="renewal_date", default=None),
                ),
                (
                    "billing_period",
                    sgqlc.types.Arg(
                        String, graphql_name="billing_period", default=None
                    ),
                ),
            )
        ),
    )
    update_board = sgqlc.types.Field(
        JSON,
        graphql_name="update_board",
        args=sgqlc.types.ArgDict(
            (
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
                (
                    "board_attribute",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(BoardAttributes),
                        graphql_name="board_attribute",
                        default=None,
                    ),
                ),
                (
                    "new_value",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="new_value",
                        default=None,
                    ),
                ),
            )
        ),
    )


class Notification(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = ("id", "text")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    text = sgqlc.types.Field(String, graphql_name="text")


class Plan(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = ("max_users", "period", "tier", "version")
    max_users = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="max_users")
    period = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="period")
    tier = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="tier")
    version = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="version")


class Query(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = (
        "account",
        "app_subscription",
        "apps_monetization_status",
        "assets",
        "boards",
        "complexity",
        "items",
        "items_by_column_values",
        "items_by_multiple_column_values",
        "me",
        "tags",
        "teams",
        "updates",
        "users",
        "webhooks",
    )
    account = sgqlc.types.Field(Account, graphql_name="account")
    app_subscription = sgqlc.types.Field(
        sgqlc.types.list_of(AppSubscription), graphql_name="app_subscription"
    )
    apps_monetization_status = sgqlc.types.Field(
        AppMonetizationStatus, graphql_name="apps_monetization_status"
    )
    assets = sgqlc.types.Field(
        sgqlc.types.list_of(Asset),
        graphql_name="assets",
        args=sgqlc.types.ArgDict(
            (
                (
                    "ids",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(sgqlc.types.list_of(Int)),
                        graphql_name="ids",
                        default=None,
                    ),
                ),
            )
        ),
    )
    boards = sgqlc.types.Field(
        sgqlc.types.list_of(Board),
        graphql_name="boards",
        args=sgqlc.types.ArgDict(
            (
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=25)),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=1)),
                (
                    "ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(Int), graphql_name="ids", default=None
                    ),
                ),
                (
                    "board_kind",
                    sgqlc.types.Arg(BoardKind, graphql_name="board_kind", default=None),
                ),
                (
                    "state",
                    sgqlc.types.Arg(State, graphql_name="state", default="active"),
                ),
                (
                    "newest_first",
                    sgqlc.types.Arg(Boolean, graphql_name="newest_first", default=None),
                ),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        BoardsOrderBy, graphql_name="order_by", default=None
                    ),
                ),
            )
        ),
    )
    complexity = sgqlc.types.Field(Complexity, graphql_name="complexity")
    items = sgqlc.types.Field(
        sgqlc.types.list_of(Item),
        graphql_name="items",
        args=sgqlc.types.ArgDict(
            (
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=25)),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=1)),
                (
                    "ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(Int), graphql_name="ids", default=None
                    ),
                ),
                (
                    "newest_first",
                    sgqlc.types.Arg(Boolean, graphql_name="newest_first", default=None),
                ),
                (
                    "exclude_nonactive",
                    sgqlc.types.Arg(
                        Boolean, graphql_name="exclude_nonactive", default=None
                    ),
                ),
            )
        ),
    )
    items_by_column_values = sgqlc.types.Field(
        sgqlc.types.list_of(Item),
        graphql_name="items_by_column_values",
        args=sgqlc.types.ArgDict(
            (
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=1)),
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
                (
                    "column_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="column_id",
                        default=None,
                    ),
                ),
                (
                    "column_value",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="column_value",
                        default=None,
                    ),
                ),
                (
                    "column_type",
                    sgqlc.types.Arg(String, graphql_name="column_type", default=None),
                ),
                (
                    "state",
                    sgqlc.types.Arg(State, graphql_name="state", default="active"),
                ),
            )
        ),
    )
    items_by_multiple_column_values = sgqlc.types.Field(
        sgqlc.types.list_of(Item),
        graphql_name="items_by_multiple_column_values",
        args=sgqlc.types.ArgDict(
            (
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=1)),
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
                (
                    "column_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="column_id",
                        default=None,
                    ),
                ),
                (
                    "column_values",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(sgqlc.types.list_of(String)),
                        graphql_name="column_values",
                        default=None,
                    ),
                ),
                (
                    "column_type",
                    sgqlc.types.Arg(String, graphql_name="column_type", default=None),
                ),
                (
                    "state",
                    sgqlc.types.Arg(State, graphql_name="state", default="active"),
                ),
            )
        ),
    )
    me = sgqlc.types.Field("User", graphql_name="me")
    tags = sgqlc.types.Field(
        sgqlc.types.list_of("Tag"),
        graphql_name="tags",
        args=sgqlc.types.ArgDict(
            (
                (
                    "ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(Int), graphql_name="ids", default=None
                    ),
                ),
            )
        ),
    )
    teams = sgqlc.types.Field(
        sgqlc.types.list_of("Team"),
        graphql_name="teams",
        args=sgqlc.types.ArgDict(
            (
                (
                    "ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(Int), graphql_name="ids", default=None
                    ),
                ),
            )
        ),
    )
    updates = sgqlc.types.Field(
        sgqlc.types.list_of("Update"),
        graphql_name="updates",
        args=sgqlc.types.ArgDict(
            (
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=25)),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=1)),
            )
        ),
    )
    users = sgqlc.types.Field(
        sgqlc.types.list_of("User"),
        graphql_name="users",
        args=sgqlc.types.ArgDict(
            (
                (
                    "ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(Int), graphql_name="ids", default=None
                    ),
                ),
                ("kind", sgqlc.types.Arg(UserKind, graphql_name="kind", default=None)),
                (
                    "newest_first",
                    sgqlc.types.Arg(Boolean, graphql_name="newest_first", default=None),
                ),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                (
                    "emails",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(String), graphql_name="emails", default=None
                    ),
                ),
            )
        ),
    )
    webhooks = sgqlc.types.Field(
        sgqlc.types.list_of("Webhook"),
        graphql_name="webhooks",
        args=sgqlc.types.ArgDict(
            (
                (
                    "board_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="board_id", default=None
                    ),
                ),
            )
        ),
    )


class Reply(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = (
        "body",
        "created_at",
        "creator",
        "creator_id",
        "id",
        "text_body",
        "updated_at",
    )
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="body")
    created_at = sgqlc.types.Field(Date, graphql_name="created_at")
    creator = sgqlc.types.Field("User", graphql_name="creator")
    creator_id = sgqlc.types.Field(String, graphql_name="creator_id")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    text_body = sgqlc.types.Field(String, graphql_name="text_body")
    updated_at = sgqlc.types.Field(Date, graphql_name="updated_at")


class Tag(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = ("color", "id", "name")
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="color")
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="id")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class Team(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = ("id", "name", "picture_url", "users")
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="id")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")
    picture_url = sgqlc.types.Field(String, graphql_name="picture_url")
    users = sgqlc.types.Field(
        sgqlc.types.list_of("User"),
        graphql_name="users",
        args=sgqlc.types.ArgDict(
            (
                (
                    "ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(Int), graphql_name="ids", default=None
                    ),
                ),
                ("kind", sgqlc.types.Arg(UserKind, graphql_name="kind", default=None)),
                (
                    "newest_first",
                    sgqlc.types.Arg(Boolean, graphql_name="newest_first", default=None),
                ),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                (
                    "emails",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(String), graphql_name="emails", default=None
                    ),
                ),
            )
        ),
    )


class Update(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = (
        "assets",
        "body",
        "created_at",
        "creator",
        "creator_id",
        "id",
        "item_id",
        "replies",
        "text_body",
        "updated_at",
    )
    assets = sgqlc.types.Field(sgqlc.types.list_of(Asset), graphql_name="assets")
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="body")
    created_at = sgqlc.types.Field(Date, graphql_name="created_at")
    creator = sgqlc.types.Field("User", graphql_name="creator")
    creator_id = sgqlc.types.Field(String, graphql_name="creator_id")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    item_id = sgqlc.types.Field(String, graphql_name="item_id")
    replies = sgqlc.types.Field(sgqlc.types.list_of(Reply), graphql_name="replies")
    text_body = sgqlc.types.Field(String, graphql_name="text_body")
    updated_at = sgqlc.types.Field(Date, graphql_name="updated_at")


class User(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = (
        "account",
        "birthday",
        "country_code",
        "created_at",
        "current_language",
        "email",
        "enabled",
        "encrypt_api_token",
        "id",
        "is_admin",
        "is_guest",
        "is_pending",
        "is_verified",
        "is_view_only",
        "join_date",
        "location",
        "mobile_phone",
        "name",
        "phone",
        "photo_original",
        "photo_small",
        "photo_thumb",
        "photo_thumb_small",
        "photo_tiny",
        "sign_up_product_kind",
        "teams",
        "time_zone_identifier",
        "title",
        "url",
        "utc_hours_diff",
    )
    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name="account")
    birthday = sgqlc.types.Field(Date, graphql_name="birthday")
    country_code = sgqlc.types.Field(String, graphql_name="country_code")
    created_at = sgqlc.types.Field(Date, graphql_name="created_at")
    current_language = sgqlc.types.Field(String, graphql_name="current_language")
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="email")
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")
    encrypt_api_token = sgqlc.types.Field(String, graphql_name="encrypt_api_token")
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="id")
    is_admin = sgqlc.types.Field(Boolean, graphql_name="is_admin")
    is_guest = sgqlc.types.Field(Boolean, graphql_name="is_guest")
    is_pending = sgqlc.types.Field(Boolean, graphql_name="is_pending")
    is_verified = sgqlc.types.Field(Boolean, graphql_name="is_verified")
    is_view_only = sgqlc.types.Field(Boolean, graphql_name="is_view_only")
    join_date = sgqlc.types.Field(Date, graphql_name="join_date")
    location = sgqlc.types.Field(String, graphql_name="location")
    mobile_phone = sgqlc.types.Field(String, graphql_name="mobile_phone")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")
    phone = sgqlc.types.Field(String, graphql_name="phone")
    photo_original = sgqlc.types.Field(String, graphql_name="photo_original")
    photo_small = sgqlc.types.Field(String, graphql_name="photo_small")
    photo_thumb = sgqlc.types.Field(String, graphql_name="photo_thumb")
    photo_thumb_small = sgqlc.types.Field(String, graphql_name="photo_thumb_small")
    photo_tiny = sgqlc.types.Field(String, graphql_name="photo_tiny")
    sign_up_product_kind = sgqlc.types.Field(
        String, graphql_name="sign_up_product_kind"
    )
    teams = sgqlc.types.Field(
        sgqlc.types.list_of(Team),
        graphql_name="teams",
        args=sgqlc.types.ArgDict(
            (
                (
                    "ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(Int), graphql_name="ids", default=None
                    ),
                ),
            )
        ),
    )
    time_zone_identifier = sgqlc.types.Field(
        String, graphql_name="time_zone_identifier"
    )
    title = sgqlc.types.Field(String, graphql_name="title")
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="url")
    utc_hours_diff = sgqlc.types.Field(Int, graphql_name="utc_hours_diff")


class Webhook(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = ("board_id", "config", "event", "id")
    board_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="board_id")
    config = sgqlc.types.Field(String, graphql_name="config")
    event = sgqlc.types.Field(
        sgqlc.types.non_null(WebhookEventType), graphql_name="event"
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")


class Workspace(sgqlc.types.Type):
    """
    See source code for the more info.
    """

    __schema__ = graphql_schema
    __field_names__ = ("account_product", "description", "id", "kind", "name")
    account_product = sgqlc.types.Field(AccountProduct, graphql_name="account_product")
    description = sgqlc.types.Field(String, graphql_name="description")
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="id")
    kind = sgqlc.types.Field(WorkspaceKind, graphql_name="kind")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
graphql_schema.query_type = Query
graphql_schema.mutation_type = Mutation
graphql_schema.subscription_type = None
