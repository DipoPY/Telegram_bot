from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message
from keyboards.keyboards import week_kb
from lexicon.lexicon import LEXICON_RU
from db.db import day
#from services.services import get_bot_choice, get_winner

router: Router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=week_kb)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=week_kb)


@router.message(Command(commands=['mospol']))
async def prcess_mospol_command(message: Message):
    await message.answer(text=LEXICON_RU['/mospol'], reply_markup=week_kb)


@router.message(Command(commands=['lk']))
async def prcess_mospol_command(message: Message):
    await message.answer(text=LEXICON_RU['/lk'], reply_markup=week_kb)

@router.message(Command(commands=['week']))
async def prcess_mospol_command(message: Message):
    await message.answer(text=LEXICON_RU['/week'], reply_markup=week_kb)

@router.message(Text(text='Понедельник'))
async def press_buttom_tuesday(message: Message):
    help_line = ''
    count_element = 0
    help_line += 'Понедельник\n\n'
    res = day(message.text)
    for i in res:
        count_element += 1
        if count_element == 5:
            
            count_element = 1
            help_line += '\n\n'
        help_line += f'{i} '
    await message.answer(text=help_line, reply_markup=week_kb)
    
    
@router.message(Text(text='Вторник'))
async def press_buttom_tuesday(message: Message):
    help_line = ''
    count_element = 0
    help_line += 'Вторник\n\n'
    res = day(message.text)
    for i in res:
        count_element += 1
        if count_element == 5:
            
            count_element = 1
            help_line += '\n\n'
        help_line += f'{i} '
    await message.answer(text=help_line, reply_markup=week_kb)

@router.message(Text(text='Среда'))
async def press_buttom_tuesday(message: Message):
    help_line = ''
    count_element = 0
    help_line += 'Среда\n\n'
    res = day(message.text)
    for i in res:
        count_element += 1
        if count_element == 5:
            
            count_element = 1
            help_line += '\n\n'
        help_line += f'{i} '
    await message.answer(text=help_line, reply_markup=week_kb)

@router.message(Text(text='Четверг'))
async def press_buttom_tuesday(message: Message):
    help_line = ''
    count_element = 0
    help_line += 'Четверг\n\n'
    res = day(message.text)
    for i in res:
        count_element += 1
        if count_element == 5:
            
            count_element = 1
            help_line += '\n\n'
        help_line += f'{i} '
    await message.answer(text=help_line, reply_markup=week_kb)

@router.message(Text(text='Пятница'))
async def press_buttom_tuesday(message: Message):
    help_line = ''
    count_element = 0
    help_line += 'Пятница\n\n'
    res = day(message.text)
    for i in res:
        count_element += 1
        if count_element == 5:
            
            count_element = 1
            help_line += '\n\n'
        help_line += f'{i} '
    await message.answer(text=help_line, reply_markup=week_kb)

@router.message(Text(text='Суббота'))
async def press_buttom_tuesday(message: Message):
    help_line = ''
    count_element = 0
    help_line += 'Вторник\n\n'
    res = day(message.text)
    for i in res:
        count_element += 1
        if count_element == 5:
            
            count_element = 1
            help_line += '\n\n'
        help_line += f'{i} '
    await message.answer(text=help_line, reply_markup=week_kb)

@router.message(Text(text='Вторник'))
async def press_buttom_tuesday(message: Message):
    help_line = ''
    count_element = 0
    help_line += 'Вторник\n\n'
    res = day(message.text)
    for i in res:
        count_element += 1
        if count_element == 5:
            
            count_element = 1
            help_line += '\n\n'
        help_line += f'{i} '
    await message.answer(text=help_line, reply_markup=week_kb)

@router.message(Text(text='Воскресенье'))
async def press_buttom_tuesday(message: Message):
    await message.answer(text='В единственный выходной надо отдыхать :)')
