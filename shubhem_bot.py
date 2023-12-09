#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import streamlit as st
import os, random
from pyrogram import Client, enums
from pyrogram.methods.utilities.idle import idle
from streamlit_javascript import st_javascript

url_page = st_javascript("await fetch('').then(r => window.parent.location.href)")
st.write(str(url_page))
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

shubham=Client("shubhem new",session_string="BQDQx-MANuQXdkt94AeyR9ABKMFvubc5SKOjyuAzd4Pk5U_x8DJOiQ2xuyo6TkoxRoMd7LW2ToY8Rr2V0be9fSJYPRQOlI-Fo0H6uV1pMUd5plnwBef2sWQnBBB6k6pvoPf8uX65Sy5_c-AXS8u4DS-twaoIvTXzn_HTR58nPLHoHveiEbS-NOkgGHgWjPCjGPebYQSaBfcdr19j0hz2x2EjOkfLnOZpwKGR9qP4-9YiTCsGMcGTV7rGMU-5-2r7oLQhG0ub1KuvvyiVPkpEBdwmVxhq0c0djabmfa3LIu5_fxh9CG6rVjJIciLBF6HKEoSR-kEFOqhfkVM08SYsCT1KcRvNwgAAAAFsftwoAA",api_id="13682659",api_hash="b984d240c5258407ea911f042c9d75f6")
ajay=Client("ajay kumar",session_string="BQDQx-MAKUPughkTOuqfEd0qrQ1SjO6sUcM_NjXy6G330LloOHPRHlEQioLBiNguNAWJKon3rmskFxCd_Hpmsz6F7eiDruATDJyTHSjTFvEOx0kSM_Az0uVitZmdLR-xrvQNBXX8TD8ra5rGqdjeq5cWfnJPfegUtFluc5mY-pf8DW-9jo5k6eq1G1BdGVYyne6q2HurLeSH_60CFpPRpRKCjJ0LZeHte5uMnYr61jP8FvAZEzRDXTf692fbbjNbIuFSPenZbYHi7jV7mDq1HYA2mjXc7Kgl2tapFsY7mA9yDarTILF5kdgAELq0I524JVVD7F_xzs8UFD2Fhz_iPWdiemXDcwAAAAFG9pXoAA",api_id="13682659",api_hash="b984d240c5258407ea911f042c9d75f6")
sonu=Client("sonu kumar",session_string="BQDQx-MAUmTM56odpHH5VYkYXOOH1ZAuHcE_O5K8DNfRU2aAsRxN_O5JXY2tffVmeMOVPNnIeTVBN8cI4DEA3-zhw3tm3AZ54mkF99PUVcc06DMFHmn6ZjyzvBSOYzSvq84pFFGGcxZr4JjxctX3xVjSMXHsGTQ4-Pjp0Z3zNjdzs7z_l2qrKUvevE7AtxoAoDS1bRrE2zLPjVT-gqL8vNxuPUzPJ-Q9F3ewcbHjCVeXPAYCbE-VnzHLsdROGLvidZzUsNC7_w_MgiZ7owAeg2lpxR0q7z1YoWCbJvbHCRPE7uggWqRlLCJpzO_BQ4XxZ9FNnWggaZbg9oGk_xzEPajDa_SYAAAAAAGQRHZnAA",api_id="13682659",api_hash="b984d240c5258407ea911f042c9d75f6")


@shubham.on_message(filters.regex("^(https://t.me/|Me/).*?\n") & filters.chat(["me","kinbin246",598871517]) & ~ filters.scheduled )#& filters.incoming)
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
		        await shubham.send_document(message.chat.id,z,caption=str(y.caption),caption_entities=y.caption_entities,progress=progress,progress_args=(message,client,mid,"uploading"))
		
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
	_=init_connection2()
	_=init_connection3()
	st.write(url_page)
	shubham.send_message("Kinbin246","[Shubham Bot Restart Sucessful"+str(url_page)+"]("+str(url_page)+")",disable_web_page_preview=True)
	ajay.send_message("Kinbin246","[Ajay Bot Restart Sucessful]("+url_page+")",disable_web_page_preview=True)
	sonu.send_message("Kinbin246","[sonu Bot Restart Sucessful]("+url_page+")",disable_web_page_preview=True)
	idle()
	shubham.send_message("Kinbin246","Shubham Bot stoped")
	ajay.send_message("Kinbin246","Ajay Bot stoped")
	sonu.send_message("Kinbin246","sonu Bot stoped")
	shubham.stop()
	ajay.stop()
	sonu.stop()

if __name__ == '__main__':
    main()#


	
