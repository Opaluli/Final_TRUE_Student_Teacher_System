import pygame
from login_screen import LoginScreen
from student_home_screen import StudentHomeScreen
from teacher_home_screen import TeacherHomeScreen
from student_request_screen import StudentRequestScreen

def get_screen_by_state(state, screen):
    if state == "login":
        return LoginScreen(screen)
    elif state == "student_home":
        return StudentHomeScreen(screen)
    elif state == "teacher_home":
        return TeacherHomeScreen(screen)
    elif state == "student_request":
        return StudentRequestScreen(screen)
    else:
        raise ValueError(f"Unknown screen state: {state}")

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Student Teacher Support System")
    clock = pygame.time.Clock()

    current_state = "login"
    current_screen = get_screen_by_state(current_state, screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            new_state = current_screen.handle_event(event)
            if new_state and new_state != current_state:
                current_state = new_state
                current_screen = get_screen_by_state(current_state, screen)

        current_screen.draw(screen)
        pygame.display.flip()
        clock.tick(20)

    pygame.quit()

if __name__ == "__main__":
    main()