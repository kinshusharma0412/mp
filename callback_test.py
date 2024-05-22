import json,requests,time,random,re
from pprint import pprint as p
import html,os
import streamlit as st
from pyrogram.errors import FloodWait
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
	
	    try:
	        (await client.get_chat_member(-1001517843177,callback_query.from_user.id)).status
	    except:
	        await callback_query.answer("First join @POLLS_QUIZ channal than click explanation button\n\nपहले @POLLS_QUIZ चैनल ज्वाइन कीजिए फिर explanation बटन दबाइए।",show_alert=True)
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
  'Cookie': os.environ["xcsrftoken"]
}





headersai = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
  'Cookie': "usprivacy=1Y--; _ga=GA1.1.126541330.1716373648; _ga_YJWJRNESS5=GS1.1.1716373647.1.0.1716373647.60.0.0"
}


key=["b4dc174b87fcf3eb677eaa767d4f470bbc06268d48c903d0a7032511d9ab0cb3",
"8a81e03bdd68c126cbe7a3f3277581d9a35eb1f8aad34d759f747024392f6edb",
"940973e878b455f3c8cd4fa1ddf358f39eac1e8a9ec4c52901eff864b2039c2d",
"d3089aa7d155758c8712508d96dd412af1032d482e4f2dd047dc45beb4bb1904",
"46f8e7c5886983b27c08c6ae0ed92e3b9dd1e454900cac51188f5a5ca76a6b47",
"014533fe515e16298fc4660c8a09126eedfdac3ec63d0570ff31fbef5be11795"]

async def gen(x ,y,m):
	key_num=random.randint(0,5)
	url2 = os.environ["url2"]
	params = {
	  'thread': str(key_num),
	  '__cacheBust': str(random.randint(100000000000000000,9999999999999999999)/10000000000000000000)
	}
	res = requests.get(url2, params=params, headers=headersai)
	try:
		userKey=res.json()["userKey"]
	except:
		userKey=key[key_num]
	await m.reply_text(str(res.json()))
	url1 = os.environ["url1"]
	
	params1 = {
	  'prompt': x,
	  'seed': "-1",
	  'resolution': y,
	  'guidanceScale': "7",
	  'negativePrompt': "",
	  'channel': os.environ["channel"],
	  'subChannel': "public",
	  'userKey': userKey,
	  'adAccessCode': "",
	  'requestId': "0.7627234888992518",
	  '__cacheBust': str(random.randint(100000000000000000,9999999999999999999)/10000000000000000000)
	}
	if True:
		response = requests.post(url1, params=params1, headers=headersai)
		await m.reply_text(str(response.json()))
		url3 = os.environ["url3"]
		params = {
		  'imageId': response.json()["imageId"]
		}
		response = requests.get(url3, params=params, headers=headersai)
		
		f= open(f"polls_quiz.jpg","wb")
		f.write(response.content)
		f.close
		return f"polls_quiz.jpg"

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

#print(scheduler.add_job(all_restart_hibernation, 'interval', minutes=30,args=("x",)))

@app_bot.on_message(filters.regex("^/text_to_image") & filters.incoming)
async def text_to_image(client:Client,message:Message):
	query=re.split("\n",message.text)
	sucess=False
	if len(query)==1:
		await message.reply_text("invalid command")
	elif len(query)==2:
		sucess=True
		query.append("3")
	elif len(query)==3:
		sucess=True
	else:
		await message.reply_text("invalid command\n\nreason = more then 3 line is provide. Syntex= /text_to_image\nquery\nNumber of images")
		sucess=False
	if sucess:
		for x in range(int(query[2])):
			await message.reply_photo(await gen(query[1] ,"512x768",message))

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