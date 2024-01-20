#!/usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import abort

import requests

app = Flask(__name__)

pic_location= "https://images.unsplash.com/photo-1613771404784-3a5686aa2be3?q=80&w=2069&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

@app.route("/") # users are able to land at root
def index():
    pokemon_url = pkmn_user_input
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon_url).json()
    name= pokeapi["name"]
    name_upper= name.upper()
    sprites= pokeapi["sprites"]["back_default"]
    
    print(f"""
    HERES YOUR POKEMON:
    Name: {name_upper}
    Image: {sprites}
    """)
    
    return render_template('format.html', pic= pic_location, pokemon=pokeapi)

@app.route('/pokemon/<pkmn>')
def pokemon(pkmn):
    return "This is " + str(pkmn)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
    


# @app.route("/pokedex") # users can also land at "/pokedex"
# def pokedex():

# pokenum= input("Pick a number between 1 and 1000!\n>")

# like in lab 113 you could save the user inputs into a seperate file and then call them from 
# if you were able to integrate week2-project
# 	def harvestkey():
#     with open("/home/student/omdb.key") as apikeyfile:
#         return apikeyfile.read().rstrip("\n") # grab the api key out of omdb.key


