import os
import re
from tkinter import filedialog


# text = """У нашій компанії працює багато людей, які користуються різними електронними адресами та телефонами для зв'язку з клієнтами.
# Наприклад, менеджер відділу продажів Джон має адресу john.smith@example.com, а його телефон для зв'язку: +1 (555) 555-5555.
# Ви можете також звертатися до нашої служби підтримки за електронною адресою support@company.com або за номером 555-555-5555.
# Що стосується роботи з клієнтами з України, то основний контактний телефон — +38 050 123 45 67,
# а електронна пошта для українських клієнтів — ukraine@company.ua.
# Для моніторингу внутрішніх серверів нашої IT-відділу ми використовуємо IP-адресу 192.168.0.1 для основного сервера, а IP-адресу 10.0.0.2 для резервного.
# Ці адреси допомагають відслідковувати активність і забезпечують безперебійний доступ до наших послуг.
# Дати важливих подій, таких як корпоративні зустрічі та оновлення, завжди публікуються на нашому вебсайті.
# Наприклад, на зустріч, яка відбудеться 15/10/2024, можна записатися через форму на сторінці www.company.com/events.
# Інші важливі події, такі як завершення квартальних звітів, мають терміни на 10-15-2024,
# що також можна дізнатися на нашому основному сайті https://company.com.
# Більше інформації про наші послуги ви знайдете за посиланням https://services.company.com."""



def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = file.readlines()  # Зчитуємо всі рядки у список
            return data
    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено.")
    except PermissionError:
        print(f"Помилка: Недостатньо прав для читання файлу '{filename}'.")
    except UnicodeDecodeError:
        print(f"Помилка: Файл '{filename}' містить некоректне кодування.")
    except Exception as e:
        print(f"Несподівана помилка: {e}")
    return None  # Повертаємо None у разі помилки


def openfile_dialog():

    # Відкриваємо діалог вибору файлу з фільтрацією на файли .txt
    file_path = filedialog.askopenfilename(
        title="Виберіть текстовий файл",
        filetypes=[("Text files", "*.txt")]
    )

    if not file_path:  # Якщо файл не обраний
        print("Файл не обрано.")
        return None
    return file_path

def process_file():
    filename = openfile_dialog()  # Викликаємо діалог вибору файлу
    if not filename:
        return  # Якщо файл не вибрано, завершуємо функцію

    content = read_file(filename)  # Читаємо вміст файлу
    if not content:
        print("Файл порожній або не вдалося прочитати.")
        return  # Завершуємо функцію, якщо читання не вдалося

    print("Вміст файлу:")
    for line in content:
        print(line.strip())
    # Об'єднуємо рядки у єдиний текст, бо у нас вони до цього як список, а нам треба працювати з текстом(Який не як кожен окремо рядок, а як один цілий)
    return ''.join(content)

# Виклик функції для обробки файлу

def filtration(text): #
    print("Task 2:\n")
# Правильний шаблон для пошуку email адрес
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    email_matches = re.findall(email_pattern, text)
    print("\nВведено наступні email:")
    print(email_matches)


# https://example.com, www.example.com
    website_pattern = r"(https?://[^\s]+|www\.[^\s]+|http?://[^\s]+)"
    website_matches = re.findall(website_pattern, text)
    print("\nВведено наступні вебсайти:")
    print(website_matches)

# +1 (555) 555-5555, 555-555-5555, +38 050 123 45 67)
    phone_pattern = r"(\+?\d{1,3}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?(\d{3}[-.\s]?\d{2,3}[-.\s]?\d{2,4})"
    phone_matches = re.findall(phone_pattern, text)
    print("\nВведно наступні мобільні телефони:")
    # Формуємо повні номери телефонів
    full_phone_numbers = [''.join(match) for match in phone_matches]  # Об'єднуємо частинки, оскільки в phone_matches воно є кортежем: там '+1, '(555)' і нам треба повністю тел
    print(full_phone_numbers)

# Шаблон для IP-адрес (формат IPv4, наприклад, 192.168.0.1)
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    ip_matches = re.findall(ip_pattern, text)
    print("\nВведено наступні IP-адреси:")
    print(ip_matches)

# Шаблон для дат (формати DD/MM/YYYY та MM-DD-YYYY)
    date_pattern = r"\b(?:\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4})\b"
    date_matches = re.findall(date_pattern, text)
    print("\nВведено наступні дати:")
    print(date_matches)

    # Формуємо словник результатів
    search_results = {
        "Emails": email_matches,
        "Websites": website_matches,
        "Phones": full_phone_numbers,  # Витягуючи тільки перший елемент телефонів
        "IP Addresses": ip_matches,
        "Dates": date_matches
    }

    return search_results
def modification(text):
    # Шаблон для номерів телефонів
    phone_pattern = r"(\+?\d{1,3}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?(\d{3}[-.\s]?\d{2,3}[-.\s]?\d{2,4})"

    # Заміна телефонних номерів на маркер
    text_with_marker = re.sub(phone_pattern, '{{номер}}', text)

    # Заміна слів довжиною більше 7 символів на абревіатури
    def abbreviate(match):
        word = match.group(0)
        if len(word) > 2:  # Перевіряємо, чи довжина слова більше 2
            return f"{word[0]}{len(word) - 2}{word[-1]}"
        return word

    # Виключаємо слова, які є в форматі '{{номер}}'
    text_with_abbreviations = re.sub(r'\b(?!{{номер}})\w{8,}\b', abbreviate, text_with_marker)

    # Повертаємо маркер назад на '[номер приховано]'
    text_final = text_with_abbreviations.replace('{{номер}}', '[номер приховано]')

    print("\nТекст після обробки:")
    print(text_final)

    return  text_final

def staistic(text):
    # Шаблони для регулярних виразів
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    phone_pattern = r"(\+?\d{1,3}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?(\d{3}[-.\s]?\d{2,3}[-.\s]?\d{2,4})"
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    date_pattern = r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b"
    url_pattern = r"(https?://[^\s]+|www\.[^\s]+|http?://[^\s]+)"

    # Знайдемо всі елементи
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    ips = re.findall(ip_pattern, text)
    dates = re.findall(date_pattern, text)
    urls = re.findall(url_pattern, text)

    # Статистика
    stats = {
        "Emails": len(emails),
        "Phones": len(phones),
        "IP Addresses": len(ips),
        "Dates": len(dates),
        "URLs": len(urls)
    }

    # Підрахунок унікальних слів (без цифр)
    words = re.findall(r"\b[a-zA-Zа-яА-Яієї']+\b", text.lower())  # Всі слова в нижньому регістрі
    unique_words = set(words)


    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    # Список службових слів
    stop_words = {"і", "або", "але", "це", "в", "на", "з", "до", "як", "не", "що", "я", "ти", "він", "вона", "воно",
                  "ми", "ви", "вони", "а", "проте", "зате", "однак", "за", "та", "для", "також"}

    # Виключаємо слова, що входять до URL
    excluded_words = set()
    for url in urls:
        excluded_words.update(re.findall(r"\b[a-zA-Zа-яА-Яієї']+\b", url.lower()))  # Знаходимо слова в URL

    # Додаємо електронні адреси
    for email in emails:
        excluded_words.update(
            re.findall(r"\b[a-zA-Zа-яА-Яієї']+\b", email.lower()))  # Знаходимо слова в електронних адресах

    # Фільтруємо словник, щоб виключити службові слова
    filtered_word_count = {word: count for word, count in word_count.items() if word not in stop_words
                           and word not in excluded_words}

    # Топ-10 найчастіше вживаних слів
    top_10_words = sorted(filtered_word_count.items(), key=lambda x: x[1], reverse=True)[:10]

    # Виводимо слова, що повторюються лише один раз, не враховуючи слова з URL
    one_time_words = {word: count for word, count in filtered_word_count.items() if
                      count == 1 and word not in excluded_words}
    unique_word_count = len(one_time_words)
    # print("Унікальні слова:")
    # for word in one_time_words:
    #     print(word)
    # Виводимо статистику
    print("\nСтатистика:")
    for key, value in stats.items():
        print(f"{key}: {value}")

    print(f"\nКількість унікальних слів: {unique_word_count}")
    print("\nТоп-10 найчастіше вживаних слів:")
    counter = 1
    print(f"№ \t Слово \t Кількість разів")

    for word, count in top_10_words:
        print(f"{counter}.\t {word}: \t {count} ")
        counter+= 1

    return ({
        "Emails": emails,
        "Телефони": phones,
        "IP адреси": ips,
        "Дати": dates,
        "URL адреси": urls,
        "Унікальні слова": list(one_time_words.keys())
    }, top_10_words)


def validate_fileName(filename):
    # Визначення шаблону для допустимих символів у назві файлу
    # Дозволяємо букви, цифри, пробіли, підкреслення, дефіси та точку
    pattern = r'^[\w\s\-\.]+$'

    # Перевірка на порожнє ім'я файлу
    if not filename:
        print("Ім'я файлу не може бути порожнім.")
        return False

    # Перевірка відповідності шаблону
    if not re.match(pattern, filename):
        print(
            "Недопустимі символи в імені файлу. Використовуйте лише букви, цифри, пробіли, підкреслення, дефіси та точки.")
        return False

    # Перевірка на наявність розширення файлу
    if not filename.lower().endswith(('.txt', '.csv', '.json', '.md')):
        print("Ім'я файлу повинно закінчуватись на .txt, .csv, .json або .md.")
        return False

    return True
def select_save_path(default_name, isEditedText ):
    """Відкриває діалогове вікно для вибору шляху збереження файлу."""
    file_path = filedialog.asksaveasfilename(
        title="Оберіть шлях для збереження файлу з відредагованим текстом"
        if isEditedText
        else "Оберіть шлях для збереження файлу з результатами статистики",
        initialfile=default_name,
        defaultextension=".txt",  # Автоматично додає .txt, якщо відсутнє розширення
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    return file_path

# def save_results(edited_text, search_results, stats, top_10_stats):
#
#     name_edited_file = "edited_text.txt"
#     name_search_stat_file = "search_statistics.txt"
#     print(f"За замовчуванням буде створено файли з назвами '{name_edited_file}' та '{name_search_stat_file}'")
#     validate = False
#     while True:
#         choise = input("\nЧи бажаєте ви продовжити(так), чи ввести власні назви файлів(ні)? (так/ні)\n  ")
#         if  choise == "так":
#             break
#         elif choise == "ні":
#             while(True):
#                 name_edited_file = input("Введіть назву файлу для зберігання відредагованого тексту (наприклад: my_file.txt):")
#                 if validate_fileName(name_edited_file):
#                     name_search_stat_file = input("Введіть назву файлу для зберігання cтатистики (наприклад: my_search_file.txt):")
#                     if  validate_fileName(name_search_stat_file) == False:
#                         validate = False
#                         continue
#                     else:
#                         validate = True
#                         break
#                 else:
#                     continue
#
#         else:
#             continue
#         if validate:
#             break
#
#     # Зберігаємо відредагований текст у новий файл
#     with open(name_edited_file, "w", encoding="utf-8") as edited_file:
#         edited_file.write(edited_text)
#
#     # Зберігаємо статистику та результати пошуку в окремий файл
#     with open(name_search_stat_file, "w", encoding="utf-8") as stats_file:
#         stats_file.write("Статистика:\n")
#         for key, value in stats.items():
#             stats_file.write(f"{key}: {value}\n")
#
#         counter = 1
#         stats_file.write("Топ-10 найчастіше вживаних слів:\n")
#         stats_file.write(f"№  Слово \t Кількість разів\n")
#
#         for word, count in top_10_stats:
#             stats_file.write(f"{counter}. {word}: \t {count}\n ")
#             counter += 1
#
#         stats_file.write("\nРезультати пошуку:\n")
#         for category, items in search_results.items():
#             stats_file.write(f"{category}:\n")
#             for item in items:
#                 stats_file.write(f" - {item}\n")
#
#     print(f"Результати успішно збережено в файли '{name_edited_file}' та '{name_search_stat_file}'.")
def save_results(edited_text, search_results, stats, top_10_stats):
    print("\nЗа замовчуванням файли будуть названі 'edited_text.txt' та 'search_statistics.txt'.")

    edited_file_path = ""
    search_stat_file_path = ""
    validated = False
    while True:
        choice = input(
            "\nЧи бажаєте ви продовжити з цими іменами файлів (так), чи обрати власні (ні)? (так/ні)\n  ").strip().lower()

        if choice == "так":
            edited_file_path = select_save_path("edited_text.txt", True)
            search_stat_file_path = select_save_path("search_statistics.txt", False)
            break

        elif choice == "ні":
            while True:
                print("Виберіть назву ваших файлів в меню: ")
                edited_file_path = select_save_path("", True)
                if edited_file_path and validate_fileName(os.path.basename(edited_file_path)):
                    search_stat_file_path = select_save_path("", False)
                    if search_stat_file_path and validate_fileName(os.path.basename(search_stat_file_path)):
                        validated = True
                        break
                    else:
                     print("Недопустиме ім'я файлу для статистики. Спробуйте ще раз.")
                elif not edited_file_path or not search_stat_file_path:
                    print("Ви не вибрали файл, спробуйте ще раз!")
        else:
            print("Будь ласка, введіть 'так' або 'ні'.")
        if validated: # якщо пройшла валідація вхиодимо з циклу
            break
    # Зберігаємо відредагований текст
    if edited_file_path:
        with open(edited_file_path, "w", encoding="utf-8") as edited_file:
            edited_file.write(edited_text)

    # Зберігаємо статистику та результати пошуку
    if search_stat_file_path:
        with open(search_stat_file_path, "w", encoding="utf-8") as stats_file:
            stats_file.write("Статистика:\n")
            for key, value in stats.items():
                stats_file.write(f"{key}: {value}\n")

            stats_file.write("\nТоп-10 найчастіше вживаних слів:\n")
            stats_file.write("№  Слово\tКількість разів\n")
            for i, (word, count) in enumerate(top_10_stats, 1):
                stats_file.write(f"{i}. {word}: {count}\n")

            stats_file.write("\nРезультати пошуку:\n")
            for category, items in search_results.items():
                stats_file.write(f"{category}:\n")
                for item in items:
                    stats_file.write(f" - {item}\n")

    print(f"Результати збережено у файли:\n'{edited_file_path}' та '{search_stat_file_path}'.")

text = process_file()
search_result = filtration(text)
modificated_text = modification(text)
stats, top_10_stats= staistic(text)
# Збереження результатів
save_results(modificated_text, search_result, stats, top_10_stats)

