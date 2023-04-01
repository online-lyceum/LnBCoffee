from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Time
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy import Date
from api_template.db.base import Base


class Example(Base):
    __tablename__ = "schools"

    school_id = Column(Integer, autoincrement=True, primary_key=True,
                       index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    is_university = Column(Boolean)

    __table_args__ = (
        UniqueConstraint('name', 'address', name='uq_name_address'),
    )

