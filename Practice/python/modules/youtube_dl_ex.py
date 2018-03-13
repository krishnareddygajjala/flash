
from __future__ import unicode_literals
import youtube_dl

url = 'https://www.youtube.com/watch?v=njb88aoN9K8'
def download_utube_video(url):
    ydl_opts = {}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #ydl.download(['url'])
        pass

def  utube_video_information(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(url, download=False) 

        print 'upload date : %s' %(meta['upload_date'])
        print 'uploader    : %s' %(meta['uploader'])
        print 'views       : %d' %(meta['view_count'])
        print 'likes       : %d' %(meta['like_count'])
        print 'dislikes    : %d' %(meta['dislike_count'])
        print 'id          : %s' %(meta['id'])
        print 'format      : %s' %(meta['format'])
        print 'duration    : %s' %(meta['duration'])
        print 'title       : %s' %(meta['title'])
        #print 'description : %s' %(meta['description'])
        
download_utube_video(url)
utube_video_information(url)