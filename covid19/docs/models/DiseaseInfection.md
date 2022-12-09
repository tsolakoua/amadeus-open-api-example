# openapi_client.model.disease_infection.DiseaseInfection

Confirmed infinction information at a given date

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Confirmed infinction information at a given date | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[DatedInformation](DatedInformation.md) | [**DatedInformation**](DatedInformation.md) | [**DatedInformation**](DatedInformation.md) |  | 

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**level** | str,  | str,  | Infection risk level. \&quot;Extreme\&quot; | \&quot;High\&quot; | \&quot;Medium\&quot; | \&quot;Moderate\&quot; | \&quot;Low\&quot; | [optional] 
**rate** | decimal.Decimal, int, float,  | decimal.Decimal,  | Covid-19 infection rate | [optional] 
**infectionMapLink** | str,  | str,  | Disease Infection map link | [optional] 
**trend** | str,  | str,  | Compares latest week to previous week. \&quot;Significant Decrease\&quot; | \&quot;Significant Increase\&quot; | \&quot;Decrease\&quot; | \&quot;Increase\&quot; | \&quot;Steady\&quot; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

