import pyktok
import aiohttp
import aiofiles
import asyncio


CHUNK_SIZE = 1024*1024
DOWNLOAD_FOLDER = "Downloads/"

def save_tiktok(video_url,
                download_obj,
                save_video=True,
                metadata_fn='',
                browser_name=None):
    if save_video is False and metadata_fn == '':
        return

    tt_json = pyktok.get_tiktok_json(video_url, browser_name)
    video_id = list(tt_json['ItemModule'].keys())[0]

    if save_video == True:
        regex_url = pyktok.re.findall(pyktok.url_regex,video_url)[0]
        video_fn = regex_url.replace('/','_') + '.mp4'
        tt_video_url = tt_json['ItemModule'][video_id]['video']['downloadAddr']
        pyktok.headers['referer'] = 'https://www.tiktok.com/'
        # include cookies with the video request
        tt_video = pyktok.requests.get(tt_video_url,allow_redirects=True,headers=pyktok.headers,cookies=pyktok.cookies)
        with open(DOWNLOAD_FOLDER + video_fn, 'wb') as fn:
            fn.write(tt_video.content)
            download_obj.fileName = video_fn
            download_obj.progress = 100
            download_obj.status = "Complete"

    if metadata_fn != '':
        data_slot = tt_json['ItemModule'][video_id]
        data_row = pyktok.generate_data_row(data_slot)
        try:
            user_id = list(tt_json['UserModule']['users'].keys())[0]
            data_row.loc[0,"author_verified"] = tt_json['UserModule']['users'][user_id]['verified']
        except Exception:
            pass
        if pyktok.os.path.exists(metadata_fn):
            metadata = pyktok.pd.read_csv(metadata_fn,keep_default_na=False)
            combined_data = pyktok.pd.concat([metadata,data_row])
        else:
            combined_data = data_row
        combined_data.to_csv(metadata_fn, index=False)


