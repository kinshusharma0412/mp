import json,requests,time,random,re
from pprint import pprint as p
import html
from urllib.parse import urlparse
from urllib.parse import parse_qs
from pyrogram import Client, enums
from pyrogram.methods.utilities.idle import idle
from urllib.parse import quote_plus
from pyrogram.raw import functions
from pyrogram.raw import types
from pyrogram.handlers import MessageHandler, PollHandler
from pyrogram import filters
from pyrogram.types import Message, ReplyKeyboardRemove, Poll,MenuButtonWebApp,WebAppInfo,MenuButtonCommands,MessageEntity,MenuButtonCommands
from pyrogram.types import ReplyKeyboardMarkup as RKM
from pyrogram.types import InlineKeyboardMarkup as IKM
from pyrogram.types import InlineKeyboardButton as IKB
from pyrogram.enums import PollType,MessageEntityType
from pyrogram.raw.functions.messages import ForwardMessages
from pyrogram.raw.functions.channels import GetFullChannel, EditAdmin
from pyrogram.raw.types import ChatAdminRights
from pyrogram.types import InputMediaPhoto, InputMediaVideo
import tgcrypto,asyncio
app_bot=Client("classplus_test",bot_token=os.environ["Soojh"],api_id=os.environ["api_id"],api_hash=os.environ["api_hash"])

#callback_query.message.chat.id
@app_bot.on_callback_query()
async def answer(client, callback_query):
    if callback_query.data.startswith("Testbook_"):
	    #print(str((await client.get_chat_member(-1001517843177,callback_query.from_user.id)).status)[15:])
	    if str((await client.get_chat_member(-1001517843177,callback_query.from_user.id)).status)[17:] in ["OWNER" , "ADMINISTRATOR" , "MEMBER"]:
	    	try:
	    		await client.answer_callback_query(callback_query_id=callback_query.id,url="t.me/SOOJHBOOJH_BOT?start=TB"+re.sub("Testbook_","",callback_query.data))
	    		await asyncio.sleep(.5)
	    		await client.copy_message(callback_query.from_user.id,-1002029684004,int(re.sub("Testbook_","",callback_query.data)))
	    	except Exception as e:
	    		print(e)
	    		await callback_query.answer("First start @SOOJHBOOJH_BOT than click explanation button\n\nपहले @SOOJHBOOJH_BOT को start कीजिए  फिर explanation बटन दबाइए।",show_alert=True)
	    else:
	    	await callback_query.answer("First join @POLLS_QUIZ channal than click explanation button\n\nपहले @POLLS_QUIZ चैनल ज्वाइन कीजिए फिर explanation बटन दबाइए।",show_alert=True)
    
#@app_bot.on_message(filters.private & filters.regex("/start TB\d"))
def test_book_exp(client, message):
    client.copy_message(message.chat.id,-1002029684004,int(re.sub("/start TB","",message.text)))
import requests, os, asyncio, time
from pyrogram.methods.utilities.idle import idle
from apscheduler.schedulers.asyncio import AsyncIOScheduler
scheduler = AsyncIOScheduler(timezone="Asia/kolkata")



headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
  'Accept': "application/json, text/plain, */*",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'sec-ch-ua': "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
  'x-csrf-token': os.environ["xcsrftoken"],
  'sec-ch-ua-mobile': "?1",
  'sec-ch-ua-platform': "\"Android\"",
  'origin': "https://share.streamlit.io",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://share.streamlit.io/",
  'accept-language': "en-IN,en;q=0.9,en-US;q=0.8,hi;q=0.7",
  'priority': "u=1, i",
  'Cookie': os.environ["cookies_header"]
}
def all_restart_hibernation(x):
	url = "https://share.streamlit.io/api/v1/apps"
	params = {
	  'workspace_name': "kinshusharma0412"
	}
	response = requests.get(url, params=params, headers=headers)
	app_=response.json()['apps']
	app_1=[]
	for x in app_:
		if x['appId']!='1e9c1a5d-3cb7-4434-aff7-5a3ab1b6c13c':
			if x['status'] not in [5,6]:
				app_1.append(x)
	for x in app_:
		if x['appId']=='1e9c1a5d-3cb7-4434-aff7-5a3ab1b6c13c':
			if x['status'] not in [5,6]:
				app_1.append(x)
	
	for app_id in app_1:
		url = "https://share.streamlit.io/api/v2/apps/"+str(app_id['appId'])+"/restart"
		response = requests.post(url, headers=headers)
		print(app_1)
		print(response.text)

def hibernation(x):
	url = "https://share.streamlit.io/api/v2/apps/"+str(x)+"/restart"
	response = requests.post(url, headers=headers)
	print(response.text)

print(scheduler.add_job(all_restart_hibernation, 'interval', minutes=30,args=("x",)))
def main():
    scheduler.start()
    def soojh_flood_wait_start(e,f):
    	@st.cache_resource
    	def init_connection1():
    		return app_bot.start()
    	_=init_connection1()
    	#app_bot.delete_messages("Polls_Quiz",f)
    try:
    	@st.cache_resource
    	def init_connection1():
    		return app_bot.start()
    	_=init_connection1()
    except FloodWait as e:
    	current=(time.localtime(time.time()+5.5*3600+int(e.value)+5))
    	CT=time.ctime(time.time()+5.5*3600+int(e.value)+5)
    	
    	print(scheduler.add_job(soojh_flood_wait_start, "cron",year=current.tm_year,month=current.tm_mon,day=current.tm_mday,hour=current.tm_hour, minute=current.tm_min, second=current.tm_sec,replace_existing=True,args=(int(e.value),),id="soojh_flood_wait_start"))
    idle()
    app_bot.stop()

	
if __name__ == '__main__':
    main()#