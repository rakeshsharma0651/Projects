# Creating Class for Binary Tree
class DictTree():
	def __init__(self, data, left, right):
		self.data = data
		self.left = left
		self.right = right

def addWord(node, string):
    '''
    DOCTRING: ADDING NEW WORD TO BINARY TREE
    '''
    if node != None:
        if list(node.data.keys())[0] > list(string.keys())[0]:
            node.left = addWord(node.left, string)
            return node
        else:
            node.right = addWord(node.right, string)
            return node
    else:
        new_node = DictTree(string, None, None)
        return new_node

#function for printing dictionary    
def printDict(node):
    '''
    DOCSTRING: FUNCTION TO PRINT WORD DICTIONARY
    '''
    if node == None:
        return
    printDict(node.left)
    print(node.data)
    printDict(node.right)

def searchWord(node, string):
    if node is None:
        return("N")
    if list(node.data.keys())[0] == string:
        return([0,list(node.data.values())[0]])
    elif list(node.data.keys())[0] > string:
        result = searchWord(node.left, string)
        return result
    else:
        result = searchWord(node.right, string)
        return result

def searchSimilar(node, string,counter=0):
    if node is None:
        return counter
    if list(node.data.keys())[0][:3] == string[:3]:
        if counter == 0:
            print("\nEntered word not present in Dictionary.")
            print("Did you mean:")
        print(list(node.data.keys())[0])
        counter = counter + 1
    counter = searchSimilar(node.left, string,counter)
    counter = searchSimilar(node.right, string,counter)
    #print(counter)
    return counter

def searchTree(node, string):
    search_result = searchWord(node, string)
    if search_result[0] == 0:
        print("\nWord entered by you is present in Dictionary.\n")
        print("Word: ", string)
        print("Meaning: ",search_result[1])
        return 0
    elif search_result == 'N':
        x = searchSimilar(node, string)
        if x == 0:
            print("\nEntered word and No similar words present in Dictionary.")
        return x
        
def load_words():
    '''
    DOCSTRING: LOADING WORDS FROM FILE
    '''
    root = None
    with open("Word Meaning.csv") as f:
        #f.seek(0)
        contents = f.readlines()
    for item in range(1,len(contents)):
        w,m = contents[item].split(",")
        a = [{w:m}]
        root = addWord(root,a[0])
    return root

#Main Program
root = load_words()
print('-'*127)
print('Dictionary Program:'.center(127))
print('-'*127)
choice = "Y"
while choice.upper() == "Y":
    print("Kindly Input word to be Searched: ")
    query = input()
    notfound = searchTree(root, query.lower())
    while notfound != 0:
        print("\nDid you mean any of the words shown above (Y/N)?")
        x = input()
        if x.upper() == "Y":
            print("Kindly enter word to be searched: ")
            rep_word = input()
            notfound = searchTree(root,rep_word.lower())
        elif x.upper() == "N":
            break
        else:
            print("\nYou did not enter the required Input!")
            continue
    print("\nDo you Wish to continue (Y/N)?")
    choice = input()
    if choice.upper() == 'N':
        break
    elif choice.upper() == 'Y':
        print("\n")
        continue
    else:
        print("You have not entered correct response! So Exiting from the Program!!!")
        break
#printDict(root)

print("\nThank you !!!")
