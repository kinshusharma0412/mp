#!/usr/bin/env python
# -*- coding: utf-8 -*-
Profile_photo_soojh=[-1001536663326,-1001375781470,-1001360402430,-1001500806585,-1001472812678,-1001145720099,-1001373589965]
import time
import streamlit as st
import os, random
from pyrogram import Client, enums
from pyrogram.methods.utilities.idle import idle
import sys
url_page=sys.argv[1]
print(url_page)
from box import box
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
import asyncio
from pyrogram.errors import FloodWait
import  json
import time, random,string
import re as reaaa
import requests
import random,string
from prog_bar import progress_for_pyrogram
import uvloop
uvloop.install()
def id_generator(size=10, chars=string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))
import time,datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from urlextract import URLExtract
extractor = URLExtract()

scheduler = AsyncIOScheduler(timezone="Asia/kolkata")
scheduler.start()
shubham=Client("shubhem new",session_string=os.environ['shubhem'],api_id="13682659",api_hash="b984d240c5258407ea911f042c9d75f6")
mohit=Client("mohit",session_string=os.environ['mohit'],api_id="13682659",api_hash="b984d240c5258407ea911f042c9d75f6")
monu=Client("monu",session_string=os.environ['monu'],api_id="13682659",api_hash="b984d240c5258407ea911f042c9d75f6")
sonu=Client("sonu kumar",session_string=os.environ['sonu'],api_id="13682659",api_hash="b984d240c5258407ea911f042c9d75f6")
Soojh = Client("SoojhT",
bot_token=os.environ['Soojh'],
api_id="13682659",
api_hash="b984d240c5258407ea911f042c9d75f6")
headersList = {
	        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	        "Accept-Encoding": "gzip, deflate, br",
	        "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
	        "Connection": "keep-alive",
	        "Cookie": os.environ['Cookie'],
	        "DNT": "1",
	        "Host": "www.terabox.app",
	        "Sec-Fetch-Dest": "document",
	        "Sec-Fetch-Mode": "navigate",
	        "Sec-Fetch-Site": "none",
	        "Sec-Fetch-User": "?1",
	        "Upgrade-Insecure-Requests": "1",
	        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
	        "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
	        "sec-ch-ua-mobile": "?0",
	        "sec-ch-ua-platform": '"Windows"',
	    }
def translate_en(x):
	url=os.environ["translate"]
	try:
		payload = json.dumps({
		  "from": "en_US",
		  "to": "hi_IN",
		  "text": str(x)
		})
		headers = {
		  'Content-Type': "application/json",
		  'authorization': "Bearer a_25rccaCYcBC9ARqMODx2BV2M0wNZgDCEl3jryYSgYZtF1a702PVi4sxqi2AmZWyCcw4x209VXnCYwesx",
		}
		response = requests.post(url, data=payload, headers=headers)
		return response.json()["result"]
	except:
		return x
@Soojh.on_message(filters.regex("(share|app|box)\.com") & filters.chat(["kinbin246",6779478298]) & filters.incoming & ~ filters.scheduled )#& filters.incoming)
async def job2g_partener4(client:Client,message:Message):
	yy=extractor.find_urls(reaaa.sub("\n", " ",message.text))
	for x in message.entities:
		if str(x.type)=="URL":
			yy.append()
	zz=[]
	for y in yy:
		if y not in zz:
			zz.append(y)
	yy=zz
			
		
	await client.send_message(message.chat.id,str(yy))
	for x in yy:
		mess=await client.send_message(message.chat.id,"Downloading is progressing...")
		try:
			file_name=x
			data,thumb=await box(x,mess)
			await asyncio.sleep(1)
			await client.send_video(message.chat.id,data,thumb=thumb,progress=progress_for_pyrogram,progress_args=(
	                    "<b>Uploading :- </b> "+data, mess, time.time()
	                ))
			await asyncio.sleep(1)
			os.remove(data)
		except:
			await mess.edit("Error link: "+x+"\n\nTerabox not support this link")
		
			
@monu.on_message(filters.regex("^(https://t.me/|Me/).*?(-|–)\d{1,}") & filters.private & ~ filters.scheduled )#& filters.incoming)
@shubham.on_message(filters.regex("^(https://t.me/|Me/).*?(-|–)\d{1,}") & filters.private & ~ filters.scheduled )#& filters.incoming)
@sonu.on_message(filters.regex("^(https://t.me/|Me/).*?(-|–)\d{1,}") & filters.private & ~ filters.scheduled )#& filters.incoming)
@mohit.on_message(filters.regex("^(https://t.me/|Me/).*?(-|–)\d{1,}") & filters.chat(["me","kinbin246",6287942937,6892701715]) & ~ filters.scheduled )#& filters.incoming)
async def job2g_partener2(client:Client,message:Message):
	
		yyy=reaaa.split("-|–|/",message.text)
		zzz="/".join(yyy[:-2])
		links=""
		for y in range(int(yyy[-2]),int(yyy[-1])+1):
			links+="/".join(yyy[:-2])+"/"+str(y)+"\n"
		yy=reaaa.split("\n",links[:-1])
		for x in yy:
			mid=None
			
			zz=reaaa.sub("^(https://t.me/|Me/)","",x)
			xx=reaaa.sub("c/","-100",zz)
			xx=reaaa.split("/",xx)
			try:
				y=await client.get_messages(int(xx[0]),int(xx[1]))
			except:
				y=await client.get_messages(xx[0],int(xx[1]))
			try:
				
				mid=(await client.send_message(message.chat.id,str(str(xx[1])+"). downloading is progressing..."))).id
				async def progress(current, total,message,client,mid,zzz):
					if current*100%11 ==0:
						if mid is None:
							await client.send_message(message.chat.id,str(f"{current * 100 / total:.1f}% "+zzz))
						else:
							pass#await asyncio.sleep(1)#await shubham.edit_message_text(message.chat.id,mid,str(f"{current * 100 / total:.1f}% "+zzz))
				
				
				
				z=await client.download_media(y, progress=progress,progress_args=(message,client,mid,"downloading"))
				if "." in z:
					await client.send_document(message.chat.id,z,caption=str(y.caption),caption_entities=y.caption_entities,progress=progress,progress_args=(message,client,mid,"uploading"))
				
				else:
					await client.send_document(message.chat.id,z,caption=str(y.caption),file_name=reaaa.split("/",z)[-1]+".mp4",caption_entities=y.caption_entities,progress=progress,progress_args=(message,client,mid,"uploading"))
		
				await client.delete_messages(chat_id=message.chat.id, message_ids=mid)
				os.remove(z)
		#
			except Exception as e:
				try:
					await client.edit_message_text(message.chat.id, mid,text=y.text,entities=y.entities)
				except:
					await client.edit_message_text(message.chat.id, mid,text=str(x)+" Error details : "+str(e))
		await asyncio.sleep(1)
	
#@monu.on_message(filters.regex("^(https://t.me/|Me/).*?\n") & filters.chat(["me","kinbin246",598871517]) & ~ filters.scheduled )#& filters.incoming)
async def job2g_partener2(client:Client,message:Message):
	
        
        
        yy=reaaa.split("\n",message.text)
        for x in yy:
        	mid=None
        	try:
	        	zz=reaaa.sub("^(https://t.me/|Me/)","",x)
		        xx=reaaa.sub("c/","-100",zz)
		        xx=reaaa.split("/",xx)
		        try:
		        	y=await monu.get_messages(int(xx[0]),int(xx[1]))
		        except:
		        	y=await monu.get_messages(xx[0],int(xx[1]))
		        
		        mid=(await monu.send_message(message.chat.id,str("downloading is progressing..."))).id
		        async def progress(current, total,message,client,mid,zzz):
		        	if current*100%11 ==0:
			        	if mid is None:
				        	await monu.send_message(message.chat.id,str(f"{current * 100 / total:.1f}% "+zzz))
			        	else:
				        	pass#await asyncio.sleep(1)#await monu.edit_message_text(message.chat.id,mid,str(f"{current * 100 / total:.1f}% "+zzz))
				
		        
		        
		        z=await monu.download_media(y, progress=progress,progress_args=(message,client,mid,"downloading"))
		        await monu.send_document(message.chat.id,z,caption=str(y.caption),caption_entities=y.caption_entities,progress=progress,progress_args=(message,client,mid,"uploading"))
		
		        await monu.delete_messages(chat_id=message.chat.id, message_ids=mid)
		        os.remove(z)
		#
	        except Exception as e:
		        await monu.edit_message_text(message.chat.id, mid,x+" Error:- "+str(e))
		
		
#@mohit.on_message(filters.regex("^(https://t.me/|Me/).*?\n") & filters.chat(["me","kinbin246",598871517]) & ~ filters.scheduled )#& filters.incoming)
async def job2g_partener2(client:Client,message:Message):
	
        
        
        yy=reaaa.split("\n",message.text)
        for x in yy:
        	mid=None
        	try:
	        	zz=reaaa.sub("^(https://t.me/|Me/)","",x)
		        xx=reaaa.sub("c/","-100",zz)
		        xx=reaaa.split("/",xx)
		        try:
		        	y=await client.get_messages(int(xx[0]),int(xx[1]))
		        except:
		        	y=await client.get_messages(xx[0],int(xx[1]))
		        
		        mid=(await client.send_message(message.chat.id,str("downloading is progressing..."))).id
		        async def progress(current, total,message,client,mid,zzz):
		        	if current*100%11 ==0:
			        	if mid is None:
				        	await client.send_message(message.chat.id,str(f"{current * 100 / total:.1f}% "+zzz))
			        	else:
				        	pass#await asyncio.sleep(1)#await sonu.edit_message_text(message.chat.id,mid,str(f"{current * 100 / total:.1f}% "+zzz))
				
		        
		        
		        z=await client.download_media(y, progress=progress,progress_args=(message,client,mid,"downloading"))
		        await client.send_document(message.chat.id,z,caption=str(y.caption),caption_entities=y.caption_entities,progress=progress,progress_args=(message,client,mid,"uploading"))
		
		        await client.delete_messages(chat_id=message.chat.id, message_ids=mid)
		        os.remove(z)
		#
	        except Exception as e:
		        await client.edit_message_text(message.chat.id, mid,x+" Error:- "+str(e))


def profile_photo_soojh():
	Soojh.send_message("BotFather","/setuserpic")
	Soojh.send_message("BotFather","@soojhboojh_bot")
	ids=[]
	for x in Soojh.search_messages(random.choice(Profile_photo_soojh),filter=enums.MessagesFilter.PHOTO):
		ids.append({str(x.chat.id):x.id})
	choice=(random.choice(ids))
	caption=""
	try:
		photo=(Soojh.get_messages(list(choice.keys())[0],list(choice.values())[0]+1))
		caption="https://t.me/c/"+reaaa.sub("-100","",str(photo.chat.id))+"/"+str(photo.id)
		photo=Soojh.download_media(photo.document.file_id,file_name=photo.document.file_name)
		#print(photo)
		Soojh.send_photo("BotFather",photo,caption=caption )
	except Exception as e:
		#Soojh.send_message("kinbin246",str(e)+"\n\n"+caption,disable_web_page_preview=True)
		photo=(Soojh.get_messages(list(choice.keys())[0],list(choice.values())[0]))
		caption="https://t.me/c/"+reaaa.sub("-100","",str(photo.chat.id))+"/"+str(photo.id)
		photo=Soojh.download_media(photo.photo.file_id,file_name=photo.photo.file_name)
		#print(photo)
		Soojh.send_photo("BotFather",photo,caption=caption )
	os.remove(photo)
#scheduler.add_job(profile_photo_soojh,"interval", minutes=1,id="minutes")
#print(scheduler.add_job(all_restart_hibernation, 'cron', hour=7,minute=50,args=("x",)))
def hibernation(x):
	headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
  'Accept': "application/json, text/plain, */*",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'sec-ch-ua': "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
  'x-csrf-token': os.environ["xcsrftoken"],
  'sec-ch-ua-mobile': "?1",
  'sec-ch-ua-platform': "\"Android\"",
  'origin': "https://share.streamlit.io",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://share.streamlit.io/",
  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
  'Cookie': os.environ["cookies_header"]
}
	url = "https://share.streamlit.io/api/v2/apps/"+x+"/restart"
	response = requests.post(url, headers=headers)
	shubham.send_message("Kinbin246","bot start message\n\n"+str(response.text))

#@monu.on_message(filters.text & filters.outgoing & ~ filters.scheduled)#& filters.incoming)
@shubham.on_message(filters.text & filters.outgoing & ~ filters.scheduled)#& filters.incoming)
#@mohit.on_message(filters.text & filters.outgoing & ~ filters.scheduled)#& filters.incoming)
async def job2g_partener2(client:Client,message:Message):
	await message.edit_text(translate_en(message.text))


for x in range(1,24):
	print(scheduler.add_job(hibernation, 'cron', hour=x,minute=40,args=('fe40a14b-bf57-4e11-b4b7-9b45b94d12e9',)))
print(scheduler.add_job(hibernation, 'cron', hour=7,minute=30,args=('568d29c8-cc98-4cee-937b-144d7ddf94f3',)))
print(scheduler.add_job(hibernation, 'cron', hour=15,minute=30,args=('568d29c8-cc98-4cee-937b-144d7ddf94f3',)))
def main():
	@st.cache_resource
	def init_connection1():
		return shubham.start()
	@st.cache_resource
	def init_connection2():
		return monu.start()
	@st.cache_resource
	def init_connection3():
		return mohit.start()
	_=init_connection1()
	_=init_connection2()
	_=init_connection3()
	
	@st.cache_resource
	def init_connection2():
		return sonu.start()
	#_=init_connection2()
	@st.cache_resource
	def init_connection2():
		return Soojh.start()
	_=init_connection2()
	
	st.write(url_page)
	shubham.send_message("Kinbin246","Shubham Bot Restart Sucessful url = "+str(url_page),disable_web_page_preview=True)
	monu.send_message("Kinbin246","[monu Bot Restart Sucessful]("+url_page+")",disable_web_page_preview=True)
	#sonu.send_message("Kinbin246","[sonu Bot Restart Sucessful]("+url_page+")",disable_web_page_preview=True)
	#sonu.send_message("Kinbin246","[sonu Bot Restart Sucessful]("+url_page+")",disable_web_page_preview=True)
	idle()
	shubham.send_message("Kinbin246","Shubham Bot stoped")
	monu.send_message("Kinbin246","monu Bot stoped")
	#sonu.send_message("Kinbin246","sonu Bot stoped")
	#Soojh.send_message("Kinbin246","sonu Bot stoped")
	shubham.stop()
	monu.stop()
	#sonu.stop()
	#Soojh.stop()

if __name__ == '__main__':
    main()#


	
