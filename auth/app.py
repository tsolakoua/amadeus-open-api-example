import openapi_client
from openapi_client.apis.tags import amadeus_o_auth2_access_token_api
from openapi_client.model.amadeus_amadeus_o_auth2_token import AmadeusAmadeusOAuth2Token
from pprint import pprint

configuration = openapi_client.Configuration(
    host = "https://test.api.amadeus.com/v1"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = amadeus_o_auth2_access_token_api.AmadeusOAuth2AccessTokenApi(api_client)

    # example passing only optional values
    body = dict(
        grant_type="client_credentials",
        client_id="",
        client_secret="",
    )
    # The OAuth 2.0 token endpoint
    api_response = api_instance.oauth2_token(
        body=body,
    )
    pprint(api_response)