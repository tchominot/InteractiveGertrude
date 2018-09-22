# encoding: utf-8
import codecs as cs
import sys

	
f=cs.open(sys.argv[1], 'r', 'utf-8')
lines=f.readlines()
f.close()
if true:
	def defineAFunction():
		###
	def callAFunction():
		###
	def newCodeBlock():
		###
	def endOfaCodeBlock():
		###
	def defineAvariable():
		###
	def assignmentStatement():
		###
	def plusEqual():
		###
	def plusOperator():
		###
	def minusEqual():
		###
	def minusOperator():
		###
	def timesEqual():
		###
	def timesOperator():
		###
	def divideEqual():
		###
	def divideOperator():
		###
	def remainderEqual():
		###
	def remainderOperator():
		###
	def orEqual():
		###
	def orOperator():
		###
	def andEqual():
		###
	def andOperator():
		###
	def nandEqual():
		###
	def nandOperator():
		###
	def bitOrEquals():
		###
	def bitOrOperator():
		###
	def bitAndEqual():
		###
	def bitAndOperator():
		###
	def isLThan():
		###
	def isEto():
		###
	def isGthan():
		###
	def isLorEqual():
		###
	def isDifferent():
		###
	def isGorEqual():
		###
	def defineLiteral():
		###
	def printIntAsChar():
		###
	def printString():
		###
	def boolNot():
		###
	def simpleIfThen():
		###
	def simpleWhileDo():
		###
	def simpleUntilDo():
		###
	def ifThenElse():
		###
	def ifThenUnless():
		###
	def ifThenProvided():
		###
	def whileDoUnless():
		###

options = {[6,3]: defineAFunction, [2,7] : callAFunction, [3,6] : newCodeBlock, [4,12] : endOfaCodeBlock, [16,15] : defineAvariable, [18,16] : assignmentStatement, [10,20] : plusEqual, [14,10] : plusOperator, [4,14] : minusEqual, [11,7] : minusOperator, [23,14] : timesEqual, [6,16] : timesOperator, [8,12] : divideEqual, [5,8] : divideOperator, [14,8] : remainderEqual,	[24,17] : remainderOperator, [23,10] : orEqual, [22,23] : orOperator, [19,22] : andEqual, [18,14] : andOperator, [10,18] : nandEqual, [15,15] : nandOperator, [14,12] : bitOrEquals,	[15,26] : bitOrOperator, [6,11] : bitAndEqual, [17,11] : bitAndOperator, [15,19] : isLthan, [18,15] : isEto, [13,13] : isGthan, [13,15] : isLorEqual, [15,14] : isDifferent,	[10,15] : isGorEqual, [3,1] : defineLiteral, [7,14] : printIntAsChar, [7,15] : printString, [23,20] : boolNot, [6,10] : simpleIfThen, [20,18] : simpleWhileDo, [14,20] : simpleUntilDo,[12,12] : ifThenElse, [10,19] : ifThenUnless, [1,6] : ifThenProvided, [25,15] : whileDoUnless}
listOfWords=[]
numberOfWords=0
for line in lines:
	listOfWords=listOfWords.append(line.split(" "))
	wordsWithoutSpaces=listOfWords.join()
	if wordsWithoutSpaces.count('.')>0:
		#wordsWithoutSpaces,theRest=wordsWithoutSpaces.split('.')
		wordsWithoutSpaces=wordsWithoutSpaces.split('.')[0]
		averageLength=wordsWithoutSpaces.len()//listOfWords.len()
		smallR=0
		bigR=0
		for word in listOfWords:
		if (word.len()>averageLength):
			bigR=bigR+1
		elif (word.len()<averageLength):
			smallR=smallR+1
		fraction=[bigR,smallR]
		options[fraction]()
