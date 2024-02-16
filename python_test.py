#https://yunwoong.tistory.com/214
import discord
from discord.ext import commands
from datetime import datetime

TOKEN = '<TOKEN>' #혹시 몰라서 지워둠
CHANNEL_ID = '1206672265811599373'
 
 
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        channel = self.get_channel(int(CHANNEL_ID))





        await self.change_presence(status=discord.Status.idle, activity=discord.Game("Coding"))
        # await channel.send('TEST')
        embed = discord.Embed(title="TEST", description="환영합니다", color=0x00aaaa)
        embed.set_author(name="python_bot")
        await channel.send(embed=embed)
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content == '핑':
            await message.channel.send('퐁 {0.author.mention}'.format(message))
        elif message.content == '정보':
            embed = discord.Embed(title="디코봇", description="아직 한참 멀었다.", color=0x00aaaa)
            embed.set_author(name="python_bot")
            
            await message.channel.send(embed=embed)
        else:
            answer = self.get_answer(message.content)
            await message.channel.send(answer)

        
    def get_answer(self, text):
        trim_text = text.replace(" ", "")


        answer_dict = {
            '안녕': '안녕하세요. python_bot입니다.',
            '시간': '현재 시간은 {}입니다.'.format(self.get_time()),
        }

 
        if trim_text == '' or None:
            return "알 수 없는 질의입니다. 답변을 드릴 수 없습니다."
        elif trim_text in answer_dict.keys():
            return answer_dict[trim_text]
        elif trim_text not in answer_dict.keys():
            return 

    def get_time(self):
         return datetime.today().strftime("%p %I시 %M분")

 
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)