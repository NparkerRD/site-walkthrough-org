import os
from flask import Flask
from walkthrough import db
# remember 'db.create_all() in terminal before running
# to add multiple variables to session: db.session.add_all([item1, item2, item3])

class Controller(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    is_expansion = db.Column(db.Boolean(), default=False)
    door_boards = db.relationship('DoorBoard', backref='controller')

    def __repr__(self) -> str:
        return f'<Controller "{self.name}">'

class DoorBoard(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    controller_id = db.Column(db.Integer(), db.ForeignKey('controller.id'))
    # When querying later to display in HTML, the controller information can be found by using Controller.query.filter_by(controller_id).first()

    def __repr__(self) -> str:
        return f'<Door Board "{self.name}" >'



# Controller is 'One'; Doorboard is "Many"

db.create_all()

controller1 = Controller(name="ACS01")
controller2 = Controller(name="ACS01-EXP", is_expansion=True)
controller3 = Controller(name="ACS02")

board1 = DoorBoard(name="DB01-1", controller_id=1)
board2 = DoorBoard(name="DB01-2", controller_id=1)
board3 = DoorBoard(name="DB02-1", controller_id=1)
board4 = DoorBoard(name="DB02-2", controller_id=1)
board5 = DoorBoard(name="DB08-1", controller_id=2)

db.session.add_all([controller1, controller2, controller3])
db.session.add_all([board1, board2, board3, board4, board5])

db.session.commit()


