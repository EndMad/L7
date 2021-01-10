#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Использовать словарь, содержащий следующие ключи: название пункта назначения; номер
# поезда; время отправления. Написать программу, выполняющую следующие действия: ввод
# с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
# быть упорядочены по времени отправления поезда; вывод на экран информации о поездах,
# направляющихся в пункт, название которого введено с клавиатуры; если таких поездов нет,
# выдать на дисплей соответствующее сообщение.

import sys
import json

if __name__ == '__main__':
    # Список работников.
    flights = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ")

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о самолётах.
            destination = input("Пункт назначения рейса? ")
            number = int(input("Номер рейса? "))
            typ = (input("Тип самолёта? "))

            # Создать словарь.
            flight = {
                'destination': destination,
                'number': number,
                'typ': typ
            }

            # Добавить словарь в список.
            flights.append(flight)
            # Отсортировать список в случае необходимости.
            if len(flights) > 1:
                flights.sort(key=lambda item: item.get('destination', ' '))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print('| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                "№",
                "Пункт назначения рейса",
                "Номер рейса",
                "Тип самолёта"
                )
            )
            print(line)

            # Вывести данные о всех рейсах.
            for idx, flight in enumerate(flights, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:<20} |'.format(
                        idx,
                        flight.get('destination', ' '),
                        flight.get('number', 0),
                        flight.get('typ', ' ')
                    )
                )
            print(line)

        elif command.startswith('select '):
            # Разбить команду на части для выделения пункта назначения.
            parts = command.split(' ', maxsplit=1)
            # Инициализировать счетчик.
            count = 0
            # Проверить сведения рейсов из списка.
            for flight in flights:
                if parts[1] == flight.get('typ'):
                    count += 1
                    print('{:>4}: Пункт назначения - {}, Номер рейса- {}'.format(count,
                                                                                 flight.get('destination', ''),
                                                                                 flight.get('number', '')
                                                                                 )
                          )
                # Если счетчик равен 0, то работники не найдены.
            if count == 0:
                print("Таких пунктов назначения не найдено.")

        elif command.startswith('load '):
            parts = command.split(' ', maxsplit=1)
            with open(parts[1], 'r') as f:
                flights = json.load(f)

        elif command.startswith('save '):
            parts = command.split(' ', maxsplit=1)
            with open(parts[1], 'w') as f:
                json.dump(flights, f)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить рейс;")
            print("list - вывести список рейсов;")
            print("select <Тип самолета> - запросить нужный рейс;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
