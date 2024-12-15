from model.entity.Product_Property_Value import Product_Property_Value
from model.entity.Group_property import Group_property
from model.entity.product import Product
from controller.controller import Controller
test_product = Product_Property_Value("fefe","wdqdddwdwd","frfrr","frferfr","rfeafr")
# print(test_product)


un = Controller.add_unit("test",1,"des00")
print(un)