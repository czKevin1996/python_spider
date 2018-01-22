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

def deal_func(table1, table2): 
    #first table
    table1_columns_name = table1[:1]    # columns name
    table1_values = table1[1:]                       #values
    table1_df = pd.DataFrame(table1_values, columns = table1_columns_name.tolist())   #change into dataframe
    table1_origin = table1_df.copy()         #origin data
    table1_df = table1_df.replace('', 0)    # replace blank with 0
    table1_df  = table1_df .apply(pd.to_numeric, errors = 'ignore')  #change into float
    df_sort_1 = table1_df .sort_values(by = table1_columns_name[0][2]   , ascending = False)   #sort 
    df_sort_2 = table1_df .sort_values(by = table1_columns_name[0][4]   , ascending = False)  #sort
    
    #second table
    table2_columns_name = table2[0:1]    # columns name
    table2_values = table2[1:]
    table2_df= pd.DataFrame(table2_values,columns = table2_columns_name.tolist() ) 
    
#     s1, s2 = metal_year(table1_origin.table1_columns_name[0])
#     table1_insert = table1_insert.copy()
#     table1_insert['metal'] = s1
#     table1_insert['year']=s2

    return table1_origin, df_sort_1,  df_sort_2, table2_df

array1, array2 = GetTwoTable()
print array1

def metal_month(first_colummn):
    metal = list()
    month = list()
    for first in first_column:
        metal.append( first[0:2] )
        month.append( first[2:] )
        s1 = pd.Series( np.array(metal) )
        s2 = pd.Series( np.array(month) )
        return s1, s2
  

        


