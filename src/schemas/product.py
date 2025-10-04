import uuid

from sqlalchemy import (
    UUID,
    Column,
    ForeignKeyConstraint,
    Index,
    Integer,
    PrimaryKeyConstraint,
    String,
    Table,
    Text,
)

from src.schemas.metadata import metadata_obj

product_group = Table(
    "product_group",
    metadata_obj,
    Column("id_product_group", UUID(as_uuid=True), default=uuid.uuid4),
    Column("name", String(length=50), nullable=False, comment="Наименование"),
    Column("memo", Text(), nullable=True, comment="Комментарий"),
    # ограничения на колонки
    PrimaryKeyConstraint("id_product_group", name="pk_product_group_id_product_group"),
    comment="Группа товаров",
)

product_group_name_ix = Index(
    "ix_product_group_name", product_group.c.name, unique=True
)

product = Table(
    "product",
    metadata_obj,
    Column("id_product", UUID(as_uuid=True), default=uuid.uuid4),
    Column(
        "fk_product_group", UUID(as_uuid=True), nullable=True, comment="FK Гр Товаров"
    ),
    Column("id_catalog", Integer(), nullable=True, comment="ID каталог"),
    Column("name", String(length=50), nullable=True, comment="Наименование"),
    Column("memo", Text(), nullable=True, comment="Комментарий"),
    # связи ключей
    ForeignKeyConstraint(
        ["id_product"],
        ["product_group.id_product_group"],
        name="fk_id_product_id_product_group",
        onupdate="CASCADE",
        ondelete="SET NULL",
    ),
    # ограничения на колонки
    PrimaryKeyConstraint("id_product", name="pk_model_thresholds_threshold_id"),
)

product_name_ix = Index("ix_product_name", product.c.name, unique=False)
