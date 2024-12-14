from model.da.data_access import DataAccess


class Service:
    @staticmethod
    def save(obj, entity):
        entity_da = DataAccess(entity)
        entity_da.save(obj)
        return obj

    @staticmethod
    def find_all(entity):
        entity_da = DataAccess(entity)
        return entity_da.find_all()

    @staticmethod
    def find_by_id(entity, id):
        entity_da = DataAccess(entity)
        return entity_da.find_by_id(id)

    @staticmethod
    def find_by_username(entity, username):
        entity_da = DataAccess(entity)
        return entity_da.find_by(entity._username == username)

    @staticmethod
    def find_by(entity, statement):
        entity_da = DataAccess(entity)
        return entity_da.find_by(statement)

    @staticmethod
    def edit(obj, entity):
        entity_da = DataAccess(entity)
        res = entity_da.edit(obj)
        return res

    @staticmethod
    def remove(entity, id):
        entity_da = DataAccess(entity)
        instance = entity_da.find_by_id(id)
        if instance:
            entity_da.remove(instance)
        else:
            raise ValueError(f"Record with ID {id} not found in {entity.__name__}.")


    @staticmethod
    def find_by_field(entity, field_name, value):
        entity_da = DataAccess(entity)
        field = getattr(entity, field_name, None)
        if not field:
            raise ValueError(f"Field {field_name} not found in {entity.__name__}.")
        return entity_da.find_by(field == value)

    @staticmethod
    def search_text(entity, text_field, keyword):
        entity_da = DataAccess(entity)
        field = getattr(entity, text_field, None)
        if not field:
            raise ValueError(f"Field {text_field} not found in {entity.__name__}.")
        return entity_da.find_by(field.like(f"%{keyword}%"))


    @staticmethod
    def date_range(entity, start_date, end_date, date_field):
        entity_da = DataAccess(entity)
        field = getattr(entity, date_field, None)
        if not field:
            raise ValueError(f"Field {date_field} not found in {entity.__name__}.")
        return entity_da.find_by((field >= start_date) & (field <= end_date))
