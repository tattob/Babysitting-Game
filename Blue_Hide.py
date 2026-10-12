
import random
import time
import os
from time import sleep
def babysitting():
    def clear_terminal():
        # Use 'cls' for Windows, 'clear' for Linux/macOS
        os.system('cls' if os.name == 'nt' else 'clear')

    inventory = []
    items = ["trunk key", "box cutter", "shovel", "filing cabinet key", "sledgehammer"]

    spot_count_list = []

    check_count = 0

    kid_hid = False
    hiding_spot = None
    kid_found = False
    secret = False

    added_rooms = ["entryway"]
    room_keys = {}

    types = ['hallway', 'kitchen', 'bedroom', 'bathroom', 'closet',
             'office', 'nursery', 'laundry', 'pantry', 'gym',
             'stairway', 'garden',]

    colors = ['yellow', 'green', 'blue', 'orange', 'red', 'white', 'purple', 'black', 'violet', 'indigo', 'cyan', 'magenta',
              'cerulean', 'ochre', ]


    class Room:
        def __init__(self,):
            super().__init__()
            self.exits = {}
            self.spots = {}
        posi_spots = [None]
        min_x, max_x = 1, 1
        min_s, max_s = 1, 1

        def randomize(self):
            nonlocal kid_hid
            nonlocal hiding_spot
            nonlocal location

            for i in range(1, random.randint(self.min_x, self.max_x) + 1 ):
                self.exits[str(i)] = "unknown"

            c = random.randint(self.min_s, self.max_s)
            d = self.posi_spots
            for i in range(1, c + 1):
                b = random.choice(d)
                self.spots[str(i)] = b
                spot_count_list.append(f"{self.name} {b}")
                d.remove(b)

                if not kid_hid:
                    if random.randint(1,30) == 1:
                        hiding_spot = f"{self.name} {b}"
                        kid_hid = True


        def check(self, spot):
            nonlocal check_count
            nonlocal kid_found
            nonlocal location
            check_count += 1

            def win():
                nonlocal kid_found
                clear_terminal()
                print(f"You found them. They were in the {hiding_spot}.")
                sleep(.5)
                print(f"Moves: {step_count}")
                sleep(.5)
                print(f"Spots checked: {check_count}")
                sleep(.5)
                if secret == True:
                    print("Blackmail collected!")
                    sleep(.5)
                input(f"Rooms seen: {len(added_rooms)}")
                kid_found = True


            def giver():
                if items != []:
                    if random.randint(1,7) == 1:
                        b = random.choice(items)
                        inventory.append(b)
                        print(f"You found a {b}!")
                        items.remove(b)
            def miss():
                print("They weren't there.")
                giver()
                spot_count_list.remove(f"{location.name} {location.spots[spot]}")
                del location.spots[spot]


            if location.spots[spot] == "in the trunk":
                if "trunk key" not in inventory:
                    print("It's locked.")
                    return
                else:
                    print("You unlock the trunk.")
                    if location.spots[spot] == hiding_spot:
                        win(kid_found, hiding_spot, added_rooms,check_count,step_count)
                    else:
                        miss()
            elif location.spots[spot] == "in a box":
                if "box cutter" not in inventory:
                    print("It's taped up.")
                    return
                else:
                    print("You cut open the box.")
                    if location.spots[spot] == hiding_spot:
                        win()
                    else:
                        miss()
            elif location.spots[spot] == "behind the one way mirror":
                if "sledgehammer" not in inventory:
                    print("What one way mirror?")
                    return
                else:
                    print("You smash the mirror.")
                    if location.spots[spot] == hiding_spot:
                        win()
                    else:
                        miss()
            elif location.spots[spot] == "in the filing cabinet":
                if "filing cabinet key" not in inventory:
                    print("It's locked.")
                    return

                else:
                    nonlocal secret
                    if not secret:
                        secret = True
                        print("You unlocked the filing cabinet.")
                        sleep(1.5)
                        print("You found a secret.")

                    if location.spots[spot] == hiding_spot:
                        win()
                    else:
                        miss()
            elif location.spots[spot] == "in the grave":
                if "shovel" not in inventory:
                    print("There sure is dirt here.")
                    return
                else:
                    print("You dug up the grave.")
                    if location.spots[spot] == hiding_spot:
                        win()
                    else:
                        miss()
            elif f"{location.name} {location.spots[spot]}" == hiding_spot:
                win()
            elif location.spots[spot] != hiding_spot:
                miss()


    class Entryway(Room):
        def __init__(self, name, color, type='entryway', ):
            super().__init__()
            self.name = name
            self.color = color
            self.type = type
            self.exits = {'1' : 'unknown', '2' : 'unknown', '3' : 'unknown', '4' : 'unknown', '5' : 'unknown', '6' : 'unknown',}
            self.posi_spots = []
        min_x, max_x = 4, 4
        min_s, max_s = 0, 0


    class Garden(Room):
        def __init__(self, name, color, type='garden',):
            super().__init__()
            self.name = name
            self.color = color
            self.type = type
            self.posi_spots = ["behind the hedge", "stuck in the rose bush", "in the grave"]
        min_x, max_x = 3, 5
        min_s, max_s = 1, 3


    class Hallway(Room):
        def __init__(self, name, color, type='hallway', ):
            super().__init__()
            self.name = name
            self.color = color
            self.type = type
            self.posi_spots = ["behind the curtain", "in the cabinet"]
        min_x, max_x = 4, 6
        min_s, max_s = 0, 2


    class Kitchen(Room):
        def __init__(self, name, color, type='kitchen', ):
            super().__init__()
            self.name = name
            self.color = color
            self.type = type
            self.posi_spots = ["under the sink", "in the fridge", "in the cupboard", "under the dining table"]
        min_x, max_x = 2, 3
        min_s, max_s = 1, 3


    class Bedroom(Room):
        def __init__(self, name, color, type='bedroom', ):
            super().__init__()
            self.name = name
            self.color = color
            self.type = type
            self.posi_spots = ["under the bed", "in the closet", "in the trunk", "under the blanket", "behind the door"]
        min_x, max_x = 2, 3
        min_s, max_s = 1, 3


    class Bathroom(Room):
        def __init__(self, name, color, type='bathroom', ):
            super().__init__()
            self.name = name
            self.color = color
            self.type = type
            self.posi_spots = ["in the tub", "under the sink", "behind the door"]
        min_x, max_x = 1, 2
        min_s, max_s = 1, 2


    class Office(Room):
        def __init__(self, name, color, type='office', ):
            super().__init__()
            self.name = name
            self.color = color
            self.type = type
            self.posi_spots = ["under the desk", "behind the shelf", "in the filing cabinet", "in the closet", "behind the door"]
        min_x, max_x = 2, 3
        min_s, max_s = 2, 4


    class Nursery(Room):
        def __init__(self, name, color, type='nursery', ):
            super().__init__()
            self.name = name
            self.color = color
            self.type = type
            self.posi_spots = ["in the crib", "in the cabinet", "behind the door", "behind the dresser", "in the closet",]
        min_x, max_x = 2, 4
        min_s, max_s = 1, 3


    class Laundry(Room):
        def __init__(self, name, color, type='laundry', ):
            super().__init__()
            self.name = name
            self.color = color
            self.type = type
            self.posi_spots = ["in the washer", "in the dryer", "under the sink", "behind the door"]
        min_x, max_x = 1, 3
        min_s, max_s = 2, 3


    class Pantry(Room):
        def __init__(self, name, color, type='pantry', ):
            super().__init__()
            self.name = name
            self.color = color
            self.type = type
            self.posi_spots = ["under the shelves", "in the cabinet", "behind the door", "behind the cereal"]
        min_x, max_x = 1, 1
        min_s, max_s = 2, 4


    class Gym(Room):
        def __init__(self, name, color, type='gym', ):
            super().__init__()
            self.name = name
            self.color = color
            self.type = type
            self.posi_spots = ["under the bench", "behind the cable machine", "on the treadmill", "behind the one way mirror",
                      "in the closet", "behind the dumbbells"]
        min_x, max_x = 2, 5
        min_s, max_s = 1, 4


    class Stairway(Room):
        def __init__(self, name, color, type='stairway', ):
            super().__init__()
            self.name = name
            self.color = color
            self.type = type
            self.posi_spots = ["under the stairs", "behind the door"]
        min_x, max_x = 2, 2
        min_s, max_s = 0, 2


    class Closet(Room):
        def __init__(self, name, color, type='closet', ):
            super().__init__()
            self.name = name
            self.color = color
            self.type = type
            self.posi_spots = ["in a box", "under the shelves", "in the cabinet", "behind the door",
                      "behind a stack of boxes", "behind the hanging clothes"]
        min_x, max_x = 1, 1
        min_s, max_s = 2, 3

    entryway = Entryway("entryway", 'white')

    location = entryway
    room_keys[location.name] = location

    def random_room():
        nonlocal location

        type = random.choice(types)
        color = random.choice(colors)
        name = f"{color} {type}"

        def map_naming():
            nonlocal location
            temp = location.name
            location.exits[go] = name
            location = room_keys[name]
            # location.exits['1'] = temp
            if location.exits['1'] == 'unknown':
                location.exits['1'] = temp
            elif '2' in location.exits:
                if location.exits['2'] == 'unknown':
                    location.exits['2'] = temp
            elif '3' in location.exits:
                if location.exits['3'] == 'unknown':
                    location.exits['3'] = temp
            elif '4' in location.exits:
                if location.exits['4'] == 'unknown':
                    location.exits['4'] = temp
            elif '5' in location.exits:
                if location.exits['5'] == 'unknown':
                    location.exits['5'] = temp
            elif '6' in location.exits:
                if location.exits['6'] == 'unknown':
                    location.exits['6'] = temp
            else:
                print("You found a secret door!")
                location.exits['9'] = temp
            # return location

        if name == location.name:
            return random_room()
        elif name in added_rooms:
            map_naming()
        else:
            added_rooms.append(name)
            if type == "hallway":
                a = Hallway(name, color, type)
                a.randomize()
                room_keys[name] = a
                map_naming()
            elif type == "kitchen":
                a = Kitchen(name, color, type)
                a.randomize()
                room_keys[name] = a
                map_naming()
            elif type == "bedroom":
                a = Bedroom(name, color, type)
                a.randomize()
                room_keys[name] = a
                map_naming()
            elif type == "bathroom":
                a = Bathroom(name, color, type)
                a.randomize()
                room_keys[name] = a
                map_naming()
            elif type == "office":
                a = Office(name, color, type)
                a.randomize()
                room_keys[name] = a
                map_naming()
            elif type == "nursery":
                a = Nursery(name, color, type)
                a.randomize()
                room_keys[name] = a
                map_naming()
            elif type == "laundry":
                a = Laundry(name, color, type)
                a.randomize()
                room_keys[name] = a
                map_naming()
            elif type == "pantry":
                a = Pantry(name, color, type)
                a.randomize()
                room_keys[name] = a
                map_naming()
            elif type == "gym":
                a = Gym(name, color, type)
                a.randomize()
                room_keys[name] = a
                map_naming()
            elif type == "stairway":
                a = Stairway(name, color, type)
                a.randomize()
                room_keys[name] = a
                map_naming()
            elif type == "closet":
                a = Closet(name, color, type)
                a.randomize()
                room_keys[name] = a
                map_naming()
            elif type == 'garden':
                a = Garden(name, color, type)
                a.randomize()
                room_keys[name] = a
                map_naming()


    print("Ready to play hide and seek?")
    time.sleep(.5)
    print('3!')
    time.sleep(.5)
    print('2!')
    time.sleep(.5)
    print('1!')
    time.sleep(.5)
    clear_terminal()

    step_count = 0

    while not kid_found:
        print(f"Inventory: {inventory}")
        print(f"Moves: {step_count}    Spots Checked: {check_count}")
        print(f"Unchecked spots: {len(spot_count_list)}")
        if len(location.spots) != 0:
         print ("There are hiding spots here!")
        go = input(f"You are in the {location.name}. You can search or go to another room. \nYour options are: [s] to search or {location.exits}. ")
        if go == "s":
            time.sleep(.5)
            clear_terminal()
            while not kid_found:
                if not location.spots:
                    print("There's nowhere to hide.")
                    time.sleep(1)
                    clear_terminal()
                    break
                else:
                    spot = input(f"You can leave : [l] or check these spots : {location.spots}.")
                    if spot == "l":
                        time.sleep(.5)
                        clear_terminal()
                        break
                    elif spot in location.spots:
                        location.check(spot)
                        time.sleep(1)
                        clear_terminal()
                    else:
                        print("That wasn't an option.")
                        time.sleep(1)
                        clear_terminal()

        elif go in location.exits:
            step_count += 1
            if location.exits[go] in added_rooms:
                location = room_keys[location.exits[go]]
                time.sleep(.5)
                clear_terminal()
            else:
                random_room()
                time.sleep(.5)
                clear_terminal()
        elif go not in location.exits or go != 's':
            print("That's not something you can do.")
            time.sleep(1)
            clear_terminal()
    else:
        y = input("Press [y] to play again. ")
        if y == 'y':
            clear_terminal()
            babysitting()
        else:
            return
babysitting()
