#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        # Asegura que haya al menos un campo minado
        self.mines = set(random.sample(range(width * height), min(mines, width * height - 1)))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # Omitir la celda misma
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            return False
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def check_win(self):
        # Verifica si todas las celdas sin minas han sido reveladas
        for y in range(self.height):
            for x in range(self.width):
                if (y * self.width + x) not in self.mines and not self.revealed[y][x]:
                    return False
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Ingrese la coordenada x: "))
                y = int(input("Ingrese la coordenada y: "))
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordenadas fuera de los límites. Inténtalo de nuevo.")
                    continue
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("¡Juego Terminado! Has tocado una mina.")
                    break
                if self.check_win():
                    self.print_board(reveal=True)
                    print("¡Felicidades! Has ganado el juego.")
                    break
            except ValueError:
                print("Entrada inválida. Por favor, ingresa solo números.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
