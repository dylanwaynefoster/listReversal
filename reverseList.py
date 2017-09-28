#Reverse a list.
#Stair stepping optional ;-)

def reverseList(x,y,z,a,b):

	myList = [x,y,z,a,b]
	p = (len(myList) - 1)
	r = 0
	xx = "" 

	for i in range(len(myList)):
		print(xx + myList[r])
		r += 1
		xx += "\t"
	for i in range(len(myList)):
		print((("\t") * p) + myList.pop())
		p -= 1

reverseList("Hello","My","Name","Is","Dylan")


