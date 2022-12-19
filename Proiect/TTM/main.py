import pygame


# init the pygame
pygame.init()
screen_x = 1280
screen_y = 720



# create the screen
screen = pygame.display.set_mode((screen_x, screen_y))

# background menu
background_menu = pygame.image.load("./images/background-menu01.png").convert()


# def create_button(coord_x, coord_y, color):
#     font = pygame.font.Font("./fonts/indie-flower.ttf", 60)
#     text = font.render("Trap The Mouse", True, "#ffb703")  # #fb8500
#     text_rect = text.get_rect()
#     text_rect.center = (coord_x, coord_y)


def main_menu():
    # create_button(screen_x // 2, screen_y // 6)

    # title
    font = pygame.font.Font("./fonts/indie-flower.ttf", 60)
    text = font.render("Trap The Mouse", True, "#ffb703")  # #fb8500
    text_rect = text.get_rect()
    text_rect.center = (screen_x // 2, screen_y // 6)

    # button start
    # font_start = pygame.font.Font("./fonts/indie-flower.ttf", 60)
    # text_start = font_start.render("Start", True, "#219ebc")
    # text_rect_start = text.get_rect()
    # text_rect_start.center = ((screen_x // 4) - 280, (screen_y // 2) + 10)

    pygame.display.set_caption("TrapTheMouse")
    screen.fill("black")
    screen.blit(background_menu, (0, 0))

    run_program = True
    while run_program:
        mouse_position = pygame.mouse.get_pos()
        print(mouse_position)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_program = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if ((screen_x // 4) - 100) <= mouse_position[0] <= (screen_x // 4) + 30 and ((screen_y // 2) + 30) <= mouse_position[1] <= (screen_y // 2) + 75:
                    run_program = False
                if ((screen_x // 4) - 100) <= mouse_position[0] <= (screen_x // 4) + 30 and ((screen_y // 2) + 130) <= mouse_position[1] <= (screen_y // 2) + 175:
                    run_program = False
                if ((screen_x // 4) - 100) <= mouse_position[0] <= (screen_x // 4) + 30 and ((screen_y // 2) + 230) <= mouse_position[1] <= (screen_y // 2) + 275:
                    run_program = False

        screen.blit(text, text_rect)
        pygame.display.flip()

        # start
        if ((screen_x // 4) - 100) <= mouse_position[0] <= (screen_x // 4) + 30 and ((screen_y // 2) + 30) <= mouse_position[1] <= (screen_y // 2) + 75:
            font_start = pygame.font.Font("./fonts/indie-flower.ttf", 60)
            text_start = font_start.render("Start", True, "#023047")
            screen.blit(text_start, ((screen_x // 4) - 100, (screen_y // 2) + 10))
        else:
            font_start = pygame.font.Font("./fonts/indie-flower.ttf", 60)
            text_start = font_start.render("Start", True, "#219ebc")
            screen.blit(text_start, ((screen_x // 4) - 100, (screen_y // 2) + 10))

        # option
        if ((screen_x // 4) - 100) <= mouse_position[0] <= (screen_x // 4) + 30 and ((screen_y // 2) + 130) <= mouse_position[1] <= (screen_y // 2) + 175:
            font_start = pygame.font.Font("./fonts/indie-flower.ttf", 60)
            text_start = font_start.render("Option", True, "#023047")
            screen.blit(text_start, ((screen_x // 4) - 100, (screen_y // 2) + 110))
        else:
            font_start = pygame.font.Font("./fonts/indie-flower.ttf", 60)
            text_start = font_start.render("Option", True, "#219ebc")
            screen.blit(text_start, ((screen_x // 4) - 100, (screen_y // 2) + 110))

        # quit
        if ((screen_x // 4) - 100) <= mouse_position[0] <= (screen_x // 4) + 30 and ((screen_y // 2) + 230) <= mouse_position[1] <= (screen_y // 2) + 275:
            font_start = pygame.font.Font("./fonts/indie-flower.ttf", 60)
            text_start = font_start.render("Quit", True, "#023047")
            screen.blit(text_start, ((screen_x // 4) - 100, (screen_y // 2) + 210))
        else:
            font_start = pygame.font.Font("./fonts/indie-flower.ttf", 60)
            text_start = font_start.render("Quit", True, "#219ebc")
            screen.blit(text_start, ((screen_x // 4) - 100, (screen_y // 2) + 210))


main_menu()
