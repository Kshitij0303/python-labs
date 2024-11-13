#!/usr/bin/env python
# coding: utf-8

# In[17]:





# In[31]:


f1= open('pcu89899.txt', 'w')
for x in range(10):
    f1.write("pcu pune\n")
f1.close()

f1=open('pcu89899.txt', 'r')

content = f.read()
for x in range(10):
    print(content)



# In[26]:


#write a program to create new file and add 10 lines of text in file by using "w" mode
f =open("pcu1099.txt","w")
f.write("hello \n")
f.write("world\n")
f.write("pcu\n")
f.write("maval\n")
f.write("pune\n")
f.write("maharashtra\n")
f.write("india\n")
f.write("asia\n")
f.write("sate\n")
f.write("vadgoan\n")
f.close()
f=open("pcu1099.txt","r")
content=f.read()
print(content)


# In[35]:


f1= open('pcu898999.txt', 'x')
for x in range(10):
    f1.write("pcu pune\n")
f1.close()

f1=open('pcu898999.txt', 'r')

content = f1.read()

print(content)


# In[43]:


#write open a notrpad add 10 lines of text and save the file.write a python program to read the file and print

f=open("hello world pcu happy.txt","r")
content=f.read()
print(content)


# In[42]:


#write a program to generate and handle division by zero error by using try except block
def aby(a, b):
    try:
        c = (a + b) / (a - b)
    except ZeroDivisionError:  
        print("Division by zero occurred!")
    else:
        print("The result is:", c)

aby(1, 11)  
aby(4, 2)  


# In[ ]:




