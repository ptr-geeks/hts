from flask import send_from_directory

from . import helpers

def home():
    return helpers.uncache(send_from_directory("./templates", "index.html", cache_timeout=0))

def win():
    return "Winning"

def favicon():
    return helpers.uncache(send_from_directory("./static", "favicon.png", cache_timeout=0))
