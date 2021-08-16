ItemInCard = 0
if ItemInCard != 2:
    # this is very usefull and tell which and why it is failed with the comment.
    #raise Exception("Items in cart does not match")
    pass #this keyword does nothing
# assert is used for checking and through error if condition not match
assert(ItemInCard == 2)