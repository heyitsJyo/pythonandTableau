# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 21:26:13 2024

@author: Administrator
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json file

with open('loan_data_json.json') as json_file:
    data=json.load(json_file)
    
#transform to dataframe

loandata=pd.DataFrame(data)    

#finding unique values to Purpose column
loandata['purpose'].unique()

#describe the data
loandata.describe()

#using EXP to get the annual income
income = np.exp(loandata['log.annual.inc'])

#working with arrays
arr=np.array([1,2,3])

# 0d array
arr=np.array(28)

#2d
arr=np.array([[1,2,3],[4,5,6]])

#working with if statements
a=40
b=500
if a > b:
    print('b is greater than a')
    
a =40
b =500
c= 1000

if b>a and b<c:
   print('b is greater than a but less than c')  
   
#what if a condition is nt met
a=40
b=500
c=20

if b>a and b<c:
    print('b is greater than a but less than c')
else:
    print('no condition met')
    
#another condition but different metrics

a=40
b=500
c=30

if b>a and b>c:
   print('b is greater than a and less than c')
elif b>a and b>c:
   print('b is greater than a and c')    

#using OR
a =40
b =500
c= 1000

if b>a or b<c:
   print('b is greater than a but less than c')  
   
#FICO score   
   
# fico >= 300 and < 400:
# 'Very Poor'
# fico >= 400 and ficoscore < 600:
# 'Poor'
# fico >= 601 and ficoscore < 660:
# 'Fair'
# fico >= 660 and ficoscore < 780:
# 'Good'
# fico >=780:
# 'Excellent'   

fico = 800

if fico >= 300 and fico < 400:
   ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
   ficocat = 'Poor'
elif fico >= 601 and fico < 660:
   ficocat = 'Fair'
elif fico >= 660 and fico < 780:
   ficocat = 'Good'
elif fico >=780:
   ficocat = 'Excellent'  
else:
    ficocat ='unknown'
print(ficocat)   


#FOR loop

fruits=['apple','pear','banana','cherry']
for x in fruits:
    print(x)
    y= (x)+' fruits'   
    print(y)

for x in range(0,4):
    y=fruits[x]+' for sale'
    print(y)
    
#applying for loops to loan data
#using first 10

length=len(loandata)
ficocat=[]
for x in range(0,length):
    category=loandata['fico'][x]
    if category >= 300 and category < 400:
        cat='very poor'
    elif category >= 400 and  category <600:
        cat='poor'
    elif category >=601 and category<660:
        cat='fair'
    elif category >=660 and category <700:
        cat='good'
    elif category>=700:
        cat='excellent'
    else:
        cat='unknown'
    ficocat.append(cat)    
    
 #to change ficocat to series
ficocat=pd.Series(ficocat)   

#creating new column to loandata
loandata['ficocat.category']=ficocat

#while loop(basic structure)

i=1
while i<10:
    print(i)
    i=i+1
    
#testing errors

length=len(loandata)
ficocat=[]
for x in range(0,length):
    category='red'
    try:
        if category >= 300 and category < 400:
            cat='very poor'
        elif category >= 400 and  category <600:
            cat='poor'
        elif category >=601 and category<660:
            cat='fair'
        elif category >=660 and category <700:
            cat='good'
        elif category>=700:
            cat='excellent'
        else:
            cat='unknown'
    except:
         cat='error'
    ficocat.append(cat)     
    
    
#df.loc as conditional statements

#df.loc[df[columnname] condition , new column name]='value if the c ondition is met'

#for interest rates , a new column is wanted , rate >o.12 then high else low

loandata.loc[loandata['int.rate']>0.12 , 'int.rate.type']='high'
loandata.loc[loandata['int.rate']<=0.12 , 'int.rate.type']='low' 

#number loans /rows by fico.category
catplot = loandata.groupby(['ficocat.category']).size()
purposecount = loandata.groupby(['purpose']).size()

#to draw plots (i.e gragh)
catplot = loandata.groupby(['ficocat.category']).size()
catplot.plot.bar()
plt.show() 

#to change the color of plot
catplot = loandata.groupby(['ficocat.category']).size()
catplot.plot.bar(color='yellow')
plt.show()

#to change the width of plots(graphs size)
catplot=loandata.groupby(['ficocat.category']).size()
catplot.plot.bar(color='yellow',width = 0.1)
plt.show()

#to change plots for purpose column
purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar()
plt.show()

#to change the colors
purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color='green')
plt.show()

#to change the size

#scattering plots

xpoint=loandata['ficocat.category']
ypoint=loandata['dti']
plt.scatter(xpoint,ypoint)
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv',index=True)

    
    
    
    






















