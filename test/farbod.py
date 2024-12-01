from controller.controller import Controller
from model.entity.department import Department
from model.entity.section import Section

status,dep = Controller.add_department("ض",1,"Department.png","task","address",
                 "سس","nadarad")
print("-------------")
print(status)
print("-------------")
print(dep)
# dep = Controller.find_by_id(Department,1)
#
# Controller.add_section(name="Section",address="sec address",phone_number="02149499293",internal_code="1",
#               access_lvl="full",section_num="1",parent_section_num=None,description="None",department=dep)
