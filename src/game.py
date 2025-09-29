import pygame

# TODO: prohibit making a move on an occupied cell
# TODO: check for winner

class Entity:
    def __init__(self, x, y):
        self.cell_is_busy = False
        self.mark = None
        self.cell_button = pygame.Rect((x, y), (97, 97))


class TicTacToe:
    def __init__(self, screen):
        self.screen = screen
        self.move = "X"

        self.field = [[Entity(0, 0), Entity(100, 0), Entity(200, 0)],
                [Entity(0, 100), Entity(100, 100), Entity(200, 100)],
                [Entity(0, 200), Entity(100, 200), Entity(200, 200)],]

    def make_move(self, cell):
        if not cell.cell_is_busy:
            cell.cell_is_busy = True
            cell.mark = self.move
            self.move = "0" if self.move == "X" else "X"


class UserInterface:
    def __init__(self, tic_tac_toe):
        self.tic_tac_toe = tic_tac_toe

    def update_buttons(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for row in self.tic_tac_toe.field:
                for cell in row: 
                    if cell.cell_button.collidepoint(event.pos):
                        self.tic_tac_toe.make_move(cell)

    def render(self):
        pygame.draw.line(self.tic_tac_toe.screen, (0, 0, 0), (100, 0), (100, 300), 2)
        pygame.draw.line(self.tic_tac_toe.screen, (0, 0, 0), (200, 0), (200, 300), 2)
        pygame.draw.line(self.tic_tac_toe.screen, (0, 0, 0), (0, 100), (300, 100), 2)
        pygame.draw.line(self.tic_tac_toe.screen, (0, 0, 0), (0, 200), (300, 200), 2)

        for row in self.tic_tac_toe.field:
            for cell in row:
                center = cell.cell_button.center
                if cell.mark == "X":
                    offset = 30
                    pygame.draw.line(self.tic_tac_toe.screen, (255, 0, 0), (center[0] - offset, center[1] - offset),
                                        (center[0] + offset, center[1] + offset), 4)
                    pygame.draw.line(self.tic_tac_toe.screen, (255, 0, 0), (center[0] + offset, center[1] - offset),
                                        (center[0] - offset, center[1] + offset), 4)
                elif cell.mark == "0":
                    pygame.draw.circle(self.tic_tac_toe.screen, (0, 0, 255), center, 35, 4)
    

def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    clock = pygame.time.Clock()

    tic_tac_toe = TicTacToe(screen)
    ui = UserInterface(tic_tac_toe)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            ui.update_buttons(event)

        screen.fill("white")
        ui.render()

        pygame.display.flip()
        clock.tick(60)

pygame.quit()

if __name__ == "__main__":
    main()
