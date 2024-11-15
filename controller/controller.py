from model.entity.organization import Organization
from model.tools.decorators import exception_handling
from model.services.service import Service
class Controller:
    @classmethod
    @exception_handling
    def add_organization(cls, name, slogan, logo, duties, address, telephone, description="",head_id=None):
        org = Organization(name, slogan, logo, duties, address, telephone, description)
        return True, Service.save(org, Organization)

