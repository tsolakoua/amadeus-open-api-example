# openapi_client.model.travel_vaccination.TravelVaccination

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

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
**isRequired** | str,  | str,  |  | [optional] 
**referenceLink** | str,  | str,  | Webpage of vaccination regulations | [optional] 
**[acceptedCertificates](#acceptedCertificates)** | list, tuple,  | tuple,  | List of accepted certificates. Not Specified/Paper Certificate/ and/or the name of the app | [optional] 
**[qualifiedVaccines](#qualifiedVaccines)** | list, tuple,  | tuple,  | Vaccine types recognized by the country/territory. Each entry contains the vaccine&#x27;s short name and the number of days after the first/second dose for full vaccination, i.e. AstraZeneca 14 days after second dose | [optional] 
**details** | str,  | str,  | Text explanation of the policies and exemptions for vaccinated travellers | [optional] 
**minimumAge** | decimal.Decimal, int,  | decimal.Decimal,  | Minimum age, in years, that a vaccine can be administered. Under this age, no vaccine is required | [optional] 
**exemptionFromVaccination** | str,  | str,  | Categories of travellers that do not require vaccination: \&quot;Aircrew\&quot;, \&quot;Transit\&quot;, \&quot;Diplomatic\&quot;, \&quot;Transport\&quot;, \&quot;Medical\&quot;, \&quot;Short\&quot;, \&quot;Urgent\&quot;, \&quot;Family\&quot; Family or close relationship \&quot;Culture\&quot;, \&quot;Sports\&quot;, \&quot;Remote\&quot;, \&quot;Commute\&quot;, \&quot;Frequent\&quot;, Citizen, Resident, Military, Seamen, Deported, Humanitarian, Healthcare, Disability, \&quot;Pregnant\&quot; | [optional] 
**[vaccinatedTravellers](#vaccinatedTravellers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# acceptedCertificates

List of accepted certificates. Not Specified/Paper Certificate/ and/or the name of the app

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of accepted certificates. Not Specified/Paper Certificate/ and/or the name of the app | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# qualifiedVaccines

Vaccine types recognized by the country/territory. Each entry contains the vaccine's short name and the number of days after the first/second dose for full vaccination, i.e. AstraZeneca 14 days after second dose

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Vaccine types recognized by the country/territory. Each entry contains the vaccine&#x27;s short name and the number of days after the first/second dose for full vaccination, i.e. AstraZeneca 14 days after second dose | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Vaccine**](Vaccine.md) | [**Vaccine**](Vaccine.md) | [**Vaccine**](Vaccine.md) |  | 

# vaccinatedTravellers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**policy** | str,  | str,  | Yes/No; &#x27;Yes&#x27; indicates fully vaccinated travellers are exempt from some requirements or restrictions | [optional] 
**exemptions** | str,  | str,  | Entry Ban Testing Documents App Quarantine Masks Exit Domestic Restrictions; indicates what exemptions fully vaccinated travellers qualify for.  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

