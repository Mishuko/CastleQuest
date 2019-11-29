from sys import exit

print("What is your name?")
name = input(">>>")

def start():
    print("It's a dark and stormy day.")
    print("You come upon a large, abandoned castle.")
    print(f"Do you want to go in or stay outside, {name}?")

    while True:
        choice = input("> ")
        if choice == "go in":
            print("You open a small door and see \na staircase and another door.")
            print(f"{name}, do you choose to go through the door or up the staircase?")
            inside()
        elif choice == "stay outside":
            print("All right..")
            print("You're outside, and it's raining.")
            print("You see a small hut and a barn.")
            print("Where would you like to go?")
            outside()
        else:
            print("Try typing \'go in\', or \'stay outside\'.")

def inside():
    while True:
        choice = input("> ")
        if choice == "up the staircase":
            staircase()
        elif choice == "go through the door":
            door_two()
        else:
            print("Try typing \'up the staircase\', or \'go through the door\'.")

def staircase():
    print("You go up to the staircase only to find an angry witch..")
    print(f"So, {name} what will you do? Do you punch her, take her wand away, or flee?")

    while True:
        choice = input("> ")
        if choice == "punch her":
            dead("The witch got more angry and knocked you out.")
        elif choice == "take her wand away":
            print("You change her into a frog. Nice job!")
            print("Now, you enter a small room.")
            door_two()
        elif choice == "flee":
            print("You run down the staircase \nto where you were before \nlike a little girl.")
            print(f"Oh, by the way {name} You can go up the staircase AGAIN or go through the door.")
            entrance()
        else:
            print("Try typing \'punch her\', \'take her wand away\', or \'flee\'.")

def entrance():
    while True:
        choice = (input("> "))
        if choice == "go up the staircase":
            dead("The witch was prepared this time and smacked you with the wand.")
        elif choice == "go through the door":
            print("Now, you're in a small room.")
            door_two()
        else:
            print("I'm not sure I understand.")
            print("Try typing \'go through the door\' or \'go up the staircase.\'")

def door_two():
    print("Uhh.. I think there is a goblin in here")
    print("Will you run past him, throw a pebble, or ask him kindly to let you through?")

    while True:
        choice = input("> ")
        if choice == "run past him":
            print("You fly past him while the goblin feeds on rotten meat.")
            print("He doesn't seem to notice you.")
            hallway()
        elif choice == "throw a pebble":
            print("You find a rock and throw it only to have it bouce back at you.")
            print("As you try to hide in your corner, the greenish goblin scampers to your side..")
            print("The goblin knocks you out and locks you in his feeding chamber.")
            dead(f"{name} you are ABOLUTELY TERRIBLE at throwing!")
        elif choice == "ask him kindly to let me through":
            print("You approach the goblin shaking in your boots.")
            print("\"Hello green goblin! Would you please let me throu...\"")
            print("Are you serious? What in the world were you thinking?")
            dead(f"I really expected better from you {name}... Give the next person a shot at the game.\nYou disgrace me.")
        else:
            print("Try typing something I can understand. \n\'run past him\', \'throw a pebble\',\'ask him kindly to let me through\'")

def hallway():
    print("You take a breather.. ")
    print("In front of you is a looong hallway.")
    print("The silent hallway mystifies you. You notice that there is a single door on the right and left of the hallway and a window to the left.")
    print("Do you want to go to the end, go back, take a right, or jump out the window?")


    while True:
        choice = input("> ")
        if choice == "go to the end":
            print("You cautiously walk to the end of the eirie hallway.")
            print("It seems so quiet that you can here your on heartbeat...")
            print("Each step you take appears to grow louder and louder.")
            print("You plunge into a world of oblivion.")
            dead(f"I think you lost your mind {name}.")
        elif choice == "go back":
            print("You just ran away from a goblin, and now, you want to go back?")
            print("Alright..")
            print("As you brazenly walk back toward the goblin, the goblin sees you and snatches you by the arm.")
            print("You try to escape, but his grip is ten times stronger than yours.")
            print("Before you know it, the four-foot goblin drags you down the stairs \nand locks you up in a dark dungeon cell.")
            dead(f"Well that was a foolish decision {name}.")
        elif choice == "take a right":
            print("Good choice! Now, you are now in a spacious room with a 10 foot giant stairing you in the eyes.")
            print("Do you have what it takes to not lose?")
            giant()
        elif choice == "jump out the window":
            print("You're too afraid of choosing the other choices, so you walk to the the window sill and yank the window open.")
            print("You jump off and sail gracefully through the air reaching incredible freefall speeds.")
            dead(f"You broke both of your legs. {name}Try not jumping out of the window next time.")
        else:
            print("Try typing something I can understand. \n\'go to the end\', \'go back\',\'jump out the window\'")

def giant():
    print("The giant faces you with a hungry grin on his face..")
    print(f"What do you do {name}?")
    print("Do you want to run through the giant's legs, tell him to move out of the way, \nor force him out of the way youself?")

    while True:
        choice = input("> ")
        if choice == "run through the giant's legs":
            print(f"You muster all your strength and dart staight between his legs! You survived! I guess your better than I thought, {name}.")
            print("Giants aren't that mobile. Good call!")
            throne_room()
        elif choice == "tell him to move out of the way":
            print("He smashes you with his enormous fist.. Ouch!")
            dead("Giants don't like to be bossed. Who ever thought of nice giants??")
        elif choice == "force him out of the way yourself":
            print("You walk up to the menacing giant and push with all your might.")
            print("Unfortunately, you aren't quite strong enough to push the giant aside.")
            print("I mean come on.. What did you excpect?")
            dead(f"Nice try though {name}..")
        else:
            print("Try typing something I can understand. \n\'run through the giant's legs\', \'tell him to move out of the way\',\'force him out of the way yourself\'")

def throne_room():
    print("You close and lock the door behind you immidiately after you enter the next room.")
    print("You lool around.. Wow!, this is amazing!")
    print("It looks like you're in the throne room!!")
    print("The faded red carpet and great stone thrown stands right in front of you.")
    print("Great tll windows line the walls of the absolutely magnificent room.")
    print("This is incredible! Maybe you'll find the the coveted crown people you came here for!")
    print("You notice a a crown hanging on the endge of the great throne.. Can this really be?")
    print("Do you run toward the throne or walk toward the throne?")

    while True:
        choice = input("> ")
        if choice == "run toward the throne":
            print("As you run, you notice the ground start to shake.")
            print("You immidiately pick up the pace and run straight toward the throne.")
            print("Blocks of cobblestone fall just inches from your feet.")
            print("You make it to the throne in a nick of time! The rubbling stops.")
            print("As you turn around, you notice a MASSIVE ravine that goes from the door you eneterd up to the foot of throne.")
            print("You take a minute to calm down..")
            print("You decide to sit down in the throne for a bit to recover you thoughts..")
            print("but are suddenly and startled by a raquet at the door.")
            print("Stairing intently at the trapdoor on the ground to the right, you notice something.")
            print("You heart starts to pound.. From out the trapdoor comes a seemingly translucent.... SPIRTIT!!!")
            print("He tells you in a grave voice, \"I am the proter of the thrown! WHO dares enter?!\"")
            print("\"Let it be known it is his final moment!\"")
            print("Your not sure what to do.. try doing at least SOMETHING!")
            spirit()
        if choice == "walk toward the throne":
            print("You walk toward the throne with a big grin on your face!")
            print("Excited though you may be, you are not aware that SOMETHING seems off.")
            print("The ground begins to shake beneath you, cobblestone blocks fall from beneath your feet..")
            print("Freefall.........................")
            dead(f"Ouch! Sinkhole? IDK, what do you think, {name}?")
        else:
            print("This is the last help you get. \'run toward the throne\', \'walk toward the throne\'  Enjoy!")

def spirit():
    while True:
        choice = input("> ")
        if choice == "run":
            print(f"Okay, let's think through this logically. Ok, {name}?")
            print("Your in the throne room and you're trying to run from a spirit.")
            print("I mean can't spririts go through walls?")
            dead("Logic is the anatomy of thought. ~ John Locke")
        elif choice == "fight":
            print("Come on.. You can\'t be serious.. Are you? A little common sense and you\'ll understand that you CAN\'T punch a spirit!")
            dead("At least you tried.")
        elif choice == "hide":
            print("You quickly hop off the throne and find a little nook under it.")
            print("You sit there in complete silence, but you can feel your heart beating out of your chest.")
            print("The spirit glides around the room.")
            print("Then, in frustration, he lets out a scream that seems to destroy your eardrums.")
            print("Total silence follows..")
            print("It looks like the spirit is gone, but you went deaf! Congratulations on surviving!")
            crown()
        elif choice == "go up to him":
            print("You approach the spririt. He says, \"Woe to you, son of Adam! How dare you enter my real!\"")
            print("You say,\"Uhh.. I was just kind of cold, so I walked into the castle.\"")
            print("The spririt replies, \"You foolish son of Adam! What is your name?\"")
            print(f"\"My name is {name}.\"")
            print(f"\"Welcome to my realm, {name} follow me. A righteous human like you deserves only the best riches.\"")
            print(f"Wow! You actually beat the game {name}! You have achieved the ending of \"Spirit Friend\".")
            exit(0)
        elif choice == "go to him":
            print("You approach the spririt. He says, \"Woe to you, son of Adam! How dare you enter my real!\"")
            print("You say,\"Uhh.. I was just kind of cold, so I walked into the castle.\"")
            print("The spririt replies, \"You foolish son of Adam! What is your name?\"")
            print(f"\"My name is {name}.\"")
            print(f"\"Welcome to my realm, {name} follow me. A righteous human like you deserves only the best riches.\"")
            print(f"Wow! You actually beat the game {name}! You have achieved the ending of \"Spirit Friend\".")
            exit(0)
        elif choice == "walk toward him":
            print("You approach the spririt. He says, \"Woe to you, son of Adam! How dare you enter my real!\"")
            print("You say,\"Uhh.. I was just kind of cold, so I walked into the castle.\"")
            print("The spririt replies, \"You foolish son of Adam! What is your name?\"")
            print(f"\"My name is {name}.\"")
            print(f"\"Welcome to my realm, {name} follow me. A righteous human like you deserves only the best riches.\"")
            print(f"Wow! You actually beat the game {name}! You have achieved the ending of \"Spirit Friend\".")
            exit(0)
        elif choice == "compliment him":
            print("You tell the spirit, \"What beautiful, transparent spirite you are!\"")
            print("He replies, \"Oh really (:! Well thank you!\"")
            print("\"You are a beautiful son of Adam! Spirit Protector of the Crown atyour service!\"")
            print("\"How might I address you?\"")
            address = input("> ")
            print(f"\"{address} at you service!\"")
            print(f"\"What can I do for you {address}?\"")
            print("\"Leave me to myself for a few moments if you would. I must recollect my thoughts..\"")
            print(f"As you say {address}.")
            print("The spirit returns the way he came.")
            crown()
        elif choice == "make fun of him":
            print("You face the spririt face to face. \"Hey spirit! I bet you can't do this!\" You take an apple and take a big bite.")
            print("\"Trickery of the sons of Adam! What foolishness! Give me that \'apple\' of yours.\"")
            print("He holds his extremity out, but the apple falls stright through! \"No, no, no, no! I have wandered this castle for ages, \nyet I cannot even eat an apple! Ohh, pity on me!!\"")
            print("\"What purpose do I hold?\"")
            print("Suddenly, the spririt disappears in an instant before your very eys.")
            crown()
        elif choice == "cry":
            print("You sit there and cry like a baby.")
            print("\"Oh my, what is it, son of Adam?\"")
            print("\"A genie plays is trying to kill me!\" you reply.")
            print("\"A genie?\" replies the spirit. \"This is unacceptable! Follow me. I'll protect you from evil blure genie.\" ")
            print(f"Your smart decision making has payed off! You have aquired the ending \"Cry Baby\" Nice job {name}.")
        elif choice == "play dumb":
            print("You play dumb.. ")
            print("The spirit yells, \"A human making a mockery of my realm? \nWhat is this stupidity? \nYou have disgraced me and my realm!\"")
            print("\"Now, you must pay dearly!\"")
            dead("The spirit returns your mind to that of your three-year-old former self.")
        elif choice == "use the wand":
            print("Smugadydugadyboop!")
            print("I don't think anything happened..")
            print("\"You fool! You will pay dearly for your smugadydugabe.....\"")
            print("\'Blah! Enough! If you cannot act normally, what right do you have to live!\'")
            dead("The spirit took your soul..")
        elif choice == "wand":
            print("Smugadydugadyboop!")
            print("I don't think anything happened..")
            print("\"You fool! You will pay dearly for your smugadydugabe.....\"")
            print("\'Blah! Enough! If you cannot act normally, what right do you have to live!\'")
            dead("The spirit took your soul..")
        elif choice == "use wand":
            print("Smugadydugadyboop!")
            print("I don't think anything happened..")
            print("\"You fool! You will pay dearly for your smugadydugabe.....\"")
            print("\'Blah! Enough! If you cannot act normally, what right do you have to live!\'")
            dead("The spirit took your soul..")
        elif choice == "turn him into a frog":
            print("Smugadydugadyboop!")
            print("I don't think anything happened..")
            print("\"You fool! You will pay dearly for your smugadydugabe.....\"")
            print("\'Blah! Enough! If you cannot act normally, what right do you have to live!\'")
            dead("The spirit took your soul..")
        else:
            print("Fine, I'll be nice. Try typing \'run\', \'fight\', \'hide\' \n \'go up to him\', \'go to him\', \'walk toward him\', \'compliment him\', \'make fun of him\', \'cry\',\n \'play dumb\', \'use the wand\', \'wand\',\n \'use wand\', \'turn him into a frog\'.")

def crown():
    print("You turn around and gaze upon the magnificent crown hanging from the corner of the thone!")
    print("\"YESS!\" you shout.")
    print(f"{name}, you are abolutely amazing!")
    print("All the obstacles and you have finally..")
    dead("Your shout seemed to have caused an an echo that lodged a brick from off the ceiling. You were so close!!")



def outside():

    while True:
        choice = input("> ")
        if choice == "small hut":
            print("You hurry toward the small hut.")
            print("No lights glow. It seems abandoned. There appears to be no door.")
            print("The gnarled wood floor suggests this place was abandoned a long time ago.")
            print("Inside, you see a couple of wooden boards fashioned into a bed.")
            print("To the left, a stack of rotten boards lines the wall.")
            print("You use the boards to block off the entrance and to protect yourself from the cold.")
            print("You decide to spend the night in the small hut.")
            morning()
        elif choice == "barn":
            print("You scamper off to the barn.")
            print("The stench of animal maneur permeates your clothes.")
            print("Despite this bad condition, you determine it is the best option.")
            print("You find your way up to the loft and and make yourself comfortable. It would be best if you spent the nigt.")
            print("Zzzzz, zzzzzz, zzzzzzz, THUMP! CRASH!")
            dead(f"You decided to sleep walk and fell off the loft... Unfortunate {name}.")
        else:
            print("You can only use \'barn\' or \'small hut\'.")


def morning():
    print("You wake up feeling refreshed.")
    print("The sun with its golden rays beams through the window.")
    print("What would you like to do today?")
    print("You can stay or explore.")

    while True:
        choice = input("> ")
        if choice == "stay":
            print("You enjoy your time in the small hut. The birds chirp, everything seems just beatiful!")
            print("Suddenly, you here someone knocking down the boards you placed at the entrance of the house!")
            print("\"NO!!\"you scream.")
            print("An angry witch walks into the room. Her green face and evil eyes seem to pierce your very soul.")
            dead("You don't stand a chance against her. She grabs her staff and smacks you on the head forcing you to kneel. She then wacks your head, making you unconscious.")
        if choice == "explore":
            print("\"Ahh, exploring is wonderful!\"you say.")
            print("You walk around enjoying the nature.")
            print("In order to get a better view, you climb a small hillock.")
            print("A small distance away, a coniferous forest lines your view.")
            print("In the opposite, the castle with its spires appears so beautiful")
            print("You also notice some sort of a secret passage carved into the mountain.")
            explore()
        else:
            print("Try typing \'stay\', or \'explore\'.")

def explore():
    print("Hmm.. What should I do? The forest looks so enchanting, but the at same time the passage is very intriguing!")

    while True:
        choice = (input("> "))
        if choice == "go to the forest":
            print("You walk liesurely toward the big forest.")
            print("After a half hour of walking, you enter into the seeminly enchanted forest.")
            print("The huge tress, litteredp pine needles, chirping birds, and smell of wood enraptures you.")
            print("\"Ahh!\" you say. \"I could live here forever!\"")
            print("You spend your hours enjoying the beauitful forest.")
            print("Time seems to fly, and you don't even notice that the sun is already setting.")
            print("You quickly come to your senses and head back in a quick pace.")
            print("Darkness falls upon you, and yet you appear to be in the same place you started..")
            dead("You got lost in Enchanted Wood.")
        if choice == "explore the secret passage":
            print("You walk down toward the side of the hillock and notice a small enrtrance running through the hillock.")
            print("It seems to head in the direction of the castle.")
            print("You open the small, simple wooden door with a slight push and notice laterns aling the walls of the passage.")
            print("\"Someone must have been here.\" you say to yourself.")
            print("Your curiosity drives you to walk down the long passage.")
            print("Left turn, then right, left, left, right..")
            print("Just around the corner, you notice something that puts you in shock...")
            print("There appears to be a zombie in the passage!?")
            print("You prepare to run away, but you notice another zombie behind you aways.")
            print("He hasn't noticed you, but blocks your path to flee..")
            print("The zombie in front of you has takes notice of you.")
            print("You need to fight. There is no way out. Make a wise decison.")
            zombie()
        else:
            print("Try typing \'go to the forest\', or \'explore the secret passage\'.")

def zombie():
    print("Do you roundhouse kick, trip, or run past the zombie?")
    while True:
        choice = input("> ")
        if choice == "roundhouse kick the zombie":
            print("You attempt to roundhouse kick the zombie in the face, but your tremendous skill in roundhouse kicking lands you on your face.")
            print("The zombie takes a bite out of your leg before you could get bacl up.")
            dead("You go infected by the zombie.")
        if choice == "trip the zombie":
            print("You ran toward the zombie, duck, and trip the zombie with your foot before he could snatch a bite out of you.")
            print("With the zombie sprawled on the floor, you run as fast as you can to the end of the secret passage.")
            print("You see a door! With feet flying, you open the door without hesitation.")
            print("In front of you is a staircase with two four flights of stairs.")
            print("Without any other options, you climb up the stairs.")
            print("Slowly, you open the door. The creaking door startles you, but after opening it all the way, you see a hallway.")
            hallway()
        if choice == "run past the zombie":
            print("You attmept to run straight past the zombie.")
            print("Without much hesitation, you gather speed and..")
            dead("You get knocked by the zombie. You quickly get up, but the fast moving zombie has you in his grip. You can't escape now..")
        else:
            print("Try typing \'roundhouse kick the zombie\', \'trip the zombie\', or \'run past the zombie\'.")


def dead(why):
    print(why, "You lost.")
    exit(0)

start()
