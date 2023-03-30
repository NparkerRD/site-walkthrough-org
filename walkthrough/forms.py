from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import Length, EqualTo

class NewSite(FlaskForm):
    name = StringField(label='Site')
    submit = SubmitField(label='Submit')

class NewCompany(FlaskForm):
    name = StringField(label='Company')
    submit = SubmitField(label='Submit')

class NewLocation(FlaskForm):
    name = StringField(label='Name')
    state = StringField(label="State")
    city = StringField(label="City")
    street_address = StringField(label="Address")
    submit = SubmitField(label='Submit')

class NewDoor(FlaskForm):
    name = StringField(label='Name')
    door_num = IntegerField(label="Door Number")
    distance = IntegerField(label="Distance from door")
    comments = StringField(label="Notes")
    # controller = SelectField(label="Controller", choices="") [REVISIT]
    # door_board = SelectField(label="Door Board", choices="")
    strike = BooleanField(label="Strike")
    reader = BooleanField(label="Reader")
    rex = BooleanField(label="REX")
    glass = BooleanField(label="Glass")
    mag_single = BooleanField(label="Mag Single")
    mag_double = BooleanField(label="Mag Double")
    keypad = BooleanField(label="Keypad")
    exit_btn = BooleanField(label="Exit Button")
    pushbar = BooleanField(label="Pushbar")
    paddle = BooleanField(label="Paddle")
    dpi = BooleanField(label="DPI")

    submit = SubmitField(label='Submit')

