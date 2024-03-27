from modul import *

notes = load_notes()

while True:
    command = input("Введите команду (add/read/edit/delete/filter/exit): ")

    if command == "add":
        add_note()
    elif command == "read":
        read_notes()
    elif command == "edit":
        edit_note()
    elif command == "delete":
        delete_note()
    elif command == 'filter':
        date_from = input('Введите дату и время начала фильтрации (формат ГГГГ-ММ-ДД ЧЧ:ММ:СС): ')
        if date_from:
            date_from = datetime.datetime.strptime(date_from, '%Y-%m-%d %H:%M:%S')
        date_to = input('Введите дату и время окончания фильтрации (формат ГГГГ-ММ-ДД ЧЧ:ММ:СС): ')
        if date_to:
            date_to = datetime.datetime.strptime(date_to, '%Y-%m-%d %H:%M:%S')
        read_notes(date_from, date_to)
    elif command == "exit":
        break
    else:
        print("Неверная команда. Повторите ввод.")