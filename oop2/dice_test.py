#!/usr/bin/python3
"""RZFeeser | Alta3 Research
Creating a simple dice program utilizing classes."""


# imports from cheadice.py (this is in the local directory)
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice

def main():
    """run-time code"""

    # create two cheater objects
    cheater1 = Cheat_Swapper() # ability is to change 3rd dice roll to 6
    cheater2 = Cheat_Loaded_Dice() # increase all rolls by +1 provided they are < 6

    # both players take turns
    cheater1.roll()
    cheater2.roll()

    # both players use their cheat methods
    cheater1.cheat()
    cheater2.cheat()

    print(f"Cheater 1 rolled {cheater1.get_dice()}")
    print(f"Cheater 2 rolled {cheater2.get_dice()}")

    if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
        print("Draw!")

    elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
        print("Cheater 1 wins!")

    else:
        print("Cheater 2 wins!")

    # if total dice is under 9, get a re-roll
    class Cheat_Mulligan(Player):
        def cheat(self):
            if sum(self.dice) <= 9:
                self.dice = []
                for i in range(3):
                    self.dice.append(random.randint(1,6))


    # add an extra dice roll
    class Cheat_Extra_Die(Player):
        def cheat(self):
            self.dice.append(random.randint(1,6))

    # first die roll is lucky and can't roll under a 3
    class Cheat_Lucky_Die(Player):
        def cheat(self):
            if self.dice[0] < 3:
                self.dice[0]= random.randint(3,6)

    # switch other player's dice with dice that can't roll above a 3
    class Cheat_Saboteur(Player):
        def cheat(self, other_player):
            other_player.dice = [random.randint(1,3) for i in range(3)]
                        # ^ this is a list comprehension;
                        # a handy way to generate list contents
                        # in one line of code


if __name__ == "__main__":
    main()

