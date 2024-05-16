import os,time
import streamlit as st
@st.cache_resource
def init_connection1():
	return os.system("/home/adminuser/venv/bin/python callback_test.py")
_=init_connection1()