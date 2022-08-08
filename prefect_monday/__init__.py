from . import _version
from .credentials import MondayCredentials  # noqa for testing

__version__ = _version.get_versions()["version"]
