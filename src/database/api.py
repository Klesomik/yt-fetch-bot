from . import session, Channel

def subscribe(channel):
    ch = session.query(Channel).filter_by(chat_id=channel.chat_id). \
                                filter_by(url=channel.url). \
                                first()

    if ch == None:
        session.add(channel)
        session.commit()

def unsubscribe(channel):
    ch = session.query(Channel).filter_by(chat_id=channel.chat_id). \
                                filter_by(url=channel.url). \
                                first()

    if ch != None:
        session.delete(ch)
        session.commit()

def import_(chat_id, urls_lst):
    for url in urls_lst:
        subscribe(Channel(chat_id, url))

def export(chat_id):
    channels_list = session.query(Channel).filter_by(chat_id=chat_id).all()

    return [ channel.url for channel in channels_list ]

def get_db():
    return session.query(Channel).all()