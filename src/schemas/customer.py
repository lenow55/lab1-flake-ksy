import uuid

from sqlalchemy import (
    UUID,
    Column,
    ForeignKeyConstraint,
    Index,
    PrimaryKeyConstraint,
    String,
    Table,
    Text,
    UniqueConstraint,
)

from src.schemas.metadata import metadata_obj

customer = Table(
    "customer",
    metadata_obj,
    Column("id", UUID(as_uuid=True), default=uuid.uuid4, comment="Id покупателя"),
    Column(
        "fk_localization_id",
        UUID(as_uuid=True),
        nullable=True,
        comment="FK ID локализации",
    ),
    Column("name", String(length=50), nullable=True, comment="Покупатель название"),
    Column("address", String(length=50), nullable=True, comment="Адрес"),
    Column("contact", String(length=50), nullable=True, comment="Контактное лицо"),
    Column("phone", String(length=50), nullable=True, comment="контектный телефон"),
    Column("email", String(length=50), nullable=True, comment="почта"),
    Column("memo", Text(), nullable=True, comment="Комментарий"),
    # связи ключей
    ForeignKeyConstraint(
        ["fk_localization_id"],
        ["localization.id"],
        name="fk_customer_localization_id",
        onupdate="CASCADE",
        ondelete="SET NULL",
    ),
    # ограничения на колонки
    PrimaryKeyConstraint("id", name="pk_customer_id"),
    comment="Покупатель",
)

customer_email_phone = UniqueConstraint(
    customer.c.email, customer.c.phone, name="uq_customer__email_phone"
)

customer_name_ix = Index("ix_customer_name", customer.c.name, unique=False)
customer_address_ix = Index("ix_customer_address", customer.c.address, unique=False)
customer_contact_ix = Index("ix_customer_contact", customer.c.contact, unique=False)
