# Discord Bot # название

import discord
from discord.ext import commands  # подгрузка библиотек

TOKEN = 'NzQzMDc1MjE1MzEwODQ4MDAw.XzPYuQ.hxq4xbcGqm2ZIz9dyXIVy9Rb8D8'  # токен бота

bot = commands.Bot(command_prefix='!')  # инициализация преффикса


@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def test(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(arg)  # отправляем обратно аргумент


bot.run(TOKEN)  # запуск бота
