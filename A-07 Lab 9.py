#!/usr/bin/env python
# coding: utf-8

# In[31]:


class Animal:               # Parent class
    def __init__(self, name):
        self.name = name 

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):        
    def speak(self):
        print(f"{self.name} barks")

a = Animal("wild animal")
a.speak()

d = Dog("Buddy")
d.speak() 

class Bird:
    def fly(self):
        print("Bird flies")
class Bat(Animal,Bird):
    
    def sleep(self):
        print("Bat sleeps")
bat=Bat("Bat")
bat.speak()
bat.sleep()
bat.fly()


# In[44]:


#polymorphism
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return self.length * self.breadth  
class Circle:
    def __init__(self, radius):
        self.radius = radius   

    def area(self):
        return self.radius**2 * 3.14  

def print_area(shape):
    print(f"Area: {shape.area()}")  
# Create instances
rectangle = Rectangle(23, 78)
circle = Circle(89)

# Print areas
print_area(rectangle)
print_area(circle)

    
    
   

        
        


# In[67]:


# Write a program to create example.txt file by using write mode,appeand mode,x mode

f = open("example121.txt", "x")
f.write("hello\n")
f.write("world\n")

f.close()
f=open("example121.txt","r")
content=f.read()
print(content)

f1=open("example122.txt","w")
f1.write("this is pcu\n")
f1.write("pune\n")

f1.close()
f=open("example122.txt","r")
content=f.read()
print(content)

f2=open("example123.txt","a")
f2.write("pcet")
f2.write("world\n")

f2.close()
f=open("example123.txt","r")
content=f.read()
print(content)



# In[76]:


# write a program to create list with string for line 1,string for line 2,string 3 for line 3 . write list into new file list_example.txt and print the content from file

l1 = ["String for line 1", "String for line 2", "String for line 3"]


f=open('list_example2.txt', 'w')
for line in l1:
        file.write(line + '\n')  
f= open('list_example2.txt', 'r') 
content = file.read()  

print(content) 







# In[ ]:





# In[ ]:




