from itertools import chain, combinations

#getting input

NFA_NumOfStates=input()
NFA_AcceptStates=input()
NFA_TranferFunction=[]
tempInput=input()
while tempInput!='end':
    NFA_TranferFunction.append(tempInput)
    tempInput = input()

#functions
def listDeduplicate(x):
    tmp=list(dict.fromkeys(x))
    tmp.sort()
    return tmp

def findSubset(set,subset):
    for i in range(len(set)):
        if set[i]==subset:
            return i
    return 0

def powerset(array):
    # Empty set is a part of powerset
    subsets = [[]]
    for element in array:
        # Add every element to existing subsets
        for idx in range(len(subsets)):
            subset = subsets[idx]
            subsets.append(subset + [element])
    return subsets

def sortListOfChars(x):
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if int(x[i])>int(x[j]):
                tmpInt=x[i]
                x[i]=x[j]
                x[j]=tmpInt


#computing

DFA_NumOfStates=2**int(NFA_NumOfStates)

tempStr=''
for i in range(int(NFA_NumOfStates)):
    tempStr+=str(i)
    i+=1                                        
DFA_States=powerset(tempStr)
DFA_States.sort()
DFA_States.sort(key=len) #to get a lexicographic sort of states

NFA_EpsilonTransitions=[]
for i in NFA_TranferFunction: #to find epsilonTransitions
    if i[2]=="'":
        NFA_EpsilonTransitions.append(i)

DFA_StartStates=['0']
for i in NFA_EpsilonTransitions:
    if i[0]=='0': #if start state is 0
        tempStr=i
        DFA_StartStates+=tempStr[4:] #add all dest states in transformation to DFA_StartStates
        DFA_StartStates=[i for i in DFA_StartStates if i!=',']


DFA_StartState=0
for i in range(len(DFA_States)): #to find the real start state in DFA
    if DFA_States[i]==DFA_StartStates:
        DFA_StartState=i
        break

DFA_AcceptStates=[]                                
for i in range(len(NFA_AcceptStates)):
    for j in range(len(DFA_States)):
        if NFA_AcceptStates[i] in DFA_States[j] and NFA_AcceptStates[i]!=",":
            DFA_AcceptStates.append(str(j))
DFA_AcceptStates=listDeduplicate(DFA_AcceptStates)
sortListOfChars(DFA_AcceptStates)

DFA_TransitionFunction=[]
tmpListA = []
tmpListB = []
for i in DFA_States:
    tmpListA = []
    tmpListB = []
    for j in i:
        for k in NFA_TranferFunction:
            if k[0] == j and k[2] == 'a':
                for l in range(len(k[4:])):     #can add 2 not 1 so we can eliminate if
                    if l % 2 == 0:
                      tmpListA.append(k[4+l])
                      for e in NFA_EpsilonTransitions:
                            if e[0] == k[4 + l] and e[2] == "'":
                                tmpListA.append(e[4])
            if k[0] == j and k[2] == 'b':
                for l in range(len(k[4:])):
                    if l % 2 == 0:
                        tmpListB.append(k[4+l])
                        for e in NFA_EpsilonTransitions:
                            if e[0]==k[4+l] and e[2]=="'":
                                tmpListB.append(e[4])

    tmpListA = listDeduplicate(tmpListA)
    tmpListB = listDeduplicate(tmpListB)
    
    #a
    tmpStr=str(findSubset(DFA_States,i))+":a:"+str(findSubset(DFA_States,tmpListA))
    DFA_TransitionFunction.append(tmpStr)
    #b
    tmpStr=str(findSubset(DFA_States,i))+":b:"+str(findSubset(DFA_States,tmpListB))
    DFA_TransitionFunction.append(tmpStr)

#output

print(DFA_NumOfStates)
print(DFA_StartState)
for i in range(len(DFA_AcceptStates)):
    if(i==len(DFA_AcceptStates)-1):
        print(DFA_AcceptStates[i])
    else:
        print(DFA_AcceptStates[i], end=',')
for i in DFA_TransitionFunction:
    print(i)

