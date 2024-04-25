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
import uvloop
uvloop.install()
def id_generator(size=10, chars=string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))
import time,datetime


mohit=Client("mohit",session_string=os.environ['mohit'],api_id="13682659",api_hash="b984d240c5258407ea911f042c9d75f6")




@mohit.on_message(filters.regex("^(https://t.me/|Me/).*?(-|–)\d{1,}") & filters.chat(reaaa.split(" ",os.environ['chat'])) & ~ filters.scheduled )#& filters.incoming)
async def job2g_partener2(client:Client,message:Message):
	
		yyy=reaaa.split("-|–|/",message.text)
		zzz="/".join(yyy[:-2])
		links=""
		for y in range(int(yyy[-2]),int(yyy[-1])+1):
			links+="/".join(yyy[:-2])+"/"+str(y)+"\n"
		yy=reaaa.split("\n",links[:-1])
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
				await client.edit_message_text(message.chat.id, mid,x+" Error:- "+str(e))
		await asyncio.sleep(1)
def main():
	@st.cache_resource
	def init_connection3():
		return mohit.start()
	_=init_connection3()
	idle()

if __name__ == '__main__':
    main()#


	
	