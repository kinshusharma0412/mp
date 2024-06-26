import requests,html,re
from bs4 import BeautifulSoup as so
import datetime,os,json
def s(te):
	return so(te,"html.parser")
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
def find_station_code_list():
	url = os.environ["stations"]
	headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
}

	response = requests.get(url, headers=headers)
	
	return (response.text)
station_list=""#find_station_code_list()
def find_station_code(x):
	ls=""
	for y in eval(re.split("\=",station_list)[1]):
		if x.lower() in y.lower():
			ls+=re.sub("- ","- `",y)+"`\n"
	for y in range((len(ls)//4095)+1):
		print(ls[y*4095:(y+1)*4095])

def train_finder(x):
	url =os.environ["search1"] 
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
	}
	
	response = requests.get(url, params={'q': x}, headers=headers)
	ls=""
	for y in response.json():
		ls+=re.sub("- ","- `",y["train"])+"`\n"
	for y in range((len(ls)//4095)+1):
		print(ls[y*4095:(y+1)*4095])
#q	[print(z["train"]) for z in response.json()]

def trains_between_stations(From,To,Date=None):
	url = os.environ["between"] +From+"/"+To
	import re
	if Date is None:
		Date=(datetime.datetime.now()+datetime.timedelta(hours=5,minutes=30)).strftime("%d-%m-%y")
	params = {
	  'doj': Date
	  }
	CLEANR = re.compile('( {,}img {,}\{.*?\} {,}| {,}<.*?> {,})')
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
	  'Upgrade-Insecure-Requests': "1",
	  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\""
	}
	
	response = requests.get(url, params=params, headers=headers)
	
	soup=s(response.content)
	#print(soup.prettify())
	all_soup=soup.findAll("div", class_="routes-card")
	details=[]
	for x in all_soup:
		det=""
		det+="Train Name: "+x.find("span").text+"\n"
		det+=""+x.find("div", class_="pull-left").text+"\n"
		det+=""+x.findAll("div", class_="col-md-3")[0].text+" ===> "
		det+=""+x.findAll("div", class_="col-md-3")[1].text+"\n"
		det+="Time taken: "+x.find("div", class_="col-md-6 text-center").text+"\n"
		
		det+="Running Status: "+x.css.select_one("div.col-6 .pull-left a[href]")["href"]+"\n"
		det+="Train Schedule: "+x.css.select_one("div.col-6 .pull-right a[href]")["href"]+"\n"
		
		details.append(det)

	return "\n\n".join(details)
#print(trains_between_stations())
#train_finder("rani")
#print(trains_between_stations("AWR","JP"))
#find_station_code("jaipur")
async def live_train_details(y,pp):
	import requests
	details=""
	url = os.environ["train_eta_data"] +str(y)+f"/{pp}.json"
	params = {
	  'start_day': pp
	}
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
	}
	response = requests.get(url, params=params, headers=headers)
	all_d=response.json()
	#print(all_d)
	details4=[]
	details+="Train Full Details\n\nTrain Name: "+all_d["train_name"]+" ["+all_d["source"]+"->"+all_d["destination"]+"]\nTrain Code: "+str(all_d["train_number"])
	if all_d.get("travelling_towards"):
		details+="\nTrain Direction: "+str(all_d["travelling_towards"])
	
	if all_d.get("status_as_of"):
		details+="\nTrain Updates : "+all_d["status_as_of"]
	if all_d.get("total_distance"):
		details+="\nTrain Total Distance : "+str(all_d["total_distance"])+"KM"
	if all_d.get("run_days"):
		details+="\nTrain Runs : "+str(all_d["run_days"])
		if all_d.get("std"):
			da=datetime.datetime.strptime(all_d["std"],"%Y-%m-%d %H:%M")
			while da.strftime("%a").upper() not in all_d["run_days"]:
				da+= datetime.timedelta(days=1)
			details+="\nTrain Start Date : "+da.strftime("%d-%m-%Y %I:%M %p")
	if all_d.get("new_message"):
		details+="\n"+str(all_d["new_message"])
	if all_d.get("new_alert_msg"):
		details+="\nTrain New Alert Msg : "+str(all_d["new_alert_msg"])
		
	if all_d.get("on_train_error_msg"):
		details+="\nTrain Error Msg : "+str(all_d["on_train_error_msg"])
	if all_d.get("current_station_name"):
		if str(all_d["stoppage_number"])!="0":
			if all_d.get("eta") and all_d.get("etd"):
				details4.append("​\n🇨 ("+str(all_d["stoppage_number"])+") "+(str(all_d["current_station_name"])+" "+datetime.datetime.strptime( all_d["eta"], "%H:%M").strftime('%I:%M %p')+"–>"+str(datetime.datetime.strptime( all_d["etd"], "%H:%M").strftime('%I:%M %p')+"\n")))
			else:
				details4.append("​\n🇨 ("+str(all_d["stoppage_number"])+") "+(str(all_d["current_station_name"])))
		details+="\nCurrent Station Name : "+"("+str(all_d["stoppage_number"])+") "+(str(all_d["current_station_name"]))+" ["+str(all_d["current_station_code"])+"]"
	
	if all_d.get("ahead_distance_text"):
		details+="\nDistance From Current Station : "+str(all_d["ahead_distance_text"])
	if all_d.get("cur_stn_sta"):
		details+="\nideal arrival and depart time : "+str(datetime.datetime.strptime( all_d["cur_stn_sta"], "%H:%M").strftime('%I:%M %p'))+"–>"+str(datetime.datetime.strptime( all_d["cur_stn_std"], "%H:%M").strftime('%I:%M %p'))+"\nToday arrival and depart time : "+str(datetime.datetime.strptime( all_d["eta"], "%H:%M").strftime('%I:%M %p'))+"–>"+str(datetime.datetime.strptime( all_d["etd"], "%H:%M").strftime('%I:%M %p'))
	if all_d.get("current_location_info"):
		details+="\nCurrent Location Info:\n"
		for i,x in enumerate(all_d["current_location_info"]):
			if x.get("readable_message"):
				details+="   "+str(i+1)+". "+x["readable_message"]+"\n"
	
	
		
	details2=""
	if all_d.get("upcoming_stations"):
		for i,x in enumerate(all_d["upcoming_stations"]):
			if False:#i==0:
				sm=""
				for z in x["non_stops"]:
					sm+=z["station_name"]+", "
				details2+="Upcomming Small Stations : "+(sm)+"\n\n"
				
			else:
				if x.get("eta") and x.get("etd") and x.get("stoppage_number") and x.get("station_name"):
					details4.append("🇺 ("+str(x["stoppage_number"])+") "+(str(x["station_name"]))+" "+str(datetime.datetime.strptime( x["eta"], "%H:%M").strftime('%I:%M %p'))+"–>"+str(datetime.datetime.strptime( x["etd"], "%H:%M").strftime('%I:%M %p')+"\n"))
				elif x.get("stoppage_number") and x.get("station_name"):
					details4.append("🇺 ("+str(x["stoppage_number"])+") "+(str(x["station_name"])))
				if x.get("eta") and x.get("etd") and x.get("stoppage_number") and x.get("station_name"):
					details2+="Upcoming Station Name : "+"("+str(x["stoppage_number"])+") "+(str(x["station_name"]))+" ["+str(x["station_code"])+"]\nDetails : "+str(x["distance_from_current_station_txt"])+"\nIdeal Time : "+datetime.datetime.strptime( x["sta"], "%H:%M").strftime('%I:%M %p')+"–>"+datetime.datetime.strptime( x["std"], "%H:%M").strftime('%I:%M %p')+"\nToday Time : "+datetime.datetime.strptime( x["eta"], "%H:%M").strftime('%I:%M %p')+"–>"+datetime.datetime.strptime( x["etd"], "%H:%M").strftime('%I:%M %p')
					if x["arrival_delay"]>0:
						details2+="\nArrival Delay : "+str(x["arrival_delay"])+" min"
					details2+="\nPlatform Number : "+str(x["platform_number"])+"\nPlatfoem Stay Time : "+str(x["halt"])
					if x["a_day"]==0:
						details2+="\nTrain comes Today"
					elif x["a_day"]==1:
						details2+="\nTrain comes Tomorrow"
					elif x["a_day"]>2:
						details2+=f"\nTrain comes after "+str(x["a_day"])+" Days"
					#print(x)
				if len(x["non_stops"])>0:
					sm=""
					for z in x["non_stops"]:
						sm+=z["station_name"]+", "
					details2+="\nSmall Stations : "+sm
						
					
				details2+="\n"
				details2+="\n"
	details1=""
	if all_d.get("upcoming_stations"):
		jjj=0
		for i,x in enumerate(all_d["previous_stations"]):
			if False:#i==0:
				sm=""
				for z in x["non_stops"]:
					sm+=z["station_name"]+", "
				details1+="Previous Small Stations : "+(sm)+"\n\n"
				
			else:
				if x.get("eta") and x.get("etd") and x.get("stoppage_number") and x.get("station_name"):
					details4.insert(jjj,"​🇵 ("+str(x["stoppage_number"])+") "+(str(x["station_name"]))+" "+str(datetime.datetime.strptime( x["eta"], "%H:%M").strftime('%I:%M %p'))+"–>"+str(datetime.datetime.strptime( x["etd"], "%H:%M").strftime('%I:%M %p')+"\n"))
				elif x.get("stoppage_number") and x.get("station_name"):
					details4.insert(jjj,"​🇵 ("+str(x["stoppage_number"])+") "+(str(x["station_name"])))
				
				jjj+=1
				if x.get("eta") and x.get("etd") and x.get("stoppage_number") and x.get("station_name"):
					details1+="Previous Station Name : "+"("+str(x["stoppage_number"])+")"+(str(x["station_name"]))+" ["+str(x["station_code"])+"]\nIdeal Time : "+datetime.datetime.strptime( x["sta"], "%H:%M").strftime('%I:%M %p')+"–>"+datetime.datetime.strptime( x["std"], "%H:%M").strftime('%I:%M %p')+"\nToday Time : "+datetime.datetime.strptime( x["eta"], "%H:%M").strftime('%I:%M %p')+"–>"+datetime.datetime.strptime( x["etd"], "%H:%M").strftime('%I:%M %p')
					if x["arrival_delay"]>0:
						details1+="\nArrival Delay : "+str(x["arrival_delay"])+" min"
					details1+="\nPlatform Number : "+str(x["platform_number"])+"\nPlatfoem Stay Time : "+str(x["halt"])
					if x["a_day"]==0:
						details1+="\nTrain comes Today"
					elif x["a_day"]==-1:
						details1+="\nTrain comes Yesterday"
					elif x["a_day"]<-1:
						details1+=f"\nTrain depart before "+str(x["a_day"]*(-1))+" Days"
				if len(x["non_stops"])>0:
					sm=""
					for z in x["non_stops"]:
						sm+=z["station_name"]+", "
					details1+="\nSmall Stations : "+sm
						
					
				details1+="\n"
				details1+="\n"
	details4.insert(0,"𝗧𝗿𝗮𝗶𝗻 𝘀𝘂𝗺𝗺𝗮𝗿𝘆​\n")
	return details,details2,details1,details4
#A,B,C=(live_train_details(22463))
def spliter(a):
	
	jointer=""
	if type(a)==type(""):
		jointer="\n\n"
		a=translate_en(a)
		b=re.split(jointer,a)
	if type(a)==type([]):
		b=[]
		for xx in a:
			b.append(translate_en(str(xx)))
		#b=a
		jointer="\n"
	ret=[]
	new=""
	for i, x in enumerate(b):
		
		if len(new+x+jointer)<4096:
			new=new+x+jointer
		else:
			ret.append(new)
			new=x+jointer
		if len(b)-1==i:
			ret.append(new)
		
	return ret
async def new_find_station_code(x):
	url = os.environ["common_city_station_search"] 
	params = {
	  'q': str(x)
	}
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
	}
	response = requests.get(url, params=params, headers=headers)
	if len(response.json()["items"])==0:
		return "No Station find by your Query = "+x
	details="Note: Copy Station Code by clicking it.\n\n"
	#p(response.json()["items"])
	for y in response.json()["items"]:
		if y.get("station_code") and y.get("station_name") and y.get("city_name") and y.get("state_name"):
			details+="Station Code: `"+y["station_code"]+"`\nStation Name: "+y["station_name"]+"\nCity: "+y["city_name"]+", "+y["state_name"]+"\n\n"
	
	return details
def sortDates(datesList):
	split_up = datesList["from_sta"].split(':')
	return int(split_up[0]), int(split_up[1])
	
async def new_trains_between_stations(a,b,c=None):
	if c is None:
		c=(datetime.datetime.now()+datetime.timedelta(hours=5,minutes=30)).strftime("%d-%m-%Y")
	url = os.environ["between_sta"]  
	
	params = {
	  'from': a,
	  'to': b,
	  'dateOfJourney': c,
	  'device_type_id': "4",
	  'from_code': a,
	  'from_name': a,
	  'journey_quota': "GN",
	  'to_code':b,
	  'to_name': b
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
	}
	
	response = requests.get(url, params=params, headers=headers)
	
	if response.json()["status"]==200:
		data=response.json()["train_between_stations"]+response.json()["reserved_trains"]+response.json()["alternate_trains"]
		data.sort(key=sortDates)
		details=""
		alternate_trains =[ij["train_number"] for ij in response.json()["alternate_trains"]]
		for x in data:
			if x["train_number"] in alternate_trains:
				details+="~~Train Name: "+x["train_name"]+"~~\n"+"Train comming Date: "+datetime.datetime.strptime(x["train_date"],"%Y-%m-%d").strftime("%d-%m-%Y")+"\nTrain Code: `"+x["train_number"]+"`\n"+x["from_station_name"]+" arrival and departure time "+datetime.datetime.strptime( x["from_sta"], "%H:%M").strftime('%I:%M %p')+" - > "+datetime.datetime.strptime( x["from_std"], "%H:%M").strftime('%I:%M %p')+"\n"+x["to_station_name"]+" arrival and departure time "+datetime.datetime.strptime( x["to_sta"], "%H:%M").strftime('%I:%M %p')+" - > "+datetime.datetime.strptime( x["to_std"], "%H:%M").strftime('%I:%M %p')+"\nTrain Run days: "+", ".join(x["run_days"])
			elif datetime.datetime.strptime(x["from_sta"],"%H:%M")<datetime.datetime.strptime((datetime.datetime.now()+datetime.timedelta(hours=5,minutes=30)).strftime("%H:%M"),"%H:%M") :
				details+="🅿🅰🆂🆃 Train Name: "+x["train_name"]+"\n"+"Train Code: `"+x["train_number"]+"`\n"+x["from_station_name"]+" arrival and departure time "+datetime.datetime.strptime( x["from_sta"], "%H:%M").strftime('%I:%M %p')+" - > "+datetime.datetime.strptime( x["from_std"], "%H:%M").strftime('%I:%M %p')+"\n"+x["to_station_name"]+" arrival and departure time "+datetime.datetime.strptime( x["to_sta"], "%H:%M").strftime('%I:%M %p')+" - > "+datetime.datetime.strptime( x["to_std"], "%H:%M").strftime('%I:%M %p')+"\nTrain Run days: "+", ".join(x["run_days"])
			else:
				details+="​🇫​​🇺​​🇹​​🇺​​🇷​​🇪​ Train Name: "+x["extended_train_name"]+"\n"+"Train Code: `"+x["train_number"]+"`\n"+x["from_station_name"]+" arrival and departure time "+datetime.datetime.strptime( x["from_sta"], "%H:%M").strftime('%I:%M %p')+" - > "+datetime.datetime.strptime( x["from_std"], "%H:%M").strftime('%I:%M %p')+"\n"+x["to_station_name"]+" arrival and departure time "+datetime.datetime.strptime( x["to_sta"], "%H:%M").strftime('%I:%M %p')+" - > "+datetime.datetime.strptime( x["to_std"], "%H:%M").strftime('%I:%M %p')+"\nTrain Run days: "+", ".join(x["run_days"])
			if len(x["journey_class"])>0:
				details+="\nJourney_Cass: "+", ".join(x["journey_class"])
			details+="\n\n"
		return details
		datetime.datetime.strptime( t_str, "%H:%M").strftime('%I:%M %p')
	else:
		return "some error comes please send station_code and date (if date is not provided than i will search for today train) like this Example 👇👇👇\n\n /train_btw_station AWR JP "+(datetime.datetime.now()+datetime.timedelta(hours=5,minutes=30)).strftime("%d-%m-%y")
#print((A))
#print((B))
#print((C))
#print(trains_between_stations("awr","jp"))