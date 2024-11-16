from model.entity import *
from model.tools.decorators import exception_handling
from model.services.service import Service


class Controller:
    @classmethod
    @exception_handling
    def add_organization(cls, name, slogan, logo, duties, address, telephone, description="", head_id=None):
        org = Organization(name, slogan, logo, duties, address, telephone, description)
        return True, Service.save(org, Organization)

    @classmethod
    @exception_handling
    def add_person(cls, sex, name, last_name, national_code):
        pers = Person(sex, name, last_name, national_code)
        return True, Service.save(pers, Person)

    @classmethod
    @exception_handling
    def add_Department(cls, name, duties, location, phone_number, extension, access_lvl, description="", manager=None,
                       deputy=None, parent_department=None):
        dep = Department(name, duties, location, phone_number, extension, access_lvl, description, manager,
                       deputy, parent_department)
        return True, Service.save(dep, Department)

    @classmethod
    @exception_handling
    def find_by_id(cls, entity, user_id):
        return Service.find_by_id(entity, user_id)

    @classmethod
    @exception_handling
    def find_by(cls, entity, statement):
        return Service.find_by(entity, statement)
