from datetime import datetime
import random
from app.controllers.openai_controller import openai_controller
from app.templates.chatgpt_templates import CATEGORIES, THEMES, system_thinking
from app.controllers.twitter_bot import create_tweet
from app.models import init_db, db_session
from app.models.twitter_model import Twitter_comment
from app.config.environments import ENVIRONMENTS

save_on_db=ENVIRONMENTS['save_on_db']


def main():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    category = random.choice(CATEGORIES)
    topic = random.choice(THEMES)
    system_think = system_thinking(category, topic)
    text = openai_controller(system_think)
    comment = text
    create_tweet(text)
    if save_on_db:
        init_db()
        twitter = Twitter_comment(comment, category, topic)
        db_session.add(twitter)
        db_session.commit()
        db_session.close()
    print(f"Current time: {current_time}: {text}")
    return 'ok'