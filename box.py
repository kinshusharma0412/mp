import requests,re
import json,os
from pprint import pprint

def box(video):
	
	url = "https://teradownloader.com/api/application"
	
	payload = json.dumps({
	  "url": video
	})
	
	headers = {
	  'User-Agent': "okhttp/5.0.0-alpha.10",
	  'Accept-Encoding': "gzip",
	  'Content-Type': "application/json",
	  'key': os.environ["key1"]
	}
	
	response = requests.post(url, data=payload, headers=headers)
	import shutil
	res=response.json()
	url = "https://tera.backend.live/stream-app"
	
	payload = json.dumps({
	  "url": video,
	  "fs_id": res[0]['fs_id'],
	  "share_id": str(res[0]['share_id']),
	  "uk": res[0]['uk'],
	  "timestamp": res[0]['timstamp'],
	  "jsToken": res[0]['jsToken']
	})
	
	headers = {
	  'User-Agent': "okhttp/5.0.0-alpha.10",
	  'Connection': "Keep-Alive",
	  'Accept-Encoding': "gzip",
	  'Content-Type': "application/json",
	  'key': os.environ["key2"]
	}
	
	response = requests.post(url, data=payload, headers=headers)
	
	streaming_url=response.json()
	print(streaming_url)
	newurl=requests.get(streaming_url["streaming_url"], stream=True).text
	urls=newurl.split("\n")
	newurl=[]
	for x in urls:
		if bool(re.search("v2.terabox.app",x)):
			newurl.append(x)
	
	with open(res[0]["server_filename"], "wb") as f:
		for x in newurl:
			r = requests.get(x, stream=True)
			for chunk in r.iter_content(chunk_size=1024*64):
				f.write(chunk)
	return res[0]["server_filename"]
