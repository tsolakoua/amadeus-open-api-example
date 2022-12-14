# coding: utf-8

"""
    Amadeus OAuth2 Login

    Amadeus for Developers uses OAuth2 to authenticate access requests. OAuth2 generates an access token which grants the client permission to access a protected resource. The method to acquire a token is called grant. There are different types of OAuth2 grants. Amadeus for Developers uses the Client Credentials Grant.   https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.security_oauth2_token_access_token.get import GetOauth2TokenInfo
from openapi_client.paths.security_oauth2_token.post import Oauth2Token


class AmadeusOAuth2AccessTokenApi(
    GetOauth2TokenInfo,
    Oauth2Token,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
