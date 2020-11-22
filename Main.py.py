#!/usr/bin/env python
# coding: utf-8

# In[71]:


import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
   # for _ in csv_reader:
   #     print(_)
        
        #create colums to store data
    Date = []
    ProfLoss = []
    
    for row in csv_reader:
        Date.append(row[0])
        ProfLoss.append(int(row[1]))
    budget = dict(zip(Date,ProfLoss))
    


#create iterator to loop through sheet
#for row in csv_reader:
        # count the total number of months
       # total_months += 1
        
#calculate changes in profit and losses over entire period

#find greatest increase in proits over entire period
    


# In[77]:


#print total month
def month_counter(_budget):
    month_counter=len(_budget) 
    
    print(str(month_counter))


# In[94]:


def totalBudget(total):
    t_budget=0
    for i in total:
        t_budget=t_budget+total[i]
    print("Total : $" +str(t_budget))


# In[103]:


def newlists (ProfLoss):
    Prof_change = []
#calculate the change in profit from month to month
    for I in range(0, len(ProfLoss)-1):
        Prof_change.append(ProfLoss[I+1]-ProfLoss[I])
        
    return Prof_change


# In[96]:


## check where _list is neeed
def Average(list):
    list=newlists(ProfLoss)
        
    num_change=len(list)

    total_changes=sum(list)

    average_change = round(total_changes/num_change, 4)
    
    print("Average Change $" +str(average_change))


# In[105]:


def sortedDictionary(_date):
    monthlyChange=[]
    for i in range(1,len(_date)):
        monthlyChange.append(_date[i])
    
    change_budget = newlists(ProfLoss)

    zippedLists = dict(zip(monthlyChange, change_budget))
    sortedDictionary = dict(sorted(zippedLists.items(), key=lambda x:x[1], reverse=True))
    return sortedDictionary


# In[106]:


def print_greatest_increase(_sorted):
    _sorted=sortedDictionary(Date)
    for x in list(_sorted)[0:1]:
        print("Greatest increase in profits: {}, ${} ".format(x, _sorted[x]))


# In[107]:


def print_greatest_decrease(sorted):
    _sorted=sortedDictionary(Date)
    for x in list(_sorted)[-1:]:
        print("Greatest decrease in profits: {}, ${} ".format(x, _sorted[x]))


# ## financial analysis
# 

# In[109]:


month_counter(budget)
totalBudget(budget)
Average(ProfLoss)
print_greatest_increase(Date)
print_greatest_decrease(Date)


# In[ ]:




