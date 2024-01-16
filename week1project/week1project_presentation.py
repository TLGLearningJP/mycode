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
    
# iterate through the dictionary, gather the three things == use an if statement from the user (all at once, rather than
# for pokemon in pokemon_dict.value()
# pokemon.items()<== play with this
# for key, value in dict.items():

questions = ("What type do you want your pokemon to be?: ",
             "What personality would you like your Pokemon to be?: ",
             "What predominate stat would you like your Pokemon to be?: ")
options = (("A. Grass", "B. Fire", "C. Water"),
           ("A. Loyal", "B. Defiant", "C. Quirky"),
           ("A. Attack", "B. Speed", "C. Defense"))

bulbasaur = ["a", "a", "a"]
charmander = ["b", "b", "b"]
squirtle = ["c", "c", "c"]
chikorita = ["a", "c", "c"]
cyndaquil = ["b", "b", "a"]
totodile = ["c", "a", "a"]
treecko = ["a", "b", "a"]
torchic = ["b", "b", "c"]
mudkip = ["c", "a", "b"]
turtwig = ["a", "c", "b"]
chimchar = ["b", "a", "a"]
piplup = ["c", "a", "c"]
snivy = ["a", "c", "a"]
tepig = ["b", "c", "c"]
oshawott = ["c", "b", "a"]
chespin = ["a", "b", "c"]
fennekin = ["b", "a", "b"]
froakie = ["c", "b", "b"]
rowlet = ["a", "a", "b"]
litten = ["b", "a", "c"]
popplio = ["c", "b", "c"]
grookey = ["a", "b", "b"]
scorbunny = ["b", "c", "a"]
sobble = ["c", "c", "a"]
sprigatito = ["a", "a", "c"]
fuecoco = ["b", "c", "b"]
quaxly = ["c", "c", "b"]
pikachu = ["no", "thunder", "stone"]

answers = []
question_num = 0

print("====================")
print("CHOOSE YOUR POKEMON:")
print("====================")
for question in questions:
    print("--------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    answer = input("Enter (A, B, C): ").lower().strip() 
    answers.append(answer)
    question_num += 1
    
if answers == bulbasaur:
    print("Your starter pokemon is: Bulbasaur")
elif answers == charmander:
    print("Your starter pokemon is: Charmander")
elif answers == squirtle:
    print("Your starter pokemon is: Squirtle")
elif answers == chikorita:
    print("Your starter pokemon is: Chikorita")
elif answers == cyndaquil:
    print("Your starter pokemon is: Cyndaquil")
elif answers == totodile:
    print("Your starter pokemon is: Totodile")
elif answers == treecko:
    print("Your starter pokemon is: Treecko")
elif answers == torchic:
    print("Your starter pokemon is: Torchic")
elif answers == mudkip:
    print("Your starter pokemon is: Mudkip")
elif answers == turtwig:
    print("Your starter pokemon is: Turtwig")
elif answers == chimchar:
    print("Your starter pokemon is: Chimchar")
elif answers == piplup:
    print("Your starter pokemon is: Piplup")
elif answers == snivy:
    print("Your starter pokemon is: Snivy")
elif answers == tepig:
    print("Your starter pokemon is: Tepig")
elif answers == oshawott:
    print("Your starter pokemon is: Oshawott")
elif answers == squirtle:
    print("Your starter pokemon is: Squirtle")
elif answers == chespin:
    print("Your starter pokemon is: Chespin")
elif answers == fennekin:
    print("Your starter pokemon is: Fennekin")
elif answers == froakie:
    print("Your starter pokemon is: Froakie")
elif answers == rowlet:
    print("Your starter pokemon is: Rowlet")
elif answers == litten:
    print("Your starter pokemon is: Litten")
elif answers == popplio:
    print("Your starter pokemon is: Popplio")
elif answers == grookey:
    print("Your starter pokemon is: Grookey")
elif answers == scorbunny:
    print("Your starter pokemon is: Scorbunny")
elif answers == sobble:
    print("Your starter pokemon is: Sobble")
elif answers == sprigatito:
    print("Your starter pokemon is: Sprigatito")
elif answers == fuecoco:
    print("Your starter pokemon is: Fuecoco")
elif answers == quaxly:
    print("Your starter pokemon is: Quaxly")
elif answers == pikachu:
    print("Your starter pokemon is Pikachu")
else:
    print("Your starter pokemon is: Eevee")


        
pokemon = {
"Bulbasaur":
    {"type": "grass",
    "personality": "loyal",
    "stats": "attack"},

"Charmander":
    {"type": "fire",
    "personality": "defiant",
    "stats": "speed"},

"Squirtle":
    {"type": "water",
    "personality": "quirky",
    "stats": "defense"}
            }


#a = pokemon["Charmander"]["type"]
#print(f"{a}")
#user_poke_type = input("What type do you like?: ").lower()
#user_poke_personality = input("What personablity would you like your Pokemon to be?: ").lower()
#user_poke_stat = input("What predominate stat would you like your Pokemon to be?: ").lower()

#for key in pokemon:
#if user_poke_type == 'water':
    #print(pokemon " : " 'Squirtle')
    #print(pokemon)
            #else:
                #print('test')
        #if pokemon[key]['personality'] == 'defiant':
            #print(key)
    #else:
        #print('test')
    #print(key, " : ", pokemon[key])

   #poke_type = pokemon[key]['type']
    #if pokemon[key]['type'] == user_poke_type:
        #if pokemon[key]['personality'] == user_poke_personality:
            #if pokemon[key]['stats'] == user_poke_stat:
