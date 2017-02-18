import discord
from discord.ext import commands
from __main__ import send_cmd_help
import subprocess
import asyncio

class Speedtest:

    def __init__(self,bot):
        self.bot = bot

    @commands.group(name="speedtest", pass_context=True)
    async def _speedtest(self, ctx):
        """Internet Speed Test of Host
        speedtest    | show this help message and exit
        """
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @_speedtest.command(pass_context=True, no_pm=True)
    async def bytes(self):
        "Display values in bytes instead of bits."
        await self.bot.say("Testing Internet Speed as Bytes..")
        x = subprocess.check_output("speedtest-cli --secure --bytes --simple", shell=True).decode()
        await self.bot.say(x)

    @_speedtest.command(pass_context=True, no_pm=True)
    async def simple(self):
        "Suppress verbose output, only show basic information."
        await self.bot.say("Testing Simple Internet Speed..")
        x = subprocess.check_output("speedtest-cli --secure --simple", shell=True).decode()
        await self.bot.say(x)

    @_speedtest.command(pass_context=True, no_pm=True)
    async def secure(self):
        "Use HTTPS instead of HTTP when communicating with speedtest.net operated servers."
        await self.bot.say("Testing Internet Speed as Bytes..")
        x = subprocess.check_output("speedtest-cli --secure", shell=True).decode()
        await self.bot.say(x)

    @_speedtest.command(pass_context=True, no_pm=True)
    async def share(self):
        """Generate and provide a URL to the speedtest.net share results image."""
        await self.bot.say("Testing Speed..")
        x = subprocess.check_output("speedtest-cli --secure --share --simple", shell=True).decode()
        await self.bot.say(x)


def setup(bot):
    speed = Speedtest(bot)
    bot.add_cog(speed)
