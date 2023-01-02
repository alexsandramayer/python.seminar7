import view
import model

print("Привет, дорогой пользователь, добро пожаловать в наш телефонный справочник.")
ch = 1
pb = model.initial_phonebook()
while ch in (1, 2, 3, 4, 5):
    ch = view.menu()
    if ch == 1:
        pb = model.add_contact(pb)
    elif ch == 2:
        pb = model.remove_existing(pb)
    elif ch == 3:
        pb = model.delete_all(pb)
    elif ch == 4:
        d = model.search_existing(pb)
        if d == -1:
            print("Контакт не существует. Пожалуйста, попробуйте еще раз")
    elif ch == 5:
        model.display_all(pb)
    else:
        model.thanks()

