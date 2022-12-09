import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.duty_of_care_diseases_covid19_area_report import DutyOfCareDiseasesCovid19AreaReport

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.DUTYOFCARE_DISEASES_COVID19AREAREPORT: DutyOfCareDiseasesCovid19AreaReport,
    }
)

path_to_api = PathToApi(
    {
        PathValues.DUTYOFCARE_DISEASES_COVID19AREAREPORT: DutyOfCareDiseasesCovid19AreaReport,
    }
)
