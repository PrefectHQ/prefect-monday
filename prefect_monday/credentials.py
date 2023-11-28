"""Credential classes used to perform authenticated interactions with Monday"""

from prefect.blocks.core import Block
from pydantic import VERSION as PYDANTIC_VERSION

if PYDANTIC_VERSION.startswith("2."):
    from pydantic.v1 import SecretStr
else:
    from pydantic import SecretStr

from sgqlc.endpoint.http import HTTPEndpoint


class MondayCredentials(Block):
    """
    Block used to manage Monday authentication.

    Attributes:
        token: the token to authenticate into Monday.

    Examples:
        Load stored Monday credentials:
        ```python
        from prefect_monday import MondayCredentials
        monday_credentials_block = MondayCredentials.load("BLOCK_NAME")
        ```
    """

    _block_type_name = "Monday Credentials"
    _logo_url = "https://cdn.sanity.io/images/3ugk85nk/production/ad8614977614bcafee59ec5a3ef080111f045ffc-250x250.png"  # noqa

    token: SecretStr = None

    def get_endpoint(self) -> HTTPEndpoint:
        """
        Gets an authenticated Monday GraphQL HTTPEndpoint.

        Returns:
            An authenticated Monday GraphQL HTTPEndpoint

        Example:
            Gets an authenticated Monday GraphQL HTTPEndpoint.
            ```python
            from prefect import flow
            from prefect_monday import MondayCredentials

            @flow
            def example_get_endpoint_flow():
                token = "token_xxxxxxx"
                monday_credentials = MondayCredentials(token=token)
                endpoint = monday_credentials.get_endpoint()
                return endpoint

            example_get_endpoint_flow()
            ```
        """
        if self.token is not None:
            base_headers = {"Authorization": f"Bearer {self.token.get_secret_value()}"}
        else:
            base_headers = None
        endpoint = HTTPEndpoint("https://api.monday.com/v2", base_headers=base_headers)
        return endpoint
