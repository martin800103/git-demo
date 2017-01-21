#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 11:45:56 2016

@author: martin
"""

f = open("la_weather.csv",'r')
data = f.read()
rows = data.split('\n')
weather_data = []
for row in rows:
    dataset = row.split(',')
    weather_data.append(dataset)

print(weather_data)

weather = []
for item in weather_data:
    weather.append(item[1])
print(weather)

count = 0

for item in weather:
    count += 1
    
print(count)

#remove the header
new_weather = weather[1:]
print(new_weather)

#learn how to use in
animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = "cat" in animals
space_monster_found = "space_monster" in animals

#save the boolean result in list
weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []
for item in weather_types:
    w_t = item in new_weather
    weather_type_found.append(w_t)
print(weather_type_found)

print(weather)
print(weather[len(weather)-1])


pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]
pantry_counts = {}
for item in pantry:
    if item in pantry_counts:
        pantry_counts[item] +=1
    else:
        pantry_counts[item] = 1

print(pantry_counts)


weather_counts = {}

for item in weather:
    if item in weather_counts:
        weather_counts[item] += 1
    else:
        weather_counts[item] = 1

print(weather_counts)
