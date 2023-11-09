"""empty message

Revision ID: 91a2c32c6289
Revises: 1f19b686cd8d
Create Date: 2023-11-08 21:55:21.559680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91a2c32c6289'
down_revision = '1f19b686cd8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_music_association')
    with op.batch_alter_table('musics', schema=None) as batch_op:
        batch_op.add_column(sa.Column('playlist_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_musics_playlist_id_playlists'), 'playlists', ['playlist_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('musics', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_musics_playlist_id_playlists'), type_='foreignkey')
        batch_op.drop_column('playlist_id')

    op.create_table('user_music_association',
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('music_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['music_id'], ['musics.id'], name='fk_user_music_association_music_id_musics'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_user_music_association_user_id_users')
    )
    # ### end Alembic commands ###