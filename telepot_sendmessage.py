import telepot

token ='6123213123:ASDASDwdsdasd' # bot token
channel_id ='6502769824' # 채팅 id

text='Have a nice dayaaaaaaaa!'

bot=telepot.Bot(token)

bot.sendDocument(channel_id, open('C://','rb')) # send file

bot.sendMessage(channel_id, text) # send text
