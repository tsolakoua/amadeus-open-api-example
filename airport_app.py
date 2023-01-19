import os
import sys

import airport_routes.openapi_client
from airport_routes.openapi_client.apis.tags import direct_destinations_api
from airport_routes.openapi_client.model.locations import Locations
from airport_routes.openapi_client.model.meta import Meta
from airport_routes.openapi_client.model.errors import Errors
from airport_routes.openapi_client.model.warnings import Warnings
from airport_routes.pprint import pprint


import auth.openapi_client
from auth.auth.openapi_client.apis.tags import amadeus_o_auth2_access_token_api
from auth.auth.openapi_client.model.amadeus_amadeus_o_auth2_token import AmadeusAmadeusOAuth2Token

sys.path.append('/Users/atsolakou/Desktop/workspace/amadeus-open-api-example/auth')
sys.path.append('/Users/atsolakou/Desktop/workspace/amadeus-open-api-example/airport_routes')


configuration = openapi_client.Configuration(
    host = "https://test.api.amadeus.com/v1"
)

with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = amadeus_o_auth2_access_token_api.AmadeusOAuth2AccessTokenApi(api_client)

    body = dict(
        grant_type="client_credentials",
        client_id="ID",
        client_secret="SECRET",
    )
    api_response = api_instance.oauth2_token(
        body=body,
    )

configuration = openapi_client.Configuration()
api_client = openapi_client.ApiClient(configuration)
api_client.default_headers['Authorization'] = 'Bearer' + api_response.body['access_token']

api_instance = direct_destinations_api.DirectDestinationsApi(api_client)

query_params = {
    'departureAirportCode': "BLR",
}
try:
    api_response = api_instance.airport__direct_destinations(
        query_params=query_params,
    )
    pprint(api_response.body)
except openapi_client.ApiException as e:
    print("Exception when calling Covid19AreaReportApi->g_et_covid_report: %s\n" % e)