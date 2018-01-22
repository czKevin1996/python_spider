#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import numpy as np

def getHTML():
  url = "http://www.shfe.com.cn/statements/delaymarket_all.html"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "lxml")

  table1 = list()
  for it in soup.find_all('table')[0].find_all('tr'):
    temptr = list()
    for lt in it: 
      temptr.append(lt.string)
    table1.append(temptr)

  tb1 = np.array(table1[1:])
  tb1 = tb1[tb1!=u'\n'].reshape(162,13)
  #print tb3.dtype, type(tb3[0,0])
  
  #for i in range(tb3.shape[0]):
  #  for j in range(tb3.shape[1]):
  #    print tb3[i,j],
  #  print 
  table2 = list()
  for it in soup.find_all('table')[1].find_all('tr'):
    temptr = list()
    for lt in it:
      temptr.append(lt.string)
    table2.append(temptr)
  tb2 = np.array(table2)
  tb2 = tb2[tb2!=u'\n'].reshape(2,9)
  
  return tb1, tb2



