import socket
import math
import errno
import time
import random
from os import system
import threading

_ = system('clear')

# Choosing Nickname
print("-------------Welcome to the Snake and Ladder Game------------------")

print ("Name will display on server")
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.15', 8888))

# effects! add a delay of 1 second before performing any action
WAIT = 1
MAX_VAL = 50
DICE_FACE = 6

# snake takes you down
snakes = {
    39: 3,
    46: 14,
    49: 13,
}

# ladder takes you up
ladders = {
    5: 43,
    9: 30,
    20: 41,
}

player_turn_text = [
    "Your turn.",
    "Go.",
    "Please proceed.",
    "Lets win this.",
    "Are you ready?",
    "",
]


ladder_jump = [
    "Alhamdulillah",
    "woww",
    "nailed it",
    "oh my God...",
    "yaayyy"
]


def welcome_msg():
    msg = """
    Welcome to Snake and Ladder Game.
 
    
    41 42 43 44 45 46 47 48 49 50
    ^     ^        *        *
    40 39 38 37 36 35 34 33 32 31
    |  *   \        \      /
    21 22 23 24 25 26 27 28 29 30
    |   \     \       \   /    ^
    20 19 18 17 16 15 14 13 12 11
         \      \            /
    1  2  3  4  5  6  7  8  9  10

    Snake    Ladder
    49->13   20->41
    46->14   9->30
    39->3    5->43


  
    """
    print(msg)



def get_dice_value():
    time.sleep(WAIT)
    dice_value = random.randint(1, DICE_FACE)
    print("Its a " + str(dice_value))
    return dice_value


def got_snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
    print("\n" + player_name + " got a snake bite. Down from " + str(old_value)+ " to " + st>

def got_ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump).upper() + " ########")
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(c>


def snake_ladder(player_name, current_value, dice_value):
    time.sleep(WAIT)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying,OKAY >
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value



def check_win(player_name, position):
    time.sleep(WAIT)
    if MAX_VAL == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing the game.\n\n")
        sys.exit(1)



# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                 welcome_msg()
                 time.sleep(SLEEP_BETWEEN_ACTIONS)
                 player_name = nickname
                 time.sleep(SLEEP_BETWEEN_ACTIONS)
                 player_current_position = 0

                 while True:
                      time.sleep(WAIT)
                      input_1 = input("\n" + player1_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
                      print("\nRolling dice...")
                      dice_value = get_dice_value()
                      time.sleep(WAIT)
                      print(player_name + " moving....")
                      player_current_position = snake_ladder(player1_name, player1_current_position, dice_value)
                      _ = system('clear')
                      check_win(player1_name, player_current_position)


        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break


receive()

