#!/usr/bin/python3
import random
import os

def clear_screen():
    # Utilisez 'cls' pour Windows et 'clear' pour Unix/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        # Assurez-vous de générer un nombre correct de mines
        self.mines = set(random.sample(range(width * height), mines))
        # Initialisation du champ de jeu
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        # Suivi des cases révélées
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
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        # Vérifier si la case est déjà révélée pour éviter la récursivité inutile
        if self.revealed[y][x]:
            return True  # Rien ne se passe si déjà révélé
        if (y * self.width + x) in self.mines:
            return False
        self.revealed[y][x] = True
        # Révélation récursive pour les cases sans mines adjacentes
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.reveal(nx, ny)
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Entrez la coordonnée x : "))
                y = int(input("Entrez la coordonnée y : "))
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Jeu terminé ! Vous avez touché une mine.")
                    break
            except ValueError:
                print("Entrée invalide. Veuillez entrer uniquement des nombres.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
