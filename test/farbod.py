from controller.controller import Controller
from model.entity.department import Department
from model.entity.section import Section

Controller.add_department("Department3",1,"Department.png","task","address",
                 "02122361258","nadarad")
dep = Controller.find_by_id(Department,1)

Controller.add_section(name="Section",address="sec address",phone_number="02149499293",internal_code="1",
              access_lvl="full",section_num="1",parent_section_num=None,description="None",department=dep)
