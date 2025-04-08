import pygame
from base_screen import BaseScreen
from text_input import TextInput
from data import get_user_by_credentials

class LoginScreen(BaseScreen):
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(None, 36)
        self.username_input = TextInput(300, 200, 200, 40, self.font, 'Username')
        self.password_input = TextInput(300, 260, 200, 40, self.font, 'Password')
        self.login_button = pygame.Rect(350, 320, 100, 40)

    def try_login(self):
        username = self.username_input.text
        password = self.password_input.text
        user = get_user_by_credentials(username, password)
        if user:
            print(f"Logged in as {user['username']} ({'Teacher' if user['role'] == 'teacher' else 'Student'})")
            return "teacher_home" if user['role'] == 'teacher' else "student_home"
        else:
            print("Login failed: user not found or wrong password")
            return None

    def handle_event(self, event):
        self.username_input.handle_event(event)
        self.password_input.handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.login_button.collidepoint(event.pos):
                return self.try_login()

    def draw(self, screen):
        super().draw()
        self.username_input.draw(self.screen)
        self.password_input.draw(self.screen)
        pygame.draw.rect(self.screen, (0, 255, 0), self.login_button)
        text = self.font.render('Login', True, (0, 0, 0))
        self.screen.blit(text, (self.login_button.x + 15, self.login_button.y + 5))