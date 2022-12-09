import openapi_client
from openapi_client.apis.tags import covid19_area_report_api
from openapi_client.model.disease_area_report import DiseaseAreaReport
from openapi_client.model.error import Error
from openapi_client.model.meta import Meta
from openapi_client.model.warning import Warning
from pprint import pprint

import time
import openapi_client
from pprint import pprint
from openapi_client.apis.tags import amadeus_o_auth2_access_token_api
from openapi_client.model.amadeus_amadeus_amadeus_o_auth2_token import AmadeusAmadeusAmadeusOAuth2Token
from openapi_client.model.amadeus_amadeus_error_response import AmadeusAmadeusErrorResponse
# Defining the host is optional and defaults to https://test.api.amadeus.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://test.api.amadeus.com/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = amadeus_o_auth2_access_token_api.AmadeusOAuth2AccessTokenApi(api_client)
    access_token = "access_token_example" # str | 

    try:
        # The OAuth 2.0 token info endpoint
        api_response = api_instance.get_oauth2_token_info(access_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AmadeusOAuth2AccessTokenApi->get_oauth2_token_info: %s\n" % e)

configuration = openapi_client.Configuration(
    host = "https://test.api.amadeus.com/v2"
)

with openapi_client.ApiClient(configuration) as api_client:
    api_instance = covid19_area_report_api.Covid19AreaReportApi(api_client)

    query_params = {
        'countryCode': "US",
    }
    try:
        api_response = api_instance.g_et_covid_report(
            query_params=query_params,
        )
        print(api_response)
    except openapi_client.ApiException as e:
        print("Exception: %s\n" % e)