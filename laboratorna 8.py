def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("Файл", file_name, "не відкрився!")
        return None
    else:
        print("Файл", file_name, "відкрився успішно")
        return file

file1_name = "laboratorna8.txt"
file_1_w = Open(file1_name, "w")

if(file_1_w != None):
    lines = [
        "Кондратенко Роман",
        "напиши, що тобі подобається у цій програмі,",
        "а також напиши те, що тобі не подобається.",
        "можеш коротко, 1-2 реченнями про кожен пункт",
        "і не забудь вписати потім своє прізвище та ім'я",
        "та не забудь написати питання наступній людині з команди.",
        "і якщо будуть проблеми з кодуванням текстового файлу, обирай віндовс-1251."
    ]

    for line in lines:
        file_1_w.write(line + "\n")

    print("Текст був успішно доданий до laboratorna8.txt!")
    file_1_w.close()
    print("Файл laboratorna8.txt закрився")

# Автор Пасішніченко Діана
print("Додавання відповіді")
file_1_a = Open(file1_name, "a")
if file_1_a != None:
    my_response = [
        "Пасішніченко Діана",
        "",
        "Відповідь на питання попереднього студента:",
        "У Python використовують функцію open() для відкриття файлів у різних режимах, наприклад,",
        "для читання - r, запису у файл - w, wb - запис у бінарний файл",
        "а також інші режимів читання та запису.",
        " "
    ]

    try:
        for line in my_response:
            file_1_a.write(line + "\n")
        print("Текст був успішно доданий до laboratorna8.txt")
    except IOError as e:
        print(f"Помилка при записі у файл: {e}")
    finally:
        file_1_a.close()
        print("Файл закрито після запису")
