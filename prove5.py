points = 0
print("You wake up inside a Rebel ship under attack by the Empire. You spot two items nearby: a LIGHTSABER and a BLASTER. Which one do you pick up?")
choice = input("Type LIGHTSABER or BLASTER: ").strip().lower()

if choice == "lightsaber":
    print("You ignite the lightsaber, its blue glow lights up the room. Stormtroopers are approaching. Do you want to ATTACK, HIDE, or TRY to ESCAPE?")
    action = input("Type ATTACK, HIDE, or ESCAPE: ").strip().lower()
    if action == "attack":
        print("You charge at the stormtroopers, deflecting their blaster fire and defeating them. You see an escape pod ahead. Do you BOARD it, LOOK for allies, or SEARCH the ship?")
        next_action = input("Type BOARD, LOOK, or SEARCH: ").strip().lower()
        if next_action == "board":
            print("You launch the escape pod and drift toward an unknown planet, beginning a new adventure.")
            points = 8
        elif next_action == "look":
            print("You find a group of Rebels and join their counterattack, turning the tide of battle!")
            points = 9
        elif next_action == "search":
            print("You search the ship and find a hidden Jedi Holocron, unlocking forgotten knowledge of the Force.")
            points = 10
        else:
            print("Invalid choice. The battle rages on, and you are captured by the Empire.")
            points = 2
    elif action == "hide":
        print("You hide behind a crate. A Rebel soldier signals you to follow. Do you FOLLOW, STAY hidden, or CREATE a diversion?")
        next_action = input("Type FOLLOW, STAY, or CREATE: ").strip().lower()
        if next_action == "follow":
            print("You join a squad and steal a shuttle, escaping just in time.")
            points = 7
        elif next_action == "stay":
            print("You remain hidden until the battle ends, only to be captured by bounty hunters.")
            points = 5
        elif next_action == "create":
            print("You throw a device to distract the troopers, then escape unnoticed!")
            points = 7
        else:
            print("Invalid choice. You hesitate too long and are taken prisoner.")
            points = 2
    elif action == "escape":
        print("You try to escape but are caught in a firefight. Do you FIGHT, SURRENDER, or NEGOTIATE?")
        next_action = input("Type FIGHT, SURRENDER, or NEGOTIATE: ").strip().lower()
        if next_action == "fight":
            print("You battle fiercely, but are ultimately overwhelmed and captured.")
            points = 6
        elif next_action == "surrender":
            print("You are taken prisoner but manage to escape later with the help of another captive.")
            points = 7
        elif next_action == "negotiate":
            print("You convince the enemy you are valuable, gaining a chance to turn the tables.")
            points = 7
        else:
            print("Invalid choice. The enemy captures you without resistance.")
            points = 2
    else:
        print("Invalid choice. The stormtroopers overwhelm you.")
        points = 1

elif choice == "blaster":
    print("You grab the blaster and take cover. The ship is shaking from enemy fire. Do you RETURN FIRE, RUN to the hangar, or SEEK cover?")
    action = input("Type RETURN FIRE, RUN, or SEEK: ").strip().lower()
    if action == "return fire":
        print("You provide cover for escaping Rebels. A pilot offers you a spot on his ship. Do you BOARD, KEEP fighting, or LOOK for another escape?")
        next_action = input("Type BOARD, KEEP, or LOOK: ").strip().lower()
        if next_action == "board":
            print("You take off, heading into hyperspace to safety.")
            points = 7
        elif next_action == "keep":
            print("You hold the line, helping the Rebels win an important victory.")
            points = 9
        elif next_action == "look":
            print("You find an alternative escape route and flee to safety.")
            points = 7
        else:
            print("Invalid choice. You are hit by enemy fire.")
            points = 1
    elif action == "run":
        print("You sprint towards the hangar and find an X-Wing. Do you PILOT it, LOOK for another ship, or WAIT for backup?")
        next_action = input("Type PILOT, LOOK, or WAIT: ").strip().lower()
        if next_action == "pilot":
            print("You engage in a space battle and escape just in time.")
            points = 7
        elif next_action == "look":
            print("You find an old freighter and escape with some fellow Rebels.")
            points = 8
        elif next_action == "wait":
            print("Backup arrives, and together, you launch a counterattack.")
            points = 8
        else:
            print("Invalid choice. The enemy forces overwhelm you.")
            points = 1
    elif action == "seek":
        print("You hide and plan your next move. Do you AMBUSH the troopers, SIGNAL for help, or STAY put?")
        next_action = input("Type AMBUSH, SIGNAL, or STAY: ").strip().lower()
        if next_action == "ambush":
            print("Your ambush is successful, and you take control of an enemy ship!")
            points = 8
        elif next_action == "signal":
            print("Help arrives just in time, and you are rescued.")
            points = 7
        elif next_action == "stay":
            print("You wait too long, and the enemy captures you.")
            points = 5
        else:
            print("Invalid choice. You are discovered and taken prisoner.")
            points = 2
    else:
        print("Invalid choice. You hesitate, and the battle is lost.")
        points = 1
else:
    print("Invalid choice. You must choose either LIGHTSABER or BLASTER.")
    points = 0

if points == 10:
    print(f"Well done you found the best path and scored a perfect 10 points")
elif points == 9:
    print(f"You survived and helped the rebel win the battle alliance scoring 9 points")
elif points == 8:
    print(f"You survived and helped the rebels scoring 8 points")
elif points == 7:
    print(f"You survived but didn't help the rebels as much as you could have scoring 7 points")
elif points == 6:
    print(f"You died bravely in battle scoring 6 points")
elif points == 5:
    print(f"You made a good run but died before you could escape scoring 5 points")
elif points == 2:
    print(f"You were doing great but hesitated and died scoring 2 points")
elif points == 1:
    print(f"You made a fatal mistake and died scoring 1 point")
elif points == 0:
    print(f"You couldn't make a choice and died before you could do anything scoring 0 points")
