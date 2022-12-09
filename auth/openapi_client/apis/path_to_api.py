import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.security_oauth2_token import AmadeusSecurityOauth2Token
from openapi_client.apis.paths.security_oauth2_token_access_token import AmadeusSecurityOauth2TokenAccessToken

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.SECURITY_OAUTH2_TOKEN: AmadeusSecurityOauth2Token,
        PathValues.SECURITY_OAUTH2_TOKEN_ACCESS_TOKEN: AmadeusSecurityOauth2TokenAccessToken,
    }
)

path_to_api = PathToApi(
    {
        PathValues.SECURITY_OAUTH2_TOKEN: AmadeusSecurityOauth2Token,
        PathValues.SECURITY_OAUTH2_TOKEN_ACCESS_TOKEN: AmadeusSecurityOauth2TokenAccessToken,
    }
)
