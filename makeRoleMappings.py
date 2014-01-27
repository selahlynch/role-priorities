import json

#manually make roles.json out of roles.js

rolesfile = open('roles.json')
roles = json.load(rolesfile)


#FOUNDERS
role_mappings = {}
company_names = [company["name"] for company in roles["companies"]]
for name in company_names:
    role_mappings[name+"_1"] = name
    role_mappings[name+"_2"] = name
    role_mappings[name+"_3"] = name
print json.dumps(role_mappings, indent=4, sort_keys=True);


#INVESTORS
role_mappings = {}
investor_names = [investor["name"] for investor in roles["investors"]]
for name in investor_names:
    role_mappings[name+"_1"] = name
    role_mappings[name+"_2"] = name
print json.dumps(role_mappings, indent=4, sort_keys=True);




