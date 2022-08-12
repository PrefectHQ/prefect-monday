import pytest
from prefect import flow
from sgqlc.operation import Operation, Selector

from prefect_monday.graphql import _subset_return_fields, execute_graphql
from prefect_monday.schemas import graphql_schema


@pytest.mark.parametrize(
    "return_fields_key", ["return_fields", "return_fields_defaults"]
)
def test_subset_return_fields(return_fields_key):
    op = Operation(graphql_schema.Query)
    op_stack = graphql_schema.Query.__field_names__[:1]
    op_selection = getattr(op, op_stack[0])
    subset_kwargs = {"return_fields": [], "return_fields_defaults": {}}
    return_fields = ["id"]
    if return_fields_key == "return_fields":
        subset_kwargs[return_fields_key] = return_fields
    else:
        subset_kwargs[return_fields_key] = {op_stack: return_fields}
    op_selection = _subset_return_fields(op_selection, op_stack, **subset_kwargs)
    assert isinstance(op_selection, Selector)


class MockCredentials:
    def __init__(self, fail_key=None):
        self.result = {fail_key: "Expected fail"} if fail_key else {"data": "success"}

    def get_endpoint(self):
        return lambda op, vars: self.result


@pytest.mark.parametrize("fail_key", ["errors", "error_message", False])
def test_execute_graphql(fail_key):
    mock_credentials = MockCredentials(fail_key=fail_key)

    @flow
    def test_flow():
        return execute_graphql("op", mock_credentials)

    if fail_key:
        match = "Errors encountered:" if fail_key == "errors" else "Expected fail"
        with pytest.raises(RuntimeError, match=match):
            test_flow()
    else:
        assert test_flow() == "success"
