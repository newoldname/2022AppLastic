f = open("/Users/kyj/Library/CloudStorage/OneDrive-SangMyungUniversity/대학/elasticTeam/Driver_Notes/countryCode.txt","r")
line = f.readlines()
for a in line:
    print("\"", end="")
    print(a[5:-1], end="\", ")
