import openapi_client
from openapi_client.apis.tags import covid19_area_report_api
from openapi_client.model.disease_area_report import DiseaseAreaReport
from openapi_client.model.error import Error
from openapi_client.model.meta import Meta
from openapi_client.model.warning import Warning
from pprint import pprint


configuration = openapi_client.Configuration()
api_client = openapi_client.ApiClient(configuration)
api_client.default_headers['Authorization'] = 'Bearer ACCESS_TOKEN'

api_instance = covid19_area_report_api.Covid19AreaReportApi(api_client)

query_params = {
    'countryCode': "US",
}

try:
    api_response = api_instance.g_et_covid_report(
        query_params=query_params,
    )
    pprint(api_response)
except openapi_client.ApiException as e:
    print("Exception when calling Covid19AreaReportApi->g_et_covid_report: %s\n" % e)