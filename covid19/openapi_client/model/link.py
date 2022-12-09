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


class Link(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Web link , see  https://tools.ietf.org/html/rfc8288
    """


    class MetaOapg:
        
        class properties:
            href = schemas.StrSchema
            
            
            class methods(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "GET": "GET",
                                "POST": "POST",
                                "PUT": "PUT",
                                "PATCH": "PATCH",
                                "DELETE": "DELETE",
                                "OPTIONS": "OPTIONS",
                            }
                        
                        @schemas.classproperty
                        def GET(cls):
                            return cls("GET")
                        
                        @schemas.classproperty
                        def POST(cls):
                            return cls("POST")
                        
                        @schemas.classproperty
                        def PUT(cls):
                            return cls("PUT")
                        
                        @schemas.classproperty
                        def PATCH(cls):
                            return cls("PATCH")
                        
                        @schemas.classproperty
                        def DELETE(cls):
                            return cls("DELETE")
                        
                        @schemas.classproperty
                        def OPTIONS(cls):
                            return cls("OPTIONS")
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'methods':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            rel = schemas.StrSchema
            __annotations__ = {
                "href": href,
                "methods": methods,
                "rel": rel,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["href"]) -> MetaOapg.properties.href: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["methods"]) -> MetaOapg.properties.methods: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rel"]) -> MetaOapg.properties.rel: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["href", "methods", "rel", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["href"]) -> typing.Union[MetaOapg.properties.href, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["methods"]) -> typing.Union[MetaOapg.properties.methods, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rel"]) -> typing.Union[MetaOapg.properties.rel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["href", "methods", "rel", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        href: typing.Union[MetaOapg.properties.href, str, schemas.Unset] = schemas.unset,
        methods: typing.Union[MetaOapg.properties.methods, list, tuple, schemas.Unset] = schemas.unset,
        rel: typing.Union[MetaOapg.properties.rel, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Link':
        return super().__new__(
            cls,
            *_args,
            href=href,
            methods=methods,
            rel=rel,
            _configuration=_configuration,
            **kwargs,
        )
