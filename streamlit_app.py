

import os
import streamlit as st


url_page = st.get_url()
st.write(url_page)
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