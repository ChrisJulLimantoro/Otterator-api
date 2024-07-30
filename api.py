import json
import google.generativeai as genai
from flask import jsonify
import re
import random


def generate(text:str):
    keys = [] # Add your API keys here
    genai.configure(api_key=keys[random.randint(0,5)])
    model = genai.GenerativeModel('gemini-1.5-pro')
    # try response
    try:
        # Generate content
        response = model.generate_content("""
            can you make me a detailed script for presentation filled with pauses and the right pace/duration for every significant pause and text with the structure like this [text: '',duration:0.0, timestamp: 0.0, is_pause: true] in complete json format only without error with the script of this (only return me the json nothing else): 

            '"""+text+"'")
        
        # Parse JSON response
        data = response.text
        data = data.strip('` \n')
        if data.startswith('json'):
            data = data[4:]
        data = json.loads(data)
        return jsonify(data)
    except json.JSONDecodeError as e:
        return jsonify({"error": "Invalid JSON response", "details": str(e)}),500
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}),500