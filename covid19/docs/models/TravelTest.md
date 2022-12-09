# openapi_client.model.travel_test.TravelTest

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
**isRequired** | str,  | str,  | Required Testing   eg , Yes,No, \&quot;Yes, conditional\&quot;. | [optional] 
**requirement** | str,  | str,  | Is the testing is required   eg Mandatory,Yes. | [optional] 
**referenceLink** | str,  | str,  | Rules regarding the testing   eg https://corona.fo/quarantine. | [optional] 
**[travelTestConditionsAndRules](#travelTestConditionsAndRules)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# travelTestConditionsAndRules

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TravelTestConditionsAndRules**](TravelTestConditionsAndRules.md) | [**TravelTestConditionsAndRules**](TravelTestConditionsAndRules.md) | [**TravelTestConditionsAndRules**](TravelTestConditionsAndRules.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

