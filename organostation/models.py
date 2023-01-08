"""
models.py


See here: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
and maybe this too:
https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application

To test table creation, run the following commands in the python shell:
>>> from organostation.models import User
>>> u = User(name='Jose', email='jose.guzman@example.com')
>>> u.__dict__
>>> {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState at 0x1088b80a0>,
    'name': 'Jose',
    'email': 'jose.guzman@example.com'}
>>> u
name: Jose>
"""
from datetime import datetime as dtime

from werkzeug.security import check_password_hash, generate_password_hash

from . import db


class User(db.Model):
    """User model with username, email and password_hash."""

    __tablename__ = "organostation_users"  # set name of resulting table

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False, nullable=False)
    surname = db.Column(db.String(100), index=True, unique=False, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(64))
    created = db.Column(db.DateTime, default=dtime.utcnow())
    admin = db.Column(
        db.Boolean, index=False, unique=False, nullable=False, default=False
    )

    def set_password(self, password: str) -> None:
        """Set password to a hashed password."""
        self.password_hash = generate_password_hash(password, method="sha256")

    def check_password(self, password: str) -> bool:
        """Check hashed password."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"username: {self.name}"
