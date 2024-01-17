import pygame

window = pygame.display.set_mode([256, 256])
is_running = True

pygame.font.init()

font = pygame.font.SysFont("Comic Sans MS", 24)
text = font.render("Tekst w \"pygame\"", False, [128, 64, 255])

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    window.blit(text, [0, 0])
    pygame.display.flip()

pygame.quit()