import pygame


# init the pygame
pygame.init()
screen_x = 1280
screen_y = 720

green = (0, 255, 0)
blue = (0, 0, 255)

# create the screen
screen = pygame.display.set_mode((screen_x, screen_y))

# background menu
background_menu = pygame.image.load("D:\\Multe chestii\\Antonio\\Facultate\\Python\\proiect\\TrapTheMouse\\images\\background-menu01.png").convert()


def main_menu():

    font = pygame.font.Font('indie-flower.ttf', 32)
    text = font.render("TrapTheMouse", True, green)

    textrect = text.get_rect()
    textrect.center = (screen_x//2, screen_y//6)

    pygame.display.set_caption("TrapTheMouse")

    run_program = True
    while run_program:
        screen.fill("black")
        screen.blit(background_menu, (0, 0))
        screen.blit(text, textrect)
        pygame.display.flip()

        mouse_position = pygame.mouse.get_pos()
        print(mouse_position)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_program = False


main_menu()
