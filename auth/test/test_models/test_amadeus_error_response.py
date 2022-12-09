# coding: utf-8

"""
    Amadeus OAuth2 Login

    Amadeus for Developers uses OAuth2 to authenticate access requests. OAuth2 generates an access token which grants the client permission to access a protected resource. The method to acquire a token is called grant. There are different types of OAuth2 grants. Amadeus for Developers uses the Client Credentials Grant.   https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import unittest

import openapi_client
from openapi_client.model.amadeus_error_response import AmadeusErrorResponse
from openapi_client import configuration


class TestAmadeusErrorResponse(unittest.TestCase):
    """AmadeusErrorResponse unit test stubs"""
    _configuration = configuration.Configuration()


if __name__ == '__main__':
    unittest.main()
