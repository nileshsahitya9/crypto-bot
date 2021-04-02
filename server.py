from flask import Flask, request, jsonify
import json
import os
import requests


app = Flask(__name__)
port = os.environ.get('PORT')
print(port)
