#!/usr/bin/env python3

import random


def ruota(premio):
    # lista di premi
    premi = [
        "viaggio",
        "ps5",
        "xbox",
        "schedavideo",
        "fidanzata",
        "biglietto aereo",
        "disco gratis",
        "cena gratis",
        "auto",
        "ferrari",
    ]
    # scegli un premio a caso dalla lista
    premio = random.choice(premi)
    return premio


print(ruota())
