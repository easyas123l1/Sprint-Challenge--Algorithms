'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # base case
    if len(word) < 2:
        return 0
    
    # if first 2 characters of string have th add 1 recursive
    if(word[0:2] == 'th'):
        return 1 + count_th(word[1:])

    return count_th(word[1:])
