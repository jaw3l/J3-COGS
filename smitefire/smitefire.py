import os
import html
import discord
import aiohttp
from selenium import WebDriver
from discord.ext import commands
from .utils.dataIO import fileIO
from selenium.webdriver.common.keys import Keys

try:
    from tabulate import tabulate
    tabulateAvailable = True
except:
    tabulateAvailable = False

try:
    from bs4 import BeautifulSoup
    soupAvailable = True
except:
    soupAvailable = False

class SmiteFire:
    """BATTLEGROUND OF GODS"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context = True)
    async def smite(self, ctx):
        """Returns various data for SMITE."""

    if ctx.invoked_subcommand is None:
        await self.bot.say("Type help smite for info.")


    @smite.command(name = "status_sel", pass_context = True)
    async def status_sel(self):
        """Checkes status of game."""
        driver = webdriver.Firefox()
        driver.get("http://status.hirezstudios.com")
        content = driver.find_element_by_class_name("container")
        contentdiv = content.self("unresolved-incidents")

        #Your code will go here
        await self.bot.say("I can do stuff!")

    # Check online players.
    @smite.command(name = 'online', pass_context = True)
    async def online(self, ctx):
        """Returns current amount of players"""

        # Build an url
        url = "https://steamdb.info/app/386360/graphs/"

        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")

        # Parse the data and send it
        try:
            online = soupObject.find(class_='home-stats').find('li').find('strong').get_text()
            await self.bot.say(":earth_americas: | " + online + ' players are playing this game at the moment')
        except:
            await self.bot.say("Couldn't load amount of players. No one is playing this game anymore or there's an error.")

    @smite.command(name = "status_bs4", pass_context = True)
    async def status_bs4(self, ctx):
        "Status from BeautifulSoup4."

        url = "https://status.hirezstudios.com")
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")

        try:
            status = soupObject.find(class_="status index status-none").find("layout-content status status-index premium").find("page-status status-none").find("status font-large").get_text()
            await self.bot.say(status)
        except:
            await self.bot.say("Nothing found.")

def setup(bot):
    if soupAvailable is False:
        raise RuntimeError("You don't have BeautifulSoup installed, run\n```pip3 install bs4```And try again")
        return
    if tabulateAvailable is False:
        raise RuntimeError("You don't have tabulate installed, run\n```pip3 install tabulate```And try again")
        return
    bot.add_cog(SmiteFire(bot))
