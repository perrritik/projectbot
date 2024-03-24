import discord
import random
from discord.ext import commands
from variables import bad_words
from variables import answer_words
from variables import cat_images



intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
intents.members = True

@bot.event
async def on_ready():
    print('Бот готов к использованию.')  # Бот загружен

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.lower() == 'привет':
        await message.channel.send(f"Привет, {message.author.mention}!")

    if message.content.lower() == ("Рандомное число от 1 до 10") or message.content.lower() == ("/монетка"):
        j = random.randint(1, 10)
        await message.channel.send(f"Выпало число {j}")

    if message.content.lower() == ('Кот'):
        await message.channel.send("Я тут!")

    if message.content.lower() == ('ты топ!'):
        await message.channel.send("Не, это ты машина!")

    if message.content.lower() == ('как дела?'):
        await message.channel.send("Отлично!")

    if message.content.lower() == ('привет кот'):
        await message.channel.send("Привет!")

    if message.content.lower() == ('канал астры'):
        await message.channel.send("[**?**] Канал называется Lolsaur, ссылка ниже!")
        await message.channel.send("[**?**] https://www.youtube.com/@lolsaur!")

    if message.content.lower() == ('тг'):
        await message.channel.send("[**?**] В этом тг-канале написано о стримах астры, почему их нет и т.д!")
        await message.channel.send("[**?**] [Нажми на меня!](https://t.me/lolsaurcommunity)")

    if message.content.lower() == ('тг музыка'):
        await message.channel.send("[**?**] В этом тг-канале написано о стримах астры, почему их нет и т.д!")
        await message.channel.send("[**?**] [Нажми на меня!](https://t.me/MUSICFAMILY_perrritik)")

    if message.content.lower() == ('айпи'):
        await message.channel.send("[**?**] На сервере нет никаких модов, только текстурпаки, которые вы можете попросить у админов (При заходе скачиваются)")
        await message.channel.send("[**?**] Lolsaur31.aternos.me")

    if message.content.lower() == ('кот кто твой создатель?'):
        await message.channel.send("Мой создатель - perritik. Этот бот написан на языке программирования Python. Совместно со школой программирования KODLAND!")


    if message.content.lower() == ('зачем нужна экология?'):
        await message.channel.send("***[?] Экология определённо нужна для того чтобы защитить нашу планету и позаботиться о ней.Да, не каждый думает об этом но если хотябы 1 страна возьмётся за это, и призовёт других думать о планете,то мы сплотимся и сделаем это!***")

    if message.content.startswith("/предсказание") or message.content.startswith("/Предсказание"):
        if message.content in ["/предсказание а4 топ?", "/Предсказание а4 топ?", "/предсказание я гей?", "/предсказание Я гей?"]:
            await message.channel.send("Это нарушает правила!")
        else:
            predsk = random.randint(1, 5)
            if predsk == 1:
                await message.channel.send("Я думаю да!")
            elif predsk == 2:
                await message.channel.send("Естественно!")
            elif predsk == 3:
                await message.channel.send("Вероятнее всего, да")
            elif predsk == 4:
                await message.channel.send("Скорее нет, чем да")
            elif predsk == 5:
                await message.channel.send("Точно нет.")       

    if message.content == "сигма момент" or message.content == "Сигма момент" or message.content == "/sigmamoment":
        await message.channel.send("https://tenor.com/view/sigma-argen-argen-sigma-sigma-rule-sigma-face-gif-27218249")

    if message.content.startswith('!hello'):
        await message.channel.send('Привет! Как дела?')

    elif message.content.startswith('!roll'):
        try:
            sides = int(message.content.split()[1])
            result = random.randint(1, sides)
            await message.channel.send(f'Выпало {result} на {sides}-гранных кубиках!')
        except IndexError:
            await message.channel.send('Укажите количество сторон кубика.')

    for word in bad_words:
        if word in message.content:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, пожалуйста, не используйте нецензурную лексику!")

    if message.content == "/cat" or message.content == "/Cat":
        random_cat = random.choice(cat_images)   
        await message.channel.send(random_cat)

    for word in answer_words:
        if word in message.content:
            await message.channel.send('Для более подробной информации о сервере напишите в чат /help')


    await bot.process_commands(message)
@bot.command()
async def insult(ctx, member: discord.Member):
    insults = ["Ты как парковка, все занято!", "У тебя больше минусов, чем у романа Толстого!", "Твой IQ такой низкий, что ты можешь стать политиком!"]
    insult_message = random.choice(insults)
    await ctx.send(f"{member.mention}, {insult_message}")

@bot.command()
async def compliment(ctx, member: discord.Member):
    compliments = ["Ты просто солнечный лучик!", "Твои шутки всегда веселят нас!", "Ты такой умный, что можно думать, что ты бот!"]
    compliment_message = random.choice(compliments)
    await ctx.send(f"{member.mention}, {compliment_message}")

@bot.command()
async def flipcoin(ctx):
    result = random.choice(["Орел", "Решка"])
    await ctx.send(f"Выпало: {result}")

@bot.command()
async def rollsafe(ctx):
    advices = ["Не забудьте сделать резервную копию ваших данных!", "Никогда не ешьте желтый снег!", "Лучший способ избежать ошибок - не делать ничего!"]
    advice_message = random.choice(advices)
    await ctx.send(f"Подсказка дня: {advice_message}")
@bot.command()
async def helpp(ctx):
    # Категория для участников
    member_commands = discord.Embed(title="Команды для участников", description="Список доступных команд для участников", color=discord.Color.green())
    member_commands.add_field(name="/hug @user", value="Обнять пользователя", inline=False)
    member_commands.add_field(name="/cat", value="Отправить случайное изображение кота", inline=False)
    member_commands.add_field(name="/roll [количество]", value="Бросить кубик с указанным количеством сторон", inline=False)
    member_commands.add_field(name="/предсказание [вопрос]", value="Получить предсказание на вопрос", inline=False)
    member_commands.add_field(name="/sigmamoment", value="Получить ссылку на гифку Sigma Moment", inline=False)
    member_commands.add_field(name="/insult @user", value="Оскорбить участника", inline=False)
    member_commands.add_field(name="/compliment @user", value="Похвалить участника", inline=False)
    member_commands.add_field(name="/flipcoin", value="Подбросить монетку", inline=False)
    member_commands.add_field(name="/rollsafe", value="Получить случайный совет", inline=False)


# Категория для администрации
    admin_commands = discord.Embed(title="Команды для администрации", description="Список доступных команд для администрации", color=discord.Color.red())
    admin_commands.add_field(name="/ban @user", value="Бан пользователя", inline=False)
    admin_commands.add_field(name="/kick @user", value="Кик пользователя", inline=False)
    admin_commands.add_field(name="/mute @user", value="Мут пользователя", inline=False)
    admin_commands.add_field(name="/servers", value="Показать список серверов, на которых находится бот", inline=False)
    admin_commands.add_field(name="/table [данные]", value="Создать красивую таблицу с указанными данными", inline=False)
    admin_commands.add_field(name="/checkstatus", value="Проверить статус участников на сервере", inline=False)
    admin_commands.add_field(name="/createrole [название] [цвет]", value="Создать роль", inline=False)
    admin_commands.add_field(name="/deleterole @role", value="Удалить роль", inline=False)
    admin_commands.add_field(name="/createtextchannel [название]", value="Создать текстовый канал", inline=False)
    admin_commands.add_field(name="/deletetextchannel #channel", value="Удалить текстовый канал", inline=False)
    admin_commands.add_field(name="/createvoicechannel [название]", value="Создать голосовой канал", inline=False)
    admin_commands.add_field(name="/deletevoicechannel #channel", value="Удалить голосовой канал", inline=False)
    admin_commands.add_field(name="/createcategory [название]", value="Создать категорию", inline=False)
    admin_commands.add_field(name="/deletecategory #category", value="Удалить категорию", inline=False)
    # Основное встраиваемое сообщение с категориями
    embed = discord.Embed(title="Список команд", description="Список доступных команд бота", color=discord.Color.blue())
    embed.add_field(name="Для участников", value="Команды доступные для всех участников", inline=False)
    embed.add_field(name="Для администрации", value="Команды доступные только администрации", inline=False)

    # Отправка сообщений
    await ctx.send(embed=embed)
    await ctx.send(embed=member_commands)
    await ctx.send(embed=admin_commands)

@bot.command()
async def hug(ctx, member: discord.Member):
    # Проверяем, что упомянут участник
    if member:
        embed = discord.Embed(title=f'{ctx.author.name} обнимает {member.name}!', color=discord.Color.green())
        await ctx.send(embed=embed)
        await ctx.send("https://cdn.discordapp.com/attachments/1207359942571327491/1221154797822935110/laverne-and.png")
        await ctx.message.delete()
    else:
        await ctx.send("Укажите участника, которого вы хотите обнять.")
@bot.command()
async def hit(ctx, member: discord.Member):
    if member:
        embed = discord.Embed(title=f'{ctx.author.name} ударил {member.name}!', color=discord.Color.green())
        embed.set_image(url="https://cdn.discordapp.com/attachments/1207359942571327491/1221154831327170590/tkthao219-peach.png")
        await ctx.send(embed=embed)
        await ctx.message.delete()
    else:
        await ctx.send("Укажите участника, которого вы хотите ударить.")
@bot.event
async def on_member_join(member):
    role_id = 1190984855211753554  # Замените на реальный ID вашей роли
    role = member.guild.get_role(role_id)
    
    if role is not None:
        await member.add_roles(role)
        print(f'{member} was given the role {role.name}')

@bot.command()
async def serverinfo(ctx):
    server = ctx.guild
    created_at = str(server.created_at).split()[0]
    embed = discord.Embed(title=f'Информация о сервере {server.name}', color=discord.Color.blue())
    embed.add_field(name='Участники', value=server.member_count)
    embed.add_field(name='Количество каналов', value=len(server.channels))
    embed.add_field(name='Создан', value=server.created_at)
    await ctx.send(embed=embed)

@bot.command()
async def reverse(ctx, *, text: str):
    reversed_text = text[::-1]
    await ctx.send(f"Реверс текста: {reversed_text}")


@bot.command()
async def wordcount(ctx, *, text: str):
    words = text.split()
    word_count = len(words)
    await ctx.send(f"Количество слов: {word_count}")

@bot.command()
async def tempinvite(ctx, duration: int):
    invite = await ctx.channel.create_invite(max_age=duration)
    await ctx.send(f"Временное приглашение создано: {invite.url}")
@bot.command()
@commands.has_permissions(manage_roles=True)
async def createrole(ctx, role_name: str, color: discord.Color = discord.Color.default()):
    guild = ctx.guild
    role = await guild.create_role(name=role_name, color=color)
    await ctx.send(f"Роль {role.name} создана.")
@bot.command()
@commands.has_permissions(manage_roles=True)
async def deleterole(ctx, role: discord.Role):
    await role.delete()
    await ctx.send(f"Роль {role.name} удалена.")
@bot.command()
@commands.has_permissions(manage_channels=True)
async def createtextchannel(ctx, channel_name: str):
    guild = ctx.guild
    await guild.create_text_channel(channel_name)
    await ctx.send(f"Текстовый канал {channel_name} создан.")
@bot.command()
@commands.has_permissions(manage_channels=True)
async def deletetextchannel(ctx, channel: discord.TextChannel):
    await channel.delete()
    await ctx.send(f"Текстовый канал {channel.name} удален.")
@bot.command()
@commands.has_permissions(manage_channels=True)
async def createvoicechannel(ctx, channel_name: str):
    guild = ctx.guild
    await guild.create_voice_channel(channel_name)
    await ctx.send(f"Голосовой канал {channel_name} создан.")
@bot.command()
@commands.has_permissions(manage_channels=True)
async def deletevoicechannel(ctx, channel: discord.VoiceChannel):
    await channel.delete()
    await ctx.send(f"Голосовой канал {channel.name} удален.")
@bot.command()
@commands.has_permissions(manage_channels=True)
async def userinfo(ctx, member: discord.Member):
    user_embed = discord.Embed(title="Информация о пользователе", color=discord.Color.blue())
    user_embed.set_thumbnail(url=member.avatar_url)
    user_embed.add_field(name="Имя", value=member.name, inline=True)
    user_embed.add_field(name="Присоединился", value=member.joined_at.strftime("%d.%m.%Y"), inline=True)
    user_embed.add_field(name="Аккаунт создан", value=member.created_at.strftime("%d.%m.%Y"), inline=True)
    user_embed.add_field(name="ID", value=member.id, inline=True)
    await ctx.send(embed=user_embed)

@bot.command()
async def servers(ctx):
    servers_list = [guild.name for guild in bot.guilds]
    await ctx.send(f"Список серверов, на которых находится бот:\n{', '.join(servers_list)}")
@bot.command()
async def table(ctx, *data: str):
    table_data = "\n".join(data)
    table_embed = discord.Embed(title="Таблица", description=table_data, color=discord.Color.green())
    await ctx.send(embed=table_embed)
@bot.command()
async def checkstatus(ctx):
    online_members = sum(member.status == discord.Status.online for member in ctx.guild.members)
    idle_members = sum(member.status == discord.Status.idle for member in ctx.guild.members)
    offline_members = sum(member.status == discord.Status.offline for member in ctx.guild.members)
    await ctx.send(f"Онлайн: {online_members}, Отошли: {idle_members}, Оффлайн: {offline_members}")
bot.run('TOKEN HERE')
