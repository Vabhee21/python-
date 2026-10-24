#Dictionary in python    (they are unordered ,mutable)
# dict={
#     "name" : "vabhee Maurya",
#     "course":"btech",
#     "branch":"CSDS",
#     "cgpa":9.5,

# }
# print(type(dict))
# print(len(dict))
# print(dict["name"])
# dict["grade"]="A"  #adding new keys
# dict["cgpa"]=9.7    #changing key value
# print(dict)

# info={
#     "name" : "vabhee",
#     "subjects" : ("math4","DS","COA","Python","UHVPE","DSTL"),
#     "age" : 20,
#     "adult" : True,
#     5 :25/5,
# }
# print(info)
# print(info["age"])
# info["age"]=21
# print(info)

# null_dict={}
# print(len(null_dict))


#Nested Dictionaries
# student={
#     "name" : "vabhee",
#     "score" : {
#         "chem" : 91,
#         "phy" : 83,
#         "math" : 96

#     }
# }
# print(student["score"])
# print(student["score"]["math"])

#Dictionary Methods
# info={
#     "name" : "vabhee",
#     "subjects" : ["math4","DS","COA","Python","UHVPE","DSTL"],
#     "age" : 20,
#     "adult" : True,
#     5 :25/5,
# }
# print(len(info))

# print(info.keys())         #return all keys values
# print(list(info.keys()))

# print(info.values())          #return all values

#print(info.items())       #returns all (key, value) pairs as tuples

# print(info.get("name"))      #return value at that key
# print(info["name"])
#print(info["name2"])     #error 
#print(info.get("name2"))   #none output


# info.update({"city" : "noida"})  #inserting specified items in to dictionary
# print(info)


#SET in python
    # set is coolection of the unorderesd items. unique and immutable.
# set={2,4,6,3,8,}
# print(set)
# print(type(set))

# collection={4,3,6,4,3,"hello","vabhee","hello",5,8}
# print(collection)
# print(len(collection))

# collection1={}  #empty dictionary
# print(type(collection1))

# collection2=set()  #empty set syntax
# print(type(collection2))

#set methods     #set is mutable,  elements are immutable
collection3={3,5,9,"vabhee","vivek"}
# collection3.add(8)
# collection3.add("vivan")
# collection3.add((1,2,3))    #tuples ko add kar skte hai but list ko nahi
# print(collection3)

#collection3.remove(9)       #remove that element

#collection3.clear()         #empties the set
#print(len(collection3))

#collection3.pop()            #remove a random elements

# collection2={"vivan",15,45}
# print(collection3.union(collection2))   #combine both set values &return new
#print(collection3)

# collection1={"vabhee","vivek"}
# print(collection3.intersection(collection1))   #combines common values & return new
# print(collection3)



# dict={
#     "table" : ("a piece of furniture","list of facts"),
#     "cat" : "a small animal"
# }
# print(dict)

# subjects={"python","java","C++","python","javascript","java","python","java","C++","c"}
# print(subjects)
# print("required classroms are",len(subjects))

#WAP to enter marks of 3 subjects from the user and store them in a dictionary . start with empty dictionary & add one by one . use subject name as key & marks as value
