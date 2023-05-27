import pygame


# Button class
class Button():
    def __init__(self, surface, x, y, image, size_x, size_y):
        self.image = pygame.transform.scale(image, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.hovered = False
        self.clicked = False
        self.surface = surface

    def draw(self):
        action = False

        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            self.hovered = True
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True
        else:
            self.hovered = False

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Adjust opacity based on hover and click states
        alpha = 150 if self.hovered and not self.clicked else 255

        # Create a copy of the button image with the adjusted opacity
        button_image = self.image.copy()
        button_image.fill((255, 255, 255, alpha), special_flags=pygame.BLEND_RGBA_MULT)

        # Draw the button
        self.surface.blit(button_image, (self.rect.x, self.rect.y))

        return action
