from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from model.entity.base import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DataAccess:
    def __init__(self, class_name):
        connection_string = "mysql+pymysql://root:root@localhost:3306/HMS"
        if not database_exists(connection_string):
            create_database(connection_string)

        engine = create_engine(connection_string)
        Base.metadata.create_all(engine)

        sessions = sessionmaker(bind=engine)
        self.session = sessions()
        self.class_name = class_name

    def save(self, entity):
        try:
            self.session.add(entity)
            self.session.commit()
            self.session.refresh(entity)
            return entity
        except Exception as e:
            raise ValueError("Error adding {} to database: {}".format(entity, e))

    def edit(self, entity):
        self.session.merge(entity)
        self.session.commit()
        return entity

    def remove(self, entity):
        self.session.delete(entity)
        self.session.commit()
        return entity

    def find_all(self):
        entity_list = self.session.query(self.class_name).all()
        return entity_list

    def find_by_id(self, id):
        entity = self.session.get(self.class_name, id)
        return entity

    def find_by(self, find_statement):
        entity = self.session.query(self.class_name).filter(find_statement).all()
        return entity

    def find_by_conditions(self, conditions, join_statement, join_class):
        _info = (
            self.session.query(self.class_name).join(join_class, join_statement).filter(conditions).all())
        return _info

    def find_by_conditions2(self, conditions):
        _info = (
            self.session.query(self.class_name).filter(conditions).all())
        return _info
