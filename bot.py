from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types,executor,Dispatcher,Bot
from keyboards import reg_menu,menu,options
from aiogram.dispatcher.filters import Text
class RegistrationState(StatesGroup):
    name = State()
    surname = State()
    age = State()
    town = State()

Bot = Bot('')
storage = MemoryStorage()
dp = Dispatcher(bot=Bot,storage=storage)    



@dp.message_handler(commands=['start'])
async def send_hi(message:types.Message):
    await message.answer(text='''чтобы пройти нашу регистрацию нажмите на кнопку ниже👇:''',reply_markup=reg_menu)

@dp.callback_query_handler()
async def send_reg(call:types.callback_query):
    data = call.data
    if data=='reg':
        await Bot.send_message(
            chat_id=call.from_user.id,
            text='нашите свое имя:',)
        await RegistrationState.name.set()

@dp.message_handler(state=RegistrationState.name)
async def send_name(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['ati']=message.text
        await message.answer('напишите свою фамилию:')
        await RegistrationState.surname.set()

@dp.message_handler(state=RegistrationState.surname)
async def get_surname(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['familiasi']=message.text
        await message.answer('теперь напишите свой возраст:')
        await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def get_age(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['jas']=message.text
        await message.answer('теперь напишите свой регион:')
        await RegistrationState.town.set()

@dp.message_handler(state=RegistrationState.town)
async def get_town(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['region']=message.text
    await message.answer('''круто вы прошли регистрацию.

 
                   /MENU      
                         
                                         

                         
                         
                         
                         
                         
                         ''')
    await state.finish()    



@dp.message_handler(commands=['MENU'])
async def send_pi(message:types.Message):
    await message.answer(text='''выберете 👇:''',reply_markup=options)














if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)
