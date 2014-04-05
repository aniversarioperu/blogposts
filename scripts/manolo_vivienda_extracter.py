# -*- coding: utf8 -*-
import codecs
import json
import re
import sys

import dataset
"""
Extae datos de la SQLite de Manolo_vivienda
"""

db = dataset.connect("sqlite:///visitas.db")

def get_visitor_frequencies(db):
    f = codecs.open("visitor_name.csv", "w", "utf8")

    res = db.query("select * from visitas")
    for i in res:
        out = i['visitor'].strip()
        out = re.sub("\s+", " ", out)
        out = out.upper() + "\n" 
        f.write(out)
    f.close()

def get_entity(db):
    f = codecs.open("entity_name.csv", "w", "utf8")
    
    res = db.query("select * from visitas")
    for i in res:
        out = i['entity'].strip()
        out = re.sub("\s+", " ", out)
        out = out.upper() + "\n" 
        f.write(out)
    f.close()

def visitor_per_day(db):
    f = codecs.open("visitor_per_day.csv", "w", "utf8")
    
    res = db.query("select * from visitas")
    for i in res:
        out = i['date'].strip()
        out = re.sub("\s+", "", out)
        out += "\n"
        f.write(out)
    f.close()

#get_visitor_frequencies(db)
#get_entity(db)
visitor_per_day(db)
