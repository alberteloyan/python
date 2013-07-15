__author__="albert"
__date__ ="$Mar 19, 2012 1:26:31 AM$"

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

def anagramCheck(string1,string2):
    if string1[::-1] == string2:
        return "Yes, they are anagrams."
    else: return "No, they are not anagrams."

# print anagramCheck("albert","trebla")

# Puzzle_4: Write a method to replace all spaces in a string with

def stringReplacement(string):
    return string.replace(' ','%20')

def stringReplacement2(string):
    stringList = string.split()
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
        # newMatrix[i].reverse() ======Reversing a list is importnant!=======
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
                #columnIndex = matrix[i].index(0)  =========Nice tool right here!========
    for i in rowIndex:
        matrix[i]=[0]*len(matrix[i])
                #break
    return matrix

#printMatrix([[1,2,3],[4,5,6],[7,0,8],[9,1,2],[3,4,5]])
#print
#printMatrix(rowColumnNulifier([[1,2,3],[4,5,6],[7,0,8],[9,1,2],[3,4,5]]))

# Write coding for Grub puzzle: ArrayLeader in linear time!

def arrLeader(A):
    for i, value in enumerate(A):
        if A.count(value) > len(A)/2:
            return A[i]
    return -1


def arrLeader2(A):
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

#print arrLeader2([1,0])

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
# only one call to isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”).

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

















