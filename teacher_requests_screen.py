
import pygame
from base_screen import BaseScreen
from data import requests_data  # assume this is a list of student requests
from text_input import draw_text

class TeacherRequestsScreen(BaseScreen):
    def __init__(self, app):
        super().__init__(app)
        self.back_button = pygame.Rect(20, 20, 100, 40)
        self.font = pygame.font.SysFont("arial", 24)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_button.collidepoint(event.pos):
                self.app.current_screen = self.app.teacher_home_screen

    def draw(self, screen):
        screen.fill((230, 230, 250))
        pygame.draw.rect(screen, (200, 0, 0), self.back_button)
        draw_text(screen, "חזור", (self.back_button.x + 10, self.back_button.y + 10), 24, (255, 255, 255))

        y = 80
        for req in requests_data:
            student_text = f"תלמיד: {req['student']} | נושאים: {req['subjects']} | הודעה: {req['message']}"
            draw_text(screen, student_text, (50, y), 20, (0, 0, 0))
            y += 40
