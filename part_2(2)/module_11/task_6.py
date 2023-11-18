class Board:
    def __init__(self):
        self.cells = []
        for i in range(9):
            self.cells.append(Cell(i + 1))

    def display(self):
        for i in range(3):
            print('-------------')
            out = '| '
            for j in range(3):
                out += str(self.cells[i * 3 + j]) + ' | '
            print(out)
        print('-------------')

    def update_cell_state(self, num_cell, symbol):
        if self.cells[num_cell - 1].symbol == ' ':
            self.cells[num_cell - 1].symbol = symbol
            return True
        else:
            return False

    def is_game_over(self):
        for i_cell in range(3):
            if (self.cells[i_cell * 3].symbol == self.cells[i_cell * 3 + 1].symbol == self.cells[i_cell * 3 + 2].symbol
                    and self.cells[i_cell * 3].symbol != ' '):
                return True
        for i_cell in range(3):
            if (self.cells[i_cell].symbol == self.cells[i_cell + 3].symbol == self.cells[i_cell + 6].symbol
                    and self.cells[i_cell].symbol != ' '):
                return True
        if self.cells[0].symbol == self.cells[4].symbol == self.cells[8].symbol and self.cells[0].symbol != ' ':
            return True
        if self.cells[2].symbol == self.cells[4].symbol == self.cells[6].symbol and self.cells[2].symbol != ' ':
            return True
        for cell in self.cells:
            if cell.symbol == ' ':
                return False
        return False

    def is_game_over_all_board(self):
        for cell in self.cells:
            if cell.symbol == ' ':
                return False
        return True


class Cell:
    def __init__(self, num):
        self.num = num
        self.symbol = ' '

    def __str__(self):
        return self.symbol


class Player:
    def __init__(self, name, symbol, score=0):
        self.name = name
        self.symbol = symbol
        self.score = score

    def get_move(self):
        try:
            cell_num = int(input(self.name + ', введите номер клетки: '))
            return cell_num
        except ValueError:
            print('Пожалуйста, введите номер.')
            return self.get_move()


class Game:
    def __init__(self, player_1, player_2):
        self.player1 = player_1
        self.player2 = player_2
        self.board = Board()
        self.current_player = player_1

    def play_turn(self):
        print(self.current_player.name + ' ходи:\n')
        self.board.display()
        cell_num = self.current_player.get_move()
        while not self.board.update_cell_state(cell_num, self.current_player.symbol):
            print('Ячейка уже занята. Пробовать снова.')
            cell_num = self.current_player.get_move()
        if self.board.is_game_over_all_board() and not self.board.is_game_over():
            print('Ничья!')
            self.board.display()
            return True
        if self.board.is_game_over():
            print(self.current_player.name + ' победил!\n')
            self.board.display()
            self.current_player.score += 1
            return True
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

        return False

    def play_game(self):
        print('Новая игра началась!')
        self.board = Board()
        self.current_player = self.player1
        while not self.board.is_game_over():
            if self.play_turn():
                break

        print('Score:')
        print(self.player1.name + ': ' + str(self.player1.score))
        print(self.player2.name + ': ' + str(self.player2.score))
        return self.player1.score, self.player2.score


def battle():
    name1 = input('Введите имя игрока 1(X): ')
    name2 = input('Введите имя игрока 2(O): ')
    result_player_1 = 0
    result_player_2 = 0
    while True:
        player1 = Player(name1, 'X', result_player_1)
        player2 = Player(name2, 'O', result_player_2)
        game = Game(player1, player2)
        result_player_1, result_player_2 = game.play_game()
        again = input('Вы хотите поиграть еще раз?(Y/N): ').lower()
        if again != 'y':
            break

    print('Спасибо за игру!')


battle()
