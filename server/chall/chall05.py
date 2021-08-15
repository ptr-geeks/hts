from flask import request, redirect, send_from_directory

from .. import helpers

def challenge(flag, next_challenge):
    if request.method == "POST":
        if request.form.get("flag") == flag:
            return next_challenge;
        else:
            return redirect(request.url)
    else:
        return helpers.uncache(send_from_directory("./templates", "chall05.html", cache_timeout=0))

def static(name):
    if name == 'privat.txt':
        return helpers.uncache(send_from_directory("./templates/chall05", "privat.txt", cache_timeout=0))
    return helpers.serve_static(name)
