#create a program to count the number of words in a string
#will need to perform 3 tasks, read input, process, write output
#for process use a method: a mehtod is a operation specific to a type of value, .count will be valuable here, if each word has a space between
#them, then count the spaces and add 1 to count the last word


#create string variable

line = 'i am learning python'

#create variable to run count method and add 1 to the number

totalWords = line.count(' ') + 1

#call the method to perform it

print(totalWords)

# for simplicity in coding, this can be done in one line

oneLine = 'i am learning python'.count(' ') + 1

print(oneLine)
#the above works, but only on a given string
#we want program to take input, so we'll create a function to do this
newLine = input()
total_words = newLine.count(' ') + 1
print(total_words)
#input collects typed string in the terminal, stores it in the newLine varianble, total_words uses the stored
# newLine variable to run the count method and add 1 to it
# print returns the value