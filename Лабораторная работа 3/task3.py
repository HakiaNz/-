def count_letters(text):
    letters_dict = {}
    text_lower = text.lower()
    for char in text_lower:
        if char.isalpha():
            if char in letters_dict:
                letters_dict[char] += 1
            else:
                letters_dict[char] = 1
    return letters_dict

def calculate_frequency(letters_count):
    total_letters = sum(letters_count.values())
    frequency_dict = {}
    for letter, count in letters_count.items():
        frequency = count / total_letters
        frequency_dict[letter] = round(frequency, 2)
    return frequency_dict

def print_frequencies(frequency_dict):
    for letter in ['у', 'л', 'к']:
        if letter in frequency_dict:
            print(f"{letter}: {frequency_dict[letter]:.2f}")
main_str = """улкоморья дуб зелёный;
Златая цепь на дубе том;
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Мёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избухна там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На берег песчаный и пустой,
И тридцать витязей прекрасных
Чудо из вод выходят ясных,
И с ними дядька их морской;
Там королевы мимоходом
Пленят грозного царя;
Там в облаках перед народом
Нерез леса, через моря
Колдун несёт богатыря;
В темнице там царенько тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кацей над златом чахнет;
Там русский дух... там Русь пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил."""
letter_counts = count_letters(main_str)
frequencies = calculate_frequency(letter_counts)
print_frequencies(frequencies)
