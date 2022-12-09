# openapi_client.model.exit.Exit

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
**specialRequirements** | str,  | str,  | Yes/No/Yes conditional; indicates whether there are special requirements to fulfill in order to leave the country/territory | [optional] 
**referenceLink** | str,  | str,  | Requirements to exit country   Website information | [optional] 
**isBanned** | str,  | str,  | Yes/Recommended/Partial/No; &#x27;Yes&#x27; indicates all travellers are banned from leaving; &#x27;Recommended&#x27; indicates that travellers should not leave, but are mostly free to do so; &#x27;Partial&#x27; indicates that some travellers may leave, but others are prevented; &#x27;No&#x27; indicates all travellers are free to leave | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

