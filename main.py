#!/usr/bin/python3
import discord
import random
import requests
import urllib.request
import asyncio
import time
from datetime import datetime
from bs4 import BeautifulSoup
from discord.ext import commands
from googletrans import Translator
from config import token, help, wal_images, bestemmie, Insulti

# TODO: - Aggiungere piú commandi... (TextToSpeech, Audio, Migliorare Insulti

bot = commands.Bot(command_prefix='!')

client = discord.Client()
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Bot ready: {0.user}".format(bot))

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
        	await ctx.send("Inserire tutti i campi richiesti. Per info o aiuti scrivi !aiuto")
	if isinstance(error, commands.CommandNotFound):
		await ctx.send("Compa' hai sbagliato commando")

@bot.command()
async def rev(ctx, *, frase):
    await ctx.send(frase[::-1])

@bot.command()
async def mamma(ctx, *, guy):
	await ctx.send("{0}'s mom".format(guy))

@bot.command()
async def misenti(ctx):
    await ctx.send("TI SENTO")

@bot.command()
async def mom(ctx, *, guy):
    await ctx.send("{}s mom".format(guy))

@bot.command()
async def corona(ctx):
    await ctx.send(get_Cases())

@bot.command()
async def best(ctx):
    bestemmia = random.choice(bestemmie)
    await ctx.send(bestemmia)

@bot.command()
async def ins(ctx, *, guy):
    sceltaIns = random.choice(Insulti)
    await ctx.send("{0}, {1}".format(guy, sceltaIns))

@bot.command()
async def lech(ctx):
    chosen_image = random.choice(wal_images)
    embed = discord.Embed(color=0xf5d116)
    embed.set_image(url=chosen_image)
    await ctx.send(embed=embed)

@bot.command()
async def tiryakewalesa(ctx):
    embed = discord.Embed(color=0xf5d116)
    embed.set_image(url="https://i.imgur.com/ClxxuFU.jpg")
    await ctx.send(embed=embed)

@bot.command()
async def saluta(ctx, *, guy):
    await ctx.send("Ciao {0}".format(guy))

@bot.command()
async def lagfrax(ctx):
    num = random.randint(1,101)
    await ctx.send("Oggi Tha Frax ha laggato {0} volte".format(num))

@bot.command()
async def storia(ctx):
    await ctx.send("https://it.wikipedia.org/wiki/Lech_Wa%C5%82%C4%99sa")

@bot.command()
async def latinus(ctx, *, testo):
    translator = Translator()
    res = translator.translate(testo, dest='la')
    await ctx.send(res.text)

@bot.command()
async def quanti_cristiani(ctx):
    await ctx.send("Ecco quanti cristiani ci su supra u server: " + str(len(ctx.guild.members)))


def get_Cases():
    dati = []
    listT = []
    url = "https://www.worldometers.info/coronavirus/country/italy/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for div in soup.find_all(class_="maincounter-number"):
        dati.append(div.text)
    for element in dati:
        listT.append(element.strip())

    finale = "Attualmente in italia ci sono: {0} casi, {1} morti e i ricoverati sono: {2} #STATTIARACASA #CORNUTU".format(listT[0],listT[1],listT[2])
    return finale

bot.run(token)
