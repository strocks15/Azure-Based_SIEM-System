import json
import datetime 
import threading

# the file to be converted
filename = 'failed_rdp.txt'
 
# resultant dictionary
dict1 = {}
 
# fields in the sample file
#latitude:47.91542,longitude:-120.60306,destinationhost:samplehost,
#username:fakeuser,sourcehost:24.16.97.222,
#state:Washington,country:United States,
#label:United States - 24.16.97.222,timestamp:2021-10-26 03:28:29

fields =['latitude','longitude','destinationhost','username','sourcehost','state','country','label','timestamp']
 
with open(filename) as fh:
     
 
     
    # count variable for each attack id creation
    l = 1
     
    for line in fh:
         
        # reading line by line from the text file
        description = list( line.strip().split(None, 4))
         
        # for output see below
        print(description)
         
        # for automatic creation of attack id for each attack
        sno ='atck'+str(l)
     
        # loop variable
        i = 0
        # intermediate dictionary
        dict2 = {}
        while i<len(fields):
             
                # creating dictionary for each attacker details
                dict2[fields[i]]= description[i]
                i = i + 1
                 
        # appending the record of each attacker to
        # the main dictionary
        dict1[sno]= dict2
        l = l + 1
 
 
# creating json file       
out_file = open("Jfailed_rdp.json", "w")
json.dump(dict1, out_file, indent = 9)
out_file.close()
