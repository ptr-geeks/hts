from flask import request, redirect, send_from_directory

import helpers

def challenge(flag, next_challenge):
    if request.method == "POST":
        if request.form.get("flag") == flag:
            return next_challenge;
        else:
            return redirect(request.url)
    else:
        return helpers.uncache(send_from_directory("./templates", "chall06.html", cache_timeout=0))

def static(name):
    data = name.split("?")[0]
    data = data.split("/")
    if data[0] != "pot":
        return helpers.serve_static(name)

    data = data[1:]
    if data[-1] == "":
        del data[-1]

    paths = {
        "igre": {
            "COD_MW_746245_Remastered": {
                "1337_hax": "You have been banned from this server!",
                "maps": "de_dust2 is still better",
                "scripts": {
                    "bhop": "Jump rabbit, jump!",
                    "aim": "5. random",
                    "wallhacks": "Zdaj vidim vse stene!",
                    "lag_switch": "Sej mi ze tko ne dela vec!",
                },
            },
            "Duke nukem": {
                "Is_this_doom": "Hudo, nisem vedel da obstajajo tudi take igre",
                "geslo": "Haha, si že mislil!",
            },
            "Šah": {
                "to_ni_igra": "No ja, ubistvu je šport, ne igra.",
                "ranking": "Celih 1363 sem nabral to leto!",
            },
            "iPhone igreeeee": "Mobilne naprave niso za igre! Za to imamo računalnike!",
            "Prestar_sem_za_igre": {
                "jaka": "8. a",
                "filip": "Od tega trenutka filipa vikamo!",
                "ne_pa_ne": "Mar ni to kar trenutno delaš igra? Mislim, da so ta skrita sporočila, kot je '8. a' le del večje sestavljanke. Morda najdeš vse in nekaj iz njih razbereš!",
            },
        },
        "datoteke": {
            "moje_datoteke": "&lt;Restricted content&gt;",
            "nase_datoteke": {
                "manifest": "Še nenapisano, try again later",
                "slike": "foto.ptr.si",
                "geslo_za_internet": {
                    "haha_ni_ga_tu": {
                        "kaj_se_delas_tu": {
                            "daj_no_nehaj": {
                                "naj_ti_bo": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                            },
                        },
                    },
                },
            },
            "tvoje_datoteke": {
                "zasebne_slike": "2. all",
                "cevapcici": "Mogoče jutri za večerjo",
                "skakač": "Se nahajajo v prvi učilnici",
            },
        },
        "system33": {
            "conf": {
                "hosts": "127.0.0.1 kubernetes.docker.internal",
                "SAM": "3. of",
                "unown": "To so pa pokemoni. Kaj to dela tu?",
            },
            "etc": {
                "bind9": "Mar ni to iz linuxa?",
                "kerberos": {
                    "ldap": {
                        "oauth": "Mogoce malo pretiravamo s tem",
                    },
                },
            },
            "proc": {
                "1": {
                    "stat": "1 (systemd) S 0 1 1 0 -1 4194560 481029 154941123 116 2603 5073 5719 1970114 625967 20 0 1 0 2 107573248 3742 18446744073709551615 1 1 0 0 0 0 671173123 4096 1260 0 0 0 17 1 0 0 278344633 0 0 0 0 0 0 0 0 0 0",
                    "wchan": "0",
                    "setgroups": "allow",
                    "syscall": "6. information"
                }
            }
        },
        "NSA_server": {
            "tools": {
                "GHidra": "Priporocam. Zelo dobro orodje za napredne uporabnike!",
                "0_days": {
                    "print_spooler": "Ah, ta čas ko si klikal link je prišla že nova napaka zanj!",
                },
            },
            "countries": {
                "slovenia": {
                    "sova": "503",
                    "ptr": "Status unknown. Monitoring.",
                    "psl": "Too closely related to ptr. Monitoring.",
                    "emil": "1. Indexing",
                }
            }
        },
        "dev": {
            "sda": {
                "1": "Bootloader? Kaj sploh je to?",
                "2": "O ne, tu je windows! Abort!",
                "3": {
                    "os": "PTR linux",
                    "secret_data": "7be3c0fe28014a03",
                    "other_data": "The secret_data is just a bait, watch out!",
                }
            },
            "random": "https://xkcd.com/221/",
        },
        ".pron": "Ne ne, tu ne gres naprej!",
        "lov_na_kravo": {
            "zakaj_lovimo_kravo": "Unga! Amba! Hama!",
            "CO2": {
                "vzrok": "Prenajedanje, seveda!... Ane?...",
                "stevilo": "9. pain...",
            },
        },
        "sola": {
            "programi": {
                "zoom": "sirina++; visina++;",
                "discord": "Uff, ampak profesorji ne zanjo te tehnologije uporabljati!",
                "teams": "7. is",
                "BBB": "BB-kaj?",
            },
            "domace_naloge": {
                "sportna_vzgoja": "Naredi 10 pocepov",
                "matematika": "2+2/2 = 2\nKako 3? A se hecate!",
                "programiranje": "Pojdi iz stanovanja. Pa prosim zares tokrat! Slika iz okna ne velja.",
            },
            "COVID-19": "A ni ze dost? Nehajte s cetrtim valom!",
        },
        "aliens": {
            "movies": {
                "ET": "ET go home!",
                "District_9": "Koliko časa je potrebno za popravilo ladje???",
                "south_park": "Ste vedeli, da sko vesoljci skriti v velikem število njihovih epizod?",
                "alien_vs_predator": "4. this",
                "X-Files": "Serija je boljša!",
                "The_thing": "1982 was a long time ago...",
                "Star_trek": "Or star wars?...",
            },
            "area51": {
                "pictures": "&lt;Restricted&gt;",
                "location": "&lt;Restricted&gt;",
                "Jetpacks": "&lt;Restricted&gt;",
                "GTA_SA": "&lt;Restricted&gt;",
                "Restricted": "&lt;Restricted&gt;",
                "Unrestricted": "&lt;Still Restricted&gt;",
            },
            "existence": "Maybe? Probably! But how can we know... BUT THERE'S WATER ON MARS!",
        },
        "sadje": {
            "slon": "Dobra glasba!",
            "kaj_pa_zelenjava": {
                "bucke": "Mmmmmm",
                "solata": "Bom vzel ob kosilu, samo da ne bo spet tako kisla!",
                "paradiznik": "Čaki, to ni zelenjava!",
            },
            "nabor": {
                "vse_skupaj": "To je že sadna solata? A to spada pol v zelenjavo?",
                "jabolko": "A je ta tisti, ki je padel Newtnu na glavo?",
                "paradiznik": "9. pain...",
                "hruske": "Super zadeva za izdelavo zvarkov! Ampak rabi biti pravi tip hruške.",
            },
        },
    }

    def get_path(paths, data):
        if len(data) == 0:
            return paths

        if data[0] not in paths:
            return None

        return get_path(paths[data[0]], data[1:])

    path = get_path(paths, data)

    html = ""
    if type(path) == dict:
        html += "<h1>\n"
        url = "/s/pot/"
        html += '<a href="' + url + '">/</a>\n'
        for d in data:
            url += d + "/"
            html += '<a href="' + url + '">' + d + '/</a>\n'
        html += "</h1><br/><br/>\n"

        for k in path.keys():
            html += '<a href="' + (url + k + "/") + '">' + k + '</a><br/>\n'

    elif type(path) == str:
        if path[:8] == "https://":
            return redirect(path)
        html = path
    else:
        html = 'Neznana pot. Vrni se <a href="/s/pot/">nazaj</a>!'

    return html
