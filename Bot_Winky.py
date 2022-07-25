import discord, asyncio, datetime, pytz, requests,urllib #내장 함수 가져옴

from bs4 import BeautifulSoup
client = discord.Client()
list_s = []
list_t = []
cout_s = 0

@client.event
async def on_ready():   # 오프라인에서 온라인으로 바뀌었을때 효과
    print("출근 했당!!!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("쌀통닭 먹고 싶당..."))  # 생태 메세지

@client.event
async def on_message(message):
    if message.content == "$목록":
        await message.channel.send ("1. $목록\n2 . $정보\n3. $썬데이")
    elif message.content == "$정보":  # 메세지 감지
        #await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention)) # 채널에
        #await message.author.send ("{} | {},User ,Hello".format(message.author, message.author.mention))  #개인한테
        await message.channel.send ("제작 -단바단-\n버전 1.0")
    elif message.content == "$썬데이": # 메세지 감지
        load_url = "https://maplestory.nexon.com/News/Event"
        inx = "https://lwi.nexon.com/"
        html = requests.get(load_url)
        soup = BeautifulSoup(html.content, "html.parser")
        for element in soup.find_all(class_="event_list_wrap"):
            list_s.append(element.find(class_='data').text)
            b = element.find('a').get('href')
            list_t.append(b)
        for i in range(len(list_s)):     
            if list_s[i] == '\n썬데이 메이플\n':
                load_url = "https://maplestory.nexon.com"+list_t[i]
                html = requests.get(load_url)
                soup = BeautifulSoup(html.content, "html.parser")
                img = soup.find("div",attrs={"class":"new_board_con"}).find("img").get('src')
                embed = discord.Embed(title="썬데이 메이플",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. 단바단")
                embed.set_image(url=img )
                await message.channel.send (embed=embed)
        await message.channel.send ("아직 안떳다면 업뎃 안된거임")
    

client.run('MTAwMDMyNjA4NzIwMjU4NjY1NA.G-ylAA.PjwnI9iBS7Y8Njvo3CgYACWUOcKgNYhqZhEgJs') # 봇을 실행 시키기 위한 토큰
