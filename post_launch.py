#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 20:21:58 2020

@author: andersmarstrand
"""


import requests # Dette module giver os mulighed for at få adgang til information fra nettet. 
from bs4 import BeautifulSoup as soup # Dette module -> class giver mulighed for at exstract info fra html. 

page = requests.get('https://www.proshop.dk/Grafikkort/MSI-GeForce-RTX-3080-  Ventus-3X-OC-10GB-GDDR6X-RAM-Grafikkort/2876879',)
soup = soup(page.content, "lxml") # .content - Returnerer html koden fra hjemmesiden. 

#print(page.status_code) # Skal printe 200, for at siden er aktiv. 
            
main_page = soup.find(id="siteContainer")
stock_status = main_page.find(class_="site-stock-text site-inline").get_text()

if stock_status == "Bestilt - ukendt leveringsdato":
    print("Ingen ændring")
else:
    print("Der er sket en ændren i lagerstatus på proshop!")

# Istedet for at printe, skal der sendes en mail i tilfælde af ændring. 
# Koden skal duplikeres og sættes op til fem forskellige hjemmesider.
# Med WayScript køres koden i loop hver time. (Mindre interval vil være bedre, men bekosteligt via WayScript)


