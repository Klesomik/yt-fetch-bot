from sqlalchemy import Column, Integer, String

from . import Base

import requests
import bs4 as bs

class Channel(Base):
    __tablename__ = 'channels'

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer)
    url = Column(String)

    def __init__(self, chat_id, url):
        self.chat_id = chat_id
        self.url = url
        '''
        html = requests.get(url + '/videos').text
        soup = bs.BeautifulSoup(html, 'lxml')
        self.rss_url = soup.find('link', {'rel':'alternate','type':'application/rss+xml','title':'RSS'})['href']
        '''

    def __repr__(self):
        return "<Channel('{}', '{}')>".format(self.chat_id, self.url)

    def get_latest_video(self):
        xml = requests.get(self.url).text
        soup = bs.BeautifulSoup(xml, 'lxml')
        all_videos = soup.findAll('link')

        if len(all_videos) <= 2:
            return None

        return all_videos[2]['href']