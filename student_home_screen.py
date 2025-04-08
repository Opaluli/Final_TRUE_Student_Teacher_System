import pygame
from base_screen import BaseScreen

class StudentHomeScreen(BaseScreen):
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(None, 40)
        self.teacher_button = pygame.Rect(300, 250, 200, 60)
        self.selected_teacher = None

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.teacher_button.collidepoint(event.pos):
                self.selected_teacher = "teacher_yossi"
                print("Selected teacher: teacher_yossi")
                return "student_request"  # next screen we will create later

    def draw(self, screen):
        self.screen = screen
        super().draw()
        pygame.draw.rect(self.screen, (100, 200, 255), self.teacher_button)
        text = self.font.render("teacher_yossi", True, (0, 0, 0))
        self.screen.blit(text, (self.teacher_button.x + 20, self.teacher_button.y + 15))