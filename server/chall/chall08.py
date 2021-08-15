from flask import request, redirect, send_from_directory

from .. import helpers


def challenge(flag, next_challenge):
    if request.method == "POST":
        if request.form.get("flag") == flag:
            return next_challenge
        else:
            return redirect(request.url)
    else:
        return helpers.uncache(send_from_directory("./templates/chall08", "chall08.html", cache_timeout=0))


def static(name):
    r = helpers.serve_static(name)
    if name == 'faviconGreen.png':
        r = helpers.uncache(send_from_directory(
            "./templates/chall07", "faviconPurple.png", cache_timeout=0))
    return r
