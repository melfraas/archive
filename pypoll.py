#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import csv


# In[36]:


election_data = os.path.join("..", "Resources", "election_data.csv")


# In[37]:


with open(data_path) as data_file:
    csvreader = csv.reader(data_file, delimiter= ',')

    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    
    
 #create lists for each item   
    voterID = []
    County = []
    Candidate = []
    for row in csvreader:
        voterID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
    countyCandidate=zip(County,Candidate)
    election_dict=dict(zip(voterID, countyCandidate))
        


# In[ ]:


#total number of votes cast

voteTotal=len(election_dict)
voteTotal


# In[21]:


#list of candidates who received votes
def unique_candi(_candidate):
    individualCandidate=[]
    for c in Candidate:
        if c not in Candidate:
            individualCandidate.append(c)
    return unique_candi


# In[22]:


def print_unique_candidate(_candidate):
    _list=unique_candidate()
    for i in _list:
        print(_list)
        


# In[29]:


#print each candidate's total votes
def voteCounter(_candidate):
    k, co, l, t = 0, 0, 0, 0

    for c in Candidate:
        if c=="Khan":
            k+=1
        elif c=="Correy":
            co+=1
        elif c=="Li":
            l+=1
        elif c=="O'Tooley":
            t+=1

    
    vote_numbers=[k,co,l,t]
    return vote_numbers


# In[27]:


voteCounter(Candidate)


# In[28]:


def percentCalc(_list):
    percentage_list=[]
    _list=voteCounter(Candidate)
    
    total_vote=sum(_list)
    for i in _list:
        percent=((i/total_vote)*100,2)
        percentage_list.append(percent)
    return percentage_list


# In[30]:


percentCalc(Candidate)


# In[34]:


def create_election_dict(_list):
    candidate=[]
    percentage = []
    vote = []
    _list=
    candidate=unique_candidate(Candidate)
    percentage=percentage_calculator(Cdandidate)
    vote=voteCounter(Candidate)
    percentage_vote=zip(percentage, vote)
    created_dict=dict(zip(candidate,percentage_vote))
    print(created_dict)
    


# In[35]:


create_election_dict(Candidate)


# In[ ]:




