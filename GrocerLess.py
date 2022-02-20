import csv
import pandas as pd
import numpy as np
df=pd.read_csv('products.csv')#
df1=pd.read_csv('stores.csv')#
#print(df)
#print(df1)
l=input().split(' ')
#print(l)
df=df[df['Product_Name'].isin(l)]#dataframe is reduced to having only particular rows of products user is interested in
#Sprint(df)
stores=[]
for i in df['Store_ID']:
    if i not in stores:
        stores.append(i)
#print(stores)
i=len(df)
#print(i)
listrows=[]
for row in range(i):
    #print(row)
    #print("dataframe\n",df.iloc[row])
    listrows.append(df.iloc[row])
    
#print(listrows)
sum=0
pricelist=[]
list_rows=[]
for i in stores:#extracting sum of the prices of the interested products from each store
    sum=0
    count=0
    for j in listrows:
            if j['Store_ID']==i:
                sum=sum+j['Price']
                count=count+1
            else: 
                count=0
            if count==len(l):
                pricelist.append(sum)       
    #sum=0
print(pricelist)
leastprice=min(pricelist)#finding min price
indexvalue=pricelist.index(leastprice)
dest_store=stores[indexvalue]#finding the store which sells the products at the least price
print (df1)
#print(df)
length_stores=len(df1)
list_store=[]
for row in range(length_stores):
    list_store.append(df1.iloc[row])
for i in list_store:
    if i['store_ID']==dest_store:
        print("The store at which the products-",l,"are available at a economical rates is at",i['store_name'],"located at",i['location'])
        break;