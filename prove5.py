print("You wake up inside a Rebel ship under attack by the Empire. You spot two items nearby: a LIGHTSABER and a BLASTER. Which one do you pick up?")
choice = input("Type LIGHTSABER or BLASTER: ").strip().lower()

if choice == "lightsaber":
    print("You ignite the lightsaber, its blue glow illuminating the room. Stormtroopers are approaching. Do you want to ATTACK or HIDE?")
    action = input("Type ATTACK or HIDE: ").strip().lower()
    if action == "attack":
        print("You charge at the stormtroopers, deflecting their blaster fire and defeating them. You see an escape pod ahead. Do you want to BOARD it or LOOK for allies?")
        next_action = input("Type BOARD or LOOK: ").strip().lower()
        if next_action == "board":
            print("You launch the escape pod and drift toward an unknown planet. You spot a Jedi Temple. Do you EXPLORE or SIGNAL for help?")
        elif next_action == "look":
            print("You find a group of Rebels planning a counterattack. Do you JOIN them or try to ESCAPE on your own?")
        else:
            print("Invalid choice. You must choose either BOARD or LOOK.")
    elif action == "hide":
        print("You hide behind a crate, waiting for the right moment. A Rebel soldier signals you to follow him. Do you FOLLOW him or STAY hidden?")
        next_action = input("Type FOLLOW or STAY: ").strip().lower()
        if next_action == "follow":
            print("You join a small squad heading for the hangar. They plan to steal a shuttle. Do you PILOT the shuttle or MAN the guns?")
        elif next_action == "stay":
            print("You remain hidden until the battle subsides. Eventually, a bounty hunter finds you. Do you SURRENDER or FIGHT?")
        else:
            print("Invalid choice. You must choose either FOLLOW or STAY.")
    else:
        print("Invalid choice. You must choose either ATTACK or HIDE.")

elif choice == "blaster":
    print("You grab the blaster and take cover. The ship is shaking from enemy fire. Do you want to RETURN FIRE or RUN to the hangar?")
    action = input("Type RETURN FIRE or RUN: ").strip().lower()
    if action == "return fire":
        print("You fire at the stormtroopers, providing cover for escaping Rebels. A pilot offers you a spot on his ship. Do you BOARD or KEEP fighting?")
        next_action = input("Type BOARD or KEEP: ").strip().lower()
        if next_action == "board":
            print("You take off and head for hyperspace. Do you go to a REBEL base or seek out a SMUGGLER safehouse?")
        elif next_action == "keep":
            print("You hold the line, allowing more Rebels to escape. Eventually, reinforcements arrive. Do you STAY and help or EVACUATE?")
        else:
            print("Invalid choice. You must choose either BOARD or KEEP.")
    elif action == "run":
        print("You sprint towards the hangar and find an X-Wing. Do you PILOT the X-Wing or LOOK for another ship?")
        next_action = input("Type PILOT or LOOK: ").strip().lower()
        if next_action == "pilot":
            print("You engage in a space battle against TIE fighters. Do you ATTACK aggressively or EVADE?")
        elif next_action == "look":
            print("You find an old YT-1300 freighter. Do you REPAIR it or WAIT for allies?")
        else:
            print("Invalid choice. You must choose either PILOT or LOOK.")
    else:
        print("Invalid choice. You must choose either RETURN FIRE or RUN.")

else:
    print("Invalid choice. You must choose either LIGHTSABER or BLASTER.")