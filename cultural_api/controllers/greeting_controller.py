# controllers/greeting_controller.py

from models.greeting_model import get_cultural_greeting

def greeting_controller():
    return {"greeting": get_cultural_greeting()}
