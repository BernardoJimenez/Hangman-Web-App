from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from .logic import GameLogic

class GameOnForm(FlaskForm):
    # field where user enters their guess
    user_guess = StringField("Guess a letter: ", validators=[DataRequired()])

class GameOverForm(FlaskForm):
    # button used to start a new game
    submit = SubmitField('Click to play again!')
