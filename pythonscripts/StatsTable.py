# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 17:54:26 2019

@author: User1
"""
quote_page = "https://www.basketball-reference.com/leagues/NBA_2018_per_game.html"

hp = HTMLTableParser()
table = hp.parse_url(quote_page)