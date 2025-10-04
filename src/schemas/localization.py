import uuid

from sqlalchemy import (
    UUID,
    Column,
    Index,
    PrimaryKeyConstraint,
    String,
    Table,
)

from src.schemas.metadata import metadata_obj

localization = Table(
    "localization",
    metadata_obj,
    Column("id", UUID(as_uuid=True), default=uuid.uuid4, comment="Id локализации"),
    Column("name", String(length=50), nullable=False, comment="Тип локализации"),
    # ограничения на колонки
    PrimaryKeyConstraint("id", name="pk_localization_id"),
    comment="Локализация покупателя",
)

localization_name_ix = Index("ix_localization_name", localization.c.name, unique=True)
