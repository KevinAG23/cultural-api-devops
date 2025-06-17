# controllers/greeting_controller.py

from models.greeting_model import get_cultural_greetings

def greeting_controller():
    greetings = get_cultural_greetings()
    return {"greetings": greetings}
