from sklearn.gaussian_process.kernels import Product

from model.entity import *
from model.tools.decorators import exception_handling
from model.services.service import Service


class Controller:

    @classmethod
    @exception_handling
    def add_entity(cls, obj, entity):
        return True, Service.save(obj, entity)

    @classmethod
    @exception_handling
    def find_by_id(cls, entity, user_id):
        return Service.find_by_id(entity, user_id)

    @classmethod
    @exception_handling
    def find_by(cls, entity, statement):
        return Service.find_by(entity, statement)

    # _____________________________________FARBOD_______________________________________#
    @classmethod
    @exception_handling
    def add_ticket(cls, user, title, ticket_datetime, group, response_type):
        ticket = Ticket(user, title, ticket_datetime, group, response_type)
        return True, Service.save(ticket, Ticket)

    @classmethod
    @exception_handling
    def add_Group(cls, name, parent_group=None):
        gp = Group(name, parent_group)
        return True, Service.save(gp, Group)

    @classmethod
    @exception_handling
    def add_organization(cls, name, slogan, logo, duties, address, telephone, description="", head_id=None):
        org = Organization(name, slogan, logo, duties, address, telephone, description)
        return True, Service.save(org, Organization)

    @classmethod
    @exception_handling
    def add_Department(cls, name, duties, location, phone_number, extension, access_lvl, description="", manager=None,
                       deputy=None, parent_department=None):
        dep = Department(name, duties, location, phone_number, extension, access_lvl, description, manager,
                         deputy, parent_department)
        return True, Service.save(dep, Department)

    # _____________________________________ALI________________________________________________#
    @classmethod
    @exception_handling
    def add_Property(cls, property_code, group_code, property_name, property_description, label_code,
                     count, property_price, delivery_date, section_code, personal_code_delivery
                     , image, status):
        prop = Property(property_code, group_code, property_name, property_description, label_code,
                        count, property_price, delivery_date, section_code, personal_code_delivery,
                        image, status)
        return True, Service.save(prop, Property)

    @classmethod
    @exception_handling
    def add_product_group(cls, group_code, product_group_name, group_code_up, description=""):
        prod = Product(group_code, product_group_name, group_code_up, description)
        return True, Service.save(prod, ProductGroup)

    # ____________________________________AMIRHOSSEIN______________________________________#
    @classmethod
    @exception_handling
    def add_person(cls, sex, name, last_name, national_code):
        pers = Person(sex, name, last_name, national_code)
        return True, Service.save(pers, Person)
