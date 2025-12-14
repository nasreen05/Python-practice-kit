info ={
    "key": "value",
    "subject": ["pthon","c","c++","java"],
    "name" : "reshma nasreen ",
    "learning":"coding",
    "age": 35,
    "is_adult":True,
    "marks":98.4
}


#print(info["surname"])
print(info["name"])
print(info["marks"])
print(info["subject"])
print(info["age"])

#------------------------------------------------------------


info["name"]= "shradhakhapra"

info["surnmame"]="Khaprs"
print(info)

#-----------------------------------------------------------


null_dict={}
null_dict["name"]= "reshma nasreenprin" 
print(null_dict)


#------------------------------------------------------
student = {
    "name": "rafia nasreen",
    "subject":{
        "phy":98,
        "che": 87,
        "math":95
    }
}
print("BEFORE")
print(student["name2"])
print("AFTER")

new_dict = {"city":"delhi","age":16}
student.update(new_dict)
print(student)


float(9)
print(list(student.keys()))
print(len(list(student.keys())))
print(student.values())
print(student.values())
pairs=list(student.items())
print(pairs[0])
print(student["name2"])
print(student.get("name2"))


#-------------------------------------------------------------


#nested dictionary
# print(teacher ["subject"]["chem"])

