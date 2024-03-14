import pygame
import sys
import qui1

# Initialize Pygame
pygame.init()

def main():
    # Set up the display
    width, height = 900, 700
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Picking Mushroom")

    # Function to load and resize images
    def load_image(image_path):
        original_image = pygame.image.load(image_path).convert_alpha()
        scale_factor = min(width / original_image.get_width(), height / original_image.get_height())
        resized_image = pygame.transform.smoothscale(original_image, (int(original_image.get_width() * scale_factor), int(original_image.get_height() * scale_factor)))
        return resized_image

    # List of image paths
    image_paths = ["Collection_1.png","Quizzes.png", "Collection_2.png", "pass.png", "Collection_2.png", "Collection_2.png"]

    # Load all images
    images = [load_image(path) for path in image_paths]

    # Define rectangles
    rect = [
        pygame.Rect(244, 204, 122, 64),
        pygame.Rect(360,204,122,64),
        pygame.Rect(480,204,122,64),
        pygame.Rect(595,204,122,64),
        pygame.Rect(715,204,122,64),
        pygame.Rect(244,321,122,64),
        pygame.Rect(360,321,122,64),
        pygame.Rect(480,321,122,64),
        pygame.Rect(595,321,122,64),
        pygame.Rect(715,321,122,64),
        pygame.Rect(244,436,122,64),
        pygame.Rect(360,436,122,64),
        pygame.Rect(480,436,122,64),
        pygame.Rect(595,436,122,64),
        pygame.Rect(715,436,122,64)
    ]
    back_to_collection = pygame.Rect(209, 616, 180, 18)
    back_button = pygame.Rect(200,277,25,40)
    next_button = pygame.Rect(828,277,25,40)
    play_button =pygame.Rect(23,163,40,20)
    settingbuttonleft= pygame.Rect(22,218,73,20)
    setting_button = pygame.Rect(22,305,73,20)
    quizz_button = pygame.Rect(447,570,163,38)
    quizz1_button = pygame.Rect(450,296,160,38)
    quizz2_button = pygame.Rect(450,544,160,38)

    # Variable to track which image to display
    current_image_index = 0

    # Function to draw images
    def draw_images():
        if 0 <= current_image_index < len(images):
            screen.fill((255, 255, 255))
            screen.blit(images[current_image_index], (width // 2 - images[current_image_index].get_width() // 2, height // 2 - images[current_image_index].get_height() // 2))

    # Variable to track if an image is displayed
    image_displayed = False

    # Main loop
    running = True
    run_quiz1 = False
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, r in enumerate(rect):
                    if r.collidepoint(event.pos) and image_displayed == False:
                        # Toggle between images when rectangle is clicked
                        current_image_index = i + 2
                        image_displayed = True
                        break
                if back_to_collection.collidepoint(event.pos):
                    # Go back to the original collection image
                    current_image_index = 0
                    image_displayed = False
                elif back_button.collidepoint(event.pos) and image_displayed:
                    # Go to the previous image
                    if current_image_index > 2:
                        current_image_index -= 1
                elif next_button.collidepoint(event.pos) and image_displayed:
                    # Go to the next image
                    if current_image_index < len(images) - 1:
                        current_image_index += 1
                elif quizz_button.collidepoint(event.pos):
                    current_image_index = 1
                elif current_image_index == 1 and quizz1_button.collidepoint(event.pos):
                    run_quiz1 = True
                '''
                elif settingbuttonleft.collidepoint(event.pos):
                    setting()'''

        if run_quiz1:
            qui1.quizz1()
            running = False
            
        print(pygame.mouse.get_pos())
        
        # Draw images
        draw_images()

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
