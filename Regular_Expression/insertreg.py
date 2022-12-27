# import re

# line = r"INSERT INTO `abcauthenticatedtypes` VALUES (1,'none'),(2,'optional'),(3,'required');\r\n"

# line2 = "INSERT INTO `abcauthenticatedtypes` VALUES (1,'none'),(2,'optional'),(3,'required');\n"
# line3 = "insert  into `abcauthenticatedtypes`(`AuthenticatedTypeID`,`AuthenticatedType`) values (1,'none'),(2,'optional'),(3,'required');\r\n"

# pat1 = r"INSERT INTO (.+?) VALUES (.+?);\r\n"
# pat2 = r"INSERT INTO (.+?) VALUES (.+?);\n"


# new1 = re.match(pat1, line2)
# if new1:
#     print(new1.groups())


import re

regex = r"INSERT INTO (.+?) VALUES (.+?);\r\n"
regexi = r"insert  into (.+?) values (.+?);\r\n"
string = "INSERT INTO `abcauthenticatedtypes`(`AuthenticatedTypeID`,`AuthenticatedType`) VALUES (1,'none'),(2,'optional'),(3,'required');\r\n"

string1 = "insert  into `abcauthenticatedtypes`(`AuthenticatedTypeID`,`AuthenticatedType`) values (1,'none'),(2,'optional'),(3,'required');\r\n"

# reg1 = re.match(regex, string) or re.match(regexi, string1)
reg1 = re.match(regex, string1, re.IGNORECASE)

if reg1:
    print("The string matches the regular expression.")
else:
    print("The string does not match the regular expression.")
