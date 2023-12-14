#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random,string
def id_generator(size=10, chars=string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))
import time,datetime
import streamlit as st
import os, random
from pyrogram import Client, enums
from pyrogram.methods.utilities.idle import idle
import sys
url_page=sys.argv[1]
print(url_page)

from pyrogram.raw import functions
from pyrogram.raw import types
from pyrogram.handlers import MessageHandler, PollHandler
from pyrogram import filters
from pyrogram.types import Message, ReplyKeyboardRemove, Poll
from pyrogram.types import ReplyKeyboardMarkup as RKM
from pyrogram.types import InlineKeyboardMarkup as IKM
from pyrogram.types import InlineKeyboardButton as IKB
from pyrogram.enums import PollType
from apscheduler.schedulers.asyncio import AsyncIOScheduler
scheduler = AsyncIOScheduler(timezone="Asia/kolkata")
scheduler.start()
import asyncio
from pyrogram.errors import FloodWait
import  json
import time, random,string
import re as reaaa
import requests
try:
	import dns.resolver
	dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
	dns.resolver.default_resolver.nameservers=['8.8.8.8']
except:
	 import dns
from pymongo import MongoClient
mongodb=os.environ['mongodb']
bot_token=os.environ['bot_token']
cm=clientmongo=MongoClient(mongodb)

app=Client("Expressway attendance bot",bot_token=bot_token, api_id="13682659",api_hash="b984d240c5258407ea911f042c9d75f6")

@app.on_message(filters.photo & filters.private)
async def img_text(client:Client,message:Message):
	fname=id_generator()
	try:
		db=cm["sharma_ji"]["Employee"].find_one({"db":{"$type":"object"}})["db"][str(message.chat.id)]
	except:
		await app.send_message(message.chat.id, "अभी आपका टेलीग्राम account हमसे जुड़ा हुआ नही है।")
	fulltime=cm["sharma_ji"]["Employee"].find_one({"time":{"$type":"array"}})["time"]
	print (db)
	employee_id=db[0]
	post=db[1]
	user=message.from_user
	name=user.first_name
	timenow=(time.ctime(time.time()+5.5*3600))
	current=(time.localtime(time.time()+5.5*3600))
	now=current.tm_hour*60*60+current.tm_min*60+current.tm_sec
	full_time=[]
	for x in fulltime:
		y=x.split(":")
		full_time.append(3600*int(y[0])+60*int(y[1]))
	if (5*3600-10)<full_time[0]<(10*3600+10):
		shift = "SHIFT - '🅰'"
	else:
		shift = "SHIFT - '🅱'"
		
	text1=""
	if full_time[0]<full_time[1]<full_time[2]<full_time[3]<full_time[4]:
		pass
	else:
		for x in range(len(full_time)):
			if full_time[x]<43200:
				full_time[x]=full_time[x]+86400
		if now<43200:
			now+=86400
		
	if now<full_time[0]:
		text1="आप ड्यूटी पर समय से पहले आ गए हो हाजिरी लगाने के निश्चित समय अंतराल में ही हाजिरी लगावे।"
	elif full_time[0]<=now<full_time[1]:
		text1="ध्न्यवाद अपने सही समय पर हाजिरी भेज दी है। सेफ्टी जैकेट और ड्रेस के साथ आए।"
	elif full_time[1]<=now<full_time[2]:
		text1="आपने अपनी समय अवधि में हाजिरी नहीं भेजी, इसलिए आपकी आधा दिन की हाजिरी का पैसा काटा जाएगा। सही समयावधि -> "+fulltime[0]+"-"+fulltime[1]+ " है।"
	elif full_time[2]<=now<full_time[3]:
		text1="आपका हाजिरी लगाने का समय खत्म हो चुका है इसलिए अब आपका एब्सेंट लगेगा।"
	elif full_time[3]<=now<full_time[4]:
		text1="bye! आपका साथी आने के बाद आप जा सकते है।"
	elif full_time[4]<=now:
		text1="bye! आपका साथी आने के बाद आप जा सकते है।"
	
		
	
	try:
		name=user.first_name+" "+user.last_name
	except:
		pass
	file=await app.download_media(message,file_name=fname+"sample.png")
	try:
		await app.send_photo(-1002050870187, fname+"sample.png",caption=f"""📛 Name: {name}
📮 Post: {post}
⏳ Time: {timenow}
Employee 🆔: {employee_id}
{shift}
Note: {text1}""")
	except:
		await app.send_photo(-1002050870187, "downloads/"+fname+"sample.png",caption=f"""📛 Name: {name}
📮 Post: {post}
⏳ Time: {timenow}
Employee 🆔: {employee_id}
{shift}
Note: {text1}""")
	await app.send_message(message.chat.id, f"""📛 Name: {name}
📮 Post: {post}
⏳ Time: {timenow}
Employee 🆔: {employee_id}
{shift}
Note: {text1}""")
def first_job(y,z):
	cid=[]
	for member in app.get_chat_members(-1002050870187):
		if member.user.id!=6967412548:
			cid.append(member.user.id)
	for x in cid:
		try:
			app.send_message(x, f"सभी {y} के स्टाफ अथवा गॉर्ड अपनी अपनी हाजिरी टाइम स्टांप कैमरे के साथ {z} बजे से पहले जरूर डाल देवे।")
		except :
			app.send_message(5948488950, f"I'd {x} user ने बोट को /start नही कर रखा है अभी तक।")

try:
	fulltime=cm["sharma_ji"]["Employee"].find_one({"time":{"$type":"array"}})
	if fulltime is not None:
		fulltime=fulltime["time"]
		
		a=fulltime[0].split(":")
		b=fulltime[1].split(":")
		if b[0]>12:
			new= str(int(b[0])-12)+":"+b[1]+" PM"
		else:
			new= str(int(b[0]))+":"+b[1]+" AM"
		if len(new)==7:
			new="0"+new
		if (5*3600-10)<3600*int(a[0])+60*int(a[1])<(10*3600+10):
			shift = "SHIFT - '🅰'"
		else:
			shift = "SHIFT - '🅱'"
		
		
		scheduler.add_job(first_job, "cron",day_of_week="mon-sun",hour=int(a[0]), minute=int(a[1]), replace_existing=True,args=(shift,new) ,id="job1")
except Exception as e:
	print (e)


@app.on_message(filters.regex("^\[(\"|')\d{1,}:\d{1,}(\"|'),( |)(\"|')\d{1,}:\d{1,}(\"|'),( |)(\"|')\d{1,}:\d{1,}(\"|'),( |)(\"|')\d{1,}:\d{1,}(\"|'),( |)(\"|')\d{1,}:\d{1,}(\"|')\]") & filters.private)
async def add_time(client:Client,message:Message):
	timer=eval(message.text)
	cm["sharma_ji"]["Employee"].find_one_and_update({"time":{"$type":"array"}},{ "$set": {"time":timer}})
	await app.send_message(message.chat.id, str(timer))
	fulltime=cm["sharma_ji"]["Employee"].find_one({"time":{"$type":"array"}})
	if fulltime is not None:
		fulltime=fulltime["time"]
		
		a=fulltime[0].split(":")
		b=fulltime[1].split(":")
		if b[0]>12:
			new= str(int(b[0])-12)+":"+b[1]+" PM"
		else:
			new= str(int(b[0]))+":"+b[1]+" AM"
		if len(new)==7:
			new="0"+new
		if (5*3600-10)<3600*int(a[0])+60*int(a[1])<(10*3600+10):
			shift = "SHIFT - '🅰'"
		else:
			shift = "SHIFT - '🅱'"
		
		
		ss=scheduler.add_job(first_job, "cron",day_of_week="mon-sun",hour=int(a[0]), minute=int(a[1]), replace_existing=True,args=(shift,new) ,id="job1")
		await app.send_message(message.chat.id, str(ss))
		await app.send_message(message.chat.id, str("Schedule updated"))
		
	

@app.on_message(filters.regex("^.add") & filters.private)
async def add_employ(client:Client,message:Message):
	texter=(message.text).split("\n")
	db=cm["sharma_ji"]["Employee"].find_one({"db":{"$type":"object"}})["db"]
	db[texter[1]]=[texter[2],texter[3]]
	cm["sharma_ji"]["Employee"].find_one_and_update({"db":{"$type":"object"}},{ "$set": {"db":db}})
	await app.send_message(message.chat.id, str("add sucessful"))
@app.on_message(filters.regex("^.remove") & filters.private)
async def remove_employ(client:Client,message:Message):
	texter=(message.text).split("\n")
	db=cm["sharma_ji"]["Employee"].find_one({"db":{"$type":"object"}})["db"]
	db.pop(texter[1])
	cm["sharma_ji"]["Employee"].find_one_and_update({"db":{"$type":"object"}},{ "$set": {"db":db}})
	await app.send_message(message.chat.id, str("remove sucessful"))

@app.on_message(filters.command(["start"]) & filters.private)
async def start(client:Client,message:Message):
	await app.send_message(message.chat.id, "सभी स्टाफ अपनी ड्यूटी पर पहुंचकर अपनी टाइम स्टांप कैमरे के साथ फोटो डालें, जिससे आपकी उपस्थिति दर्ज हो सके।")

@app.on_message(filters.location & filters.private)
async def start(client:Client,message:Message):
	print(message)
	await app.send_message(message.chat.id, "सभी स्टाफ अपनी ड्यूटी पर पहुंचकर अपनी टाइम स्टांप कैमरे के साथ फोटो डालें, जिससे आपकी उपस्थिति दर्ज हो सके।")

def main():
	@st.cache_resource
	def init_connection1():
		return app.start()
	_=init_connection1()
	
	app.send_message("Kinbin246","[Attendance Bot Restart sucessful]("+url_page+")",disable_web_page_preview=True)
	app.send_message("Negtestsir","[Attendance Bot Restart sucessful]("+url_page+")",disable_web_page_preview=True)
	idle()
	app.send_message("Kinbin246","[Attendance Bot stoped]("+url_page+")",disable_web_page_preview=True)
	app.send_message("Negtestsir","Attendance Bot stoped]("+url_page+")",disable_web_page_preview=True)
	app.stop()


if __name__ == '__main__':
    main()#


	
