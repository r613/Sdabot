#v1.1
from stf import finish 
from stf import checker
from stf import patt
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
        text = ""
        for i in list:
            text = str(text) + str(i) + " "
        print text
        finish(list,alist,dif)


    

#print checker([])
searcher([0,3,-1,4,7,3,8,11])

# 