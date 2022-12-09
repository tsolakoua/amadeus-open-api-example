# openapi_client.model.entry.Entry

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
**ban** | str,  | str,  | Indicates if entry for all or some types of people is banned. \&quot;Yes\&quot; includes situations that are equivalent to a ban | [optional] 
**throughDate** | str,  | str,  | Latest end date for entry ban. Date in YYYY-MM-DD format OR \&quot;indefinite\&quot; OR blank | [optional] 
**referenceLink** | str,  | str,  | Rules implied with specific to borders | [optional] 
**exemptions** | str,  | str,  | Webpage for entry exemptions | [optional] 
**[bannedArea](#bannedArea)** | list, tuple,  | tuple,  | Countries/territories from where travellers are generally banned from entry due to covid-19 rules. If no travellers are banned based on origin, this will be blank. Uses ISO 3166 country codes | [optional] 
**[borderBan](#borderBan)** | list, tuple,  | tuple,  | Open/Partially Open/Closed | [optional] 
**bannedTravellers** | str,  | str,  | travellers who are banned | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# bannedArea

Countries/territories from where travellers are generally banned from entry due to covid-19 rules. If no travellers are banned based on origin, this will be blank. Uses ISO 3166 country codes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Countries/territories from where travellers are generally banned from entry due to covid-19 rules. If no travellers are banned based on origin, this will be blank. Uses ISO 3166 country codes | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Area**](Area.md) | [**Area**](Area.md) | [**Area**](Area.md) |  | 

# borderBan

Open/Partially Open/Closed

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Open/Partially Open/Closed | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**borderType** | str,  | str,  | Land or Maritime or Air | [optional] 
**status** | str,  | str,  | Open/Partially open/Closed | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

