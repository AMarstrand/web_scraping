#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:33:02 2020

@author: andersmarstrand

Documentation: https://www.edureka.co/blog/web-scraping-with-python/

"""

#%% RTX 3000-serien

import pandas as pd
import requests # Dette module giver os mulighed for at få adgang til information fra nettet. 
from bs4 import BeautifulSoup as soup # Dette module -> class giver mulighed for at exstract info fra html. 

page = requests.get('https://www.komplett.dk/kampagne/121254/nvidia-geforce-3080-3090-3070?tag=Vis%20alt',)
soup = soup(page.content, "lxml") # .content - Returnerer html koden fra hjemmesiden. 

#print(page.status_code) # Skal printe 200, for at siden er aktiv. 

main_page = soup.find(id="MainContent")
items = main_page.find_all(class_="product-list-item")


produkt_navn = [item.find(class_="text-content").find("h2").get_text() for item in items] 
produkt_pris = "-"


""" 
***** 1. Forsøg på Error handler *****  
produkt_pris = [item.find(class_="product-price-now")]
if produkt_pris:
    produkt_pris = [item.find(class_="product-price-now").get_text()]
else:
    produkt_pris = "Pris: -"
continue
"""

"""
***** 2. forsøg på Error handler *****  

try:
    produkt_pris = [item.find(class_="product-price-now").get_text() for item in items]
except(TypeError,KeyError):
    produkt_pris = "Pris: -"
"""

gpu_liste = pd.DataFrame(
    {
     'Produkt': produkt_navn,
     'Pris': produkt_pris,
     })


print(gpu_liste)
#print(produkt_navn)
#print(produkt_pris)

#gpu_liste.to_csv("/Users/andersmarstrand/Desktop/web scraping/gpu_liste.csv")



