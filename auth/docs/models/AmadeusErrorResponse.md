# openapi_client.model.amadeus_error_response.AmadeusErrorResponse

Error responses are sent when an error (e.g. unauthorized, bad request, ...) occurred.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Error responses are sent when an error (e.g. unauthorized, bad request, ...) occurred. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | decimal.Decimal, int,  | decimal.Decimal,  | Debug contains debug information. | value must be a 64 bit integer
**error_description** | str,  | str,  | A small description about the error | 
**error** | str,  | str,  | Name is the error name. | 
**title** | str,  | str,  | Debug contains debug information. This is usually not available and has to be enabled. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

