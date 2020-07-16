import json

jsonfile = open('cities_list.json', 'r')
data = json.load(jsonfile)

size = len(data["data"])
print(size)
"""
TO DO: 
# find unique countries 
# parse json file
# parse key values 
we managed to retrieve unique countries 
but we need name (city) and unique country 
pull file to database
export this file to flight_scheduling.py (Choose destination) cos Anais is hardcoding in countries is BAD
Anais to add method to append to current booking
Booking method inside assistant method Humza 
To create booking do stuff to link to aircraft 
"""



# def uniqueCountry_find():
#     countries = []
#     uniqueCountry = []
#     with open('cities_list.json') as data:
#         for line in data:
#             jsondata = json.loads(line)
#             dictjson = json.dumps(jsondata)
#             if 'country' in jsondata:
#                 uniqueCountry.append(jsondata['country']['name'])
#                 # countries.append(i)
#         jsonfile.close()
#         print(uniqueCountry)
# uniqueCountry_find()


# import csv
# import pandas as pd
# # with open('cities_list.csv', 'r+') as citylist:
# #     reader = csv.reader(citylist)
# #     citydict = {}
# #     for i in reader:
# #         k, v = i
# #         citydict[k] = v
#
# #p = pd.read_csv('cities_list.csv', header=None, index_col=0, squeeze=True).to_dict()
# #print(p)
#
# import json
#
# # Opening JSON file
#
# with open('cities_list.json') as json_file:
#     data = json.load(json_file)
#
#
#     # for reading nested data [0] represents
#
#     # the index value of the list
#
#     #print(data['country'][0])
#
#     # for printing the key-value pair of
#
#     # nested dictionary for looop can be used
#
#     print("\nPrinting nested dicitonary as a key-value pair\n")
#
#
#     for i in data:
#
#         print("Country:", i['country'])
#
#         print("Name:", i['name'])
#
#
# # print("Started Reading JSON file")
# # with open("developer.json", "r") as read_file:
# #     print("Converting JSON encoded data into Python dictionary")
# #     developer = json.load(read_file)
# #
# #     print("Decoded JSON Data From File")
# #     for key, value in developer.items():
# #         print(key, ":", value)
# #     print("Done reading json file")
#
# # country_set
#
# returnValue =