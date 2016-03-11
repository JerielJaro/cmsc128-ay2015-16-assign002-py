"""
Name: Jeriel G. Jaro
Lab:  AB-1L
Exer: Programming Assignment 02
"""

#import regular expression module
import re

#computes for Hamming Distance
def getHammingDistance(str1, str2):
	hammingDistance = 0

	#if strings are empty or has negative length,
	#	the function returns string error
	if len(str1) < 1 or len(str2) < 1:
		return "Error! String of length 0 or lower"

	#the strings are converted to all uppercase
	str1 = str1.upper()
	str2 = str2.upper()

	#if string lengths are not equal,
	#	the function returns string error
	if len(str1) != len(str2):
		return "Error! String lengths are not equal"
	
	#if characters at index i are not equal,
	#	the function increments hammingDistance
	for i in range(len(str1)):
		if(str1[i] != str2[i]):
			hammingDistance += 1

	return hammingDistance


#counts the total number of occurences of a substring
def countSubstrPattern(original, pattern):
	substrCount = 0

	#loops depending on how many times
	#	the regex of substring match in the 
	#	original string
	for a in re.finditer('(?='+pattern+')', original):
		substrCount += 1
	
	return substrCount

#checks if a string contains characters
#	in the given alphabet string
def isValidString(str_, alphabet):
	#if strings are empty or has negative length,
	#	the function returns string error
	if len(str_) < 1 or len(alphabet) < 1:
		return "Error! String of length 0 or lower"
	
	#loops on all characters of the string
	#	to be checked
	for s in str_:
	
	#if the character did not match any character 
	#	from the alphabet string, the function
	#	returns false
		if alphabet.find(s) == -1:
			return False

	return True

#computes number of G's - number of C's
def getSkew(genome, n):
	skew = 0
	
	#if genome string is empty or has negative length,
	#	the function returns string error
	if len(genome) < 1:
		return "Error! String of length 0 or lower"
	
	if n < 1:
		return 0

	#if the genome string exceeds the length
	#	indicated by n, the genome string is sliced
	if len(genome) > n:
		genome = genome[0:n].upper()


	for c in genome:
		if c == 'C':
			skew -= 1
		elif c == 'G':
			skew += 1
	
	return skew

#computes for number of G's 
def getMaxSkewN(genome, n):
	maxSkew = 0
	
	#if genome string is empty or has negative length,
	#	the function returns string error
	if len(genome) < 1:
		return "Error! String of length 0 or lower"
	if n < 1:
		return 0
	
	#if the genome string exceeds the length
	#	indicated by n, the genome string is sliced
	if len(genome) > n:
		genome = genome[0:n].upper()

	for c in genome:
		if c == 'G':
			maxSkew += 1

	return maxSkew

#computes for number of G's - number of C's
#	with condition if number of G's exceeds 1,
#	the functions still returns 1
def getMinSkewN(genome, n):
	minSkew = getSkew(genome, n)
	return 1 if (minSkew >= 1) else minSkew