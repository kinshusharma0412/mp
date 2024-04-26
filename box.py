import requests,os
from tqdm import tqdm
from pprint import pprint as p
from urllib.parse import urlparse
from urllib.parse import parse_qs
def box(video):
	
	url = "http://www.nephobox.com/api/shorturlinfo"
	
	params = {
	  'type': "0",
	  'root': "1",
	  'shorturl': video.split("/")[-1],
	  'bdstoken': "a651886f55e214a155d1650d797d9fa0",
	  'wp_retry_num': "2",
	  'devuid': "CEF3CB84F01687048B6DDF92CEA6823F|VVCAT2JPH",
	  'clienttype': "1",
	  'channel': "android_12_M2102J20SI_bd-dubox_1024074a",
	  'version': "3.10.6",
	  'logid': "MTcxNDEwNjU1NDgyMyxmZTgwOjoyOWU4OmI4NGE6OGM1YTo4ZTZiJXJtbmV0X2RhdGEwLDQwMjQwMQ",
	  'lang': "en_IN",
	  'versioncode': "270",
	  'ZID': "TGpMaygLfzHBdgUM3nc1d3W19GAsWUlVJVP8nW5lXbUxAJQhiMoH4mrstFsN4DWxfDsWagaZKJuSyO5G94gLG9w",
	  'isVip': "1",
	  'bgstatus': "0",
	  'carrier_country': "in",
	  'device_country': "in",
	  'activestatus': "0",
	  'startDevTime': "1714106554825",
	  'firstlaunchtime': "1682157138",
	  'time': "1714106554127",
	  'cuid': "CEF3CB84F01687048B6DDF92CEA6823F|VVCAT2JPH",
	  'network_type': "wifi",
	  'apn_id': "1_-1",
	  'carrier': "_in",
	  'af_media_source': "null",
	  'rand': "11f44ef836ff37a8549fe88e9886f53199e1a61a"
	}
	
	headers = {
	  'User-Agent': "dubox;3.10.6;M2102J20SI;android-android;12;JSbridge1.0.10;jointbridge;1.1.39;",
	  'Connection': "Keep-Alive",
	  'Accept-Encoding': "gzip",
	  'Referer': "https://terabox.com/",
	  'Cookie': os.environ["cookies_header"]
	}
	
	response = requests.get(url, params=params, headers=headers)
	
	res0=(response.json())
	
	
	
	url = "http://www.nephobox.com/share/list"
	
	params = {
	  'shareid': str(res0['shareid']),
	  'uk': str(res0['uk']),
	  'root': "1",
	  'sign': "207d2b7eb562b28f5d06f651f673d2887dc30517",
	  'timestamp': "1714106555",
	  'share_type': "100",
	  'bdstoken': "a651886f55e214a155d1650d797d9fa0",
	  'wp_retry_num': "2",
	  'devuid': "CEF3CB84F01687048B6DDF92CEA6823F|VVCAT2JPH",
	  'clienttype': "1",
	  'channel': "android_12_M2102J20SI_bd-dubox_1024074a",
	  'version': "3.10.6",
	  'logid': "MTcxNDEwNjU1NjkwMixmZTgwOjoyOWU4OmI4NGE6OGM1YTo4ZTZiJXJtbmV0X2RhdGEwLDM1MjAzOA",
	  'lang': "en_IN",
	  'versioncode': "270",
	  'ZID': "TGpMaygLfzHBdgUM3nc1d3W19GAsWUlVJVP8nW5lXbUxAJQhiMoH4mrstFsN4DWxfDsWagaZKJuSyO5G94gLG9w",
	  'isVip': "1",
	  'bgstatus': "0",
	  'carrier_country': "in",
	  'device_country': "in",
	  'activestatus': "0",
	  'startDevTime': "1714106556903",
	  'firstlaunchtime': "1682157138",
	  'time': "1714106556205",
	  'cuid': "CEF3CB84F01687048B6DDF92CEA6823F|VVCAT2JPH",
	  'network_type': "wifi",
	  'apn_id': "1_-1",
	  'carrier': "_in",
	  'af_media_source': "null",
	  'rand': "ed5f5e41fc94871889e86c6e52db96f9682c8148"
	}
	
	headers = {
	  'User-Agent': os.environ["User_Agent"],
	  'Connection': "Keep-Alive",
	  'Accept-Encoding': "gzip",
	  'Referer': "https://terabox.com/",
	  'Cookie': os.environ["cookies_header"]
	}
	
	response = requests.get(url, params=params, headers=headers)
	
	res1=(response.json())
	#p(res1)
	
	
	url = "https://data.nephobox.com/rest/2.0/pcs/file"
	
	params = {
	  'app_id': "250528",
	  'method': "locatedownload",
	  'check_blue': "1",
	  'es': "1",
	  'esl': "1",
	  'path': "c8feeaa3936a0fde63d488655ac3df3e",
	  'fid': "4400322554685-250528-757674488109978",
	  'dstime': "1714108605",
	  'rt': "sh",
	  'sign': "FDtAER-DCb740ccc5511e5e8fedcff06b081203-wC1nLEODPupIwHQWbltcUvS6V+s=",
	  'expires': "8h",
	  'chkv': "0",
	  'chkbd': "0",
	  'chkpc': "",
	  'dp-logid': "397357232512726888",
	  'dp-callid': "0",
	  'r': "647231068",
	  'sh': "1",
	  'region': "jp",
	  'ver': "4.0",
	  'dtype': "1",
	  'err_ver': "1.0",
	  'ehps': "1",
	  'eck': "1",
	  'vip': "2",
	  'clienttype': "17",
	  'version': "2.2.91.165",
	  'time': "1714108524",
	  'rand': "1f41be8945fd4c63c4b12659760d2d6bb2e9e4ce",
	  'devuid': "CEF3CB84F01687048B6DDF92CEA6823F|VVCAT2JPH",
	  'channel': "0",
	  'version_app': "3.10.6"
	}
	
	payload = "+="
	
	headers = {
	  'User-Agent': os.environ["User_Agent"],
	  'Content-Type': "application/x-www-form-urlencoded",
	  'Cookie': os.environ["cookies_header"]
	}
	dlink=res1["list"][0]["dlink"]
	parsed_url = urlparse(dlink)
	captured_value = parse_qs(parsed_url.query)
	for x in params.keys():
		if x in captured_value:
			params[x]=",".join(captured_value[x])
	params["path"]=dlink.split("/")[-1].split("?")[0]
	response = requests.post(url, params=params, data=payload, headers=headers)
	
	res2=(response.json())
	#p(res2)
	
	url = res2["urls"][0]["url"]
	
	
	#url = res1['list'][0]['dlink'].split("?")[0]
	#print(url)
	params = {
	  'bkt': "en-2e2b5030dd6ff03722e8ca2e41a83e9939ae9853cf9bbe07b07d2378dae580f4a5e80eef67f79149",
	  'xcode': "1ac243f1beaf965eb719edec90225c1e3aee7835678ab9ef3d9d519f170236157461330ab8d8541fd5747c8387c428647eec1dc943ac4176",
	  'fid': "4402084097765-250528-309144370580587",
	  'time': "1714114519",
	  'sign': "FDTAXUGERLQlBHSKfaon-DCb740ccc5511e5e8fedcff06b081203-TdoDjzxp3kaYVKCd+Iw5E6UuGW4=",
	  'signbak': "",
	  'to': "nd7",
	  'size': "710767110",
	  'sta_dx': "710767110",
	  'sta_cs': "6268",
	  'sta_ft': "Mp4",
	  'sta_ct': "4",
	  'sta_mt': "4",
	  'fm2': "MH,jp,Anywhere,,UmFqYXN0aGFu,any",
	  'region': "jp",
	  'ctime': "1711709604",
	  'mtime': "1711710941",
	  'resv0': "-1",
	  'resv1': "0",
	  'resv2': "rlim",
	  'resv3': "5",
	  'resv4': "710767110",
	  'vuk': "4400809866228",
	  'iv': "0",
	  'htype': "",
	  'randtype': "",
	  'esl': "1",
	  'newver': "1",
	  'newfm': "1",
	  'secfm': "1",
	  'flow_ver': "3",
	  'pkey': "en-e5d0c2861d6dfc8416eec296be081ef5f95a8bbbe42b3767162935c70d0ee0acf70cdaa8d74724f6",
	  'sl': "70713421",
	  'expires': "1714143319",
	  'rt': "sh",
	  'r': "887051128",
	  'sh': "1",
	  'mlogid': "398943845783269659",
	  'vbdid': "-",
	  'fin': "_Queen_Of_Tears_2024_S01E04_720p_Hindi_Dubbed_NF_WEB_DL_×264.Mp4",
	  'bflag': "nd7,nd7,147,365,141,316-nd7",
	  'err_ver': "1.0",
	  'check_blue': "1",
	  'rtype': "1",
	  'devuid': "CEF3CB84F01687048B6DDF92CEA6823F|VVCAT2JPH",
	  'dp-logid': "398943845783269659",
	  'dp-callid': "0.1.1",
	  'hps': "1",
	  'tsl': "1000",
	  'csl': "1000",
	  'fsl': "-1",
	  'csign': "BOnV7ZQN0gX+EC0Ne6+760cujMk=",
	  'so': "0",
	  'ut': "6",
	  'uter': "3",
	  'serv': "1",
	  'uc': "1945175977",
	  'ti': "14a3010384c1ca3c38b1884a650b6e44f891c8c22f00a781a6c2ad6eeb587c84",
	  'sta_eck': "1",
	  'ogr': "0",
	  'rregion': "",
	  'adg': "",
	  'reqlabel': "250528_l_db2294ef898b68b41c3d0033783bad19_-1_00e15eb90919fa1a7ce03aeb2ad3c95d",
	  'ccn': "IN",
	  'by': "themis"
	}
	parsed_url = urlparse(url)
	captured_value = parse_qs(parsed_url.query)
	for x in params.keys():
		if x in captured_value:
			params[x]=",".join(captured_value[x])
	
	
	headers = {
	  'User-Agent': os.environ["User_Agent"],
	  'Connection': "Keep-Alive",
	  'Range': "bytes=0-"+params['size']
	}
	
	response = requests.get(res1["list"][0]["thumbs"]['url3'], stream=True)
	with open("thumb.jpeg", "wb") as handle:
	    for data in tqdm(response.iter_content()):
	        handle.write(data)
	response = requests.get(url.split("?")[0], params=params, headers=headers,stream=True)
	
	
	with open(params["fin"],'wb') as f: 
	    f.write(response.content)
	
	#with open(params["fin"], "wb") as handle:
#	    for data in tqdm(response.iter_content(chunk_size=1024*1024)):
#	        handle.write(data)
	return params["fin"],"thumb.jpeg"