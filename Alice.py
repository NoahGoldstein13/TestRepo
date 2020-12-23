#Dictonary creation challenge

user = {'name': 'Alice',
'height': '1.60 meters',
'shoe_size': 'American size 6.5, European size 37',
'hair': 'brown',
'eye_color': 'brown'}

print(user["name"], user["height"], user["shoe_size"], user["hair"], user["eye_color"])

print(f"My name is {user['name']}, my height is {user['height']}, my shoe size is {user['shoe_size']}, my hair color is {user['hair']}, my eyes are {user['eye_color']}.")

#If I want to print the keys
for key in user.keys():
     print(key)
#if I want to print everything print(user)
#if i want to print just the value, print(user["value"]) etc.
#or ask matteo if there is a possibility to print value with for or other stuff

#created another Key:value
user["favorite_movies"] = ["Dead poets society",
                        "The Talented Mr.Ripley",
                        "Jack the Ripper"]
print(user["favorite_movies"])
print(user)

#define a variable and .join function to be used to convert a list to a string

string2print = ", ".join(user["favorite_movies"])
print(f"My favorite movies are {string2print}")

for key in user.keys():
     print(key)

#define a variable
favorite_movies = user["favorite_movies"]

for movie in favorite_movies:
    print(movie)
