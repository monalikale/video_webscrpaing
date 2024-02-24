#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests

class ipl_scraper:
    def __init__(self):
        self.name="Magic Moments"
        self.header={
                'authority': 'edge.api.brightcove.com',
                'accept': 'application/json;pk=BCpkADawqM1HAZVeYx6iS1Oqr12hCyvC8IGQSuDaTfRbJK_pYnfZoexbte9KOmx0moKY-9kcDMp-YPmJaBTdmZi_SYqnWJs-qANYeAOvpjncLe86hNPaG5XEdSCTTFk-ktvWxZhbK4Yel9UX',
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
        
    

    
    def get_url(self,response):
        url_list=[]
        r=response.json()
        sources=r['sources']
        for i in range(0,len(sources)):        
            src_url=r['sources'][i]['src']
            url_list.append(src_url)
        filtered_urls = [url for url in url_list if "manifest" not in url]
        filtered_urls=filtered_urls
        return filtered_urls
    
    def get_save_response(self,urls):
        for url in urls:
            num=1
            filename="video2"+str(num)+".mp4"
            response=requests.get(url)
            num+=1
            with open(filename,"wb") as f:
                f.write(response.content)
                return True
        else:
            return False
        
if __name__ == "__main__":

    headers={
                'authority': 'edge.api.brightcove.com',
                'accept': 'application/json;pk=BCpkADawqM1HAZVeYx6iS1Oqr12hCyvC8IGQSuDaTfRbJK_pYnfZoexbte9KOmx0moKY-9kcDMp-YPmJaBTdmZi_SYqnWJs-qANYeAOvpjncLe86hNPaG5XEdSCTTFk-ktvWxZhbK4Yel9UX',
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
    obj = ipl_scraper()
    api_url="https://edge.api.brightcove.com/playback/v1/accounts/3588749423001/videos/6328442218112"
    api_url2="https://edge.api.brightcove.com/playback/v1/accounts/3588749423001/videos/6343529121112"

    response = requests.get(api_url2,headers=headers,)
    urls_list=obj.get_url(response)
    status=obj.get_save_response(urls_list)
    if status:
        print("Video saved..")
    else:
        print("Error while video Extraction..")

  


# In[ ]:




