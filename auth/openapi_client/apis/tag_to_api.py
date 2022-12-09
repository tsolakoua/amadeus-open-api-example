import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.amadeus_o_auth2_access_token_api import AmadeusOAuth2AccessTokenApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.OAUTH2_ACCESS_TOKEN: AmadeusOAuth2AccessTokenApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.OAUTH2_ACCESS_TOKEN: AmadeusOAuth2AccessTokenApi,
    }
)
