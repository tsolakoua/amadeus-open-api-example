# openapi_client.model.link.Link

Web link , see  https://tools.ietf.org/html/rfc8288

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Web link , see  https://tools.ietf.org/html/rfc8288 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**href** | str,  | str,  | URL value | [optional] 
**[methods](#methods)** | list, tuple,  | tuple,  | HTTP methods supported by the sibling URL | [optional] 
**rel** | str,  | str,  | Expose the type of relation between the current entity and the describe entity : https://www.iana.org/assignments/link-relations/link-relations.xhtml | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# methods

HTTP methods supported by the sibling URL

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | HTTP methods supported by the sibling URL | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

