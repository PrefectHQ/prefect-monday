"""Credential classes used to perform authenticated interactions with Monday"""

from prefect.blocks.core import Block
from pydantic import SecretStr
from sgqlc.endpoint.http import HTTPEndpoint


class MondayCredentials(Block):
    """
    Block used to manage Monday authentication.

    Args:
        token: the token to authenticate into Monday.

    Examples:
        Load stored Monday credentials:
        ```python
        from prefect_monday import MondayCredentials
        monday_credentials_block = MondayCredentials.load("BLOCK_NAME")
        ```
    """

    _block_type_name = "Monday Credentials"
    _logo_url = "https://images.ctfassets.net/gm98wzqotmnx/3ohoKiYTO3Kjt6sri58HXu/27b45e8641127b196008976dde856058/imageedit_5_6047243931.png?h=250"  # noqa

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
                token = "consumer_key"
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
