from flask import Flask
from walkthrough import db
# remember 'db.create_all() in terminal before running
# LOOK INTO USING TABLES INSTEAD OF MODELS
#       This may make it easier to add, remove and edit information
#       Might only be needed for a few models/tables

# BEGIN MAIN MODELS
class Company(db.Model):
    # Example: Innovacare
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    # locations = db.relationship('Location', backref='company')

    def __repr__(self) -> str:
        return f'{self.name}'
    
class Location(db.Model):
    # Example: Jacksonville, Fl
    id = db.Column(db.Integer(), primary_key=True)
    city = db.Column(db.String(length=50), nullable=False)
    state = db.Column(db.String(length=50), nullable=False)
    company = db.Column(db.String(length=55))
    # company_id = db.Column(db.Integer(), db.ForeignKey('company.id'))
    # sites = db.relationship('Site', backref='location')


    def __repr__(self) -> str:
        return f'{self.city}, {self.state}'
    
class Site(db.Model):
    # Example: Flemming Island
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    address = db.Column(db.String(length=120), nullable=False, unique=True)
    zip_code = db.Column(db.String(length=10), nullable=False)
    location = db.Column(db.String(length=110), nullable=False)
    # location_id = db.Column(db.Integer(), db.ForeignKey('location.id'))
    # controllers = db.relationship('Controller', backref='site')

    def __repr__(self) -> str:
        return f'"{self.name}"'
    
class Door(db.Model):
    # Example: Front Door
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    description = db.Column(db.String(length=50))
    comments = db.Column(db.String(length=1024))
    doorboard = db.Column(db.String(length=55))
    # doorboard_id = db.Column(db.Integer(), db.ForeignKey('door_board.id'))
    distance = db.Column(db.Integer())
    # Features
    has_strike = db.Column(db.Boolean(), default=False)
    has_reader = db.Column(db.Boolean(), default=False)
    has_rex = db.Column(db.Boolean(), default=False)
    has_exitBtn = db.Column(db.Boolean(), default=False)
    has_dpi = db.Column(db.Boolean(), default=False)
    has_glass = db.Column(db.Boolean(), default=False)
    has_magSingle = db.Column(db.Boolean(), default=False)
    has_magDouble = db.Column(db.Boolean(), default=False)
    has_keypad = db.Column(db.Boolean(), default=False)
    has_pushbar = db.Column(db.Boolean(), default=False)
    has_paddle = db.Column(db.Boolean(), default=False)
    has_vidBell = db.Column(db.Boolean(), default=False)

    def __repr__(self) -> str:
        return f'{self.name}'
    

# BEGIN 'SMALLER' MODELS

class Controller(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    site = db.Column(db.String(length=55), nullable=False)
    is_expansion = db.Column(db.Boolean(), default=False)
    # site_id = db.Column(db.Integer(), db.ForeignKey('site.id'))
    # door_boards = db.relationship('DoorBoard', backref='controller')

    def __repr__(self) -> str:
        return f'{self.name}'


class DoorBoard(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length=50), nullable=False)
    controller = db.Column(db.String(length=55))
    # controller_id = db.Column(db.Integer(), db.ForeignKey('controller.id'))
    # doors = db.relationship('Door', backref='door_board')

    def __repr__(self) -> str:
        return f'{self.name}'
