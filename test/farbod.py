from model.entity.department import Department
from model.entity.section import Section

dep = Department("Department",1,"Department.png","task","address",
                 "02122361258","nadarad")
sec = Section("Section","sec address","02149499293","1",
              "full","1",None,None,dep)

print(sec.address)
print(dep.address)