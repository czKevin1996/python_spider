#-*coding:utf-8-*-
import numpy as np
import re
import requests

# GetTwoArray: get two arrays from page
# return: array1(big array), array2(small array)
def GetTwoTable():
    # get html
    url = "http://www.shfe.com.cn/statements/delaymarket_all.html"
    res = requests.get(url)
    # get data
    reg1 = r'">[\w|/|\.]*</td>|[n|d]>-*[\d|\.]*</fon'
    data = [x[2:len(x) - 5] for x in re.findall(reg1, res.content)]
    reg2 = r't">[^ ]*<'
    title = [x[3:len(x) - 1] for x in re.findall(reg2, res.content)]
    # change to array
    array1 = np.array(title[:12] + data[:len(data) - 8])
    array2 = np.array(title[12:] + data[len(data) - 8:])
    array1.shape = array1.size / 12, 12
    array2.shape = array2.size / 8, 8
    return (array1, array2)