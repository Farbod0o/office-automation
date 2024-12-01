from model.da.data_access import DataAccess
from model.entity.person import Person
from model.entity.permission import Permission
from model.entity.Role import Role
from model.entity.user import User

# test Person
person_da = DataAccess(Person)
person = Person(
    name="Ali",
    family="Ahmadi",
    national_id="1234567890",
    birth_date="1990-01-01",
    phone="09121234567",
    address="Tehran, Iran",
    post_code="1234567890"
)
person_da.save(person)
print("save Person:", person)

# test Permission
permission_da = DataAccess(Permission)
permission = Permission(name="Admin Access")
permission_da.save(permission)
print("ذخیره Permission:", permission)

# test Role
role_da = DataAccess(Role)
role = Role(role_name="Admin")
role_da.save(role)
print("save Role:", role)

# test User
user_da = DataAccess(User)
user = User(
    user_name="ali_admin",
    password="securepassword",
    email="ali@example.com",
    role_id=1,
    person_id=1
)
user_da.save(user)
print("save User:", user)
