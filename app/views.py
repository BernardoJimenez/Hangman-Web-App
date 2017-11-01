from flask import Flask, render_template, flash, redirect, session, url_for
from app import app
from .forms import GameOnForm, GameOverForm
from .logic import GameLogic
import jsonpickle

@app.route('/', methods=['GET', 'POST'])
@app.route('/hangman', methods=['GET', 'POST'])
def hangman():
    if session.get('game_logic') == None:
        # if there is no previously saved game, create
        gl = GameLogic()
        session['game_logic'] = jsonpickle.encode(gl) # we can pickle that!
        # jsonpickle allows for serialization of non-primitives
        session['wins'] = 0
        session['losses'] = 0

    game_logic = jsonpickle.decode(session.get('game_logic'))
    # deserialize in order to use GameLogic instance

    if game_logic.game_over:
        form = GameOverForm()

        if game_logic.all_guesses:
            if game_logic.bad_guesses > 9:
                session['losses'] += 1
            else:
                session['wins'] += 1
        else:
            pass

        gl = GameLogic()
        session['game_logic'] = jsonpickle.encode(gl) # repickle new instance
    else:
        form = GameOnForm()

        if form.validate_on_submit():
            if (not str(form.user_guess.data)[0].isalpha()):
                # not a letter
                flash('Please enter a LETTER!')
            elif (str(form.user_guess.data).lower()[0] in game_logic.all_guesses):
                # user guesses a previously made guess
                flash('You\'ve entered that guess already!')
            else:
                # valid guesses are saved in the session cookie
                session['user_guess'] = form.user_guess.data
                # and processed with the GameLogic() class instance
                game_logic.process_guess(session.get('user_guess'))

            session['game_logic'] = jsonpickle.encode(game_logic) # repickle

            return redirect(url_for('hangman')) # prevents form-resubmission

    return render_template('hangman.html',
                            form = form,
                            wins = session.get('wins'),
                            losses = session.get('losses'),
                            game_logic = game_logic)
