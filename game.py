from gameparts import Board

from gameparts.exceptions import CellOccupiedError, FieldIndexError

def save_result(text):
        with open('results.txt', 'a', encoding='utf-8') as file:
            file.write(text + '\n')

def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:

        print(f'Ход делают {current_player}')

        # Запускается бесконечный цикл.
        while True:
            # В этом блоке содержатся операции, которые могут вызвать исключение.
            try:
                # Пользователь вводит значение номера строки.
                row = int(input('Введите номер строки: '))
                # Если введённое число меньше 0 или больше
                # или равно game.field_size...
                if row < 0 or row >= game.field_size:
                    # ...выбрасывается собственное исключение FieldIndexError.
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                # Если введённое число меньше 0 или больше
                # или равно game.field_size...
                if column < 0 or column >= game.field_size:
                    # ...выбрасывается собственное исключение FieldIndexError.
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            # Если возникает исключение FieldIndexError...
            except FieldIndexError:
                # ...выводятся сообщения...
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
                # ...и цикл начинает свою работу сначала,
                # предоставляя пользователю ещё одну попытку ввести данные.
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
            # Если в блоке try исключения не возникло...
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')

            else:
                # ...значит, введённые значения прошли все проверки
                # и могут быть использованы в дальнейшем.
                # Цикл прерывается.
                break

        game.make_move(row, column, current_player)
        game.display()
        if game.check_win(current_player):
            text = f'Победили {current_player}.'
            print(text)
            save_result(text)
            running = False
        elif game.is_board_full():
            text = 'Ничья!'
            print(text)
            save_result(text)
            running = False
            
        current_player = "O" if current_player == 'X' else "X"

if __name__ == '__main__':
    main()