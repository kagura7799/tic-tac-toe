import pygame

class Entity:
    def __init__(self, x, y):
        self.cell_is_busy = False
        self.mark = None
        self.cell_button = pygame.Rect((x, y), (97, 97))


class TicTacToe:
    def __init__(self, screen):
        self.screen = screen
        self.move = "X"

        self.field = [
            [Entity(0, 0), Entity(100, 0), Entity(200, 0)],
            [Entity(0, 100), Entity(100, 100), Entity(200, 100)],
            [Entity(0, 200), Entity(100, 200), Entity(200, 200)],
        ]

    def make_move(self, cell):
        if not cell.cell_is_busy:
            cell.cell_is_busy = True

        cell.mark = self.move
        self.move = "0" if self.move == "X" else "X"

    def update_buttons(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for row in self.field:
                for cell in row: 
                    if cell.cell_button.collidepoint(event.pos):
                        cell.cell_is_busy = True
                        self.make_move(cell)

    # TODO: check for winners
    # def check_for_triple():    

    def render(self):
        pygame.draw.line(self.screen, (0, 0, 0), (100, 0), (100, 300), 2)
        pygame.draw.line(self.screen, (0, 0, 0), (200, 0), (200, 300), 2)
        pygame.draw.line(self.screen, (0, 0, 0), (0, 100), (300, 100), 2)
        pygame.draw.line(self.screen, (0, 0, 0), (0, 200), (300, 200), 2)

        for row in self.field:
            for cell in row:
                center = cell.cell_button.center
                if cell.mark == "X":
                    offset = 30
                    pygame.draw.line(self.screen, (0, 0, 0), (center[0] - offset, center[1] - offset),
                                        (center[0] + offset, center[1] + offset), 3)
                    pygame.draw.line(self.screen, (0, 0, 0), (center[0] + offset, center[1] - offset),
                                        (center[0] - offset, center[1] + offset), 3)
                elif cell.mark == "0":
                    pygame.draw.circle(self.screen, (0, 0, 0), center, 35, 3)

def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    clock = pygame.time.Clock()

    tic_tac_toe = TicTacToe(screen)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            tic_tac_toe.update_buttons(event)

        screen.fill("white")
        tic_tac_toe.render()

        pygame.display.flip()
        clock.tick(60)

pygame.quit()

if __name__ == "__main__":
    main()
