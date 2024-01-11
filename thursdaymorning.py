demo= {
       "a":"letter",
        "b":"letter"
    }

for x in demo:
    #print(type(x))
    print(x, end=" ")
    print("-----")

with open("otherfile.txt") as zoink:
    for x in zoink:
        print(type(x))
        print(x)
