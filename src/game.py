import pygame

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
        self.winner_line = None

        self.field = [[Entity(0, 0), Entity(100, 0), Entity(200, 0)],
                [Entity(0, 100), Entity(100, 100), Entity(200, 100)],
                [Entity(0, 200), Entity(100, 200), Entity(200, 200)],]

    def make_move(self, cell):
        if not cell.cell_is_busy and not self.winner_line:
            cell.cell_is_busy = True
            cell.mark = self.move
            self.move = "0" if self.move == "X" else "X"

        self.check_for_winner()

    def check_for_winner(self):
        win_lines = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)] 
        ]

        for line in win_lines:
            a, b, c = line
            m1 = self.field[a[0]][a[1]].mark
            m2 = self.field[b[0]][b[1]].mark
            m3 = self.field[c[0]][c[1]].mark

            if m1 and m1 == m2 == m3:
                self.winner_line = line
                break


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
        self.draw_grid()
        self.draw_winner_line()

        for row in self.tic_tac_toe.field:
            for cell in row:
                center = cell.cell_button.center
                if cell.mark == "X":
                    offset = 30
                    pygame.draw.line(self.tic_tac_toe.screen, (255, 0, 0),
                                    (center[0] - offset, center[1] - offset),
                                    (center[0] + offset, center[1] + offset), 4)
                    pygame.draw.line(self.tic_tac_toe.screen, (255, 0, 0),
                                    (center[0] + offset, center[1] - offset),
                                    (center[0] - offset, center[1] + offset), 4)
                elif cell.mark == "0":
                    pygame.draw.circle(self.tic_tac_toe.screen, (0, 0, 255), center, 35, 4)

    def draw_winner_line(self):
        if self.tic_tac_toe.winner_line:
            a, _, c = self.tic_tac_toe.winner_line
            start_cell = self.tic_tac_toe.field[a[0]][a[1]]
            end_cell = self.tic_tac_toe.field[c[0]][c[1]]

            start = start_cell.cell_button.center
            end = end_cell.cell_button.center

            pygame.draw.line(self.tic_tac_toe.screen, (0, 255, 0), (start[0] - 10, start[1] - 10), end, 4)

    def draw_grid(self):
        pygame.draw.line(self.tic_tac_toe.screen, (0, 0, 0), (100, 0), (100, 300), 2)
        pygame.draw.line(self.tic_tac_toe.screen, (0, 0, 0), (200, 0), (200, 300), 2)
        pygame.draw.line(self.tic_tac_toe.screen, (0, 0, 0), (0, 100), (300, 100), 2)
        pygame.draw.line(self.tic_tac_toe.screen, (0, 0, 0), (0, 200), (300, 200), 2)
    

def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    clock = pygame.time.Clock()
    running = True

    tic_tac_toe = TicTacToe(screen)
    ui = UserInterface(tic_tac_toe)

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
