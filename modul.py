import datetime
import json

def load_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

def read_notes(date_from=None, date_to=None):
    print("Список заметок:")
    notes = load_notes()
    if date_from or date_to:
        filtered_notes = []
        for note in notes:
            created_at = datetime.datetime.strptime(note['timestamp'], '%Y-%m-%d %H:%M:%S')            
            if (not date_from or created_at >= date_from) and (not date_to or created_at <= date_to):
                filtered_notes.append(note)
        notes = filtered_notes
    for note in notes:
        print(f'ID: {note['id']}')
        print(f'Заголовок: {note['title']}')
        print(f'Тело: {note['body']}')
        print(f'Дата создания: {note['timestamp']}')
        print('--------------------------------------')

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новое тело заметки: ")
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            note['title'] = title
            note['body'] = body
            note['timestamp'] = timestamp
            save_notes(notes)
            print("Заметка успешно отредактирована")
            return
    print("Заметка с таким ID не найдена")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена")
            return
    print("Заметка с таким ID не найдена")

notes =  []