# coding: utf-8

"""
    Travel Restrictions

    Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class TravelVaccination(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        
        class all_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    isRequired = schemas.StrSchema
                    referenceLink = schemas.StrSchema
                    
                    
                    class acceptedCertificates(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.StrSchema
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'acceptedCertificates':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    
                    
                    class qualifiedVaccines(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['Vaccine']:
                                return Vaccine
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple['Vaccine'], typing.List['Vaccine']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'qualifiedVaccines':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'Vaccine':
                            return super().__getitem__(i)
                    details = schemas.StrSchema
                    minimumAge = schemas.IntSchema
                    exemptionFromVaccination = schemas.StrSchema
                    
                    
                    class vaccinatedTravellers(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                policy = schemas.StrSchema
                                exemptions = schemas.StrSchema
                                __annotations__ = {
                                    "policy": policy,
                                    "exemptions": exemptions,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["policy"]) -> MetaOapg.properties.policy: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["exemptions"]) -> MetaOapg.properties.exemptions: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["policy", "exemptions", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["policy"]) -> typing.Union[MetaOapg.properties.policy, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["exemptions"]) -> typing.Union[MetaOapg.properties.exemptions, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["policy", "exemptions", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            policy: typing.Union[MetaOapg.properties.policy, str, schemas.Unset] = schemas.unset,
                            exemptions: typing.Union[MetaOapg.properties.exemptions, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'vaccinatedTravellers':
                            return super().__new__(
                                cls,
                                *_args,
                                policy=policy,
                                exemptions=exemptions,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    __annotations__ = {
                        "isRequired": isRequired,
                        "referenceLink": referenceLink,
                        "acceptedCertificates": acceptedCertificates,
                        "qualifiedVaccines": qualifiedVaccines,
                        "details": details,
                        "minimumAge": minimumAge,
                        "exemptionFromVaccination": exemptionFromVaccination,
                        "vaccinatedTravellers": vaccinatedTravellers,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["isRequired"]) -> MetaOapg.properties.isRequired: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["referenceLink"]) -> MetaOapg.properties.referenceLink: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["acceptedCertificates"]) -> MetaOapg.properties.acceptedCertificates: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["qualifiedVaccines"]) -> MetaOapg.properties.qualifiedVaccines: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["details"]) -> MetaOapg.properties.details: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["minimumAge"]) -> MetaOapg.properties.minimumAge: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["exemptionFromVaccination"]) -> MetaOapg.properties.exemptionFromVaccination: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["vaccinatedTravellers"]) -> MetaOapg.properties.vaccinatedTravellers: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["isRequired", "referenceLink", "acceptedCertificates", "qualifiedVaccines", "details", "minimumAge", "exemptionFromVaccination", "vaccinatedTravellers", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["isRequired"]) -> typing.Union[MetaOapg.properties.isRequired, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["referenceLink"]) -> typing.Union[MetaOapg.properties.referenceLink, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["acceptedCertificates"]) -> typing.Union[MetaOapg.properties.acceptedCertificates, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["qualifiedVaccines"]) -> typing.Union[MetaOapg.properties.qualifiedVaccines, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> typing.Union[MetaOapg.properties.details, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["minimumAge"]) -> typing.Union[MetaOapg.properties.minimumAge, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["exemptionFromVaccination"]) -> typing.Union[MetaOapg.properties.exemptionFromVaccination, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["vaccinatedTravellers"]) -> typing.Union[MetaOapg.properties.vaccinatedTravellers, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["isRequired", "referenceLink", "acceptedCertificates", "qualifiedVaccines", "details", "minimumAge", "exemptionFromVaccination", "vaccinatedTravellers", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                isRequired: typing.Union[MetaOapg.properties.isRequired, str, schemas.Unset] = schemas.unset,
                referenceLink: typing.Union[MetaOapg.properties.referenceLink, str, schemas.Unset] = schemas.unset,
                acceptedCertificates: typing.Union[MetaOapg.properties.acceptedCertificates, list, tuple, schemas.Unset] = schemas.unset,
                qualifiedVaccines: typing.Union[MetaOapg.properties.qualifiedVaccines, list, tuple, schemas.Unset] = schemas.unset,
                details: typing.Union[MetaOapg.properties.details, str, schemas.Unset] = schemas.unset,
                minimumAge: typing.Union[MetaOapg.properties.minimumAge, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                exemptionFromVaccination: typing.Union[MetaOapg.properties.exemptionFromVaccination, str, schemas.Unset] = schemas.unset,
                vaccinatedTravellers: typing.Union[MetaOapg.properties.vaccinatedTravellers, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *_args,
                    isRequired=isRequired,
                    referenceLink=referenceLink,
                    acceptedCertificates=acceptedCertificates,
                    qualifiedVaccines=qualifiedVaccines,
                    details=details,
                    minimumAge=minimumAge,
                    exemptionFromVaccination=exemptionFromVaccination,
                    vaccinatedTravellers=vaccinatedTravellers,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.all_of_0,
                DatedInformation,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TravelVaccination':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.dated_information import DatedInformation
from openapi_client.model.vaccine import Vaccine