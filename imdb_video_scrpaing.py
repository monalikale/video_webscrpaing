#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import time
import m3u8
import re

cookies = {
    'session-id': '134-7983639-6165620',
    'session-id-time': '2082787201l',
    'ad-oo': '0',
    'ubid-main': '135-4898046-7908343',
    'ci': 'e30',
    'session-token': '4UX7pkIqT9ilYaBlDMSYlsEF2rbgEx1kqneJhSIrnqYP9xfwJx4sJivAlB7e9+rXRwmvkWNf5e9aYFkAv2zvz60wqBy0EWEsyIGZYm0KJ2UjdolcuM6U3AvA1syKJoGDsFDAoIjRyq5w4ltHQbq8LWwvlq8sXz7ZwA7GakceAMPkdzrlEj3eEBLsKtjn+D7hxccrSU8nfxZCXmGDP/Y0VVE1WXwHT/ng13fUIU12/X7Wx6bmU0TAUK6IPFRgAU2z1JlL9sTviioKCCbQ3338T4TRzOyGR0K7JmFXLZRA01lBx6pfs7WApa0/tH9nfCMBvXiW0s0U1fBtmbCMV23GPHjE+J6Aqt07',
    'csm-hit': 'tb:VH3J7MEEZKVECYSDXTB1+s-RD5T7GRHVQXQQXBXRBFD|1709006680559&t:1709006680559&adb:adblk_no',
}

headers = {
    'authority': 'www.imdb.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'session-id=134-7983639-6165620; session-id-time=2082787201l; ad-oo=0; ubid-main=135-4898046-7908343; ci=e30; session-token=4UX7pkIqT9ilYaBlDMSYlsEF2rbgEx1kqneJhSIrnqYP9xfwJx4sJivAlB7e9+rXRwmvkWNf5e9aYFkAv2zvz60wqBy0EWEsyIGZYm0KJ2UjdolcuM6U3AvA1syKJoGDsFDAoIjRyq5w4ltHQbq8LWwvlq8sXz7ZwA7GakceAMPkdzrlEj3eEBLsKtjn+D7hxccrSU8nfxZCXmGDP/Y0VVE1WXwHT/ng13fUIU12/X7Wx6bmU0TAUK6IPFRgAU2z1JlL9sTviioKCCbQ3338T4TRzOyGR0K7JmFXLZRA01lBx6pfs7WApa0/tH9nfCMBvXiW0s0U1fBtmbCMV23GPHjE+J6Aqt07; csm-hit=tb:VH3J7MEEZKVECYSDXTB1+s-RD5T7GRHVQXQQXBXRBFD|1709006680559&t:1709006680559&adb:adblk_no',
    'referer': 'https://www.imdb.com/video/vi1941161497/?listId=ls053181649&ref_=hp_hp_e_3',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'x-nextjs-data': '1',
}

params = {
    'listId': 'ls053181649',
    'ref_': 'vp_pl_ap_2',
    'viconst': 'vi3803825689',
}

response = requests.get(
    'https://www.imdb.com/_next/data/vD1IK4l2jpmxFYCuu3lMx/video/vi3803825689.json',
    params=params,
    cookies=cookies,
    headers=headers,
)
r=response.text


# In[5]:


data=response.json()
urls=data['pageProps']['videoPlaybackData']['video']['playbackURLs']
url_len=len(urls)
for index in range(0,url_len):
    url=urls[index]['url']
    print(url)
    time.sleep(10)
    response=requests.get(url)
    filename="video"+str(index)+".mp4"
    with open(filename,"wb") as f:
        print("filename: ", filename)
        f.write(response.content)
        
    
    
    


# In[6]:


m3us8data=requests.get("https://imdb-video.media-imdb.com/vi3803825689/hls-1708618374208-master.m3u8?Expires=1709095262&Signature=Zov5Ref0zDTr3H3evvH700gSQpg59vgdc2XSpF76AoYolzpqYMjdPeWN3uJQP~t57jOjHWEDJeCrDAEYpGkoLF6RNzfQUgDLCW0Ld~r1xwUZQRBkjZJv2LfSxA1RHSZnoVl97M~fHDqUZ~CPBf~LXLgtJwNsroBFWKdynLI-k4bekrh4Gjm6bmZp0tIzXFNrZJP52Mbve-KSfisPEXkqleG8SqeUlvlxOSTYpDm4o7b5L0l~EWZX237TuKtloSFoSH1xTzOnCvrxzVJDCibA~vnBIFuj5m~MyzRPqplwab9mR4Qa9lMlGkmv0rnSVNyyZr63qYmBt~Qx~txFBYaAnw__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA")


# In[7]:


m3u8.loads(m3us8data.text).data


# In[3]:


m3us8data=requests.get("https://imdb-video.media-imdb.com/vi3803825689/1701734515261-esrwmn-1708618374208.m3u8?Expires=1709095262&Signature=Zov5Ref0zDTr3H3evvH700gSQpg59vgdc2XSpF76AoYolzpqYMjdPeWN3uJQP~t57jOjHWEDJeCrDAEYpGkoLF6RNzfQUgDLCW0Ld~r1xwUZQRBkjZJv2LfSxA1RHSZnoVl97M~fHDqUZ~CPBf~LXLgtJwNsroBFWKdynLI-k4bekrh4Gjm6bmZp0tIzXFNrZJP52Mbve-KSfisPEXkqleG8SqeUlvlxOSTYpDm4o7b5L0l~EWZX237TuKtloSFoSH1xTzOnCvrxzVJDCibA~vnBIFuj5m~MyzRPqplwab9mR4Qa9lMlGkmv0rnSVNyyZr63qYmBt~Qx~txFBYaAnw__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA")


# In[4]:


print(m3us8data.text)


# In[5]:


pattern = re.compile(r'(\d+-esrwmn-\d+\.ts)')

# Find all matches in the M3U8 content
ts_filenames = pattern.findall(m3us8data.text)


# In[8]:


base_url="https://imdb-video.media-imdb.com/vi3803825689/"
credentials="?Expires=1709095262&Signature=Zov5Ref0zDTr3H3evvH700gSQpg59vgdc2XSpF76AoYolzpqYMjdPeWN3uJQP~t57jOjHWEDJeCrDAEYpGkoLF6RNzfQUgDLCW0Ld~r1xwUZQRBkjZJv2LfSxA1RHSZnoVl97M~fHDqUZ~CPBf~LXLgtJwNsroBFWKdynLI-k4bekrh4Gjm6bmZp0tIzXFNrZJP52Mbve-KSfisPEXkqleG8SqeUlvlxOSTYpDm4o7b5L0l~EWZX237TuKtloSFoSH1xTzOnCvrxzVJDCibA~vnBIFuj5m~MyzRPqplwab9mR4Qa9lMlGkmv0rnSVNyyZr63qYmBt~Qx~txFBYaAnw__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA"

video_num=0
for ts_url in ts_filenames:
    ts_url=base_url+ts_url+credentials
    print(ts_url)
    ts_reponse=requests.get(ts_url)
    video_num=video_num+1
    file_name="video"+str(video_num)+".mp4"
    with open(file_name , "wb") as f:
        f.write(ts_reponse.content)
        print(file_name)
        
        
    


# In[ ]:




