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
import tgcrypto,asyncio,datetime
app_bot=Client("classplus_test",bot_token=os.environ["Soojh"],api_id=os.environ["api_id"],api_hash=os.environ["api_hash"])
from find_train import spliter,live_train_details,new_find_station_code,new_trains_between_stations
#callback_query.message.chat.id
@app_bot.on_message(filters.regex("^/train$") & ~ filters.scheduled )#& filters.incoming)
async def job2_partener2(client:Client,message:Message):
	await app_bot.send_message(message.chat.id, str("""commands is here

1) `/find_station Jai`
to get Jai....... station details

2) `/train_btw_station AWR JP """+(datetime.datetime.now()+datetime.timedelta(hours=5,minutes=30)).strftime("%d-%m-%Y")+"""`
to get train details between two stations

3) `/live_train_status 15013 0`
to get live train details 
0 means train start today 
-1 means train start yesterday and today is 2 day of train
1 means train will start tomorrow 

more command comming soon"""))

@app_bot.on_message(filters.regex("^/find_station ") & ~ filters.scheduled )#& filters.incoming)
async def job2_partener2_1(client:Client,message:Message):
	A=await new_find_station_code(re.sub("/find_station( |\n)","",message.text))
	for x in spliter(A):
		await app_bot.send_message(message.chat.id, str(x))
		if message.chat.id<0:
			await asyncio.sleep(5)
	await asyncio.sleep(5)
@app_bot.on_message(filters.regex("^/train_btw_station ") & ~ filters.scheduled )#& filters.incoming)
async def job2_partener2_2(client:Client,message:Message):
	q=re.split(" {1,}",re.sub("/train_btw_station( |\n)","",message.text))
	a=q[0]
	b=q[1]
	if len(q)>2:
		c=q[2]
	else:
		c=None
	A=await new_trains_between_stations(a,b,c)
	for x in spliter(A):
		await app_bot.send_message(message.chat.id, str(x))
		if message.chat.id<0:
			await asyncio.sleep(5)
	await asyncio.sleep(5)
@app_bot.on_message(filters.regex("^/live_train_status( |\n)\d{1,}") & ~ filters.scheduled )#& filters.incoming)
async def job2_partener2_3(client:Client,message:Message):
	await app_bot.send_message(message.chat.id, "Bot is Alive! finding your train details...\nDon't forget to join channel @Polls_Quiz")
	q=re.split(" {1,}",re.sub("/live_train_status( |\n)","",message.text))
	a=q[0]
	if len(q)>1:
		b=str(int(q[1])*(-1))
	else:
		b="0"
	A,B,C,D=await live_train_details(a,b)
	for x in spliter(A):
		await app_bot.send_message(message.chat.id, str(x))
		if message.chat.id<0:
			await asyncio.sleep(5)
	await asyncio.sleep(5)
	for x in spliter(D):
		await app_bot.send_message(message.chat.id, str(x))
		if message.chat.id<0:
			await asyncio.sleep(5)
	await asyncio.sleep(5)
	for x in spliter(B):
		await app_bot.send_message(message.chat.id, str(x))
		if message.chat.id<0:
			await asyncio.sleep(5)
	await asyncio.sleep(5)
	for x in spliter(C):
		await app_bot.send_message(message.chat.id, str(x))
		if message.chat.id<0:
			await asyncio.sleep(5)
	
	
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





async def gen(y,m):
	payload = json.dumps({
	  "prompt": y
	})
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
	  'Content-Type': "application/json"
	}
	
	response = requests.post(os.environ["url1"], data=payload, headers=headers)
	
	
	
	
	url2 = os.environ["url2"]+response.json()["uuid"]
	print(response.json())
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
	}
	
	response = requests.get(url2, headers=headers)
	
	while len(response.json()["images"])==0:
		response = requests.get(url2, headers=headers)
		
	for i,x in enumerate(response.json()["images"]):
		response = requests.get(os.environ["url3"]+x)
		f= open(f"polls_quiz_y {i+1}.jpg","wb")
		f.write(response.content)
		f.close
		await m.reply_photo(f"polls_quiz_y {i+1}.jpg", caption="created by @SoojhBoojh_Bot")
		await asyncio.sleep(5)

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
os.system("playwright install")
#os.system("sudo playwright install-deps")
@app_bot.on_message(filters.regex("^/text_to_image") & filters.incoming)
async def text_to_image(client:Client,message:Message):
	query=re.split("\n",message.text)
	sucess=False
	if len(query)==1:
		await message.reply_text("invalid command")
	else:
		sucess=True
	if sucess:
		await gen("\n".join(query[1:]) ,message)
		await message.reply_text(str(os.system(f'/home/adminuser/venv/bin/python  main.py -f newimage{message.chat.id} -n 3 -p "'+"\n".join(query[1:])+'"'))[:4000])
		for zz in range(3):
			await message.reply_photo(f"generated-pictures/newimage{message.chat.id}{zz+1}.jpeg", caption="created by @SoojhBoojh_Bot")
			os.remove(f"generated-pictures/newimage{message.chat.id}{zz+1}.jpeg")
		
		

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