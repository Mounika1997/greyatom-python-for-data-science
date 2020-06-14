# --------------
# Code starts here

# Create the lists 
class_1 = ["Geoffrey Hinton" , "Andrew Ng" , "Sebastian Raschka" , "Yoshua Bengio"]

class_2 = ["Hilary Mason" , "Carla Gentry", "Corinna Cortes" ]

# Concatenate both the strings
new_class = class_1 + class_2 
print(new_class)

# Append the list
new_class.append("Peter Warden")

# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove("Carla Gentry")
# Print the list
print(new_class)



# Create the Dictionary
courses  = {"Maths" :65, "English" :70, "History" :80, "French" :70, "Science" :60} 
     
 
total = 65 + 70 + 80 + 70 + 60
print(total)
percentage = (total/500) * 100
print(percentage)
# Slice the dict and stores  the all subjects marks in variable


# Store the all the subject in one variable `Total`

# Print the total

# Insert percentage formula

# Print the percentage




# Create the Dictionary
 
mathematics = {"Geoffrey Hinton" :78, "Andrew Ng" :95, "Sebastian Raschka" :65, "Yoshua Benjio" :50, "Hilary Mason" :70, "Corinna Cortes" :66, "Peter Warden" :75}

max_marks_scored = max(courses,key = courses.get)
print(max_marks_scored)

topper = max(mathematics,key = mathematics.get)
print(topper)

first_name = topper.split( )
Last_name = topper.split( )
# Given string
#print(first_name)
#print(Last_name)
full_name = first_name[1] + " " + Last_name[0]
#print(full_name)
certificate_name = full_name.upper()

print(certificate_name)
# Create variable first_name 

# Create variable Last_name and store last two element in the list

# Concatenate the string

# print the full_name

# print the name in upper case

# Code ends here


