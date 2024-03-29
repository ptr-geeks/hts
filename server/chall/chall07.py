from flask import request, redirect, send_from_directory

import helpers


def challenge(flag, next_challenge):
    if request.method == "POST":
        if request.form.get("flag") == flag:
            return next_challenge
        else:
            return redirect(request.url)
    else:
        return helpers.uncache(send_from_directory("./templates", "chall07.html", cache_timeout=0))


def static(name):
    r = helpers.serve_static(name)
    if name == 'styleHts.css':
        r.headers['Flag'] = 'Racunalniski vodovodar'
    return r
