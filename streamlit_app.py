

import os
import streamlit as st
from streamlit_javascript import st_javascript

url_page = st_javascript("await fetch('').then(r => window.parent.location.href)")
@st.cache_resource
def init_connection1():
	return os.system("/home/adminuser/venv/bin/python shubhem_bot.py "+str(url_page))
_=init_connection1()
#STREAMLIT SITE
#/home/adminuser/venv/bin/.py & /home/adminuser/venv/bin/python bb.py")
#import os
#os.system("""/home/adminuser/venv/bin/python soojh.py & /home/adminuser/venv/bin/python aa.py & /home/adminuser/venv/bin/python bb.py""")
#/home/adminuser/venv/bin/python -m pip install --upgrade pip & 
#/home/adminuser/venv/bin/python multi-acc.py & 