import pygame
import sys
import test

def quizz1():
    pygame.init()
    width, height = 900, 700
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Quizz 1")

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    font = pygame.font.Font(None, 30)

    clock = pygame.time.Clock()

    timeup_image = pygame.image.load("timeup.png")
    fail_image = pygame.image.load("fail.png")
    pass_image = pygame.image.load("pass.png")
    menu_playon_image = pygame.image.load("menu_playon.png")

    abutton = pygame.Rect(325, 315, 35, 35)
    bbutton = pygame.Rect(325, 425, 35, 35)
    cbutton = pygame.Rect(590, 315, 35, 35)
    dbutton = pygame.Rect(590, 425, 35, 35)
    try_againbutton = pygame.Rect(447,433,160,40)
    go_ahead_button = pygame.Rect(446,432,160,41)
    image_paths = ["quizz1.png", "quizz1_2.png", "quizz1.png", "quizz1_2.png", "quizz1.png", "quizz1_2.png"]
    answers = ['A', 'B', 'C', 'D', 'A', 'B']  

    menu_playon_image = pygame.transform.smoothscale(menu_playon_image,(width,height))
    fail_image = pygame.transform.smoothscale(fail_image, (width, height))
    pass_image = pygame.transform.smoothscale(pass_image, (width, height))
    timeup_image = pygame.transform.smoothscale(timeup_image, (width, height))

    def load_image(image_path):
        original_image = pygame.image.load(image_path).convert_alpha()
        scale_factor = min(width / original_image.get_width(), height / original_image.get_height())
        resized_image = pygame.transform.smoothscale(original_image, (int(original_image.get_width() * scale_factor), int(original_image.get_height() * scale_factor)))
        return resized_image

    images = [load_image(path) for path in image_paths]
    current_image_index = 0
    score = 0 
    image_times = [3, 30, 30, 30, 30, 30]
    game_over = False
    running = True
    is_timeup = False
    total_seconds = image_times[current_image_index]  
    at_last_index = False 
    go_ahead = False
    fail = False

    def check_answer(selected_answer):
        nonlocal score, current_image_index, total_seconds
        if current_image_index <= len(images)-1:
            correct_answer = answers[current_image_index]
            if selected_answer == correct_answer:
                score += 1
            current_image_index += 1
            if current_image_index < len(image_times):
                total_seconds = image_times[current_image_index]

    while running:
        for event in pygame.event.get():
            print(pygame.mouse.get_pos())
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if abutton.collidepoint(event.pos):
                    check_answer('A')
                elif bbutton.collidepoint(event.pos):
                    check_answer('B')
                elif cbutton.collidepoint(event.pos):
                    check_answer('C')
                elif dbutton.collidepoint(event.pos):
                    check_answer('D')
                if is_timeup or fail and try_againbutton.collidepoint(event.pos):
                    quizz1()
                    break
                if go_ahead and go_ahead_button.collidepoint(event.pos):
                    pygame.display.update()
                    screen.blit(menu_playon_image, (0, 0))
                    


        if not game_over:
            total_seconds -= clock.tick_busy_loop(60) / 1000.0

        if current_image_index == len(images):
            at_last_index = True
            if score < 5:
                screen.blit(fail_image, (0, 0))
                game_over = True
                fail = True
            else:
                screen.blit(pass_image, (0, 0))
                go_ahead = True
                game_over = True
            pygame.display.update()

        if not is_timeup and total_seconds <= 0:
            is_timeup = True 
            score = 0  
            continue  

        screen.fill(WHITE)

        if not at_last_index:
            if not is_timeup :
                minutes = int(total_seconds // 60)
                seconds = int(total_seconds % 60)
                text = font.render("{:02d}:{:02d}".format(minutes, seconds), True, BLACK)
                text_rect = text.get_rect(center=(780, 100))
                score_text = font.render("{}".format(score), True, BLACK)
                score_rect = score_text.get_rect(center=(790, 135))
                screen.blit(images[current_image_index], (
                    width // 2 - images[current_image_index].get_width() // 2,
                    height // 2 - images[current_image_index].get_height() // 2))
                screen.blit(text, text_rect)
                screen.blit(score_text, score_rect)
                index_text = font.render("{}".format(current_image_index), True, BLACK)
                index_rect = index_text.get_rect(center=(560, 147))
                screen.blit(index_text, index_rect)
            else:
                screen.blit(timeup_image, (0, 0)) 

            pygame.display.update()

