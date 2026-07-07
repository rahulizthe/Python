#-------solution 1
# name = input("enter your name: ")
# print(f"good Afternoon {name.capitalize()}")#using f string method here.
# print("good Afternoon", name.capitalize())

#-------solution 2
# letter = '''Dear <|name|>,
# You are selected!
# <|Date|>'''
# print(letter.replace("<|name|>","Rahul").replace("<|Date|>","28 september 2026"))

#--------solution 3 
# paragraph = "why suppose to be out baby grab your coffee out in a good time daily."
# print(paragraph.find("  "))

#--------solution 4
paragraph = "why  suppose to be out baby  grab  your  coffee out in a good time daily."
print(paragraph.replace("  "," "))
print(paragraph)#String is immutable that is why it is printing the previous string and here we can see in replacing the new string creats.








