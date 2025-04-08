import pygame
from base_screen import BaseScreen

class StudentHomeScreen(BaseScreen):
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(None, 40)
        self.math_button = pygame.Rect(300, 250, 200, 60)
        self.selected_subject = None

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.math_button.collidepoint(event.pos):
                self.selected_subject = f"math"
                print("Selected subject - Math")
                return "student_request"

    def draw(self, screen):
        self.screen = screen
        super().draw()
        pygame.draw.rect(self.screen, (100, 200, 255), self.teacher_button)
        text = self.font.render("teacher_yossi", True, (0, 0, 0))
        self.screen.blit(text, (self.teacher_button.x + 20, self.teacher_button.y + 15))