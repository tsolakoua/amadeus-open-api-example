# openapi_client.model.disease_area_report.DiseaseAreaReport

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Resource Type | [optional] 
**area** | [**Area**](Area.md) | [**Area**](Area.md) |  | [optional] 
**[subAreas](#subAreas)** | list, tuple,  | tuple,  | it can be city or region | [optional] 
**summary** | [**DatedInformation**](DatedInformation.md) | [**DatedInformation**](DatedInformation.md) |  | [optional] 
**dataSources** | [**DataSources**](DataSources.md) | [**DataSources**](DataSources.md) |  | [optional] 
**[relatedArea](#relatedArea)** | list, tuple,  | tuple,  |  | [optional] 
**[areaVaccinated](#areaVaccinated)** | list, tuple,  | tuple,  |  | [optional] 
**hotspots** | [**DatedInformation**](DatedInformation.md) | [**DatedInformation**](DatedInformation.md) |  | [optional] 
**diseaseCases** | [**DiseaseCase**](DiseaseCase.md) | [**DiseaseCase**](DiseaseCase.md) |  | [optional] 
**diseaseInfection** | [**DiseaseInfection**](DiseaseInfection.md) | [**DiseaseInfection**](DiseaseInfection.md) |  | [optional] 
**diseaseRiskLevel** | [**DatedInformation**](DatedInformation.md) | [**DatedInformation**](DatedInformation.md) |  | [optional] 
**AreaPolicy** | [**AreaPolicy**](AreaPolicy.md) | [**AreaPolicy**](AreaPolicy.md) |  | [optional] 
**areaAccessRestriction** | [**AreaAccessRestriction**](AreaAccessRestriction.md) | [**AreaAccessRestriction**](AreaAccessRestriction.md) |  | [optional] 
**[areaRestrictions](#areaRestrictions)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subAreas

it can be city or region

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | it can be city or region | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DiseaseAreaReport**](DiseaseAreaReport.md) | [**DiseaseAreaReport**](DiseaseAreaReport.md) | [**DiseaseAreaReport**](DiseaseAreaReport.md) |  | 

# relatedArea

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Link**](Link.md) | [**Link**](Link.md) | [**Link**](Link.md) |  | 

# areaVaccinated

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AreaVaccinated**](AreaVaccinated.md) | [**AreaVaccinated**](AreaVaccinated.md) | [**AreaVaccinated**](AreaVaccinated.md) |  | 

# areaRestrictions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AreaRestrictions**](AreaRestrictions.md) | [**AreaRestrictions**](AreaRestrictions.md) | [**AreaRestrictions**](AreaRestrictions.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

