from gameparts import Board

from gameparts.exceptions import FieldIndexError3


def main():
    # Создать игровое поле - объект класса Board.
    game = Board()
    # Отрисовать поле в терминале.
    game.display()
    row = int(input('Введите номер строки: '))
    column = int(input('Введите номер столбца: '))
    # Разместить на поле символ по указанным координатам - сделать ход.
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    # Перерисовать поле с учётом сделанного хода.
    game.display()

if __name__ == '__main__':
    main()