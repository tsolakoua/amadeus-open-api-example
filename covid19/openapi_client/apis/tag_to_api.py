import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.covid19_area_report_api import Covid19AreaReportApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.COVID19_AREA_REPORT: Covid19AreaReportApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.COVID19_AREA_REPORT: Covid19AreaReportApi,
    }
)
