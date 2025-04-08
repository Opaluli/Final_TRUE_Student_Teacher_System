import pygame

class TextInput:
    def __init__(self, x, y, width, height, font, placeholder=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = pygame.Color('lightskyblue3')
        self.text = ''
        self.font = font
        self.placeholder = placeholder
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.color = pygame.Color('dodgerblue2') if self.active else pygame.Color('lightskyblue3')
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                pass
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, screen):
        txt_surface = self.font.render(self.text or self.placeholder, True, self.color)
        screen.blit(txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

def draw_text(surface, text, position, size=24, color=(0, 0, 0)):
    font = pygame.font.SysFont("arial", size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)
