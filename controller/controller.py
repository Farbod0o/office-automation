from model.entity import User, Department, ProductGroup, Permission, Role, Person, Ticket
from model.entity.bank import Bank
from model.entity.message import Message
from model.entity.payment import Payment
from model.entity.refrence import Reference
from model.entity.ticket_group import TicketGroup
from model.entity.transaction import Transaction
from model.entity.unit import Unit
from model.entity.section import Section
from model.tools.decorators import exception_handling
from model.services.service import Service
from model.entity.Group_property import Group_property
from model.entity.product import Product
from model.entity.Product_Property_Value import Product_Property_Value
from model.entity.inventory import Inventory
from model.entity.inventory_transaction import InventoryTransaction


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
    def add_department(cls, name, department_num, logo, task, address, phone_number, description=""):
        dep = Department(name, department_num, logo, task, address, phone_number, description=description)
        return True, Service.save(dep, Department)

    @classmethod
    @exception_handling
    def add_section(cls, name, address, phone_number, internal_code, access_lvl, section_num, parent_section_num=None,
                    description=None, department=None):
        sec = Section(name, address, phone_number, internal_code, access_lvl, section_num, parent_section_num,
                      description, department)
        return True, Service.save(sec, Section)

    # ____________________________________MOBINA______________________________________#

    @classmethod
    @exception_handling
    def find_by_reference_num(cls, reference_num):
        return Service.find_by(Reference, Reference.reference_num == reference_num)

    # todo: baraye peyda kardan name bar asas user aval bayad relation ha tarif shavad
    # @classmethod
    # @exception_handling
    # def find_by_user(cls, session, user_id):
    #     return session.query(cls).filter_by(user_id=user_id).all()

    @classmethod
    @exception_handling
    def find_by_referral_date_time(cls, referral_date_time):
        return Service.find_by(Reference, Reference._referral_date_time == referral_date_time)

    @classmethod
    @exception_handling
    def find_by_expire_date_time(cls, expire_date_time):
        return Service.find_by(Reference, Reference._expire_date_time == expire_date_time)

    # todo: bayad service jadid tarif shavad
    # @classmethod
    # @exception_handling
    # def find_by_paraph(cls, session, paraph):
    #     return session.query(cls).filter(cls._paraph.like(f"%{paraph}%")).all()

    @classmethod
    @exception_handling
    def find_by_priority(cls, priority):
        return Service.find_by(Reference, Reference._priority == priority)

    @classmethod
    @exception_handling
    def find_by_type(cls, type_):
        return Service.find_by(Reference, Reference._type == type_)

    @classmethod
    @exception_handling
    def find_by_status(cls, status):
        return Service.find_by(Reference, Reference._status == status)

    @classmethod
    @exception_handling
    def find_by_confirmation(cls, confirmation):
        return Service.find_by(Reference, Reference._confirmation == confirmation)

    @classmethod
    @exception_handling
    def find_by_receive_send(cls, receive_send):
        return Service.find_by(Reference, Reference._receive_send == receive_send)

    # ____________________________________MAHTAB______________________________________#
    @classmethod
    @exception_handling
    def add_bank(cls, name, account_number, branch_code):
        bnk = Bank(name, account_number, branch_code)
        return True, Service.save(bnk, Bank)

    @classmethod
    @exception_handling
    def add_transaction(cls, payment_method, amount, tracking_code, payment, bank):
        trans = Transaction(payment_method, amount, tracking_code, payment, bank)
        return True, Service.save(trans, Transaction)

    @classmethod
    @exception_handling
    def add_payment(cls, doc_number, description):
        pay = Payment(doc_number, description)
        return True, Service.save(pay, Payment)

    # _____________________________________ALI________________________________________________#
    @classmethod
    @exception_handling
    def add_product_group(cls, title):
        pg = ProductGroup(title)
        return True, Service.save(pg, ProductGroup)

    @classmethod
    @exception_handling
    def add_unit(cls, name, amount, description):
        un = Unit(name, amount, description)
        return True, Service.save(un, Unit)

    @classmethod
    @exception_handling
    def add_product(cls, name, price, code, description, image):
        pro = Product(name, price, code, description, image)
        return True, Service.save(pro, Product)

    @classmethod
    @exception_handling
    def add_product_property_value(cls, color, size, weight, description, material):
        pro_v = Product_Property_Value(color, size, weight, description, material)
        return True, Service.save(pro_v, Product_Property_Value)

    # controller for group property:
    @classmethod
    @exception_handling
    def find_by_title(cls, title):
        return Service.find_by(Group_property, Group_property.title == title)

    # todo: product == product
    @classmethod
    @exception_handling
    def find_by_product(cls, product):
        return Service.find_by(Product, Product.name == product)

    # controller for product
    @classmethod
    @exception_handling
    def find_by_name(cls, name):
        return Service.find_by(Product, Product.name == name)

    @classmethod
    @exception_handling
    def find_by_price(cls, price):
        return Service.find_by(Product, Product.price == price)

    @classmethod
    @exception_handling
    def find_by_code(cls, code):
        return Service.find_by(Product, Product.code == code)


    @classmethod
    @exception_handling
    def find_by_inventory(cls, inventory):
        return Service.find_by(Inventory, Inventory.id == inventory)


    @classmethod
    @exception_handling
    def find_by_inventory_transactions(cls, inventory_transactions):
        return Service.find_by(InventoryTransaction, InventoryTransaction.id == inventory_transactions)


    @classmethod
    @exception_handling
    def find_by_group_property(cls, group_property):
        return Service.find_by(Group_property, Group_property.id == group_property)

    @classmethod
    @exception_handling
    def find_by_property_value(cls, product_property_value):
        return Service.find_by(Product_Property_Value, Product_Property_Value.id == product_property_value)

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

        # todo: shart {"user_name": user_name}
        @classmethod
        @exception_handling
        def find_user_by_user_name(cls, user_name):
            return Service.find_by(User, {"user_name": user_name})

        # todo: shart {"role_id": role_id}
        @classmethod
        @exception_handling
        def find_users_by_role(cls, role_id):
            return Service.find_by(User, {"role_id": role_id})

        # todo: shart {"person_id": person_id}
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

    # todo: shart {"name": name}
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

    # todo: shart {"role_name": role_name}
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


class MassageController:

    @classmethod
    @exception_handling
    def add_message(cls, title, date_time, membername, text):
        massage = Message(title, date_time, membername, text)
        return True, Service.save(message, Message)

    @classmethod
    @exception_handling
    def find_message_by_title(cls, title):
        return Service.find_by(Message, {"title": title})

    @classmethod
    @exception_handling
    def find_message_by_date_time(cls, date_time):
        return Service.find_by(Message, {"date_time": date_time})

    @classmethod
    @exception_handling
    def find_message_by_ticket(cls, ticket):
        return Service.find_by(Message, {"ticket": ticket})

    @classmethod
    @exception_handling
    def find_message_by_text(cls, text):
        return Service.find_by(Message, {"text": text})

    @classmethod
    @exception_handling
    def find_message_by_user(cls, user):
        return Service.find_by(Message, {"user": user})


class TicketController:

    @classmethod
    @exception_handling
    def add_ticket(cls, datetime, response_type, title, text):
        ticket = Ticket(datetime, response_type, title, text)
        return True, Service.save(ticket, Ticket)

    @classmethod
    @exception_handling
    def find_ticket_by_datetime(cls, datetime):
        return Service.find_by(Ticket, {"datetime": datetime})

    @classmethod
    @exception_handling
    def find_ticket_by_response_type(cls, response_type):
        return Service.find_by(Ticket, {"response_type": response_type})

    @classmethod
    @exception_handling
    def find_ticket_by_title(cls, title):
        return Service.find_by(Ticket, {"title": title})

    @classmethod
    @exception_handling
    def find_ticket_by_text(cls, text):
        return Service.find_by(Ticket, {"text": text})

    @classmethod
    @exception_handling
    def find_ticket_by_message(cls, message):
        return Service.find_by(Ticket, {"massage": message})


class TicketGroupController:

    @classmethod
    @exception_handling
    def add_ticket_group(cls, name, parent=None,):
        ticket_group = TicketGroup(name, parent=None)
        return True, Service.save(ticket_group, TicketGroup)
