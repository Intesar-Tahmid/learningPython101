# We are going to write a program that will convert a 3 digit month name to the full month name
#Firstly we have to give it a name

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",

}

print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Dex"))
print(monthConversions.get("Loc", "Not a valid key"))