#!/usr/bin/env python3
# Take in user input
# Incorporate conditionals("if", "elif", "else"; however you need to use them)
# Code shuold be within functions (not just hanging out on the script)
# Challenge yourself! But be realistic. Have some goals for you MVP -- a series of questions 
    # resulting in a starter Pokemon selection. 29 possible outcomes
    # There are three different types of starters (fire, water, grass), save two types (pikachu, eevee)
    # this could allow three different branches of questions to help steer question narrative
    # from type selection, questions could be geared towards personalities of pokemon
    # I would need to assign personalities to each pokemon -- or be determined by predominate stat
    # selections would add counters to a variable 
    # would each pokemon have a counter set to 0 and each answer would add to (a) given pokemon?
    # or would the counter and the end result give pokemon? 
    # or "nested" counters? 1, 2, 3, or 4 for types -- 1, 2, 3 for personalities -- 1, 2, 3 for stats to help navigate selection
        # just start with the 27 regular starter pokemon -- and add special break points for pikachu and eevee
            # pikachu could be given as a starter is questions aren't answered correctly a certain number of times
            # eevee could be the tie breaker on the different counters
    # store the pokemon in different dictionaries, and potentially assign them key:values that would help determine selection flow

pokemon = {
"Bulbasaur":
    {"type": "grass",
    "personality": "loyal",
    "stats": "Attack"},

"Charmander":
    {"type": "fire",
    "personality": "defiant", 
    "stats": "Speed"},

"Squirtle":
    {"type": "water",
    "personality": "quirky",
    "stats": "Defense"}
            }

a = pokemon["Charmander"]["type"]

#print(f"{a}")


user_poke_type = input("What type do you like?: ").lower()

for key in pokemon:
    #poke_type = pokemon[key]['type']
    if pokemon[key]['type'] == user_poke_type:
        
        print(key)
        #if pokemon[key]['personality'] == 'defiant':
            #print(key)
    else:
        print('test')
    #print(key, " : ", pokemon[key]['type'])

# iterate through the dictionary, gather the three things == use an if statement from the user (all at once, rather than
# for pokemon in pokemon_dict.value()
# pokemon.items()<== play with this
# for key, value in dict.items():


