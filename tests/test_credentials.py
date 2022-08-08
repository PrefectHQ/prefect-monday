import pytest
from sgqlc.endpoint.http import HTTPEndpoint

from prefect_monday import MondayCredentials


@pytest.mark.parametrize("token", [None, "token_value"])
def test_monday_credentials_get_endpoint(token):
    endpoint = MondayCredentials(token=token).get_endpoint()
    assert isinstance(endpoint, HTTPEndpoint)
    if token is not None:
        assert endpoint.base_headers == {"Authorization": "Bearer token_value"}
