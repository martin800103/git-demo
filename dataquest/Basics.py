
# coding: utf-8

# In[2]:

f = open("US_births_1994-2003_CDC_NCHS.csv","r").read().split("\n")
print(f[:10])


# In[2]:

def read_csv(file):
    string_list = open(file,"r").read().split("\n")[1:]
    final_list=[]
    for i in string_list:
        string_fields=i.split(",")
        int_fields = []
        for a in string_fields:    
            int_fields.append(int(a))
        final_list.append(int_fields)
    return final_list
        
cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
print(cdc_list[:10])


# In[3]:

def month_births(input_list):
    births_per_month = {}
    for item in input_list:
        if item[1] in births_per_month:
            births_per_month[item[1]] +=item[4]
        else:
            births_per_month[item[1]] = item[4]
    return births_per_month
cdc_month_births=month_births(cdc_list)
print(cdc_month_births)


# In[4]:

def dow_births(input_list2):
    births_per_week = {}
    for item in input_list2:
        if item[3] in births_per_week:
            births_per_week[item[3]] +=item[4]
        else:
            births_per_week[item[3]] = item[4]
    return births_per_week
cdc_day_births=dow_births(cdc_list)
print(cdc_day_births)


# In[5]:

def calc_counts(data,column):
    births_per_time = {}
    for item in data:
        if item[column] in births_per_time:
            births_per_time[item[column]] +=item[4]
        else:
            births_per_time[item[column]] = item[4]
    return births_per_time


# In[6]:

cdc_dow_births=calc_counts(cdc_list,3)
print(cdc_dow_births)


# In[7]:

cdc_year_births=calc_counts(cdc_list,0)
print(cdc_year_births)


# In[8]:

cdc_month_births=calc_counts(cdc_list,1)
print(cdc_month_births)


# In[9]:

cdc_dom_births=calc_counts(cdc_list,3)
print(cdc_dom_births)


# Write a function that can calculate the min and max values for any dictionary that's passed in.

# Write a function that extracts the same values across years and calculates the differences between consecutive values to show if number of births is increasing or decreasing.
# For example, how did the number of births on Saturday change each year between 1994 and 2003?

# 
