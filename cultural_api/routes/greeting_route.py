# routes/greeting_route.py

from flask import Blueprint, jsonify
from controllers.greeting_controller import greeting_controller

greeting_bp = Blueprint('greeting', __name__)

@greeting_bp.route('/cultural-greeting', methods=['GET'])
def cultural_greeting():
    return jsonify(greeting_controller())
