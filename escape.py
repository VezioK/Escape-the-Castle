import random

def Escape_From_The_Castle():
    print("The cold stone beneath your body sends chills through your spine. You blink. The air smells of mildew, rot, and old metal.\nMoonlight spills weakly through a barred slit high on the wall. You're in a dungeon. A castle, you think—but not one from any map you know.\nChains hang unused on the wall. There's a cracked bowl of water in the corner and a flickering torchlight beyond the door’s peephole.\nYou vaguely remember an ambush on the road… cloaked figures… then blackness.\nYou're alone now—but you won’t be for long.\n")
    print("You take stock of your surroundings:\nA loose stone in the wall near the floor, just big enough to wedge a hand into.\nA heavy iron door, locked, but with rusted hinges.\nA narrow window slit, barred but reachable if you climb the wall using cracks and an old shelf.")

    while True:
        start = input("What do you do?\n[A] Check the loose stone.\n[B] Bang on the door to attract someone.").lower()
        if start == 'a':
            situation_A()
            #complete
            break
        elif start == 'b':
            situation_B()
            #complete
            break
        else:
            print("Invalid choice. Please try again.")


def situation_A():
    print("You kneel beside the stone, your fingers numb from the cold floor. With effort, you pry the rock loose—revealing a dark crawl space behind it.\nThe air that wafts from it smells old… but fresh enough to suggest movement.You listen. Faint wind. Maybe even... water?\nIt could be a way out—or a trap.")
    while True:
        A_choice = input("What do you do?\n[A] Crawl into the tunnel.\n[B] Leave it be and look elsewhere.").lower()
        if A_choice == 'a': 
            situation_A1()
            break
        elif A_choice == 'b':
            situation_A2()
            break
        else:
            print("Invalid choice. Please try again.")

def situation_A1():
    print('You squeeze in. The tunnel is narrow, carved by time or prisoners past. You can barely breathe. You feel rats scurry over your legs.\nEventually, it splits:On the left, the stone is damp, the air thick with mildew.On the right, a breeze whispers through, faint and cold.')
    while True:
        A1_choice = input("What do you do?\n[A] Go left—maybe there's water and an underground stream?\n[B] Go right—the breeze suggests a way out.").lower()
        if A1_choice == 'a':
            print('You crawl slowly, the air growing heavier with every inch. Eventually, the tunnel widens—only to open suddenly into a pit.\nThe floor crumbles under your weight.You fall and as you do, you see impending doom below you as your eyes meet the spike trap set there for escapees.\nYou die.')
            #death, add option to restart or redo choice
            break
        elif A1_choice == 'b':
            situation_A1_2()
            break
        else:
            print("Invalid choice. Please try again.")

def situation_A1_2():
    print("You follow the current of air, scraping your knees raw. At last, you find a loose grate. You listen—no voices.\nYou kick it out.You drop into... a castle kitchen. It's dimly lit, cluttered with pots and cauldrons. You hear faint music above—maybe a feast?")
    while True:
        A1_2_choice = input("There are three ways out:\n[A] A side servant’s door cracked open, leading to a dark hallway.\n[B] A large pantry where you could hide.\n[C] A dumbwaiter, big enough to climb into—it might lead upstairs.\nWhich do you choose?").lower()
        if A1_2_choice == 'a':
            situation_A1_2_1()
            break
        elif A1_2_choice == 'b':
            print('You squeeze behind sacks of grain and wait. Hours pass. Your eyes droop. The door bursts open. A cook screams. Within seconds, guards are on you and you are caught.\nSecurity increases after your attempt and you spend the rest of your days in a cell.')
            #capture, add option to restart or redo choice
            break
        elif A1_2_choice == 'c':
            situation_A1_2_3()
            break
        else:
            print("Invalid choice. Please try again.")

def situation_A1_2_1():
    print("You move silently down the hall. You hear muffled laughter and music from the main dining room. The hallway forks—one stairway goes up, the other down.\nYou spot a few empty barrels stacked near the stairs. You're exposed out here.")
    while True:
        A1_2_1_choice = input("Do you:\n[A] Go upstairs toward the noble quarters.\n[B] Go downstairs—maybe the stables or dungeon.\n[C] Hide in a barrel near the stairs.").lower()
        if A1_2_1_choice == 'a':
            situation_A1_2_1_1()
            break
        if A1_2_1_choice == 'b':
            situation_A1_2_1_2()
            break
        if A1_2_1_choice == 'c':
            situation_A1_2_1_3()
            break
        else:
            print("Invalid choice. Please try again.")

def situation_A1_2_1_1():
    print("You creep up the stairs, each step creaking underfoot. You reach a long hallway lined with velvet carpets and grim portraits.\nYou’re halfway across when a door opens.A nobleman steps out, surprised.")
    while True:
        A1_2_1_1_choice = input("Before he speaks, you:\n[A] Knock them out and steal their robes.\n[B] Run down the hall and hope for the best.").lower()
        if A1_2_1_1_choice == 'a':
            print("In the process of putting on the nobles clothes, the other nobles heard the commotion and caught you in the act.\nYour are put back in your cell and live the rest of your days there")
            break
            #end
        elif A1_2_1_1_choice == 'b':
            print("You sprint, breath ragged. Behind you, the noble shouts for guards.You take a wrong turn and run straight into a knight.\nSteel and pain are the last things you feel before being executed for attacking a noble.")
            break
            #end
        else:
            print("Invalid choice. Please try again.")

def situation_A1_2_1_2():
    print("You descend into the lower levels—colder, damper. You find yourself in the stables. Horses whinny as you slip past. A stablehand looks up, startled. 'Hey! You ain't supposed to—'")
    while True:
        A1_2_1_2_choice = input('Do you:\n[A] Knock him out and take a horse.\n[B] Convince him you’re a new servant.').lower()
        if A1_2_1_2_choice == 'a':
            print('You lunge at him. He shouts, but you silence him with a blow. You mount a horse and kick off into the forest before the alarm rings, making it to safety')
            break
            #end
        elif A1_2_1_2_choice == 'b':
            print("You stammer something about kitchen duty. He narrows his eyes…")
            num = random.randint(0,10)
            if num <=5:
                print("He doesnt believe you and calls for gaurds. Your escape is cut short")
                break
            else:
                print("The stablehand is convinced and leaves you be. You steal a horse and make it to safety")
            #end
        else:
            print("Invalid choice. Please try again.")

def situation_A1_2_1_3():
    print("You squeeze into the barrel, holding your breath. Minutes pass. Footsteps come close—then a grunt. Rough hands roll your barrel down a hall.\nIt bumps and crashes.They toss it onto a cart. You faintly make out the what the guards are saying are hear the word 'gift', refering to the barrels.\nFeeling relief you settle in and the ride lasts for hours. Finally, the barrel breaks opens...")
    num = random.randint(0,10)
    if num >=7:
        print("Lucky you, your barrel was a gift to a neighboring town. Once the coast is clear you hop out the barrel, finally free")
    else:
        print("It turns out you were a gift to a nation ran by demons. Visibly angry, the demons murder you and wage war for such a rude gift. \nDie knowing your captors didnt win the war.")
    #end

def situation_A1_2_3():
    print("You climb into the dumbwaiter and pull the rope. It creaks and strains under your weight—but it lifts. You arrive in a dim study room.\nBooks and maps line the walls. There’s a narrow window, a trapdoor in the floor, and a writing desk with a flickering lantern.")
    while True:
        A1_2_3_choice = input("You're left with 3 options:\n[A] Climb out the window—it leads to a sloped rooftop.\n[B] Search the desk for useful items.\n[C] Try the trapdoor—where does it go?").lower()
        if A1_2_3_choice == 'a':
            print("You open the window carefully and step onto the steep tile roof. The wind bites. You balance across the slope, moving toward the outer wall.\nGuards spot you.Arrows whistle past as you leap for a vine-covered tower.")
            num = random.randint(0,10)
            if num >= 6:
                print("You barely make it. You climb down, scrape your knees, and vanish into the forest.")
            else:
                print("One of the arrows hit you straight through the chest ending your life")
            #end
            break
        if A1_2_3_choice == 'b':
            situation_A1_2_3_2()
            break
        if A1_2_3_choice == 'c':
            print("You pry open the trapdoor. It leads to a hidden shaft and a ladder going down into darkness.You descend.\nAt the bottom: a dusty armory. Old armor, swords, even a forgotten crossbow.\nYou arm yourself.You’re not escaping. You’re fighting your way out.")
            #end
            break
        else:
            print("Invalid choice. Please try again.")

def situation_A1_2_3_2():
    print("You dig through parchment and trinkets. You find a map of the castle—escape routes marked in red—and a small key labeled 'Gate'.\nSuddenly, voices approach.You pocket the items and sneak back into the dumbwaiter, praying they didn’t hear.")
    while True:
        A1_2_3_2_choice = input("Do you:\n[A] Ride it back down to the kitchen.\n[B]Climb up higher to see where it goes.").lower()
        if A1_2_3_2_choice == 'a':
            print("You return to the kitchen, now armed with the key and knowledge. You exit through the servant’s hall, find the side gate, and slip into the night.")
            #end
            break
        elif A1_2_3_2_choice == 'b':
            print("The dumbwaiter groans as it lifts you higher. It stops in a royal bedroom. You step out—only to see a queenly figure scream.\nSeconds later, guards flood in and you are killed for 'attempting to assisinate the queen'")
            #end
            break
        else:
            print("Invalid choice. Please try again.")

def situation_A2():
    print("You decide the tunnel might be too risky. Who knows how deep it goes—or if you’d ever come back. You rise and look around again.\nThe dungeon offers few options, but hesitation isn’t safety.You now turn to the next best options...")
    while True:
        A2_choice = input("Do you:\n[A] Try the heavy iron door—it’s rusted, maybe you can force it open?\n[B] Climb up to the narrow window slit using cracks and the shelf.\n[C] Sit back and wait—maybe someone will come.").lower()
        if A2_choice == 'a':
            situation_A2_1()
            break
        elif A2_choice == 'b':
            situation_A2_2()
            break
        elif A2_choice == 'c':
            print("You sit back against the wall. Time creeps by. Eventually, the sound of keysThe door opens. A tall man in crimson robes enters, flanked by two armored guards.\n“Ah,” he murmurs, “the vessel is awake.”You scream—but it's too late. The kingdom uses you for ritual sacrifice")
            break
            #end
        else:
            print("Invalid choice. Please try again.")

def situation_A2_1():
    print("You brace your shoulder against the rusted iron door. It creaks and groans but holds fast. You grab a loose stone and smash it against the bottom hinge.\nClang.Clang.Crack.It breaks.You squeeze through the narrow opening into a dim hallway. Torches flicker on the walls. \nAt one end, you hear slow footsteps approaching. At the other is a winding spiral staircase, disappearing upward.")
    while True:
        A2_1_choice = input("What do you do next?\n[A] Run up the spiral stairs.\n[B] Wait and ambush the person approaching.\n[C] Panic and slip back into the cell.").lower()
        if A2_1_choice == 'a':
            print("You rush up the steps two at a time, heart pounding.They spiral tightly, disorienting you. You reach a wooden door and push it open.\nLight floods in. You're in a courtyard. A guard dog growls.Before you can react, you’re tackled.\n")
            num = random.randint(0,10)
            if num >= 4:
                print("You are severely overpowered and are taken back to your cell")
            else:
                print("You kick and punch with all the strength you have left and manage to incapacitate the guard. You run as fast as you can and make it to the woods surronding the castle.\nYou are never caught")
                break
            #end
        elif A2_1_choice == 'b':
            print("You hide behind the door, stone in hand. A shadow passes...WHAM!The figure crumples—just a servant, not a guard.\nYou drag their body into your cell and take their clothes.Now disguised, you calmly ascend the stairs and blend in with the staff.\n Weeks go by and no one questions your prescence. The real staff's body is discovered and thrown out with no second thought This is your life now.")
            break
            #end
        elif A2_1_choice == 'c':
            print("You retreat to your cell, hoping the noise went unnoticed. Upon reaching your cell you realize its no longer empty and are met with a pair of glowing eyes watching you from the darkness.\nYou never get the chance to scream.")
            break
            #end
        else:
            print("Invalid choice. Please try again.")

def situation_A2_2():
    print("You haul the old shelf under the wall and begin to climb. The cracked stones give just enough hold. You reach the window—it’s narrow and barred.\nA weird vial fell out the shelf while you were moving it and you decide to pick it up before pressing your face through\nYou see moonlight, a courtyard, guards pacing.Then—Voices. Footsteps. They're coming to your cell.")
    while True:
        A2_2_choice = input("Do you:\n[A] Try squeezing through the bars, even if it hurts.\n[B] Climb down fast and hide before they enter.").lower()
        if A2_2_choice == 'a':
            situation_A2_2_1()
            break
        elif A2_2_choice == 'b':
            print("You try to climb down quickly—but your foot slips. You hit the floor just as the door bursts open.A guard spots you instantly.\nYou’re back to your cell screaming.")
            break
            #end
        else:
            print("Invalid choice. Please try again.")   

def situation_A2_2_1():
    print("You force yourself through the gap. The stone rips your clothes, cuts your skin—But you make it through.\nWith the guards now in the room, grappling at your feet to pull you back in, you make a hasty move and jump out the window, misjudging the fall.\nMost of your bones are broken and you're stuck on the floor dying slowly. In a last ditch effort you drink the vial you picked up.")
    num = random.randint(0,6)
    if num !=6:
        print('The vial is filled with water so at least you dont die thirsty')
    else:
        print("The vial was an experimental healing serum and it works. Your body is restored and you run to your freedom.")
    #end

def situation_B():
    print("You slam your fists on the heavy iron door, desperate for a reaction.\nAfter a tense pause, a sliding peephole creaks open. A bored guard’s eyes narrow at you. 'You wanna get flogged? Keep yelling.'\nYou don't stop. Your voice echoes through the stone.\nMoments later, you hear keys rattling… then the door creaks open. The guard steps in alone, holding a lantern and a short sword.")
    while True:
        B_choice = input("What do you do next?\n[A] Fake an injury to lure him closer.\n[B] Rush him while the door is open.").lower()
        if B_choice == 'a':
            situation_B1()
            break
        elif B_choice == 'b':
            situation_B2()
            break
        else:
            print("Invalid choice. Please try again.")

def situation_B1():
    print("You collapse dramatically, groaning in pain. “Please… help…” The guard hesitates, then takes a few steps closer, wary but intrigued.")
    while True:
        B1_choice = input("What do you do next?\n[A] Grab the lantern and attack.\n[B] Trip him and lock the door behind you.").lower()
        if B1_choice == 'a':
            situation_B1_1()
            break
        elif B1_choice == 'b':
            situation_B1_2()
            break
        else:
            print("Invalid choice. Please try again.")

def situation_B1_1():
    print("You spring up, snatching the lantern and smashing it into his face. He stumbles back screaming, flames licking his cloak.\nYou take his sword and bolt into the corridor. The fire has spread to old hay and dry wood nearby.")
    while True:
        B1_1_choice = input("What do you do next?\n[A] Use the fire as cover to escape left toward the commotion.\n[B] Ignore the chaos and go right, into darkness and silence.").lower()
        if B1_1_choice == 'a':
            situation_B1_1_1()
            break
        elif B1_1_choice == 'b':
            situation_B1_1_2()
            break
        else:
            print("Invalid choice. Please try again.")

def situation_B1_1_1():
    print("You escape into the chaos caused by the spreading fire. Guards shout and servants flee as thick smoke fills the air.\nYou duck low, choking on the fumes, and make it through a side gate into the outer courtyard.Ahead, the castle perimeter is faintly visible in the haze.\nYou’ve made it out of the dungeon—but not out of danger.")
    while True:
        B1_1_1_choice = input("What do you do next?\n[A] Run straight for the outer wall, hoping to scale it before you’re seen.\n[B] Hide behind a statue and wait for the commotion to die down.\n[C] Attempt to grab a crossbow from a burning guard tower to defend yourself.").lower()
        if B1_1_1_choice == 'a':
            print("You sprint through the smoke, zig-zagging across the open courtyard. A few guards spot you—but you're already halfway up a vine-covered section of wall.\nArrows whizz past as you scramble over and drop into a muddy trench outside.You don’t stop running until the castle is a silhouette behind you.")
            #end
            break
        elif B1_1_1_choice == 'b':
            print("You crouch behind a marble knight statue as the fire consumes more of the nearby buildings. For a while, it works—guards are too busy elsewhere.\nBut soon the smoke thins, and a patrol circles the yard. They spot you. Hands grab you roughly and haul you back in chains.")
            #end
            break
        elif B1_1_1_choice == 'c':
            print("You race toward a burning tower, spotting a loaded crossbow on a rack. Flames crackle above as the structure sways.You grab the weapon—then the tower gives way.\nA burning beam collapses and crushes you in an instant.")
            #end
            break
        else:
            print("Invalid choice. Please try again.")

def situation_B1_1_2():
    print("You slip down a narrow hallway where smoke doesn’t reach. It's quiet—too quiet.\nYou feel along the walls until your fingers brush a hanging tapestry. Behind it, you find a crumbling stairwell leading down.\nThe air grows colder as you descend. You reach a dead-end crypt lined with rotting coffins and a heavy iron gate sealed with ancient rust.")
    while True:
        B1_1_2_choice = input("What do you do next?\n[A] Search the coffins for a hidden exit or tool.\n[B] Try to force the rusted gate open.\n[C] Sit in silence and wait to see if anything happens.").lower()
        if B1_1_2_choice == 'a':
            situation_B1_1_2_1()
            break
        elif B1_1_2_choice == 'b':
            situation_B1_1_2_2()
            break
        elif B1_1_2_choice == 'c':
            situation_B1_1_2_3()
            break
        else:
            print("Invalid choice. Please try again.")

def situation_B1_1_2_1():
    print("Inside one coffin, you find a loose brick and a tunnel behind it—narrow but passable. You crawl inside, scraping against stone.\nAfter minutes of panic, it opens into a forgotten well shaft lit by moonlight. There's a rope dangling.")
    while True:
        B1_1_2_1_choice = input("What do you do next?\n[A] Climb the rope to the surface.\n[B] Shout for help, hoping someone above hears.").lower()
        if B1_1_2_1_choice == 'a':
            print("You emerge outside the castle, hidden in the woods beyond. After a moment to rejoice and take in the fresh air you sprint through the forest, searching for an exit you'll never find.")
            #end
            break
        elif B1_1_2_1_choice == 'b':
            print("The rope is pulled—by a guard. They drag you up, bind you, and take you back to the dungeon where you spend the rest of your days.")
            #end
            break
        else:
            print("Invalid choice. Please try again.")

def situation_B1_1_2_2():
    print("You brace your feet and push. The hinges groan, and with a sharp crack, the gate swings open into a long, torch-lit tunnel—clearly not abandoned.\nYou hear voices ahead. Footsteps. Something is coming.")
    while True:
        B1_1_2_2_choice = input("What do you do next?\n[A] Hide and wait for them to pass.\n[B] Step into the open and pretend to be a lost servant.").lower()
        if B1_1_2_2_choice == 'a':
            print("You tuck behind a pillar. Two guards pass, muttering about the fire above.\nOnce they’re gone, you slip out through the tunnel exit behind them and escape the castle.")
            #end
            break
        elif B1_1_2_2_choice == 'b':
            print("They immediately recognize you as the escaped prisoner.\nYou’re seized and dragged back in chains.")
            #end
            break
        else:
            print("Invalid choice. Please try again.")

def situation_B1_1_2_3():
    print("You sit down, back against the crypt wall. Minutes pass. Then, from the darkness behind the gate, faint chanting echoes.\nA hidden door opens, revealing robed figures with pale skin and glowing eyes.They’ve found you.")
    while True:
        B1_1_2_3_choice = input("What do you do next?\n[A] Run for the stairs.\n[B] Stay frozen and hope they spare you.").lower()
        if B1_1_2_3_choice == 'a':
            print("You almost make it—but one reaches out, impossibly fast, and drags you into the shadows. No one hears from you again.")
            #end
            break
        elif B1_1_2_3_choice == 'b':
            print("They stop. One tilts their head, curious. 'This isnt the one we wanted', one grumbles. They let you pass through their secret tunnel into the outside world.\nYou may never understand why... but you're free.")
            #end
            break
        else:
            print("Invalid choice. Please try again.")

def situation_B1_2():
    print("As he nears, you suddenly sweep his legs and slam the cell door shut with him inside. He yells and pounds on it.You grab his keys and sword.\nYou’ve got seconds before someone hears.")
    while True:
        B1_2_choice = input("What do you do next?\n[A] Knock him out and take his armor.\n[B] Use his keys and sneak away down a servant’s corridor").lower()
        if B1_2_choice == 'a':
            situation_B1_2_1()
            break
        elif B1_2_choice == 'b':
            situation_B1_2_2()
            break
        else:
            print("Invalid choice. Please try again.")

def situation_B1_2_1():
    print("You walk calmly through the torch-lit halls in the guard’s armor. Another soldier nods at you, unaware of your deception.\nWhen the main gate opens for the evening patrol shift, you march right out with the others—heart pounding.Once you're beyond the walls, the patrol splits off down the road.\nYou're alone at a crossroads, the castle behind you, freedom ahead.")
    while True:
        B1_2_1_choice = input("What do you do next?\n[A] Head to a nearby village and try to live a quiet life.\n[B] Bury the armor, change clothes, and vanish into the forest.\n[C] Follow the other guards, hoping to stay hidden within the patrol until you’re far enough to escape again.").lower()
        if B1_2_1_choice == 'a':
            print("You find an inn in a sleepy village and try to blend in. For a few days, it works.\nYou pose as a discharged soldier, help with odd jobs, and earn some coins.But one night, bounty hunters ride into town. A wanted poster with your face is nailed to the tavern door.\nYou're recognized.")
            num = random.randint(0,1)
            if num !=0:
                print("The town ignores your wanted statues out of distain for the kingdom that captured you. You live in peace among them.")
            else:
                print("The people of the town are peaents in need of your wanted money. They bind you in your sleep and you are taken back into custody.")
            #end
            break
        elif B1_2_1_choice == 'b':
            print("You find a quiet grove, bury the armor, and slip into the wilderness. You survive off berries, rainwater, and raw determination.\nWeeks later, you encounter a band of outcasts—runaways and rebels. They welcome you, and soon you find purpose fighting the very system that imprisoned you.")
            #end
            break
        elif B1_2_1_choice == 'c':
            print("You stick with the patrol, trying to avoid notice. But during a checkpoint inspection, a captain starts asking questions: name, post, shift rotation.\nYou stammer. The other guards notice.The captain draws his sword. “Impostor.” Before you can flee, they surround you.\nYou're executed on the spot.")
            #end
            break
        else:
            print("Invalid choice. Please try again.")

def situation_B1_2_2():
    print("You drag the unconscious guard behind barrels and wipe your hands quickly. You slip down a narrow servant’s corridor, keeping your steps quiet as the chaos of the fire roars in the distance.\nThe passage splits ahead—one way dips into the kitchens, the other slopes deeper underground. Faint noises echo from both directions.")
    while True:
        B1_2_2_choice = input("What do you do next?\n[A] Head into the kitchen, hoping to blend in with fleeing staff.\n[B] Take the sloping tunnel downward—maybe there’s a forgotten passage to escape.").lower()
        if B1_2_2_choice == 'a':
            num = random.randint(0,10)
            if num % 2 == 0:
                print("A sharp-eyed captain notices your stolen cloak and draws his blade. “That’s not one of ours!”\nYou’re stabbed before you can run and left to bleed out alone.")
            else:
                print("You slip out with the fleeing servants, undetected. You escape in the chaos.")
            #end
            break
        elif B1_2_2_choice == 'b':
            print("You descend into the deeper halls—dusty, unused. Eventually, you stumble on a wine cellar hidden behind a false wall.\nCobwebs hang thick, but there's a small grate broken open at floor level.You crawl through and emerge in a dry aqueduct outside the castle walls.\nFaced with no other choice you follow the aquaducts under the expectation they lead to a city. After hours of wading through heavy streams of water you make out what appears to be a village.\nRelief washes over you, you are saved")
            #end
            break        
        else:
            print("Invalid choice. Please try again.")

def situation_B2():
    print("You explode into action, tackling the guard before he can react. A short but brutal fight ends with him unconscious. You grab his keys, panting and bleeding.")
    while True:
        B2_choice = input("What do you do next?\n[A] Take his armor and walk out.\n[B] Try to find an alternate route away from the main halls.").lower()
        if B2_choice == 'a':
            situation_B1_2_1()
            break
        elif B2_choice == 'b':
            situation_B2_2()
            break
        else:
            print("Invalid choice. Please try again.")

def situation_B2_2():
    print("You tighten your grip on the stolen keys and sword, then move swiftly past the main hallway. You push open a servant’s door and slip into a cold, narrow corridor.\nDust clings to every surface. Cobwebs drape the corners. These halls haven’t been used in years.You pass through crumbling storerooms and down an uneven stairwell, eventually reaching a strange fork.")
    while True:
        B2_2_choice = input("Which path do you take?\n[A] Follow the shaft downward—it might lead to a drainage system or escape tunnel.\n[B] Enter a side passage lined with strange symbols and whispering wind.").lower()
        if B2_2_choice == 'a':
            situation_B2_2_1()
            break
        elif B2_2_choice == 'b':
            situation_B2_2_2()
            break
        else:
            print("Invalid choice. Please try again.")
    
def situation_B2_2_1():
    print("You descend the narrow, damp shaft. The walls weep moisture, and the air grows colder with every step.\nEventually, you stumble into a massive underground reservoir, half-forgotten and echoing with dripping water. Rusted machinery lines the walls and an old wooden boat floats nearby.")
    while True:
        B2_2_1_choice = input("What will you do?\n[A] Take the boat and follow the underground river.\n[B] Search the machinery for an alternate tunnel or tool.").lower()
        if B2_2_1_choice == 'a':
            situation_B2_2_1_1()
            break
        elif B2_2_1_choice == 'b':
            situation_B2_2_1_2()
            break
        else:
            print("Invalid choice. Please try again.")

def situation_B2_2_1_1():
    print("You push off quietly into the current, using a broken oar to guide yourself through the darkness.\nAfter some time, glowing fungi begin to light the walls. But then you hear it: splashing—something's following your boat.")
    while True:
        B2_2_1_1_choice = input("Will you:\n[A] Jump into the water and swim to shore.\n [B] Hide under a tarp in the boat and hope it passes.").lower()
        if B2_2_1_1_choice == 'a':
            print("You hurl yourself into the cold black water, heart pounding as the sound of pursuit grows louder.\nYour limbs burn as you swim toward the nearest outcropping of rock, desperate to get out of the current.Just as your fingers brush the edge, something wraps around your ankle—wet, strong, and alive.\nYou scream, but it's muffled by the water as you're dragged under, deeper and deeper, until the world fades.")
            break
            #end
        elif B2_2_1_1_choice == 'b':
            print("You duck beneath the musty tarp, heart racing, barely daring to breathe. The splashing grows louder. Then silence. Moments later, the boat rocks violently.\nThe tarp is ripped away, and in the brief glow of the fungi, you see a grotesque humanoid creature, skin stretched tight over jagged bones, eyes milky white.\nIt shrieks and lunges.Your scream echoes through the tunnels, then vanishes forever.")
            #end
        else:
            print("Invalid choice. Please try again.")

def situation_B2_2_1_2():
    print("You inspect the rusted gears and piping, eventually uncovering a metal hatch partially buried under grime.\nForcing it open, you reveal a tight crawlspace with warm air coming from within.")
    while True:
        B2_2_1_2_choice = input("What do you do next?\n[A] Crawl inside—it might lead to a boiler room or hidden exit.\n[B] Stay in the reservoir and set a trap for whatever might follow.").lower()
        if B2_2_1_2_choice == 'a':
            print("You squeeze into the crawlspace, dragging yourself forward as the warmth intensifies. The air grows thicker, filled with steam and the clank of ancient pipes.\nYou emerge into what must have once been the castle’s old boiler room—now a derelict chamber lit by flickering furnaces and molten metal vents.As you cross the catwalk, a rusted pipe bursts.\nScalding steam floods the walkway. You scream as it envelops you.Your body is never found. Only the quiet hissing of steam remains.")
            #end
            break
        elif B2_2_1_2_choice == 'b':
            print("You gather rusted chains, debris, and a broken spearhead, rigging a makeshift trap near the mouth of the shaft.\nThen, you wait. Something does come—slithering, sniffing, unaware of your ambush. With a scream, you spring the trap. There's a thrash of limbs, a gurgling cry... then stillness.\nYou survived.But the exit is gone. The tunnel collapses in the fight. You’re alone in the dark, alive but sealed in a tomb of your own making. Days blur.\nEventually, you make peace with your fate.")
            #end
            break
        else:
            print("Invalid choice. Please try again.")

def situation_B2_2_2():
    print("The walls pulse with a cold energy. As you walk, the whispers sharpen—speaking fragments of your own memories.\nThe tunnel finally opens into a strange chamber, bathed in green light. At the center, a floating crystal hums with power.\nThree doors stand behind it—each marked with a different symbol.")
    while True:
        B2_2_2_choice = input("What do you do next?\n[A] Touch the crystal—it might reveal the meaning of the symbols.\n[B] Choose the door marked with a spiral—intuitively it feels... safe.").lower()
        if B2_2_2_choice == 'a':
            situation_B2_2_2_1()
            break
        elif B2_2_2_choice == 'b':
            situation_B2_2_2_2()
            break
        else:
            print("Invalid choice. Please try again.")
        
def situation_B2_2_2_1():
    print("The instant your fingers meet the surface, the whispers scream. You’re shown visions—routes through the castle, traps to avoid, even a glimpse of a courtyard gate.\nThe crystal then shatters, revealing a hidden stairway beneath it.")
    while True:
        B2_2_2_1_choice = input("What do you do next?\n[A] Descend the stairway toward the visions.\n[B] Use the knowledge gained and retrace your path back to the main hall.").lower()
        if B2_2_2_1_choice == 'a':
            print("You follow the stairway into a glowing chamber. Strange runes hum as the walls pulse softly.\nA surge of energy envelops you—and suddenly, you awaken in a peaceful village with no memory of who you are.")
            break
            #end
        elif B2_2_2_1_choice == 'b':
            print("With the crystal’s visions fresh in your mind, you move through the castle like a shadow, avoiding traps and guards perfectly.\nYou reach the outer gate—only to find it collapsed, sealed shut by a recent cave-in. You survive, but the way out is gone.")
            break
            #end
        else:   
            print("Invalid choice. Please try again.")

def situation_B2_2_2_2():
    print("You open the door and find yourself in a perfectly silent corridor. The air is still. You pass through a series of archways, each one slightly different.\nEventually, you realize you're being followed by your own footsteps, echoing behind you even when you stop walking.")
    while True:
        B2_2_2_2_choice = input("What do you do next?\n[A] Break into a sprint and try to escape the loop.\n[B] Turn and confront whatever shadow follows you.").lower()
        if B2_2_2_2_choice == 'a':
            print("You bolt forward, sprinting through the archways, heart racing. The footsteps grow louder—closer.")
            num = random.randint(0,10)
            if num >= 5:
                print("You burst through a final arch and collapse into a moonlit courtyard. The curse breaks. The echo vanishes. You’re free.")
            else:
                print("You run endlessly, arch after arch, until your legs give out. The footsteps stop—because they’ve caught up. A shadow envelops you, and everything fades to black.")
            break
            #end
        elif B2_2_2_2_choice == 'b':
            print("You spin around, fists clenched, ready. Nothing is there—until a shape peels itself from the darkness behind you.")
            num = random.randint(0,10)
            if num >= 5:
                print("The shadow pauses, then slowly bows. You’ve shown courage. A hidden door appears beside you, and the figure vanishes. You step through to freedom.")    
            else:
                print("The shadow grins, then leaps. It merges with you—cold, eternal. You remain standing... but you’re no longer you.")
            break
            #end
        else:
            print("Invalid choice. Please try again.")