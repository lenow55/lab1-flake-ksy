import uuid

from sqlalchemy import (
    UUID,
    Column,
    DateTime,
    Index,
    PrimaryKeyConstraint,
    Table,
)

from src.schemas.metadata import metadata_obj

date_operation = Table(
    "date_operation",
    metadata_obj,
    Column("id", UUID(as_uuid=True), default=uuid.uuid4),
    Column("date", DateTime(timezone=True), nullable=True, comment="Дата события"),
    # ограничения на колонки
    PrimaryKeyConstraint("id", name="pk_city_type_id"),
    comment="Дата операции",
)


city_type_name_ix = Index("ix_date_operation_date", date_operation.c.date, unique=False)
