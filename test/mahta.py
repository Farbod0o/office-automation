from controller.controller import Controller
from model.entity.payment import Payment
from model.entity.transaction import Transaction
from model.entity.section import Section
# p1 = Controller.add_payment(1,"sdfsf")
Controller.add_bank("Bank A","1",656)
pay = Controller.find_by_id(Payment,1)

# ddd