import csv
import json
import math

#To update role priorities use me:
#copy the latest version of the role descriptions constant, JSON ONLY!! to roles.json
##NOTE - the roles, must be in priority order
#create the desired version of RatiosModified.csv
#run the script and copy and paste the output to appropirate places
##paste to the model, four lines


#get list of founder roles
rolesfile = open('roles.json')
roles = json.load(rolesfile)
employees = [role["name"] for role in roles["employees"]]
founders = [role["name"] for role in roles["companies"]]
investors = [role["name"] for role in roles["investors"]]
#print employees
#print founders
#print investors

#get string of added types from ratios csv files
priorityfile = open('ratios.csv')
prioritycsv = csv.reader(priorityfile, delimiter='\t')
prioritydata = []
next(prioritycsv)  #skipping heading
for row in prioritycsv:
    prioritydata.append([int(row[1]),int(row[2]),int(row[3])])
#print prioritydata

#get a string of role type's
added_types = [None]*(len(prioritydata)-1)
for i in range(0,len(prioritydata)-1):
    diff = [x - y for x, y in zip(prioritydata[i+1], prioritydata[i])]
    if diff[0] > 0:
        added_types[i] = "founder"
    if diff[1] > 0:
        added_types[i] = "investor"
    if diff[2] > 0:
        added_types[i] = "employee"

#for each increment, add the appropriate role

prioritized_roles = {}
prioritized_roles["founder"] = founders
prioritized_roles["investor"] = investors
prioritized_roles["employee"] = employees

count = {}
count["founder"] = 0
count["investor"] = 0
count["employee"] = 0

priority_list = []
for role_type in added_types:
    priority_index = count[role_type]%len(prioritized_roles[role_type])
    which_pass = int(math.floor(count[role_type]/len(prioritized_roles[role_type])) + 1)
    next_role = prioritized_roles[role_type][priority_index]
    if role_type in ("founder","investor"):
        next_role = next_role + "_" + str(which_pass)
    priority_list.append(next_role)
    count[role_type] += 1

print ", ".join(priority_list)
print ""
print ", ".join(prioritized_roles["founder"])
print ""
print ", ".join(prioritized_roles["investor"])
print ""
print ", ".join(prioritized_roles["employee"])
print ""
print "\n".join(priority_list)















