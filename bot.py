import discord
from discord.ext import commands
import asyncio
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=">>", intents=intents)
Token = "MTEzMzk4NjI0ODQwNzY2MjYwNA.GqzL-n.Xk5226DmYZ-RVVAgS9xL9VLdgRBYlzyEKFI4NQ"
Channel_Id1 = 806052853030060035
Channel_Id2 = 1109746148345905233

# Ngasi tau kalo udah ready
@bot.event
async def on_ready():
    channel = bot.get_channel(Channel_Id2)
    await channel.send('Sabar Cokkk..')
    await channel.send('Oke Udah Siapp')

@bot.command()
async def Clist(ctx):
    await ctx.send("```>>Clist: Command Untuk Menampilkan List Commmand2 Yang Ada\n>>ping: Command Untuk Perkenalan\n>>join: Command Untuk Join Voice\n>>start_GHero: Command Untuk Memulai Permainan Tebak Hero\n>>guessH: Command Untuk Menebak Permainan Hero\n>>start_NumGame: Command Untuk Memulai Tebak Angka\n>>guessNum: Command Untuk Menebak Angka Pada Game tebak Angka```")

# Info
@bot.command()
async def ping(ctx):
    await ctx.send('Halo Ngabs.. Kenalin Nihh Ane Hamid, Bot Buatan si Fatih Cuyy')

@bot.command()
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("Ente kagak Di Voice Channel Kocakk")
        return

    channel = ctx.message.author.voice.channel
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if voice_client is None:
        voice_client = await channel.connect()
    else:
        await voice_client.move_to(channel)

#=================================== Tebak Hero =====================================================

# Daftar nama-nama hero yang akan digunakan dalam permainan
hero_names = [
    "Spider-Man",
    "Superman",
    "Batman",
    "Iron Man",
    "Wonder Woman",
    "Hulk",
    "Captain America",
    "Black Panther",
    "Thor",
    "Wolverine",
]

# Hero yang dipilih untuk permainan
chosen_hero = None

@bot.command()
async def start_GHero(ctx):
    global chosen_hero
    chosen_hero = random.choice(hero_names)
    await ctx.send(f"Berikut List Hero yang Akan Keluar: ")
    await ctx.send("```Spiderman\nBatman\nSuperman\nIron Man\nWonder Woman\nHulk\nCaptain America\nBlack Panther\nThor\nWolverine```")
    await ctx.send("Permainan dimulai! Tebak siapa hero berikut:")
    await ctx.send(obfuscate_hero_name(chosen_hero))

@bot.command()
async def guessH(ctx, *, guessed_name):
    if chosen_hero is None:
        await ctx.send("Permainan belum dimulai. Ketik `>>start_GHero` untuk memulai permainan.")
        return

    if guessed_name.lower() == chosen_hero.lower():
        await ctx.send(f"Selamat! Anda benar. Hero yang benar adalah: {chosen_hero}")
    else:
        await ctx.send("Tebakan Anda salah. Coba lagi!")

def obfuscate_hero_name(hero_name):
    # Fungsi untuk mengaburkan nama hero dengan mengganti karakter tengah dengan '*'
    if len(hero_name) <= 2:
        return hero_name
    else:
        first_char = hero_name[0]
        last_char = hero_name[-1]
        middle_chars = " _" * (len(hero_name) - 2)
        return "```" + first_char + middle_chars + " " + last_char + "```" 

#================================== Tebak Angka ========================================================

min_number = 1
max_number = 100
guesses_allowed = 10

@bot.command()
async def start_NumGame(ctx):
    await ctx.send("Selamat datang di Number Guessing Game!")
    await ctx.send(f"Saya telah memilih angka antara {min_number} dan {max_number}.")
    await ctx.send(f"Kamu memiliki {guesses_allowed} kesempatan untuk menebak angka tersebut.")
    await ctx.send("Mulai menebak dengan perintah >>guessNum <angka>.")

    global secret_number
    secret_number = random.randint(min_number, max_number)

@bot.command()
async def guessNum(ctx, number: int):
    global guesses_allowed, secret_number

    if guesses_allowed == 0:
        await ctx.send("Waktu habis. Permainan berakhir.")
        return

    guesses_allowed -= 1
    if number == secret_number:
        await ctx.send("Selamat! Kamu berhasil menebak angka yang benar.")
        guesses_allowed = 0
    elif number < secret_number:
        await ctx.send("Angka terlalu rendah. Coba lagi.")
    else:
        await ctx.send("Angka terlalu tinggi. Coba lagi.")

@bot.command()
async def end_game(ctx):
    global guesses_allowed
    guesses_allowed = 0
    await ctx.send("Permainan berakhir. Sampai jumpa!")

# Aktivasi bot
bot.run(Token)