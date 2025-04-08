
import pygame
from base_screen import BaseScreen
from text_input import draw_text

class TeacherHomeScreen(BaseScreen):
    def __init__(self, app):
        super().__init__(app)
        self.view_requests_button = pygame.Rect(250, 250, 300, 50)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.view_requests_button.collidepoint(event.pos):
                from teacher_requests_screen import TeacherRequestsScreen
                self.app.current_screen = TeacherRequestsScreen(self.app)

    def draw(self, screen):
        screen.fill((200, 255, 200))
        pygame.draw.rect(screen, (0, 100, 200), self.view_requests_button)
        draw_text(screen, "צפה בבקשות תלמידים", (self.view_requests_button.x + 10, self.view_requests_button.y + 10), 24, (255, 255, 255))
