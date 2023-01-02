import sys
def initial_phonebook():
    temp = []
    print('Чтобы начать, предлагаем сохранить первый контакт\n')
    print('В случае если Вы не собираетесь сейчас ничего вводить, нажмите 0')
    phone_book = []
    rows = 1
    cols = 4
    for i in range(rows):
        print("....................................................................")
        
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Введите фамилию: ")))
                if temp[j] == '' or temp[j] == ' ':
                    with open('file.csv', 'w') as file:
                        file.write(f'Фамилия: {temp.append}')
            if j == 1:
                temp.append(str(input("Введите имя: "))) 
                if temp[j] == '' or temp[j] == ' ': 
                    with open('file.csv', 'w') as file:
                        file.write(f'Имя: {temp.append}')
            if j == 2:
                temp.append(str(input("Введите номер: "))) 
                if temp[j] == '' or temp[j] == ' ': 
                    with open('file.csv', 'w') as file:
                        file.write(f'Номер: {temp.append}')
            if j == 3:
                temp.append(str(input("Введите категорию (Семья/Друзья/Работа/Другие): "))) 
                if temp[j] == '' or temp[j] == ' ': 
                    with open('file.csv', 'w') as file:
                        file.write(f'Категория: {temp.append}')
    phone_book.append(temp)
    print(phone_book)
    with open('file.csv', 'a', encoding='utf-8') as file:
        file.write(f"\nФамилия: {temp[0]}\nИмя: {temp[1]}\nНомер: {temp[2]}\nКатегория : {temp[3]}\n")
    return phone_book



def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Введите фамилию: ")))
        if i == 1:
            dip.append(str(input("Введите имя: "))) 
        if i == 2:
            dip.append(str(input("Введите номер: ")))
        if i == 3:
            dip.append(str(input("Введите категорию (Семья/Друзья/Работа/Другие): ")))
    pb.append(dip)
    with open('file.csv', 'a', encoding='utf-8') as file:
        file.write(f"\nФамилия: {dip[0]}\nИмя: {dip[1]}\nНомер: {dip[2]}\nКатегория: {dip[3]}\n")
    return pb

def remove_existing(pb):
# Эта функция предназначена для удаления сведений о контакте из существующей телефонной книги.
    query = str(input("\nПожалуйста, введите имя контакта, который вы хотите удалить: "))
    temp = 0
    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            print(pb.pop(i))
            # Функция pop удалит запись с индексом i.
            print("\nЭтот запрос был удален")
# После удаления вернем измененную телефонную книгу  
            return pb
    if temp == 0:
        print("Извините, вы ввели неверный запрос.\
    Пожалуйста, перепроверьте и повторите попытку позже.")
        return pb


def display_all(pb):
    if not pb:
# если функция отображения вызывается после удаления всех контактов, то len будет 0
# А без этого условия выдаст ошибку
        print("Список пуст: ")
    else:
        for i in range(len(pb)):
            print(pb[i])
 
def delete_all(pb):
# Эта функция просто удалит все записи в телефонной книге pb.
# Он вернет пустую телефонную книгу после очистки
    return pb.clear()


def search_existing(pb):
# Эта функция ищет существующий контакт и отображает результат
    choice = int(input("\nВведите критерии поиска\
    \n1. Фамилия\n2. Имя\n3. Номер\n4. Категория(Семья/Друзья/Работа/Другое)\
    \nПожалуйста, введите: "))
    temp = []
    check = -1
    if choice == 1:
        query = str(input("Пожалуйста, введите фамилию контакта, который вы хотите найти: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])
    elif choice == 2:
        query = str(input("Пожалуйста, введите имя контакта, который вы хотите найти: "))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i
                temp.append(pb[i])
    elif choice == 3:
        query = str(input("Пожалуйста, введите номер контакта, который вы хотите найти: "))
        for i in range(len(pb)):
            if query == pb[i][2]:
                check = i
                temp.append(pb[i])
    elif choice == 4:
        query = str(input("Пожалуйста, введите категорию контакта, который вы хотите найти: "))
        for i in range(len(pb)):
            if query == pb[i][3]:
                check = i
                temp.append(pb[i])
    else:
        print("Неверные критерии поиска")
        return -1
    # возврат -1 означает, что поиск не увенчался успехом
    if check == -1:
        return -1
    # возвращение -1 указывает, что запрос не существует в каталоге
    else:
        display_all.display_all(temp)
        return check

import sys
def thanks():
    print("********************************************************************")
    print("Спасибо за использование телефонного справочника.")
    print("********************************************************************")
    sys.exit("До свидания!")



