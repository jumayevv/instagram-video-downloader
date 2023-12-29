import requests
import json

def insta_downloader(link:str):


    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url":link}

    # your api key and host
    headers = {
        "X-RapidAPI-Key": "47d5ebc4d8msh2016a1447ba89c6p137494jsnada972aa59dd",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    res = json.loads(response.text)
    details = {}


    if(len(res) == 1):
        if 'message' in res:
            return 'limit error'
        else:
            return'link error'
    try:
        if 'story_by_id' in res:
            if res['story_by_id']['Type'] == 'Story-Video':
                details['type']='Story-Video'
                details['media']=res['story_by_id']['media']
            else:
                details['type']='Story-Image'
                details['media']=res['story_by_id']['media']
            return details
        elif res['Type']=='Carousel':
            details['type']='Multiple-Data'
            details['media']=res['media']
            return details
        elif res['Type']=='Post-Image':
            details['type']='Image'
            details['media']=res['media']   
            return details
        elif res['Type']=='Post-Video':
            details['type']='Video'
            details['media']=res['media']
            return details
        else:
            return 'link error'    
    except Exception:
        return "system error"
