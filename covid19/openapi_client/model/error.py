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


class Error(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The Error Definition
    """


    class MetaOapg:
        
        class properties:
            status = schemas.IntSchema
            code = schemas.IntSchema
            title = schemas.StrSchema
            detail = schemas.StrSchema
            
            
            class source(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        parameter = schemas.StrSchema
                        pointer = schemas.StrSchema
                        example = schemas.StrSchema
                        __annotations__ = {
                            "parameter": parameter,
                            "pointer": pointer,
                            "example": example,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["parameter"]) -> MetaOapg.properties.parameter: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["pointer"]) -> MetaOapg.properties.pointer: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["example"]) -> MetaOapg.properties.example: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["parameter", "pointer", "example", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["parameter"]) -> typing.Union[MetaOapg.properties.parameter, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["pointer"]) -> typing.Union[MetaOapg.properties.pointer, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["example"]) -> typing.Union[MetaOapg.properties.example, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["parameter", "pointer", "example", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    parameter: typing.Union[MetaOapg.properties.parameter, str, schemas.Unset] = schemas.unset,
                    pointer: typing.Union[MetaOapg.properties.pointer, str, schemas.Unset] = schemas.unset,
                    example: typing.Union[MetaOapg.properties.example, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'source':
                    return super().__new__(
                        cls,
                        *_args,
                        parameter=parameter,
                        pointer=pointer,
                        example=example,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "status": status,
                "code": code,
                "title": title,
                "detail": detail,
                "source": source,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["detail"]) -> MetaOapg.properties.detail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "code", "title", "detail", "source", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["detail"]) -> typing.Union[MetaOapg.properties.detail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "code", "title", "detail", "source", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        status: typing.Union[MetaOapg.properties.status, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        code: typing.Union[MetaOapg.properties.code, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        detail: typing.Union[MetaOapg.properties.detail, str, schemas.Unset] = schemas.unset,
        source: typing.Union[MetaOapg.properties.source, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Error':
        return super().__new__(
            cls,
            *_args,
            status=status,
            code=code,
            title=title,
            detail=detail,
            source=source,
            _configuration=_configuration,
            **kwargs,
        )
