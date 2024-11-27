from sklearn.gaussian_process.kernels import Product
from model.entity.Role import Role
from model.entity.User import User
from model.entity.permission import Permission
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
    class UserController:

        @classmethod
        @exception_handling
        def add_user(cls, user_name, password, email, role_id, person_id):
            user = User(user_name, password, email, role_id, person_id)
            return True, Service.save(user, User)

        @classmethod
        @exception_handling
        def find_user_by_id(cls, user_id):
            return Service.find_by_id(User, user_id)

        @classmethod
        @exception_handling
        def find_user_by_user_name(cls, user_name):
            return Service.find_by(User, {"user_name": user_name})

        @classmethod
        @exception_handling
        def find_users_by_role(cls, role_id):
            return Service.find_by(User, {"role_id": role_id})

        @classmethod
        @exception_handling
        def find_users_by_person(cls, person_id):
            return Service.find_by(User, {"person_id": person_id})


class PermissionController:

    @classmethod
    @exception_handling
    def add_permission(cls, name):
        permission = Permission(name)
        return True, Service.save(permission, Permission)

    @classmethod
    @exception_handling
    def find_permission_by_id(cls, permission_id):
        return Service.find_by_id(Permission, permission_id)

    @classmethod
    @exception_handling
    def find_permission_by_name(cls, name):
        return Service.find_by(Permission, {"name": name})






class RoleController:

    @classmethod
    @exception_handling
    def add_role(cls, role_name):
        role = Role(role_name)
        return True, Service.save(role, Role)

    @classmethod
    @exception_handling
    def find_role_by_id(cls, role_id):
        return Service.find_by_id(Role, role_id)

    @classmethod
    @exception_handling
    def find_role_by_name(cls, role_name):
        return Service.find_by(Role, {"role_name": role_name})





class PersonController:

    @classmethod
    @exception_handling
    def add_person(cls, name, last_name, national_code, birth_date=None, phone=None, address=None, post_code=None):
        person = Person(name, last_name, national_code, birth_date, phone, address, post_code)
        return True, Service.save(person, Person)

    @classmethod
    @exception_handling
    def find_person_by_id(cls, person_id):
        result = Service.find_by_id(Person, person_id)
        if not result:
            raise ValueError(f"شخصی با شناسه {person_id} یافت نشد.")
        return result

    @classmethod
    @exception_handling
    def find_person_by_national_code(cls, national_code):
        result = Service.find_by(Person, {"national_id": national_code})
        if not result:
            raise ValueError(f"شخصی با کد ملی {national_code} یافت نشد.")
        return result



    # ____________________________________MAHTAB______________________________________#
    @classmethod
    @exception_handling
    def add_bank(cls, name, account_number, branch_code):
        ban = Bank( name, account_number, branch_code)
        return True, Service.save(ban, Bank)
    
    @classmethod
    @exception_handling
    def add_transaction(cls,  payment_method, amount, date, tracking_code):
        Transactn = Transaction(  payment_method, amount, date, tracking_code)
        return True, Service.save(Transactn, Transaction)    
   
    @classmethod
    @exception_handling
    def add_payment(cls,  payment_method, amount, date, tracking_code):
        Paymnt = Payment(  payment_method, amount, date, tracking_code)
        return True, Service.save(Paymnt, Payment)
