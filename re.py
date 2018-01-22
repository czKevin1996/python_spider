import requests
import re

# get response
#res = requests.get("http://www.shfe.com.cn/statements/delaymarket_all.html")
#data = [x[2:len(x) - 5] for x in mat]
import numpy as np
import re
import requests
url = "http://www.shfe.com.cn/statements/delaymarket_all.html"
res = requests.get(url)
reg = r'">[\w|/|\.]*</td>|[n|d]>-*[\d|\.]*</fon'
mat = re.findall(reg, res.content)
data = [x[2:len(x) - 5] for x in mat]
table2 = data[len(data) - 8:]
table1 = data[:len(data) - 8]
p = np.array(table1)
p.shape = len(table1) / 12, 12
l = p.tolist()
print table2
for i in range(p.shape[0]):
    print l[i]