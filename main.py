# Made by quehole.

import json
import random
import discord
import requests
import threading

from colorama import Fore
from discord.ext import commands

with open('config.json') as f:
    cfg = json.load(f)

token = cfg['Config']['token']
prefix = cfg['Config']['prefix']
color = cfg['Config']['color']
bot_channel = cfg['Config']['bot_channel']
mod_channel = cfg['Config']['mod_channel']
default_role_id = cfg['Config']['default_role_id']
premium_role_id = cfg['Config']['premium_role_id']

bot = commands.Bot(command_prefix=prefix, help_command=None, intents=discord.Intents.all())

class backend:
    def __init__(self) -> None:
        self.session = requests.Session()

    def get_id(self, username):
        try:
            headers = {
                'authority': 'i.instagram.com',
                'accept': '*/*',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'x-csrftoken': '2SAvFYoHgS8GwleiP7j5vTLPqRJX4IFL',
                'x-ig-app-id': '936619743392459',
            }
            params = {'username': username,}
            r = self.session.get('https://i.instagram.com/api/v1/users/web_profile_info/', params=params, headers=headers)
            return r.text.split('"id":"')[2].split('"')[0]
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} User does not exist")

    def get_post(self, post_id):
        try:
            headers = {
                'authority': 'www.instagram.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'en-GB,en;q=0.9',
                'cache-control': 'max-age=0',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            }
            response = self.session.get(f'https://www.instagram.com/p/{post_id}/', headers=headers).text
            return response.split('postPage_')[1].split('"')[0]
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Post does not exist")

    def follow(self, user_id):
        try:
            cookie = random.choice(open('cookies.txt', 'r').read().splitlines())
            headers = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'sessionid={cookie}',
                'origin': 'https://www.instagram.com',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'x-csrftoken': '2SAvFYoHgS8GwleiP7j5vTLPqRJX4IFL',
                'x-requested-with': 'XMLHttpRequest',
            }
            r = self.session.post(f'https://www.instagram.com/web/friendships/{user_id}/follow/', headers=headers)
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")

    def unfollow(self, user_id):
        try:
            cookie = random.choice(open('cookies.txt', 'r').read().splitlines())
            headers = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'sessionid={cookie}',
                'origin': 'https://www.instagram.com',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'x-csrftoken': '2SAvFYoHgS8GwleiP7j5vTLPqRJX4IFL',
                'x-requested-with': 'XMLHttpRequest',
            }
            r = self.session.post(f'https://www.instagram.com/web/friendships/{user_id}/unfollow/', headers=headers)
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")

    def like(self, postID):
        try:
            cookie = random.choice(open('cookies.txt', 'r').read().splitlines())
            headers = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': 'en-GB,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'sessionid={cookie}',
                'origin': 'https://www.instagram.com',
                'referer': f'https://www.instagram.com/p/{postID}/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'x-csrftoken': 'eB8F8DBi9fUrycehIas063lomgcrfwLS',
                'x-requested-with': 'XMLHttpRequest',
            }
            r = self.session.post(f'https://www.instagram.com/web/likes/{postID}/like/', headers=headers)
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")

    def comment(self, postID, message):
        try:
            cookie = random.choice(open('cookies.txt', 'r').read().splitlines())
            headers = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': 'en-GB,en;q=0.9',
                'cookie': f'sessionid={cookie}',
                'origin': 'https://www.instagram.com',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'x-csrftoken': 'eB8F8DBi9fUrycehIas063lomgcrfwLS',
                'x-requested-with': 'XMLHttpRequest',
            }
            data = {
                'comment_text': message,
            }
            r = self.session.post(f'https://www.instagram.com/web/comments/{postID}/add/', headers=headers, data=data)
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="Instagram Automation"))

@bot.command()
async def follow(ctx, username: str):
    if ctx.channel.id != bot_channel:
        return
    if default_role_id not in [role.id for role in ctx.author.roles]:
        await ctx.send("You don't have the required role to use this command.")
        return
    ig_backend = backend()
    user_id = ig_backend.get_id(username)
    if user_id:
        threading.Thread(target=ig_backend.follow, args=(user_id,)).start()
        await ctx.send(f"Started following {username}.")

@bot.command()
async def unfollow(ctx, username: str):
    if ctx.channel.id != bot_channel:
        return
    if default_role_id not in [role.id for role in ctx.author.roles]:
        await ctx.send("You don't have the required role to use this command.")
        return
    ig_backend = backend()
    user_id = ig_backend.get_id(username)
    if user_id:
        threading.Thread(target=ig_backend.unfollow, args=(user_id,)).start()
        await ctx.send(f"Started unfollowing {username}.")

@bot.command()
async def like(ctx, post_id: str):
    if ctx.channel.id != bot_channel:
        return
    if default_role_id not in [role.id for role in ctx.author.roles]:
        await ctx.send("You don't have the required role to use this command.")
        return
    ig_backend = backend()
    threading.Thread(target=ig_backend.like, args=(post_id,)).start()
    await ctx.send(f"Started liking post {post_id}.")

@bot.command()
async def comment(ctx, post_id: str, *, message: str):
    if ctx.channel.id != bot_channel:
        return
    if default_role_id not in [role.id for role in ctx.author.roles]:
        await ctx.send("You don't have the required role to use this command.")
        return
    ig_backend = backend()
    threading.Thread(target=ig_backend.comment, args=(post_id, message)).start()
    await ctx.send(f"Started commenting on post {post_id}.")

@bot.command()
async def follow_all(ctx, *, usernames: str):
    if ctx.channel.id != mod_channel:
        return
    if premium_role_id not in [role.id for role in ctx.author.roles]:
        await ctx.send("You don't have the required role to use this command.")
        return
    ig_backend = backend()
    usernames = usernames.split()
    for username in usernames:
        user_id = ig_backend.get_id(username)
        if user_id:
            threading.Thread(target=ig_backend.follow, args=(user_id,)).start()
            await ctx.send(f"Started following {username}.")

@bot.command()
async def unfollow_all(ctx, *, usernames: str):
    if ctx.channel.id != mod_channel:
        return
    if premium_role_id not in [role.id for role in ctx.author.roles]:
        await ctx.send("You don't have the required role to use this command.")
        return
    ig_backend = backend()
    usernames = usernames.split()
    for username in usernames:
        user_id = ig_backend.get_id(username)
        if user_id:
            threading.Thread(target=ig_backend.unfollow, args=(user_id,)).start()
            await ctx.send(f"Started unfollowing {username}.")

bot.run(token)
