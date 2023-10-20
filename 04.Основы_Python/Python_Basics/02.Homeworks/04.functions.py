documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def find_user(docs: list):
    user_id = input("Введите номер документа: ")
    user_found = None
    for doc in docs:
        if doc['number'] == user_id:
            user_found = doc
            break
    if user_found != None:
        print(f"Владелец документа: {doc['name']}")
    else:
        print("Документ не найден в базе")


def find_directory(dirs: dict):
    user_id = input("Введите номер документа: ")
    directory = None
    for dir in dirs:
        for d in dirs[dir]:
            if d == user_id:
                directory = dir
                break
    if directory != None:
        print(f"Документ хранится на полке: {directory}")
    else:
        print("Документ не найден в базе")


def full_information(docs: list, dirs: dict):
    for doc in docs:
        for dr in dirs:
            for d in dirs[dr]:
                if doc['number'] == d:
                    type, num, name = doc
                    print(f"№: {doc[num]}, тип: {doc[type]}, владелец: {doc[name]}, полка хранения: {dr}")


def add_new_directory(dirs: dict):
    add_dir = input("Введите номер полки: ")
    if add_dir not in dirs.keys():
        dirs[add_dir] = []
        print(f"Полка добавлена. Текущий перечень полок: {', '.join(dirs.keys())}")
    else:
        print(f"Такая полка уже существует. Текущий перечень полок: {', '.join(dirs.keys())}")


def delete_empty_directory(dirs: dict):
    remove_dir_no = input("Введите номер полки: ")
    if remove_dir_no in dirs.keys():
        if dirs[remove_dir_no] == []:
            del dirs[remove_dir_no]
            print(f"Полка удалена. Текущий перечень полок: {', '.join(dirs.keys())}")
        else:
            print(f"На полке есть документы, удалите их перед удалением полки. Текущий перечень полок:"
                  f" {', '.join(dirs.keys())}")
    else:
        print(f"Такой полки не существует. Текущий перечень полок: {', '.join(dirs.keys())}")


def add_new_document(docs: list, dirs: dict):
    new_doc = {'number': input("Введите номер документа: "), 'type': input("Введите тип документа: "),
               'name': input("Введите владельца документа: ")}
    docs.append(new_doc)
    new_dir = input("Введите полку для хранения: ")
    if new_dir in dirs.keys():
        dirs[new_dir].append(new_doc['number'])
    else:
        print("Такой полки не существует. Добавьте полку командой 'ads'.")

    print("Текущий список документов: ")
    full_information(docs, dirs)


def delete_document(docs: list, dirs: dict):
    user_id = input("Введите номер документа: ")
    if not any(d['number'] == user_id for d in docs):
        print('Документ не найден в базе. Текущий список документов: ')
    for doc in docs:
        if doc['number'] == user_id:
            docs.remove(doc)
            print("Документ удален. Текущий список документов: ")
            break
    for dirct in dirs:
        for d in dirs[dirct]:
            if d == user_id:
                dirs[dirct].remove(user_id)
    full_information(docs, dirs)


def change_dir(docs: list, dirs: dict):
    doc_no = input("Введите номер документа: ")
    dir_no = input("Введите номер полки: ")
    for dirct in dirs:
        for d in dirs[dirct]:
            if d == doc_no and dir_no in dirs.keys():
                dirs[dirct].remove(d)
                dirs[dir_no].append(d)
    print('Документ перемещен. Текущий список документов: ')
    full_information(docs, dirs)
    if dir_no not in dirs.keys():
        print(f"Такой полки не существует. Текущий перечень полок: {', '.join(dirs.keys())}")
    if not any(d['number'] == doc_no for d in docs):
        print('Документ не найден в базе. Текущий список документов: ')
        full_information(docs, dirs)


def work_automatizer(docs: list, dirs: dict):
    """
    Данная программа предназначена для автоматизации работы сотрудников компании.
    Перечень пользовательских команд:
    'p' - пользователь может узнать владельца документа по его номеру;
    's' - пользователь может по номеру документа узнать на какой полке он хранится;
    'l' - пользователь может увидеть полную информацию по всем документам;
    'ads' - пользователь может добавить новую полку;
    'ds' - пользователь может удалить существующую полку, если она пустая;
    'ad' - пользователь может добавить новый документ в данные;
    'd' - пользователь может удалить документ из данных;
    'm' - пользователь может переместить документ из полки на полку.

    После каждой команды для продолжения работы с данными необходимо ввести любую букву, для выхода из программы
    необходимо ввести букву 'q'.
    """

    quit_input = ''
    while quit_input != 'q':
        command = input("Введите команду: ")
        if command == 'p':
            find_user(docs)
        elif command == 's':
            find_directory(dirs)
        elif command == 'l':
            full_information(docs, dirs)
        elif command == 'ads':
            add_new_directory(dirs)
        elif command == 'ds':
            delete_empty_directory(dirs)
        elif command == 'ad':
            add_new_document(docs, dirs)
        elif command == 'd':
            delete_document(docs, dirs)
        elif command == 'm':
            change_dir(docs, dirs)
        else:
            print("Ошибка: неизвестная команда.")
        quit_input = input("Введите любую букву, чтобы продолжить, 'q' чтобы выйти: ")


work_automatizer(documents, directories)
