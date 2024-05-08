
from sqlalchemy import Column, Integer, String, DateTime
from app.models import Model
import pytz
from datetime import datetime

chile_timezone = pytz.timezone('Chile/Continental')

class Twitter_comment(Model):
    __tablename__ = 'twitter_comments'
    id = Column(Integer, primary_key=True)
    comment = Column(String())
    category = Column(String())
    topic = Column(String())
    created_at = Column(DateTime, default=datetime.now)

    def __init__(self, comment, category, topic):
        self.comment = comment
        self.category = category
        self.topic = topic

    def to_json(self):
        return dict(
            id=self.id,
            comment=self.comment,
            category=self.category,
            topic=self.topic,
            created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        )

    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)