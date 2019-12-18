#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def main():
    s = str(input("Please enter the sentence: "))
    numWords = len(s.split(" "))
    average = 0
    for n in s:
        average = average + len(n)  
    average = (average - s.count(" "))/numWords   
    print("Average Word Length:", len(s))
    print("Number of words:",  numWords)
    print("Number of Characters:", average)
    
main()


# In[ ]:




