# openapi_client.model.amadeus_amadeus_o_auth2_token.AmadeusAmadeusOAuth2Token

The token response

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The token response | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The access token issued by the authorization server. | [optional] 
**username** | str,  | str,  | The user who requested the access_token | [optional] 
**application_name** | str,  | str,  | The application which is requested the access_token | [optional] 
**client_id** | str,  | str,  | The client_id is a public identifier for apps | [optional] 
**token_type** | str,  | str,  | token_type is a parameter in Access Token generate call to Authorization server, which essentially represents how an access_token will be generated and presented for resource access calls | [optional] 
**access_token** | str,  | str,  | Access tokens are a String which applications use to make API requests on behalf of a user. | [optional] 
**expires_in** | decimal.Decimal, int,  | decimal.Decimal,  | The lifetime in seconds of the access token | [optional] value must be a 64 bit integer
**state** | str,  | str,  | The state | [optional] 
**scope** | str,  | str,  | Scope is a mechanism in OAuth 2.0 to limit an application&#x27;s access to a user&#x27;s account | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

