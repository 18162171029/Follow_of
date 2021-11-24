fterminals=[]
diction={}

def pterminals(chars):
    global fterminals
    fterminals.append(chars)

def getterminal(cha):
    global diction
    global non_terminals
    att=''
    a=diction[cha]
    if a[0] in non_terminals:
        return getterminal(a[0])
    else:
        if '|' in a:
            ind1=a.index('|')
            att=a[0]+a[ind1+1:]
        else:
            att=a[0]
        return att


def firstof(gra):
    global diction
    global non_terminals            
    # gra=['E->TX', 'X->+TX|e', 'T->FY', 'Y->*FY|e', 'F->(E)|z']    
    non_terminals=[]
    for i in gra:
        temp=i[0]
        non_terminals.append(temp)
        temp=''
    
    diction={}
    
    for i in range(len(gra)):
        diction[non_terminals[i]]=gra[i][3:]
        
    tstr=''
    for i in range(len(gra)):
        if gra[i][3] not in non_terminals:
            tstr=gra[i][3]
            if '|' in gra[i]:
                ind=gra[i].index('|')
                tstr+=gra[i][ind+1:]
                pterminals(tstr)
            else:
                pterminals(tstr)
        else:
            if len(gra[i]) >= 4:
                if gra[i][4] in non_terminals:
                    aa=getterminal(gra[i][3])
                    aa+=getterminal(gra[i][4])
                    aaa=''
                    for lst in aa:
                        if lst not in aaa:
                            aaa+=lst
                    pterminals(aaa)
                else:
                    aa=getterminal(gra[i][3])
                    pterminals(aa)

    for i in range(len(fterminals)):
        print(f'First({non_terminals[i]}) -> {fterminals[i]}')
    
    return fterminals, non_terminals;

t=int(input("Enter the total no. of grammar: "))
gra=[]
temp=''
for i in range(t):
    temp=input(f"Enter the elements of {i+1} grammar: ")
    gra.append(temp)
    temp=''
print('\n\n')

# gra=['E->TX', 'X->+TX|e', 'T->FY', 'Y->*FY|e', 'F->(E)|z'] 
# gra=['S->aBDh', 'B->cC', 'C->bC|e', 'D->EF', 'E->g|e', 'F->f|e']
rhs=[]
strin=''
first=[]
firsto={}
terminals=[]
terminal=[]
follow={}
ffirst, non_term=firstof(gra)
for i in range(len(non_term)):
    follow[non_term[i]]=''
follow[non_term[0]]+='$'

# print(ffirst)

for i in ffirst:
    stri2=''
    if 'e' in i:
        for j in i:
            if j!='e':
                stri2+=j
        stri2+='e'
    else:
        stri2=i
    first.append(stri2)

for i in range(len(non_term)):
    firsto[non_term[i]]=first[i]


for i in gra:
    strin=i[3:]
    rhs.append(strin)

for i in rhs:
    for j in i:
        if j not in non_term:
            terminals.append(j)
                        
for i in terminals:
    if i=='|':
        terminals.remove(i)

for i in terminals:
    if i not in terminal:
        terminal.append(i)



for i in non_term:
    for j in rhs:
        
        if i in j:
            gi=j.index(i)
            gii=gi+1
            if gii==len(j):
                inde=rhs.index(j)
                ab=follow[non_term[inde]]
                follow[i]+=ab
            elif j[gii] in terminal:
                follow[i]+=j[gii]
            elif j[gii] in non_term:
                this=firsto[j[gii]]
                if 'e' in this:
                    if gii==len(j)-1:
                        indii=rhs.index(j)
                        this+=follow[non_term[indii]]
                    elif j[gii+1] in terminal:
                        this+=j[gii+1]
                    elif j[gii+1] in non_term:
                        this+=firsto[j[gii+1]]
                        
                follow[i]+=this


for i in non_term:
    tstri1=''
    if 'e' in follow[i]:
        for j in follow[i]:
            if j!='e':
                tstri1+=j
        follow[i]=tstri1
# print(follow)

for i in range(len(non_term)):
    st2=''
    st1=follow[non_term[i]]
    for j in st1:
        if j not in st2:
            st2+=j
    follow[non_term[i]]=st2
    


print('\n')
for i in non_term:
    print(f'Follow({i}): {follow[i]}')


    
























































