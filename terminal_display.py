# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 20:04:45 2023

@author: jaiga
"""
import pandas as pd
import numpy as np


name_width = 33
location_width = 33
lodging_width = 12
price_width = 5
reviews_width = 10
locationFilter = 0
    

# custom function to generate next table row
def genNextRow(dfRow):
        name = dfRow['name']
        words = name.split()
        if locationFilter == 0:
            location = dfRow['neighbourhood'] + ', ' + dfRow['neighbourhood_group']
        elif locationFilter == 1:
            location = dfRow['neighbourhood']
        lodging = 'Home/Apt' if dfRow['room_type'] != 'Private room' else 'Private Room'
        price = dfRow['price']
        reviews = dfRow['number_of_reviews']
        
        row = ""
        extraRow = True
        
        while (extraRow):
            extraRow = False
            row += "\n|"
            
            # other name display logic
            name = ''
            for i in range(len(words)):
                if (len(name)==0 and len(words[0])==name_width):
                    name = " " + words[0]
                    break
                elif ((len(words[i])+len(name)) > (name_width-1)):
                    extraRow = True
                    words = words[i:]
                    break
                else:
                    name = name + " " + words[i]
            else:
                words = ['']
            row += name + (" " * (name_width-len(name)+1))
            row += " | "
            
            # location display logic
            if (len(location) > location_width): 
                extraRow = True
                row += location[:location_width]
                location = location[location_width:]
            else:
                row += location + (" " * (location_width-len(location)))
                location = ''
            row += " | "
            
            # lodging display logic
            if (len(lodging) > lodging_width): 
                extraRow = True
                row += lodging[:lodging_width]
                lodging = lodging[lodging_width:]
            else:
                row += lodging + (" " * (lodging_width-len(lodging)))
                lodging = ''
            row += " | "
            
            # price display logic
            if (len(price) > price_width): 
                extraRow = True
                row += price[:price_width]
                price = price[price_width:]
            else:
                row += price + (" " * (price_width-len(price)))
                price = ''
            row += " | "
            
            # reviews display logic
            if (len(reviews) > reviews_width): 
                extraRow = True
                row += reviews[:reviews_width]
                reviews = reviews[reviews_width:]
            else:
                row += reviews + (" " * (reviews_width-len(reviews)))
                reviews = ''
            row += " | "
            
        return (row + genRowDivider())


# custom function to create table row divider
def genRowDivider():
    rowDiv = ("\n+" + "-"*(name_width + 2) + 
              "+" + "-"*(location_width + 2) + 
              "+" + "-"*(lodging_width + 2) +
              "+" + "-"*(price_width + 2) +
              "+" + "-"*(reviews_width + 2) + "+")
    return rowDiv


# custom function to create table header
def genHeader():
    header = ("\n| Name"    + " "*(name_width-3) +
              "| Location"  + " "*(location_width-7) +
              "| Lodging"   + " "*(lodging_width-6) +
              "| Price"     + " "*(price_width-4) +
              "| Reviews"   + " "*(reviews_width-6) + "|")
    return (genRowDivider() + header + genRowDivider())


# driver code
df = pd.read_csv(r"C:\Users\jaiga\Test Folder\DWDM Lab\AB_NYC_2019.csv")
df = df.astype(str)

output = genHeader()
for i in range(10, 140, 13):
    output += genNextRow(df.iloc[i])

print(output)
input("Close")