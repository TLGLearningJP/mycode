#!/usr/env/python3
def main():
    list = []
    user_name = input("What is your name?\n")
    user_name = user_name.title()
    list.append(user_name)

    user_age = input("How old are you?\n")
    user_age = int(user_age)
    print(type(user_age))
    list.append(user_age)
    # age = int(input("what is your age: "))

    user_fav_movie = input("What is your favorite movie?\n")
    user_fav_movie = user_fav_movie.title()
    list.append(user_fav_movie)

    inner = []
    genre = input("What is the genre: ")
    actor = input("Name one actor: ")
    inner.append(genre.title())
    inner.append(actor.title())
    list.append(inner)

    print(f"Hello {list[0]}, you are {list[1]} years old and your favorite movie is {list[2]}.")
    print(f"The movie's genre is {list[3][0]} and {list[3][1]} acts in it.")
main()
