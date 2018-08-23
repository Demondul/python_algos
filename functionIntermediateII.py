# PART I
""" students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for student in students:
    print(str(student["first_name"]) + " " + str(student["last_name"])) """

###################

# PART II

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for userType in users:
    print(str(userType))
    for user in users[userType]:
        fName=str(user["first_name"])
        lName=str(user["last_name"])
        fullName=fName+lName
        print("1 - " + fName + " " + lName + " - " + str(len(fullName)))
