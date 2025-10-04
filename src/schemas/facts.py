import uuid

from sqlalchemy import (
    UUID,
    Column,
    ForeignKeyConstraint,
    Integer,
    Numeric,
    PrimaryKeyConstraint,
    Table,
)

from src.schemas.metadata import metadata_obj

facts = Table(
    "facts",
    metadata_obj,
    Column("id", UUID(as_uuid=True), default=uuid.uuid4),
    Column("fk_id_city", UUID(as_uuid=True), nullable=True, comment="FK ID Город"),
    Column(
        "fk_id_customer", UUID(as_uuid=True), nullable=True, comment="FK ID Покупатель"
    ),
    Column("fk_id_product", UUID(as_uuid=True), nullable=True, comment="FK ID Продукт"),
    Column("fk_id_date", UUID(as_uuid=True), nullable=True, comment="FK ID Дата"),
    Column("price", Numeric(10, 2), nullable=True, comment="Цена"),
    Column("volume", Integer, nullable=True, comment="Количество"),
    Column("amount_of_money", Numeric(10, 2), nullable=True, comment="Сумма"),
    Column("remains", Numeric(10, 2), nullable=True, comment="Остаток"),
    Column("debt", Numeric(10, 2), nullable=True, comment="Задолженность"),
    # связи ключей
    ForeignKeyConstraint(
        ["fk_id_product"],
        ["product.id_product"],
        name="fk_facts_product_id_product",
        onupdate="CASCADE",
        ondelete="SET NULL",
    ),
    ForeignKeyConstraint(
        ["fk_id_date"],
        ["date_operation.id"],
        name="fk_facts_date_operation_id",
        onupdate="CASCADE",
        ondelete="SET NULL",
    ),
    ForeignKeyConstraint(
        ["fk_id_city"],
        ["city.id"],
        name="fk_facts_city_id",
        onupdate="CASCADE",
        ondelete="SET NULL",
    ),
    # ограничения на колонки
    PrimaryKeyConstraint("id", name="pk_facts_id"),
    comment="Факты",
)
