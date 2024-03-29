"""Adicionado o campo currency em person

Revision ID: 123ae1703623
Revises: 6cae39312f94
Create Date: 2022-08-31 20:58:40.491178

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = "123ae1703623"
down_revision = "6cae39312f94"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "person",
        sa.Column(
            "currency", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("person", "currency")
    # ### end Alembic commands ###
