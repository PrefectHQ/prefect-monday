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
    def __init__(self, fail=False):
        self.result = {"errors": 42} if fail else {"data": "success"}

    def get_endpoint(self):
        return lambda op, vars: self.result


@pytest.mark.parametrize("fail", [True, False])
def test_execute_graphql(fail):
    mock_credentials = MockCredentials(fail=fail)

    @flow
    def test_flow():
        return execute_graphql("op", mock_credentials)

    if fail:
        with pytest.raises(RuntimeError, match="Errors encountered:"):
            test_flow()
    else:
        assert test_flow() == "success"