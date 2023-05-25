from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON_RU

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами согласия и отказа
button_monday: KeyboardButton = KeyboardButton(text=LEXICON_RU['button_monday'])
button_tuesday: KeyboardButton = KeyboardButton(text=LEXICON_RU['button_tuesday'])
button_wednesday: KeyboardButton = KeyboardButton(text=LEXICON_RU['button_wednesday'])
button_thursday: KeyboardButton = KeyboardButton(text=LEXICON_RU['button_thursday'])
button_friday:  KeyboardButton = KeyboardButton(text=LEXICON_RU['button_friday'])
button_saturday: KeyboardButton = KeyboardButton(text=LEXICON_RU['button_saturday'])
button_sunday: KeyboardButton = KeyboardButton(text=LEXICON_RU['button_sunday'])


# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
week_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с параметром width=2
week_kb_builder.row(button_monday, button_tuesday, button_wednesday, button_thursday, 
                    button_friday, button_saturday, button_sunday, width=2)

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
week_kb = week_kb_builder.as_markup(
                                one_time_keyboard=True,
                                resize_keyboard=True)