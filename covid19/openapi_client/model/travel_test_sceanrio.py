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


class TravelTestSceanrio(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            name_ = schemas.StrSchema
        
            @staticmethod
            def condition() -> typing.Type['TravelTestCondition']:
                return TravelTestCondition
        
            @staticmethod
            def rule() -> typing.Type['TravelTestRules']:
                return TravelTestRules
            __annotations__ = {
                "name ": name_,
                "condition": condition,
                "rule": rule,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name "]) -> MetaOapg.properties.name_: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["condition"]) -> 'TravelTestCondition': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rule"]) -> 'TravelTestRules': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name ", "condition", "rule", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name "]) -> typing.Union[MetaOapg.properties.name_, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["condition"]) -> typing.Union['TravelTestCondition', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rule"]) -> typing.Union['TravelTestRules', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name ", "condition", "rule", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        condition: typing.Union['TravelTestCondition', schemas.Unset] = schemas.unset,
        rule: typing.Union['TravelTestRules', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TravelTestSceanrio':
        return super().__new__(
            cls,
            *_args,
            condition=condition,
            rule=rule,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.travel_test_condition import TravelTestCondition
from openapi_client.model.travel_test_rules import TravelTestRules
