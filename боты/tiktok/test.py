from TikTokApi import TikTokApi
verifyfp = ''
api = TikTokApi()
 
for video in api.trending.videos():
    video_bites = video.bytes()
    break
with open('test.mp4', 'wb') as out:
    out.write(video_bites)