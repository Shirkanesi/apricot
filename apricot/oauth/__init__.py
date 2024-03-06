from .enums import OAuthBackend
from .microsoft_entra_client import MicrosoftEntraClient
from .oauth_client import OAuthClient
from .types import LDAPAttributeDict, LDAPControlTuple

OAuthClientMap = {OAuthBackend.MICROSOFT_ENTRA: MicrosoftEntraClient}

__all__ = [
    "LDAPAttributeDict",
    "LDAPControlTuple",
    "OAuthBackend",
    "OAuthClient",
    "OAuthClientMap",
]
