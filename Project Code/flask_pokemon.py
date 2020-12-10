from flask import Flask, render_template, url_for, flash, redirect
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from pokemon_info import pokemon_info
from PIL import Image

app = Flask(__name__)
boostrap = Bootstrap(app)

# form for asking what pokemon they want to choose
class Pokemon(FlaskForm):
    pokemon_1 = StringField(
        'Choose your first Pokemon from Generation 6: ', 
        validators=[DataRequired()]
    )

    pokemon_2 = StringField(
        'Choose your second Pokemon from Generation 6: ', 
        validators=[DataRequired()]
    )

# storing chosen pokemon in a list
def store_pokemon(poke_1, poke_2):

    both_pokemon = []

    both_pokemon.append(poke_1)
    both_pokemon.append(poke_2)


@app.route('/', methods=('GET', 'POST'))
def home():

    form = Pokemon()
    
    if form.validate_on_submit():
        store_pokemon(form.pokemon_1.data, form.pokemon_2.data)
        return redirect('/battle_arena')

    # home page
    return render_template('home.html', pokemon_info = pokemon_info, form = form)


@app.route('/battle_arena')
def battle_arena():
        
    # page displaying pokemon on battle arena
    return render_template('battle_arena.html', pokemon_info = pokemon_info, both_pokemon = both_pokemon)


@app.route('/winner')
def winner(pokemon_winner):
        
    # page displaying the winner pokemon
    return render_template('winner.html', pokemon_info = pokemon_info, pokemon_winner = pokemon_winner, both_pokemon = both_pokemon)
