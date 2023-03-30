import sqlalchemy as sa
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from walkthrough import metadata_obj, engine, db

# user = Table(
#     "user",
#     metadata_obj,
#     Column("user_id", Integer, primary_key=True),
#     Column("user_name", String(16), nullable=False),
#     Column("email_address", String(60), key="email"),
#     Column("nickname", String(50), nullable=False)
# )

# user_prefs = Table(
#     "user_prefs",
#     metadata_obj,
#     Column("pref_id", Integer, primary_key=True),
#     Column("user_id", Integer, ForeignKey("user.user_id"), nullable=False),
#     Column("pref_name", String(40), nullable=False),
#     Column("pref_value", String(100))
# )


user = db.Table(
    "user",
    sa.Column("id", Integer, primary_key=True),
    sa.Column("user_name", String(16), nullable=False),
    sa.Column("email_address", String(60), key="email"),
    sa.Column("nickname", String(50), nullable=False)
)

user_prefs = db.Table(
    "user_prefs",
    sa.Column("pref_id", Integer, primary_key=True),
    sa.Column("user_id", sa.ForeignKey(user.id)),
    sa.Column("pref_name", String(40), nullable=False),
    sa.Column("pref_value", String(100)),
)


# NOTES ON FLASK-SQLALCHEMY

# DEFINE MODELS - https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#define-models
# db.session.add(obj) adds an object to session
# db.session.delete(obj) deletes an object
# Always call db.session.commit() after any change to data
# db.session.execute(db.select(...)) constructs a query to select data from the database
# Result.scalars() method to get a list of results
# Result.scalar() method to get a single result
# Model.query is considered legacy; prefer db.session.execute(db.select(...)) instead

# MODELS AND TABLES - https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/models/
# For tables in flask_sqlalchemy, metadata argument is not required. Metadata will be chosen base on bind_key argument, or default will be used
# Common readon for tables is when defining many-to-many relationships. Association table doesn't need its own model class, as it will be accessed through the relevant relationship attributes on the related models.