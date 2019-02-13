#v1.0
def searcher(list):
    alist = [] #alist will be the list of the differences between the numbers on the list
    for i in range(len(list)-1):
        alist.append( (list[i+1]) - (list[i])) 
        #print diff
    print alist
    dif = checker(alist)
    if dif == 0:
        print "We got nothing!"
    else:
        finish(list,alist,dif)

def finish(list,alist,cs):
    length = len(list) - 1 
    number = list[length]
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
    

#print checker([])
searcher([9,18,12,21,15])

# 