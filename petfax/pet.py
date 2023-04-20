from flask import (Blueprint, render_template) 
import json 

pets = json.load(open('pets.json'))
# print(pets)
bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)

# https://flask.palletsprojects.com/en/2.0.x/quickstart/#variable-rules 
@bp.route('/<pet_id>')
def show_pet(pet_id):
    return render_template('show.html', pets =pets)