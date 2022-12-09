# openapi_client.model.travel_quarantine_modality.TravelQuarantineModality

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
**eligiblePerson** | str,  | str,  | Who needs to Quarantine on Arrival   eg Some travellers | [optional] 
**quarantineType** | str,  | str,  | Type of Quarantine   Self/Gov | [optional] 
**duration** | decimal.Decimal, int,  | decimal.Decimal,  | Minimum number of days for quarantine period. | [optional] 
**referenceLink** | str,  | str,  | Rules of Quarantine on Arrival  | [optional] 
**mandateList** | str,  | str,  | Mandatory On Quarantine on Arrival   eg Websites  | [optional] 
**[quarantineOnArrivalAreas](#quarantineOnArrivalAreas)** | list, tuple,  | tuple,  | Countries/territories from where travellers are generally required to quarantine on arrival. If no travellers are required to quarantine, this will be blank. Uses ISO 3166 country codes | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# quarantineOnArrivalAreas

Countries/territories from where travellers are generally required to quarantine on arrival. If no travellers are required to quarantine, this will be blank. Uses ISO 3166 country codes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Countries/territories from where travellers are generally required to quarantine on arrival. If no travellers are required to quarantine, this will be blank. Uses ISO 3166 country codes | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Area**](Area.md) | [**Area**](Area.md) | [**Area**](Area.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

