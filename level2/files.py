"""
Word Frequency Analysis from 'input.txt'

This script reads a text file ('input.txt'), performs word frequency analysis, 
and prints the count of each unique word in sorted order.

Steps:
1. Open the file 'input.txt' in read mode.
2. Read the content of the file and preprocess it.
    - Replace newline characters with a space.
    - Strip leading/trailing whitespaces.
    - Split the content into a list of words using spaces as separators.
3. Flatten the list of words by splitting each word on periods and appending sub-words.
4. Create a set of unique words and count the occurrences of each word.
5. Create a dictionary to store the count of each unique word.
6. Print the results in sorted order.
"""

# Open the file 'input.txt' in read mode
f=open('input.txt','r')

# Open the file 'input.txt' in read mode
file=f.read()

# Replace newline characters with a space, strip leading/trailing whitespaces,
# and split the content into a list of words using spaces as separators
file=file.replace("\n"," ").strip().split(" ")

# Initialize an empty list to store individual words
data=[]
# Split each word by periods and flatten the result, adding each sub-word to the 'data' list
for i in file:
    a=(i.split("."))
    for j in a:
        data.append(j)

# Initialize an empty list to store the count of each unique word
counting=[]

# Create a set of unique words
words=set(data)

# Count the occurrences of each unique word
for a in words:
    count=0
    for b in data:
        if(a==b):
            count+=1
    counting.append(count)

# Initialize an index variable
index=0

# Create a dictionary to store the count of each unique word
dic={}
for k in words:
    # Update the dictionary with the unique word and its count
    dic.update({k: counting[index]})
    index+=1

# Convert the set of unique words to a sorted list
res=list(words)
res.sort()

# Print the results in sorted order
for item in res:
    print(f"{item}: {dic[item]}")