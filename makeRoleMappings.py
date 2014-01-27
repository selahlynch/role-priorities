import json

#manually make roles.json out of roles.js

#take a roles.json file and pull out the company names
#for each company name create two mappings of xxxx_1=>xxxx and xxxx_2=>xxxx


rolesfile = open('roles.json')
roles = json.load(rolesfile)
role_mappings = {}

#company_names = [company["name"] for company in roles["companies"]]
#for name in company_names:
#    role_mappings[name+"_1"] = name
#    role_mappings[name+"_2"] = name
#    role_mappings[name+"_3"] = name

investor_names = [investor["name"] for investor in roles["investors"]]
for name in investor_names:
    role_mappings[name+"_1"] = name
    role_mappings[name+"_2"] = name


#print json.dumps(company_names, indent=4);
print json.dumps(role_mappings, indent=4, sort_keys=True);



