import uuid

from sqlalchemy import (
    UUID,
    Column,
    Index,
    PrimaryKeyConstraint,
    String,
    Table,
    Text,
)

from src.schemas.metadata import metadata_obj

city_type = Table(
    "city_type",
    metadata_obj,
    Column("id", UUID(as_uuid=True), default=uuid.uuid4),
    Column("name", String(length=50), nullable=False, comment="Наименование"),
    # ограничения на колонки
    PrimaryKeyConstraint("id", name="pk_city_type_id"),
    comment="Тип",
)


city_type_name_ix = Index("ix_city_type_name", city_type.c.name, unique=True)

city = Table(
    "city",
    metadata_obj,
    Column("id", UUID(as_uuid=True), default=uuid.uuid4),
    Column(
        "fk_city_type_id", UUID(as_uuid=True), nullable=True, comment="FK Тип города"
    ),
    Column("city", String(length=50), nullable=False, comment="Город"),
    Column("memo", Text(), nullable=True, comment="Комментарий"),
)

city_city_ix = Index("ix_city_city", city.c.city, unique=False)
