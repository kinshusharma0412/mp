import requests,os
from urllib.parse import parse_qs, urlparse
from pprint import pprint
def box(url: str) -> str:
	r = requests.Session()
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
	payload = ""
	def get_formatted_size(size_bytes: int) -> str:
	    """
	    Returns a human-readable file size from the given number of bytes.
	
	    Parameters:
	        size_bytes (int): The number of bytes to be converted to a file size.
	
	    Returns:
	        str: The file size in a human-readable format.
	    """
	    if size_bytes >= 1024 * 1024:
	        size = size_bytes / (1024 * 1024)
	        unit = "MB"
	    elif size_bytes >= 1024:
	        size = size_bytes / 1024
	        unit = "KB"
	    else:
	        size = size_bytes
	        unit = "b"
	
	    return f"{size:.2f} {unit}"
	def extract_surl_from_url(url: str) -> str:
	    """
	    Extracts the surl parameter from a given URL.
	
	    Args:
	        url (str): The URL from which to extract the surl parameter.
	
	    Returns:
	        str: The surl parameter, or False if the parameter could not be found.
	    """
	    parsed_url = urlparse(url)
	    query_params = parse_qs(parsed_url.query)
	    surl = query_params.get("surl", [])
	
	    if surl:
	        return surl[0]
	    else:
	        return False
	
	def find_between(data: str, first: str, last: str) -> str:
	    try:
	        start = data.index(first) + len(first)
	        end = data.index(last, start)
	        return data[start:end]
	    except ValueError:
	        return None
	
	response = r.get(url, data=payload, headers=headersList)
	
	response = r.get(response.url, data=payload, headers=headersList)
	logid = find_between(response.text, "dp-logid=", "&")
	jsToken = find_between(response.text, "fn%28%22", "%22%29")
	bdstoken = find_between(response.text, 'bdstoken":"', '"')
	shorturl = extract_surl_from_url(response.url)
	
	reqUrl = f"https://www.terabox.app/share/list?app_id=250528&web=1&channel=0&jsToken={jsToken}&dp-logid={logid}&page=1&num=20&by=name&order=asc&site_referer=&shorturl={shorturl}&root=1"
	response = r.get(reqUrl, data=payload, headers=headersList)
	
	r_j = response.json()
	response = r.head(r_j["list"][0]["dlink"], headers=headersList)
	direct_link = response.headers.get("location")
	#for x in r_j["list"][0]["thumbs"]:
	#	find_between(r_j["list"][0]["thumbs"][x], "size=", "&"))
	data = {
	        "file_name": r_j["list"][0]["server_filename"],
	        "link": r_j["list"][0]["dlink"],
	        "direct_link": direct_link,
	        "thumb": [r_j["list"][0]["thumbs"][x] for x in r_j["list"][0]["thumbs"]],
	        "size": get_formatted_size(int(r_j["list"][0]["size"])),
	        "sizebytes": int(r_j["list"][0]["size"]),
	    }
	r1 = r.get(data["thumb"][-2],headers=headersList,stream=True)
	chunk_size = 256
	with open("thumb.jpeg", 'wb') as f:
		for chunk in r1.iter_content(chunk_size=chunk_size):
			f.write(chunk)
	r1 = requests.get(data["link"],stream=True)
	chunk_size = 1024*1024
	with open(data["file_name"], 'wb') as f:
		for chunk in r1.iter_content(chunk_size=chunk_size):
			f.write(chunk)
	return (data)
