#!/usr/bin/env python
# coding: utf-8

# In[21]:


import wbdata
import datetime
wbdata.get_source()
wbdata.get_topic()
wbdata.search_countries('Pakistan')
wbdata.search_indicators("GDP per capita") #NY.GDP.PCAP.PP.CD, GDP per capita (current US$)
wbdata.search_indicators("Undernourishment") #SN.ITK.DEFC.ZS, Prevalence of undernourishment (% of population)
wbdata.search_indicators("Life expectancy") #SP.DYN.LE00.IN, Life expectancy at birth, total (years)
data_date = datetime.datetime(1900, 1, 1), datetime.datetime(2020, 1, 1)
indicators = {"NY.GDP.PCAP.PP.CD": "GDP Per capita","SN.ITK.DEFC.ZS": "Prevalence of undernourishment (% of population)", "SP.DYN.LE00.IN": "Life expectancy at birth, total (years)"}
country = [i['id'] for i in wbdata.get_country(country_id='PAK')] 
df = wbdata.get_dataframe(indicators, country=country, convert_date=True)
df.dropna(inplace=True)
df.count()
df.to_csv('pakistan.csv',index=False)

