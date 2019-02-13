def finish(list,alist,cs):
    length = len(list) - 1
    
    
    end = ( length - (length)%cs ) 
    print end
    print "This is the place of the last number in the last sequence"
    print end
    number = list[end]
    print number 
    for a in range(0,cs):
        number = number + alist[a]
        print number 
    print "That's what we got!"

def checker(alist):
    
    for stc in range(1, (len(alist)/2) + 1): #stc space to check (couldn't come up with something better than this)) (it's half which might make it one before the end, but on the other hand the length is the full length (not including zeros))
        if alist[0] == alist[stc]:
            if patt(alist,0,stc):
                return stc

                
            else:
                pass
        else:
            pass
    return 0 #This means that we got nothing 

def patt(alist,cs,stc): #identifies a pattern inside a pattern
    for i in range(cs, (len(alist)-(stc-cs) -1) ): #we go though the entire 
        if alist[cs+i] == alist[stc+i]:
            pass
        else:
            return False 
    print "We have confirmed that the sequence starts at " + str(cs)  + " and at: " + str(stc)

    return True 