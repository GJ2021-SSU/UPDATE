import pygame
import Entities
import Utility

pygame.init()


def draw_text(string, x, y):
    temp_text = font.render(string, False, white, black)
    height = temp_text.get_height()
    window.blit(temp_text, (x, y))
    return height


# MONOLITHIC VARIABLES
Running = True
Paused = False
Debug = False
Sound = True
clock = pygame.time.Clock()
pygame.display.set_caption('Main.py')

# Window Variables
window_width = 3200
window_height = 2400
window = pygame.display.set_mode((window_width // 4, window_height // 4), 0, 32)

# Player Variables
player = Entities.Player(375, 375)

# Camera Variables
camera = Entities.Camera(10, 10, 780, 580)

# Button Variables
button_list = {'Play_Button': Entities.Buttons(100, 100, 300, 100), 'Quit_Button': Entities.Buttons(100, 250, 150, 70)}

# Room Variables
room_count_total = 0
cur_level = 0
room_size = 11
room_model = 1
room = Utility.create_room(cur_level, room_size, room_model)
platform_list = room[0]
door_dict = room[1]
door_pos = room[2]
path = Utility.create_path(0, False, [2, 2])
cur_step = 0

Room_width = 1600
Room_height = 1200
Room_position = [0, 0]
Room = pygame.Surface((Room_width, Room_height))

# Color Variables
black = (0, 0, 0)
white = (245, 245, 245)
red = (255, 50, 50)
green = (50, 255, 50)

# Font Variables
font = pygame.font.SysFont("Courier New", 16)

# GAME LOOP
while Running:
    # UPDATE #
    delta_time = clock.tick(60) / 1000
    event = pygame.event.poll()
    keys = pygame.key.get_pressed()

    if Paused:
        delta_time = 0

    # Update the Player
    player.update(event, keys, delta_time, room)
    camera.update()
    camera.global_position(player.x, player.y)

    # Update the Room

    if cur_level != 0:
        for d in door_dict:
            door_num = d
            door_rect = door_dict[door_num]
            if door_rect.colliderect(player.hitbox):
                room_count_total += 1
                if cur_step <= len(path):
                    if door_num != path[cur_step]:
                        room = Utility.create_room(cur_level, 11, 0)
                    elif door_num == path[cur_step]:
                        cur_step += 1
                        # room_size = random.choice((11, 12, 21, 22))
                        room_size = 11
                        #room_model = random.randint(1, 5)
                        room_model = 1
                        room = Utility.create_room(cur_level, room_size, room_model)
                elif cur_step > len(path):
                    cur_level += 1
                    cur_step = 0
                    path = Utility.create_path(4)
                    room = Utility.create_room(cur_level, 11, 0)

                # Reset Player Position
                platform_list = room[0]
                door_dict = room[1]
                door_pos = room[2]
                print(room)
                Room_position = Utility.door_movement(player, door_num, Room_position, door_pos)

    # INPUT #
    # Buttons
    mouse_button = pygame.mouse.get_pressed(3)
    left_click = mouse_button[0]
    mouse_position = pygame.mouse.get_pos()
    if 'Play_Button' in button_list:
        if button_list['Play_Button'].update(mouse_position, left_click):
            cur_level = 1
            player.x = 375
            player.y = 375
            path = Utility.create_path(4)
            Room_position = [0, 100]
        if cur_level != 0:
            del button_list['Play_Button']
    if 'Quit_Button' in button_list:
        if button_list['Quit_Button'].update(mouse_position, left_click):
            Running = False

    if event.type == pygame.QUIT:
        Running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            Running = False
        elif event.key == pygame.K_o:
            Debug ^= True
        elif event.key == pygame.K_p:
            Paused ^= True

    # Camera
    cam_offset_x = camera.x + (camera.width // 2) - camera.Global_x
    cam_offset_y = camera.y + (camera.height // 2) - camera.Global_y

    # DRAW #
    window.fill(black)
    Room.fill(black)
    window.set_clip(camera.rect)

    # Draw the Player
    # TEMPORARY UNTIL CAMERA
    player.draw(Room, [])

    # Draw the Platforms
    for p in platform_list:
        pygame.draw.rect(Room, white, p, 0)

    if Debug:
        for p in platform_list:
            pygame.draw.rect(Room, red, p, 2)
        for d in door_dict:
            pygame.draw.rect(Room, green, door_dict[d], 2)

    window.blit(Room, (Room_position[0] + cam_offset_x, Room_position[1] + cam_offset_y), (0, 0, window_width, window_height))

    # Debug
    if Debug:
        text_height = draw_text("Room Type = {0}, {1}, {2}".format(cur_level, room_size, room_model), 0, 0)
        draw_text("Path = {0}, Step = {1}, Door {2}".format(path, cur_step, path[cur_step]), 0, text_height)
        draw_text("Room (X,Y) = {0}, {1}".format(int(Room_position[0]), int(Room_position[1])), 0, 2 * text_height)
        draw_text("Player (X,Y) = {0}, {1}".format(int(player.x), int(player.y)), 0, 3 * text_height)
    if cur_level == 0:
        button_list['Play_Button'].draw(window, pygame.font.SysFont("Courier New", 64), '  PLAY')
        button_list['Quit_Button'].draw(window, pygame.font.SysFont("Courier New", 32), '  QUIT')

    pygame.display.flip()

pygame.quit()
