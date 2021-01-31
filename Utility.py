import pygame
import random
import Lists


def create_path(length, randomized=True, preset=None):
    """ Creates a sequence of Numbers correlating to directions that the Player can follow,
     without going back on themselves."""
    if randomized:
        path = [random.randint(1, 4)]
        L = (0, (1, 2, 4), (1, 2, 3), (2, 3, 4), (1, 3, 4))
        for i in range(length):
            x = random.choice(L[path[i]])
            path.append(x)
        del path[0]
    else:
        path = preset
    return path


def door_movement(player, door_number, room_position, door_entrances):
    """ Sets the Player and Room (Surface) positions upon stage transition. """
    print(door_entrances)
    if door_number == 1:
        print(door_entrances)
        player.x = door_entrances[3][0]
        player.y = door_entrances[3][1]
        # Player in correct position, Camera Not
        room_position[0] = player.x - door_entrances[3][0]
        room_position[1] = player.y - door_entrances[3][1]
    elif door_number == 2:
        print(door_entrances)
        player.x = door_entrances[4][0]
        player.y = door_entrances[4][1]
        room_position[0] = player.x - door_entrances[4][0]
        room_position[1] = player.y - door_entrances[4][1]
    elif door_number == 3:
        print(door_entrances)
        player.x = door_entrances[1][0]
        player.y = door_entrances[1][1]
        room_position[0] = player.x - door_entrances[1][0]
        room_position[1] = player.y - door_entrances[1][1]
    elif door_number == 4:
        print(door_entrances)
        player.x = door_entrances[2][0]
        player.y = door_entrances[2][1]
        room_position[0] = player.x - door_entrances[2][0]
        room_position[1] = player.y - door_entrances[2][1]
    return room_position


def r(x, y, w, h):
    """ Makes a Rectangle"""
    return pygame.Rect(x, y, w, h)


def map_to_rect(col_map):
    list_a = []
    list_b = []
    y = 0
    for row in col_map:
        x = 0
        for tile in row:
            if tile == '1':
                a = (x * 20, y * 20, 20, 20)
                list_a.append(a)
            if tile == '2':
                b = (x * 20, y * 20, 20, 20)
                list_b.append(b)
            x += 1
        y += 1
    return list_a, list_b


def create_room(layer, size, model):
    """ Creates a Platform List and a Door List that the Player can interact with. """
    plat_list = []
    door_list = {}
    door_entrances = {}
    level_border = []
    if layer == 0:
        plat_list = [r(0, 0, 20, 600), r(20, 0, 780, 20), r(780, 20, 20, 580), r(20, 580, 760, 20)]
        door_list = {0: r(375, 375, 10, 10)}
        door_entrances = {1: [375, 375], 2: [375, 375], 3: [375, 375], 4: [375, 375]}
    elif layer == 1:
        if size == 11:
            level_border = [0, 0, 1600, 1200]
            if model == 1:
                # MANUAL COODRS METHOD
                plat_list = [r(60, 560, 20, 120), r(0, 660, 60, 20), r(0, 840, 360, 20), r(340, 860, 40, 20),
                             r(360, 880, 80, 20), r(420, 900, 20, 120), r(440, 1000, 20, 40), r(460, 1020, 20, 40),
                             r(480, 1040, 40, 20), r(500, 1060, 60, 20), r(540, 1080, 100, 20), r(620, 1100, 100, 20),
                             r(700, 1120, 300, 20), r(960, 1100, 60, 20), r(980, 1140, 20, 60), r(1160, 1120, 20, 80),
                             r(1180, 1120, 40, 20), r(1200, 1080, 20, 40), r(1220, 1080, 180, 20),
                             r(1380, 1060, 40, 20), r(1400, 1040, 40, 20), r(1420, 1020, 40, 20),
                             r(1440, 1000, 100, 20), r(1520, 800, 20, 200), r(1500, 780, 20, 40), r(1460, 780, 40, 20),
                             r(1400, 760, 80, 20), r(1280, 740, 140, 20)]
                door_list = {1: r(480, 0, 160, 40), 2: r(1560, 480, 60, 120), 3: r(1000, 1160, 160, 60), 4: r(0, 680, 40, 160)}
                door_entrances = {1: [600, 240], 2: [1500, 420], 3: [1000, 1055], 4: [80, 780]}
            elif model == 2:
                plat_list = []
                door_list = []
            elif model == 3:
                plat_list = []
                door_list = []
            elif model == 4:
                plat_list = []
                door_list = []
            elif model == 5:
                plat_list = []
                door_list = []
            elif model == 0:
                plat_list = [r(0, 0, 25, 250), r(0, 350, 25, 225), r(0, 575, 350, 25), r(450, 575, 350, 25),
                             r(775, 350, 25, 225), r(775, 0, 25, 250), r(450, 0, 350, 25), r(25, 0, 325, 25),
                             r(25, 350, 50, 25), r(150, 200, 100, 25), r(550, 225, 100, 25)]
                door_list = {1: r(350, 0, 100, 10), 2: r(790, 250, 10, 100), 3: r(350, 590, 100, 10),
                             4: r(0, 250, 10, 100)}
                door_entrances = {1: [375, 375], 2: [375, 375], 3: [375, 375], 4: [375, 375]}

        elif size == 12:
            level_border = [0, 0, 1600, 2400]
            if model == 1:
                plat_list = []
                door_list = []
            elif model == 2:
                plat_list = []
                door_list = []
            elif model == 3:
                plat_list = []
                door_list = []
            elif model == 4:
                plat_list = []
                door_list = []
            elif model == 5:
                plat_list = []
                door_list = []

        if size == 21:
            level_border = [0, 0, 3200, 1200]
            if model == 1:
                plat_list = []
                door_list = []
            elif model == 2:
                plat_list = []
                door_list = []
            elif model == 3:
                plat_list = []
                door_list = []
            elif model == 4:
                plat_list = []
                door_list = []
            elif model == 5:
                plat_list = []
                door_list = []

        if size == 22:
            level_border = [0, 0, 3200, 2400]
            if model == 1:
                plat_list = []
                door_list = []
            elif model == 2:
                plat_list = []
                door_list = []
            elif model == 3:
                plat_list = []
                door_list = []
            elif model == 4:
                plat_list = []
                door_list = []
            elif model == 5:
                plat_list = []
                door_list = []

    # elif layer == 2:
    # elif layer == 3:
    # elif layer == -1:
    # elif layer == -2:

    print(door_entrances)

    return plat_list, door_list, door_entrances, level_border
