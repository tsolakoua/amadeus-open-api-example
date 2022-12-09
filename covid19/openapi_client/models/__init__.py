# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.model.area import Area
from openapi_client.model.area_access_restriction import AreaAccessRestriction
from openapi_client.model.area_health_pass import AreaHealthPass
from openapi_client.model.area_policy import AreaPolicy
from openapi_client.model.area_restrictions import AreaRestrictions
from openapi_client.model.area_vaccinated import AreaVaccinated
from openapi_client.model.data_sources import DataSources
from openapi_client.model.dated_information import DatedInformation
from openapi_client.model.declaration_documents import DeclarationDocuments
from openapi_client.model.disease_area_report import DiseaseAreaReport
from openapi_client.model.disease_case import DiseaseCase
from openapi_client.model.disease_infection import DiseaseInfection
from openapi_client.model.entry import Entry
from openapi_client.model.error import Error
from openapi_client.model.exit import Exit
from openapi_client.model.expiration import Expiration
from openapi_client.model.health_insurance_modality import HealthInsuranceModality
from openapi_client.model.link import Link
from openapi_client.model.masks import Masks
from openapi_client.model.meta import Meta
from openapi_client.model.tracing_application import TracingApplication
from openapi_client.model.transportation import Transportation
from openapi_client.model.travel_quarantine_modality import TravelQuarantineModality
from openapi_client.model.travel_test import TravelTest
from openapi_client.model.travel_test_condition import TravelTestCondition
from openapi_client.model.travel_test_conditions_and_rules import TravelTestConditionsAndRules
from openapi_client.model.travel_test_requirements_rule import TravelTestRequirementsRule
from openapi_client.model.travel_test_rules import TravelTestRules
from openapi_client.model.travel_test_sceanrio import TravelTestSceanrio
from openapi_client.model.travel_test_traveller_condition import TravelTestTravellerCondition
from openapi_client.model.travel_test_trip_condition import TravelTestTripCondition
from openapi_client.model.travel_vaccination import TravelVaccination
from openapi_client.model.vaccine import Vaccine
from openapi_client.model.validity import Validity
from openapi_client.model.warning import Warning
