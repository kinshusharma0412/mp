import re,os 
from urllib.parse import parse_qs, urlparse

import requests
import tqdm
import requests,os,time
from tqdm import tqdm
from pprint import pprint as p
from urllib.parse import urlparse
from urllib.parse import parse_qs
from prog_bar import progress_for_pyrogram




import re
from urllib.parse import parse_qs, urlparse

import requests
import tqdm



COOKIE=os.environ["Cookie"]


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


def check_url_patterns(url):
    patterns = [
        r"ww\.mirrobox\.com",
        r"www\.nephobox\.com",
        r"freeterabox\.com",
        r"www\.freeterabox\.com",
        r"1024tera\.com",
        r"4funbox\.co",
        r"www\.4funbox\.com",
        r"mirrobox\.com",
        r"nephobox\.com",
        r"terabox\.app",
        r"terabox\.com",
        r"www\.terabox\.ap",
        r"www\.terabox\.com",
        r"www\.1024tera\.co",
        r"www\.momerybox\.com",
        r"teraboxapp\.com",
        r"momerybox\.com",
        r"tibibox\.com",
        r"www\.tibibox\.com",
        r"www\.teraboxapp\.com",
        #r"teraboxlinks\.com",
    ]

    for pattern in patterns:
        if re.search(pattern, url):
            return True

    return True


def get_urls_from_string(string: str) -> list[str]:
    """
    Extracts URLs from a given string.

    Args:
        string (str): The input string from which to extract URLs.

    Returns:
        list[str]: A list of URLs extracted from the input string. If no URLs are found, an empty list is returned.
    """
    pattern = r"(https?://\S+)"
    urls = re.findall(pattern, string)
    urls = [url for url in urls if check_url_patterns(url)]
    if not urls:
        return []
    return urls[0]


def find_between(data: str, first: str, last: str) -> str:
    """
    Searches for the first occurrence of the `first` string in `data`,
    and returns the text between the two strings.

    Args:
        data (str): The input string.
        first (str): The first string to search for.
        last (str): The last string to search for.

    Returns:
        str | None: The text between the two strings, or None if the
            `first` string was not found in `data`.
    """
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None


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



async def box(video,message):
    r = requests.Session()
    headersList = {
'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  'Upgrade-Insecure-Requests': "1",
  'Sec-Fetch-Site': "none",
  'Sec-Fetch-Mode': "navigate",
  'Sec-Fetch-Dest': "document",
  'sec-ch-ua': "\"Not A;Brand\";v=\"99\", \"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\"",
  'sec-ch-ua-mobile': "?0",
  'sec-ch-ua-platform': "\"Windows\"",
  'Accept-Language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": COOKIE,

    }

    payload = ""

    response = r.get(url, data=payload, headers=headersList)
    response = r.get(response.url, data=payload, headers=headersList)
    logid = find_between(response.text, "dp-logid=", "&")
    jsToken = find_between(response.text, "fn%28%22", "%22%29")
    bdstoken = find_between(response.text, 'bdstoken":"', '"')
    shorturl = extract_surl_from_url(response.url)
    if not shorturl:
        return False

    reqUrl = f"https://www.terabox.app/share/list?app_id=250528&web=1&channel=0&jsToken={jsToken}&dp-logid={logid}&page=1&num=20&by=name&order=asc&site_referer=&shorturl={shorturl}&root=1"

    headersList = {
'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  'Upgrade-Insecure-Requests': "1",
  'Sec-Fetch-Site': "none",
  'Sec-Fetch-Mode': "navigate",
  'Sec-Fetch-Dest': "document",
  'sec-ch-ua': "\"Not A;Brand\";v=\"99\", \"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\"",
  'sec-ch-ua-mobile': "?0",
  'sec-ch-ua-platform': "\"Windows\"",
  'Accept-Language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": COOKIE,

    }

    payload = ""

    response = r.get(reqUrl, data=payload, headers=headersList)

    if not response.status_code == 200:
        return False
    r_j = response.json()
    print(r_j)
    if r_j["errno"]:
        return False
    if not "list" in r_j and not r_j["list"]:
        return False

    response = r.head(r_j["list"][0]["dlink"], headers=headersList)
    direct_link = response.headers.get("location")
    data = {
        "file_name": r_j["list"][0]["server_filename"],
        "link": r_j["list"][0]["dlink"],
        "direct_link": direct_link,
        "thumb": r_j["list"][0]["thumbs"]["url3"],
        "size": get_formatted_size(int(r_j["list"][0]["size"])),
        "sizebytes": int(r_j["list"][0]["size"]),
    }
    headers = {'User-Agent': "dubox;3.31.2;M2102J20SI;android-android;12;JSbridge1.0.10;jointbridge;1.1.39;",
  'Connection': "Keep-Alive",
  'Range': "bytes=0-"+str(data["sizebytes"])}
    reaponce=requests.get(re.sub("https://d.terabox.app","https://d.terabox.app",data["link"]),headers=headers, stream=True)
    print(data["file_name"])
    now = time.time()
    
    with open(data["file_name"], 'wb') as f, tqdm.tqdm(
      desc="Downloading",
      total=data["sizebytes"],
      unit='MB',
      unit_scale=True,
      unit_divisor=1024,
  ) as bar:
        dl=0
        for chunk in reaponce.iter_content(chunk_size=1024*1024):
           if chunk:
              dl+=len(chunk)
              await progress_for_pyrogram(current=dl,
    total=data["sizebytes"],
    ud_type="Downloading :-  "+data["file_name"],
    message=message,
    start=now)
              size=f.write(chunk)
              bar.update(size)
    return data["file_name"],data["thumb"]


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


def check_url_patterns(url):
    patterns = [
        r"ww\.mirrobox\.com",
        r"www\.nephobox\.com",
        r"freeterabox\.com",
        r"www\.freeterabox\.com",
        r"1024tera\.com",
        r"4funbox\.co",
        r"www\.4funbox\.com",
        r"mirrobox\.com",
        r"nephobox\.com",
        r"terabox\.app",
        r"terabox\.com",
        r"www\.terabox\.ap",
        r"www\.terabox\.com",
        r"www\.1024tera\.co",
        r"www\.momerybox\.com",
        r"teraboxapp\.com",
        r"momerybox\.com",
        r"tibibox\.com",
        r"www\.tibibox\.com",
        r"www\.teraboxapp\.com",
        #r"teraboxlinks\.com",
    ]

    for pattern in patterns:
        if re.search(pattern, url):
            return True

    return True


def get_urls_from_string(string: str) -> list[str]:
    """
    Extracts URLs from a given string.

    Args:
        string (str): The input string from which to extract URLs.

    Returns:
        list[str]: A list of URLs extracted from the input string. If no URLs are found, an empty list is returned.
    """
    pattern = r"(https?://\S+)"
    urls = re.findall(pattern, string)
    urls = [url for url in urls if check_url_patterns(url)]
    if not urls:
        return []
    return urls[0]


def find_between(data: str, first: str, last: str) -> str:
    """
    Searches for the first occurrence of the `first` string in `data`,
    and returns the text between the two strings.

    Args:
        data (str): The input string.
        first (str): The first string to search for.
        last (str): The last string to search for.

    Returns:
        str | None: The text between the two strings, or None if the
            `first` string was not found in `data`.
    """
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None


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


def get_data(url: str):
    r = requests.Session()
    headersList = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
        "Connection": "keep-alive",
        "Cookie": COOKIE,
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

    response = r.get(url, data=payload, headers=headersList)
    response = r.get(response.url, data=payload, headers=headersList)
    logid = find_between(response.text, "dp-logid=", "&")
    jsToken = find_between(response.text, "fn%28%22", "%22%29")
    bdstoken = find_between(response.text, 'bdstoken":"', '"')
    shorturl = extract_surl_from_url(response.url)
    if not shorturl:
        return False

    reqUrl = f"https://www.terabox.app/share/list?app_id=250528&web=1&channel=0&jsToken={jsToken}&dp-logid={logid}&page=1&num=20&by=name&order=asc&site_referer=&shorturl={shorturl}&root=1"

    headersList = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
        "Connection": "keep-alive",
        "Cookie": COOKIE,
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

    response = r.get(reqUrl, data=payload, headers=headersList)

    if not response.status_code == 200:
        return False
    r_j = response.json()
    if r_j["errno"]:
        return False
    if not "list" in r_j and not r_j["list"]:
        return False

    response = r.head(r_j["list"][0]["dlink"], headers=headersList)
    direct_link = response.headers.get("location")
    data = {
        "file_name": r_j["list"][0]["server_filename"],
        "link": r_j["list"][0]["dlink"],
        "direct_link": direct_link,
        "thumb": r_j["list"][0]["thumbs"]["url3"],
        "size": get_formatted_size(int(r_j["list"][0]["size"])),
        "sizebytes": int(r_j["list"][0]["size"]),
    }
    if os.path.exists(data["file_name"]):
    	start1=os.path.getsize(data["file_name"])
    	file_type="ab"
    else:
    	start1=0
    	file_type="wb"
    headers = {'User-Agent': "dubox;3.31.2;M2102J20SI;android-android;12;JSbridge1.0.10;jointbridge;1.1.39;",
  'Connection': "Keep-Alive",
  'Range': f"bytes={start}-"+str(data["sizebytes"])}
    reaponce=requests.get(re.sub("https://d.terabox.app","https://d.terabox.app",data["link"]),headers=headers, stream=True)
    print(data["file_name"])
    now = time.time()
    with open(data["file_name"], file_type) as f, tqdm.tqdm(
      desc="Downloading",
      total=data["sizebytes"]-start1,
      unit='MB',
      unit_scale=True,
      unit_divisor=1024,
  ) as bar:
	    dl=0
	    for chunk in reaponce.iter_content(chunk_size=1024*1024):
	       if chunk:
	          dl+=len(chunk)
	          await progress_for_pyrogram(current=dl,
    total=data["sizebytes"]-start1,
    ud_type="Downloading :-  "+data["file_name"],
    message=message,
    start=now)
	          size=f.write(chunk)
	          bar.update(size)
    return data["file_name"],data["thumb"]
get_data("https://nephobox.com/s/13VEzhOTi51_TRGMDJMNnJw")
