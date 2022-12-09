<a name="__pageTop"></a>
# openapi_client.apis.tags.covid19_area_report_api.Covid19AreaReportApi

All URIs are relative to *https://test.api.amadeus.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**g_et_covid_report**](#g_et_covid_report) | **get** /duty-of-care/diseases/covid19-area-report | GET covid area report

# **g_et_covid_report**
<a name="g_et_covid_report"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} g_et_covid_report(country_code)

GET covid area report

### Example

```python
import openapi_client
from openapi_client.apis.tags import covid19_area_report_api
from openapi_client.model.disease_area_report import DiseaseAreaReport
from openapi_client.model.error import Error
from openapi_client.model.meta import Meta
from openapi_client.model.warning import Warning
from pprint import pprint
# Defining the host is optional and defaults to https://test.api.amadeus.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://test.api.amadeus.com/v2"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = covid19_area_report_api.Covid19AreaReportApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'countryCode': "US",
    }
    try:
        # GET covid area report
        api_response = api_instance.g_et_covid_report(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling Covid19AreaReportApi->g_et_covid_report: %s\n" % e)

    # example passing only optional values
    query_params = {
        'countryCode': "US",
        'cityCode': "NYC",
        'language': "EN",
    }
    try:
        # GET covid area report
        api_response = api_instance.g_et_covid_report(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling Covid19AreaReportApi->g_et_covid_report: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
countryCode | CountryCodeSchema | | 
cityCode | CityCodeSchema | | optional
language | LanguageSchema | | optional


# CountryCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CityCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#g_et_covid_report.ApiResponseFor200) | Successful Reply
400 | [ApiResponseFor400](#g_et_covid_report.ApiResponseFor400) | Bad Request  code    | title                                  ------- | -------------------------------------  4926    | INVALID DATA RECEIVED                           32171   | MANDATORY DATA MISSING   477    | INVALID FORMAT  572    | INVALID OPTION 2781    | INVALID LENGTH
500 | [ApiResponseFor500](#g_et_covid_report.ApiResponseFor500) | Internal Server Error  code    | title                                  ------- | -------------------------------------  141     | SYSTEM ERROR HAS OCCURRED
501 | [ApiResponseFor501](#g_et_covid_report.ApiResponseFor501) | Not Implemented code    | title                                  ------- | -------------------------------------  141     | UNABLE TO SUPPORT

#### g_et_covid_report.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[warnings](#warnings)** | list, tuple,  | tuple,  |  | [optional] 
**meta** | [**Meta**]({{complexTypePrefix}}Meta.md) | [**Meta**]({{complexTypePrefix}}Meta.md) |  | [optional] 
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# warnings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Warning**]({{complexTypePrefix}}Warning.md) | [**Warning**]({{complexTypePrefix}}Warning.md) | [**Warning**]({{complexTypePrefix}}Warning.md) |  | 

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DiseaseAreaReport**]({{complexTypePrefix}}DiseaseAreaReport.md) | [**DiseaseAreaReport**]({{complexTypePrefix}}DiseaseAreaReport.md) | [**DiseaseAreaReport**]({{complexTypePrefix}}DiseaseAreaReport.md) |  | 

#### g_et_covid_report.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[errors](#errors)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# errors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 

#### g_et_covid_report.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[errors](#errors)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# errors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 

#### g_et_covid_report.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor501ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor501ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[errors](#errors)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# errors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

