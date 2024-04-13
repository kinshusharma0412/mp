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

def id_generator(size=10, chars=string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))
import time,datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
scheduler = AsyncIOScheduler(timezone="Asia/kolkata")
scheduler.start()
shubham=Client("shubhem new",session_string=os.environ['shubhem'],api_id="13682659",api_hash="b984d240c5258407ea911f042c9d75f6")
ajay=Client("ajay kumar",session_string="BQDQx-MAKUPughkTOuqfEd0qrQ1SjO6sUcM_NjXy6G330LloOHPRHlEQioLBiNguNAWJKon3rmskFxCd_HlZmdLR-xrvQNBXX8TD8ra5rGqdjeq5cWfnJPfegUtFluc5mY-pf8DW-9jo5k6eq1G1BdGVYyne6q2HurLeSH_60CFpPRpRKCjJ0LZeHte5uMnYr61jP8FvAZEzRDXTf692fbbjNbIuFSPenZbYHi7jV7mDq1HYA2mjXc7Kgl2tapFsY7mA9yDarTILF5kdgAELq0I524JVVD7F_xzs8UFD2Fhz_iPWdiemXDcwAAAAFG9pXoAA",api_id="13682659",api_hash="b984d240c5258407ea911f042c9d75f6")
sonu=Client("sonu kumar",session_string="BQDQx-MAu5H0aHV_jebewJzC_jqu4v4ZhB94iPIs9JLLkkjHSPrEbC8AGTX-IzOFI7ijQ1mdmwNpXZFL5fANFSBy2M5r6zUJltR-xJsQicsIeQZ0QjCUeFA6o64KIENGE0j_K6UssGwh7j-G9uHcPPN1dthewNzdDLcRvITu9Gcx1EsUjvQth_TZz5AxudPX6fnAOolKIa3BIEJKAUFHbpfyCp8Xq_HjdcFilHwy4KSd0I_xc_uE1UxYBfO3EPaT-GPbfseGdI_FpPYrTAusD_HMToTkVy0b41Hw5QI6FAYr8_7AqcMY-SzH6wJufhHKjUOOvwAAAAGQRHZnAA",api_id="13682659",api_hash="b984d240c5258407ea911f042c9d75f6")
robo = Client("ROBOT",
#bot_token="6200186150:AAFq1E9S9CgV-l",
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
@shubham.on_message(filters.regex("^https\://.*app\.com.*?\n") & filters.chat(["me","kinbin246",6287942937,6892701715]) & ~ filters.scheduled )#& filters.incoming)
async def job2g_partener4(client:Client,message:Message):
	yy=reaaa.split("\n",message.text)
	await client.send_message(message.chat.id,str("downloading is progressing..."))
	for x in yy:
		try:
			data=box(x)
			await client.send_video(message.chat.id,video=data["file_name"], caption="["+data["file_name"]+"]("+data["link"]+")",thumb="thumb.jpeg",file_name=data["file_name"])
			os.remove(data["file_name"])
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			await client.send_message(message.chat.id,(str(exc_type)+"\n\n"+ fname+"\n\n"+str(e)+"\n\n"+str(exc_tb.tb_lineno))[0:4090])


@shubham.on_message(filters.regex("^(https://t.me/|Me/).*?\n") & filters.chat(["me","kinbin246",6287942937,6892701715]) & ~ filters.scheduled )#& filters.incoming)
async def job2g_partener2(client:Client,message:Message):
	
        
        
        yy=reaaa.split("\n",message.text)
        for x in yy:
        	mid=None
        	try:
	        	zz=reaaa.sub("^(https://t.me/|Me/)","",x)
		        xx=reaaa.sub("c/","-100",zz)
		        xx=reaaa.split("/",xx)
		        try:
		        	y=await shubham.get_messages(int(xx[0]),int(xx[1]))
		        except:
		        	y=await shubham.get_messages(xx[0],int(xx[1]))
		        
		        mid=(await shubham.send_message(message.chat.id,str("downloading is progressing..."))).id
		        async def progress(current, total,message,client,mid,zzz):
		        	if current*100%11 ==0:
			        	if mid is None:
				        	await shubham.send_message(message.chat.id,str(f"{current * 100 / total:.1f}% "+zzz))
			        	else:
				        	pass#await asyncio.sleep(1)#await shubham.edit_message_text(message.chat.id,mid,str(f"{current * 100 / total:.1f}% "+zzz))
				
		        
		        
		        z=await shubham.download_media(y, progress=progress,progress_args=(message,client,mid,"downloading"))
		        if "." in z:
		        	await shubham.send_document(message.chat.id,z,caption=str(y.caption),caption_entities=y.caption_entities,progress=progress,progress_args=(message,client,mid,"uploading"))
		        
		        else:
		        	await shubham.send_document(message.chat.id,z,caption=str(y.caption),file_name=reaaa.split("/",z)[-1]+".mp4",caption_entities=y.caption_entities,progress=progress,progress_args=(message,client,mid,"uploading"))
		
		        await shubham.delete_messages(chat_id=message.chat.id, message_ids=mid)
		        os.remove(z)
		#
	        except Exception as e:
		        await shubham.edit_message_text(message.chat.id, mid,x+" Error:- "+str(e))
	
@ajay.on_message(filters.regex("^(https://t.me/|Me/).*?\n") & filters.chat(["me","kinbin246",598871517]) & ~ filters.scheduled )#& filters.incoming)
async def job2g_partener2(client:Client,message:Message):
	
        
        
        yy=reaaa.split("\n",message.text)
        for x in yy:
        	mid=None
        	try:
	        	zz=reaaa.sub("^(https://t.me/|Me/)","",x)
		        xx=reaaa.sub("c/","-100",zz)
		        xx=reaaa.split("/",xx)
		        try:
		        	y=await ajay.get_messages(int(xx[0]),int(xx[1]))
		        except:
		        	y=await ajay.get_messages(xx[0],int(xx[1]))
		        
		        mid=(await ajay.send_message(message.chat.id,str("downloading is progressing..."))).id
		        async def progress(current, total,message,client,mid,zzz):
		        	if current*100%11 ==0:
			        	if mid is None:
				        	await ajay.send_message(message.chat.id,str(f"{current * 100 / total:.1f}% "+zzz))
			        	else:
				        	pass#await asyncio.sleep(1)#await ajay.edit_message_text(message.chat.id,mid,str(f"{current * 100 / total:.1f}% "+zzz))
				
		        
		        
		        z=await ajay.download_media(y, progress=progress,progress_args=(message,client,mid,"downloading"))
		        await ajay.send_document(message.chat.id,z,caption=str(y.caption),caption_entities=y.caption_entities,progress=progress,progress_args=(message,client,mid,"uploading"))
		
		        await ajay.delete_messages(chat_id=message.chat.id, message_ids=mid)
		        os.remove(z)
		#
	        except Exception as e:
		        await ajay.edit_message_text(message.chat.id, mid,x+" Error:- "+str(e))
		
		
@sonu.on_message(filters.regex("^(https://t.me/|Me/).*?\n") & filters.chat(["me","kinbin246",598871517]) & ~ filters.scheduled )#& filters.incoming)
async def job2g_partener2(client:Client,message:Message):
	
        
        
        yy=reaaa.split("\n",message.text)
        for x in yy:
        	mid=None
        	try:
	        	zz=reaaa.sub("^(https://t.me/|Me/)","",x)
		        xx=reaaa.sub("c/","-100",zz)
		        xx=reaaa.split("/",xx)
		        try:
		        	y=await sonu.get_messages(int(xx[0]),int(xx[1]))
		        except:
		        	y=await sonu.get_messages(xx[0],int(xx[1]))
		        
		        mid=(await sonu.send_message(message.chat.id,str("downloading is progressing..."))).id
		        async def progress(current, total,message,client,mid,zzz):
		        	if current*100%11 ==0:
			        	if mid is None:
				        	await sonu.send_message(message.chat.id,str(f"{current * 100 / total:.1f}% "+zzz))
			        	else:
				        	pass#await asyncio.sleep(1)#await sonu.edit_message_text(message.chat.id,mid,str(f"{current * 100 / total:.1f}% "+zzz))
				
		        
		        
		        z=await sonu.download_media(y, progress=progress,progress_args=(message,client,mid,"downloading"))
		        await sonu.send_document(message.chat.id,z,caption=str(y.caption),caption_entities=y.caption_entities,progress=progress,progress_args=(message,client,mid,"uploading"))
		
		        await sonu.delete_messages(chat_id=message.chat.id, message_ids=mid)
		        os.remove(z)
		#
	        except Exception as e:
		        await sonu.edit_message_text(message.chat.id, mid,x+" Error:- "+str(e))
def hibernation():
	status_code_now=requests.head(url_page).status_code
	robo.send_message("kinbin246",str(status_code_now))
def profile_photo_soojh():
	robo.send_message("BotFather","/setuserpic")
	robo.send_message("BotFather","@soojhboojh_bot")
	ids=[]
	for x in robo.search_messages(random.choice(Profile_photo_soojh),filter=enums.MessagesFilter.PHOTO):
		ids.append({str(x.chat.id):x.id})
	choice=(random.choice(ids))
	caption=""
	try:
		photo=(robo.get_messages(list(choice.keys())[0],list(choice.values())[0]+1))
		caption="https://t.me/c/"+reaaa.sub("-100","",str(photo.chat.id))+"/"+str(photo.id)
		photo=robo.download_media(photo.document.file_id,file_name=photo.document.file_name)
		#print(photo)
		robo.send_photo("BotFather",photo,caption=caption )
	except Exception as e:
		#robo.send_message("kinbin246",str(e)+"\n\n"+caption,disable_web_page_preview=True)
		photo=(robo.get_messages(list(choice.keys())[0],list(choice.values())[0]))
		caption="https://t.me/c/"+reaaa.sub("-100","",str(photo.chat.id))+"/"+str(photo.id)
		photo=robo.download_media(photo.photo.file_id,file_name=photo.photo.file_name)
		#print(photo)
		robo.send_photo("BotFather",photo,caption=caption )
	os.remove(photo)
scheduler.add_job(profile_photo_soojh,"interval", minutes=1,id="minutes")
print(scheduler.add_job(hibernation,"interval", days=1,id="day"))
def main():
	@st.cache_resource
	def init_connection1():
		return shubham.start()
	@st.cache_resource
	def init_connection2():
		return ajay.start()
	@st.cache_resource
	def init_connection3():
		return sonu.start()
	_=init_connection1()
	#_=init_connection2()
	#_=init_connection3()
	
	@st.cache_resource
	def init_connection2():
		return robo.start()
	#_=init_connection2()
	
	st.write(url_page)
	shubham.send_message("Kinbin246","Shubham Bot Restart Sucessful url = "+str(url_page),disable_web_page_preview=True)
	#ajay.send_message("Kinbin246","[Ajay Bot Restart Sucessful]("+url_page+")",disable_web_page_preview=True)
	#sonu.send_message("Kinbin246","[sonu Bot Restart Sucessful]("+url_page+")",disable_web_page_preview=True)
	idle()
	shubham.send_message("Kinbin246","Shubham Bot stoped")
	#ajay.send_message("Kinbin246","Ajay Bot stoped")
	#sonu.send_message("Kinbin246","sonu Bot stoped")
	#robo.send_message("Kinbin246","sonu Bot stoped")
	shubham.stop()
	#ajay.stop()
	#sonu.stop()
	#robo.stop()

if __name__ == '__main__':
    main()#


	
