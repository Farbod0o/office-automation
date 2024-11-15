from model.entity.department import Department
from model.entity.organization import Organization
from model.entity.person import Person
from model.tools.decorators import exception_handling
from model.services.service import Service
class Controller:
    @classmethod
    @exception_handling
    def add_organization(cls, name, slogan, logo, duties, address, telephone, description="",head_id=None):
        org = Organization(name, slogan, logo, duties, address, telephone, description)
        return True, Service.save(org, Organization)

    @classmethod
    @exception_handling
    def add_person(cls, sex, name, last_name, national_code):
        pers = Person( sex, name, last_name, national_code)
        return True, Service.save(pers, Person)

    @classmethod
    @exception_handling
    def add_Department(cls, name, duties, location, phone_number, extension, access_lvl, manager=None, deputy=None,
                 description="", parent_department=None):
        dep = Department(name, duties, location, phone_number, extension, access_lvl, manager, deputy,
                 description, parent_department)
        return True, Service.save(dep, Department)