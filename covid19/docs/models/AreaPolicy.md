# openapi_client.model.area_policy.AreaPolicy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[DatedInformation](DatedInformation.md) | [**DatedInformation**](DatedInformation.md) | [**DatedInformation**](DatedInformation.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**status** | str,  | str,  | Current level of regional movement control. Can be de jure or de facto control. \&quot;Lockdown\&quot; | \&quot;Curfew\&quot; | \&quot;Distancing\&quot; | \&quot;None\&quot; | \&quot;Partial Measures\&quot; | \&quot;Opening\&quot; | \&quot;Closing\&quot; | \&quot;Open\&quot; | [optional] 
**startDate** | str,  | str,  | Start Date | [optional] 
**endDate** | str,  | str,  | Latest end date for current control measures. Date in YYYY-MM-DD format OR \&quot;indefinite\&quot; OR blank  | [optional] 
**referenceLink** | str,  | str,  | Webpage for national Covid-19 policy | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

