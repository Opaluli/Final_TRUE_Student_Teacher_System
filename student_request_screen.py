import pygame
from base_screen import BaseScreen

class StudentRequestScreen(BaseScreen):
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(None, 32)
        self.options = {
            "Math": "gray",
            "English": "gray",
            "Science": "gray"
        }
        self.option_rects = {}
        self.text_input = ''
        self.active = False
        self.submit_button = pygame.Rect(320, 500, 160, 50)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for topic, rect in self.option_rects.items():
                if rect.collidepoint(event.pos):
                    current = self.options[topic]
                    self.options[topic] = {
                        "gray": "green",
                        "green": "yellow",
                        "yellow": "red",
                        "red": "gray"
                    }[current]
            if self.input_box.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

            if self.submit_button.collidepoint(event.pos):
                print("Submitted Request:")
                print("Difficulties:", self.options)
                print("Message:", self.text_input)
                return "student_home"

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.text_input += '\n'
            elif event.key == pygame.K_BACKSPACE:
                self.text_input = self.text_input[:-1]
            else:
                self.text_input += event.unicode

    def draw(self, screen):
        self.screen = screen
        super().draw()
        y = 100
        for topic, color in self.options.items():
            rect = pygame.Rect(100, y, 200, 40)
            self.option_rects[topic] = rect
            pygame.draw.rect(self.screen, pygame.Color(color), rect)
            text = self.font.render(f"{topic}: {color}", True, (0, 0, 0))
            self.screen.blit(text, (rect.x + 10, rect.y + 5))
            y += 60

        self.input_box = pygame.Rect(350, 100, 400, 200)
        pygame.draw.rect(self.screen, pygame.Color("white"), self.input_box)
        msg_surface = self.font.render(self.text_input, True, (0, 0, 0))
        self.screen.blit(msg_surface, (self.input_box.x + 10, self.input_box.y + 10))

        pygame.draw.rect(self.screen, (0, 255, 0), self.submit_button)
        submit_text = self.font.render("Send Request", True, (0, 0, 0))
        self.screen.blit(submit_text, (self.submit_button.x + 10, self.submit_button.y + 10))