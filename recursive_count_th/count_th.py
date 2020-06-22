'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #Base case 
    #Check if word has no letters or 1 letter
    if len(word) == 0 or (len(word) < len("th")):
        return 0
    #Recursive case
    #Break the word into smaller words and each time check if it contains th
    if word[0:2] == "th":
        #if the two letter contains th, return 1 and recall the function with the word minus the first letter
        return 1 + count_th(word[1:])
    #Otherwise recall the function with the word minus the first letter
    return count_th(word[1:])

