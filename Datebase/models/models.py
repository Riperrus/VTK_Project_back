from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, Boolean

metadata=MetaData()

# Таблица ролей
role=Table(
    "role",
    metadata,
    Column("id", Integer,primary_key=True),
    Column("role_name", String, nullable=False),
    Column("permissions", Integer)# Возможности пока не определены
)

# Таблица пользователя
user = Table(
    "user",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("username",String,nullable=False),
    Column("email",String),# email или callnumber на данный момент не являются обязательными
    Column("callnumber",Integer),
    Column("hashed_password", String,nullable=False),
    Column("registered_at", TIMESTAMP,default=datetime.utcnow),# время регестрации
    Column("role_id",Integer, ForeignKey("role.id")),
    Column("is_active",Boolean, default=True, nullable=False),
    Column("is_superuser",Boolean, default=False, nullable=False),
    Column("is_verified",Boolean, default=False, nullable=False)
)