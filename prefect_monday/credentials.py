"""Credential classes used to perform authenticated interactions with Monday"""

from dataclasses import dataclass

from sgqlc.endpoint.http import HTTPEndpoint


@dataclass
class MondayCredentials:
    """
    Dataclass used to manage Monday authentication.

    Args:
        token: the token to authenticate into Monday.
    """

    token: str

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
                monday_credentials = MondayCredentials(token)
                endpoint = monday_credentials.get_endpoint()
                return endpoint

            example_get_endpoint_flow()
            ```
        """
        endpoint = HTTPEndpoint(
            "https://api.monday.com/v2", {"Authorization": f"Bearer {self.token}"}
        )
        return endpoint
