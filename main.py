import spider
import pandas

# FROM:xjm
#firsttable->array1  secondtable->array2
array1, array2 = spider.GetTwoTable() 

table1_dataframe, table1_sort_1, table1_sort_2, table2_dataframe  = spider.deal_func(array1, array2)

table1_dataframe.to_csv('table_one.csv')
table2_dataframe.to_csv('table_second.csv')
table1_sort_1.to_csv('ups_and_downs.csv')
table1_sort_2.to_csv('VOL.csv')

print table1_dataframe
print table2_dataframe
print table1_sort_1
print table1_sort_2 