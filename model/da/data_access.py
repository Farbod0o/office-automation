from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DataAccess:
    def __init__(self, entity_class):
        connection_string = "mysql+pymysql://root:root@localhost:3306/office-automation"
        if not database_exists(connection_string):
            create_database(connection_string)

        engine = create_engine(connection_string)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.entity_class = entity_class

    def save(self, entity):
        try:
            self.session.add(entity)
            self.session.commit()
            self.session.refresh(entity)
            return entity
        except Exception as e:
            self.session.rollback()
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
        return self.session.query(self.entity_class).all()

    def find_by_id(self, id):
        return self.session.query(self.entity_class).get(id)

    def find_by(self, find_statement):
        return self.session.query(self.entity_class).filter(find_statement).all()

    def find_by_conditions(self, conditions, join_statement, join_class):
        return (
            self.session.query(self.entity_class)
            .join(join_class, join_statement)
            .filter(conditions)
            .all()
        )

    def find_by_conditions2(self, conditions):
        return self.session.query(self.entity_class).filter(conditions).all()

    def close(self):
        self.session.close()
