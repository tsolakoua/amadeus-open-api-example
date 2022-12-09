<a name="__pageTop"></a>
# openapi_client.apis.tags.amadeus_o_auth2_access_token_api.AmadeusOAuth2AccessTokenApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_oauth2_token_info**](#get_oauth2_token_info) | **get** /security/oauth2/token/{access_token} | The OAuth 2.0 token info endpoint
[**oauth2_token**](#oauth2_token) | **post** /security/oauth2/token | The OAuth 2.0 token endpoint

# **get_oauth2_token_info**
<a name="get_oauth2_token_info"></a>
> AmadeusAmadeusOAuth2Token get_oauth2_token_info(access_token)

The OAuth 2.0 token info endpoint

Get token information

### Example

```python
import openapi_client
from openapi_client.apis.tags import amadeus_o_auth2_access_token_api
from openapi_client.model.amadeus_amadeus_amadeus_o_auth2_token import AmadeusAmadeusAmadeusOAuth2Token
from openapi_client.model.amadeus_amadeus_error_response import AmadeusAmadeusErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://test.api.amadeus.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://test.api.amadeus.com/v1"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = amadeus_o_auth2_access_token_api.AmadeusOAuth2AccessTokenApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'access_token': "access_token_example",
    }
    try:
        # The OAuth 2.0 token info endpoint
        api_response = api_instance.get_oauth2_token_info(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AmadeusOAuth2AccessTokenApi->get_oauth2_token_info: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
access_token | AmadeusAccessTokenSchema | | 

# AmadeusAccessTokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_oauth2_token_info.ApiResponseFor200) | oauth2TokenResponse
404 | [ApiResponseFor404](#get_oauth2_token_info.ApiResponseFor404) | genericError

#### get_oauth2_token_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyAmadeusApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyAmadeusApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AmadeusAmadeusOAuth2Token**](../../models/AmadeusAmadeusOAuth2Token.md) |  | 


#### get_oauth2_token_info.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyAmadeusApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyAmadeusApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AmadeusErrorResponse**](../../models/AmadeusErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **oauth2_token**
<a name="oauth2_token"></a>
> AmadeusAmadeusOAuth2Token oauth2_token()

The OAuth 2.0 token endpoint

The token endpoint is used by the client to obtain an access token by presenting its authorization grant. To learn more about this endpoint please refer to the specification at https://tools.ietf.org/html/rfc6749#section-3.2

### Example

```python
import openapi_client
from openapi_client.apis.tags import amadeus_o_auth2_access_token_api
from openapi_client.model.amadeus_amadeus_amadeus_o_auth2_token import AmadeusAmadeusAmadeusOAuth2Token
from openapi_client.model.amadeus_amadeus_error_response import AmadeusAmadeusErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://test.api.amadeus.com/v1
# See configuration.py for a list of all supported configuration parameters.
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
        client_id="client_id_example",
        client_secret="client_secret_example",
    )
    try:
        # The OAuth 2.0 token endpoint
        api_response = api_instance.oauth2_token(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AmadeusOAuth2AccessTokenApi->oauth2_token: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyAmadeusApplicationXWwwFormUrlencoded, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/x-www-form-urlencoded' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyAmadeusApplicationXWwwFormUrlencoded

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**grant_type** | str,  | str,  |  | 
**client_secret** | str,  | str,  |  | 
**client_id** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#oauth2_token.ApiResponseFor200) | oauth2TokenResponse
401 | [ApiResponseFor401](#oauth2_token.ApiResponseFor401) | genericError
500 | [ApiResponseFor500](#oauth2_token.ApiResponseFor500) | genericError

#### oauth2_token.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyAmadeusApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyAmadeusApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AmadeusAmadeusOAuth2Token**](../../models/AmadeusAmadeusOAuth2Token.md) |  | 


#### oauth2_token.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyAmadeusApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyAmadeusApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AmadeusErrorResponse**](../../models/AmadeusErrorResponse.md) |  | 


#### oauth2_token.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyAmadeusApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyAmadeusApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AmadeusErrorResponse**](../../models/AmadeusErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

