#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


#Get below url from insepct of ipl.com in network tab
"https://secure.brightcove.com/services/mobile/streaming/index/master.m3u8?videoId=5790273860001&pubId=3588749423001&secure=true"


# In[ ]:


import requests
import subprocess
import m3u8

headers = {
    'authority': 'manifest.prod.boltdns.net',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://www.iplt20.com',
    'referer': 'https://www.iplt20.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

params = {
    'fastly_token': 'NjVkYmFkZWFfMGU0ODA3ZDEwNjk5M2JiYWFiMTM0NWIzOTk3ZTU1Y2QwNGYzMTI5MTQyZGQyMTgzMDRkYjA3ODRjNjNiNmVjZg==',
}

response = requests.get(
    'https://manifest.prod.boltdns.net/manifest/v1/hls/v4/aes128/3588749423001/2c7f4930-be56-4a57-ac5d-a1369e72cb3d/dcea357c-2812-49f0-89ae-aa2377cd4a49/10s/rendition.m3u8',
    params=params,
    headers=headers,
)

m3u8_master=m3u8.loads(response.text)

with open("video21.ts", "wb") as f:
    for segment in m3u8_master.data['segments']:
        url=segment['uri']
        r=requests.get(url)
        f.write(r.content)
    print("Video Saved Successfully..")

#convert .ts format to mp4 format
input_file="video21.ts"
output_file="video21.mp4"

command=['ffmpeg',
        '-i', input_file,  # Input .ts file
        '-c:v', 'copy',   # Copy video codec
        '-c:a', 'aac',    # AAC audio codec
        '-strict', 'experimental',  # Needed for some AAC encoders
        '-b:a', '128k',   # Audio bitrate
        output_file ]  
        
subprocess.run(command)


# In[ ]:




