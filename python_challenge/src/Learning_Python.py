__author__="albert"
__date__ ="$Mar 19, 2012 1:26:31 AM$"

import heapq

# Puzzle_1: string with unique characters
def unique_char(string):
    letters = []
    for i in string:
        if i in letters:
            return "not all are unique!"
        else:
            letters.append(i)
    return "You have a unique string!"
#print unique_char("abcdefg")

# Puzzle_2: reverse a c-style null-terminated string

def reverse_string(string):
    return string[::-1]
# print reverse_string("albert")

# Puzzle_3: Design an algorithm and write code to remove the duplicate characters in a string
# without using any additional buffer. NOTE: One or two additional variables are fine.

def removeDuplicate(string):
    charList = list(string)
    for i, ch in enumerate(charList):
        if ch in charList[:i] or ch in charList[i+1:]:
            while ch in charList:
                charList.remove(ch)
    return ''.join(charList)

#print removeDuplicate("abcccdef")

# Puzzle_4: Write a method to decide if two strings are anagrams or not.

def anagramCheckTrivial(string1,string2):
    if string1[::-1] == string2:
        print "Yes, they are anagrams."
        return 1
    else:
        print "No, they are not anagrams."
        return 0

def anagramCheck(string1, string2):
    charList1 = list(string1)
    charList2 = list(string2)
    if sorted(charList1) == sorted(charList2):
        print "Yes, those are anagrams!"
        return 1
    else:
        print "No, not anagrams."
        return 0

#print anagramCheck("albert","trebla")

# Puzzle_4: Write a method to replace all spaces in a string with

def stringReplacementPythonic(string):
    return string.replace(' ','%20')

def stringReplacement2(string):
    stringList = string.split()   # Important way to split a string, it finds whitespaces and splits into a list. Similarly to join.
    print list(string)
    return '%20'.join(stringList)

# print stringReplacement2('This is a smooth operator!')

# Puzzle_5: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

def rotateMatrixStatic(imageMatrix):
    matrixSize = len(imageMatrix)
    newMatrix = [[] for i in range(matrixSize)]
    for i,columnValue in enumerate(imageMatrix):
        for j,rowValue in enumerate(imageMatrix[i]):
            newMatrix[i].append(imageMatrix[j][i])
        # newMatrix[i].reverse() ======Reversing a list is importnant! Could also use newMatrix[i] = newMatrix[::-1]=======
    return newMatrix

def printMatrix(imageMatrix):
    for i,columnValue in enumerate(imageMatrix):
        for j,rowValue in enumerate(imageMatrix[i]):
            print '[', rowValue, ']', #notice the trailing ',' which eliminates the newline character
        print '\n',

#testMatrix = [[(1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4)],[0,0,0,0,0],
#[0,0,0,0,0],[0,0,0,0,0],[(1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4)]]
#printMatrix(testMatrix)
#print
#printMatrix(rotateMatrixStatic(testMatrix))

# Puzzle_6: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column is set to 0.

def rowColumnNulifier(matrix):
    rowIndex = []
    #Nullifying rows
    for i,columnValue in enumerate(matrix):
        if 0 in matrix[i]:
            rowIndex.append(i)
    #Nullifying columns
    for i,columnValue in enumerate(matrix):
        if 0 in matrix[i]:
            columnIndex = []
            for j, rowValue in enumerate(matrix[i]):
                if rowValue == 0:
                    columnIndex.append(j)
            for k,columnValue2 in enumerate(matrix):
                for l in columnIndex:
                    matrix[k][l] = 0
                #columnIndex = matrix[i].index(0)  =========Nice tool right here! returns the indedx of the passed value========
    for i in rowIndex:
        matrix[i]=[0]*len(matrix[i])
                #break
    return matrix

#printMatrix([[1,2,3],[4,5,6],[7,0,8],[9,1,2],[3,4,5]])
#print
#printMatrix(rowColumnNulifier([[1,2,3],[4,5,6],[7,0,8],[9,1,2],[3,4,5]])

# Write coding for Grub puzzle: ArrayLeader in linear time!

def arrLeader(A):
    for i, value in enumerate(A):
        if A.count(value) > len(A)/2:
            return A[i]
    return -1


def arrLeaderHashMap(A):
    dict = {}
    if len(A) == 0:
        return -1
    if len(A) == 1:
        return A[0]
    for i, value in enumerate(A):
        try:
            dict[value] += 1
        except:
            dict[value] = 1
    maxKey = max(dict,key = lambda a: dict.get(a))
    print dict
    print maxKey
    print dict[maxKey]
    print len(A)/2
    if dict[maxKey] > len(A)/2:
        return maxKey
    else:
        return -1

#print arrLeaderHashMap([1,0])

def arrLeader3(A):
    counter = 0
    preValue = 0
    for i, value in enumerate(sorted(A)):
        try:
            preValue = sorted(A)[i-1]
        except:
            preValue = value
        if value == preValue:
            counter+=1
            if counter>(len(A)/2):
                return value
    return -1

#print arrLeader3([3,1,1,1,1,1,5,1,0,9])

#positive_int_generator = lambda n: big_o.datagen.integers(100000, 0, 10000)
#best, others = big_o.big_o(arrLeader2, positive_int_generator, n_repeats=1)
#print best

# Puzzle_7: Assume you have a method isSubstring which checks if one word is a substring of
# another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using
# only one call to isSubstring (i.e., ÒwaterbottleÓ is a rotation of ÒerbottlewatÓ).

def isSubstring(string1,string2):
    if len(string1) != len(string2):
       return "Not sublists of each other."
    if len(string1)==0:
        return "The strings are empty."
    if string1 == string2:
        return "Yes, those 2 strings are subs."
    for i, char in enumerate(string1):
        #print string1[:i]
        #print string1[i:]
        if string1[:i] in string2 and string1[i:] in string2:
            return "Yes, those 2 strings are subs."
    return "Not sublists of each other."

# print isSubstring("albert","talber")

# Puzzle_8: You are given two sorted arrays, A and B, and A has a large enough buffer at the end
#to hold B. Write a method to merge B into A in sorted order.

def decreaseByOne(num1,num2):
    num1-=1
    num2-=1
    #this, unfortunately will not work, because although parameters in python are passed by reference, integers are immutable, so you cannot influence the outside scope

def arrayMerge(array1,array2):
    i = len(array2)-1 #the index of array2's last element
    j = len(array1)-1 #the index of array1's last element
    #the following is only necessary is the passed array does not have a buffer, so let's assume that.
    for i, value in enumerate(array2):
        array1.append(-1)
    k = len(array1)-1 #index of the joint array's last index (remember, array1 has its tail buffer filled with -1s)
    while i>=0 and j>=0:
        if array1[i] > array2[j]:
            k-=1
            i-=1
            array1[k]=array1[i]
        else:
            k-=1
            j-=1
            array1[k]=array2[j]
    while j>=0:
        k-=1
        j-=1
        array1[k] = array2[j]
    return array1

def arrayMergePythonic(array1,array2):
    for i, value in enumerate(array2):
        array1.append(value)
    return sorted(array1)

# This helper function will shift the given array and insert the value at given (zero-indexed) position
def shiftAndInsert(array, position, value):
    try:
        for i in range(len(array)-position):
            if i==0:
                array.append(array[-1])
            else:
                array[-(i+1)]=array[-(i+2)]
        array[position]=value
        return array
    except (IndexError, TypeError):
        print("Index out of range -> appending")
        array.append(value)
        return array


#print arrayMerge([1,4,5,6],[3,7,8,9])
#print shiftAndInsert([1,2,3,4,5],0,33)
#print shiftAndInsert([],0,33)
#print shiftAndInsert([1,2,3,4,5],4,33)

# The Python Challenge - Level 2
# Description: A mapping is given on the website that maps 3 letter to replacements (like a cipher).
# There is a text in the source code that needs to be decyphered.

def level2():
	challenge = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
	listed = list(challenge)
	for x, letter in enumerate(challenge):
		listed[x] = chr((ord(letter)+2))
	challenge = "".join(listed)
	print(challenge)

#level1()

# The Python Challenge - Level 3
# Description: A large massive of random characters is given - you need to find rare characters.
# I approcahed this problem using my intuition, instead of using a dictionary or hash map to map unique characters
# I used the fact that the clue must me alphanumeric.

def level3(string):
    disallowed = """!@#$%^&*()_+=-~`" ':;<>/?\|}]{["""
    final = "This is the final string: "

    for letter in string:
        if letter not in disallowed:
            final += letter

    print final

# The Python Challenge - Level 4
# Description: A large massive of random characters is given -
# you need to find a character that is surrounded by exactly three uppercase ones.

def level4(word):
    word_list = list(word)
    pre=0
    post=0
    temp=[]
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    lowercase = "abcdefghijklmnopqrstuvwxyz "

    for i in range(len(word_list)):
        temp_string="".join(word_list[i])

        if temp_string in lowercase:
            temp_string="".join(word_list[i-3:i])

            if temp_string in uppercase and i>2:
                temp_string="".join(word_list[i+1:i+4])

                if temp_string in uppercase and i<len(word_list)-3:
                    temp.append(word_list[i])
    return "".join(temp)

# The Python Challenge - Level 5
# Description: A continuing linked list of php pages is given that generate a sequence of numbers.
# Need to feed the server the continuing numbers until a response is unusual.

import urllib

def level5():
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    objects = []
    data = []
    clean = []
    nothing = "12345"

    # the commented implementation below is correct yielding the 403rd "nothing" number per specification

    #for i in range(403):
    #    objects.append(urllib.urlopen(url+nothing))
    #    data.append(objects[i].readline())
    #    clean.append(data[i][-5:])
    #    if clean[i][0]==' ':
    #        nothing = clean[i][1:]
    #    else:
    #        nothing = clean[i]

    returnString = "and the next nothing is (\d+)"

    while True:
       try:
           site = urllib.urlopen(url+nothing).read()
           nothing = re.search(returnString, site).group(1)
       except:
           break
    print clean
    print nothing

# Puzzle_8: Write a method to sort an array of strings so that all the anagrams are next to each
# other.

def anagramSorting(stringArray):
    sorted(stringArray, key=anagramCheck())

# Puzzle_9: Write a pythonic recursive binary search function

def binarySearch(array,value,minIndex,maxIndex):
    if maxIndex < minIndex: #key couldn't be found
        print "Value was not found."
        return -1
    midIndex = (minIndex+maxIndex)/2
    if array[midIndex] == value:
        foundIndex = midIndex
        return midIndex
    elif array[midIndex] < value:
        return binarySearch(array,value,midIndex+1, maxIndex)
    else:
        return binarySearch(array,value, minIndex, midIndex-1)

def pythonicBinarySearch(array,value):
    foundIndex = -1
    midIndex = (len(array)-1)/2
    if array[midIndex] == value:
        return midIndex
    elif array[midIndex] < value:
        foundIndex += pythonicBinarySearch(array[midIndex+1:],value)
    else:
        foundIndex -= pythonicBinarySearch(array[:midIndex],value)
    return midIndex

# the way recursion is implemented in python doesn't really allow for this exact slicing implementation.
# although the calls are tail recursive and everythoing is passed by reference,
# the fact that integers are immutable doesn't allow for global index manipulation
# this necessitates the use of another argument in the function, say: indexSoFar, that will keep track of the calls

#print binarySearch([1,2,3,4,5,6,7,8,9,10],10,0,9)
#print pythonicBinarySearch([1,2,3,4,5,6,7,8,9,10],9)

#Lookup sets in python


