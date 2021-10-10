#All the exercises were solved in python3 (except those for which it was not possible according to HR)
#Exercises marked with "*" are the ones which i used solutions to solve them 

#PROBLEM 01

#1-Say "Hello, World!" With Python

print('Hello, World!')

#2-Python If-Else

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
def Weird(n):
    if(n%2!=0):
        print('Weird')
    else:
        if(n>20):
            print('Not Weird')
        elif(n>=6):
            print('Weird')
        elif(n>=2):
            print('Not Weird'
            
Weird(n)

#3-Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
def calculator(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    
calculator(a,b)

#4-Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
                  
def calculator(a,b):
    print(a//b)
    print(a/b)
    
calculator(a,b)

#5-Loops

if __name__ == '__main__':
    n = int(input())
    
def calculator(n):
    i=0
    while i<n:
        print(i**2)
        i=i+1

calculator(n)

#6-Write a function

def is_leap(year):
    leap = False
    if(year%4==0 and year%100!=0):
        leap=True
    if(year%400==0):
        leap=True
    return leap

year = int(input())
print(is_leap(year))

#7-Print Function

if __name__ == '__main__':
    n = int(input())
def factorial(n):
    lista=[]
    i=1
    while i<n+1:
        lista.append(i)
        i+=1
    print(*lista,sep='')
    
factorial(n)

#8-List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
print([[i, j, k] for i in range(0,x+1) for j in  range(0,y+1) for k in range(0,z+1) if i+j+k != n] )

#9-Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr =list(map(int, input().split()))
massimo=max(arr)
while max(arr)==massimo:
    arr.remove(massimo)
print(max(arr))

#10-Nested Lists

if __name__ == '__main__':
    lista=[]
    for _ in range(int(input())):
        ls=[]
        name = input()
        ls.append(name)
        score = float(input())
        ls.append(score)
        lista.append(ls)
lista=sorted(lista, key=lambda x: x[1])
minimo=lista[0][1]
for i in lista:
    if (i[1]>minimo):
        secondo=i[1]
        break
n=[]
for i in lista:
    if (i[1]==secondo):
        n.append(i[0])
n=sorted(n)
for i in n:
    print(i)

#11-Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
print("{0:.2f}".format(sum(student_marks[query_name])/len(student_marks[query_name])))

#12-Lists

if __name__ == '__main__':
    N = int(input())
L = []
for _ in range(0, N):
    user_input = input().split(' ')
    command = user_input.pop(0)
    if len(user_input) > 0:
        if 'insert' == command:
            eval("L.{0}({1}, {2})".format(command, user_input[0], user_input[1]))
        else:
            eval("L.{0}({1})".format(command, user_input[0]))
    elif command == 'print':
        print (L)
    else:
        eval("L.{0}()".format(command))

#13-Tuples

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
print(hash(tuple(integer_list)))exit

#14-swap case 

def swap_case(s):
    return(s.swapcase())

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
#15-String Split and Join

def split_and_join(line):
    line=line.split(' ')
    return "-".join(line)
                  
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
#16-What's Your Name?

def print_full_name(first, last):
    print('Hello {} {}! You just delved into python.'.format(first,last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
 
#17-Mutations
 
def mutate_string(string, position, character):
    return (string[:position]+character+string[position+1:])

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
                  
#18-Find a string

def count_substring(string, sub_string):
    l=len(string)
    sl=len(sub_string)
    o=0
    for i in range(l-sl+1):
        if (string[i:i+sl]==sub_string):
            o+=1
    return o

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
                  
#19-String Validators

if __name__ == '__main__':
    s = input()
    alnum=False
    alpha=False
    num=False
    low=False
    upp=False
    for i in s:
        if (i.isalpha()):
            alnum=True
            alpha=True
        if (i.isdigit()):
            alnum=True
            num=True
        if (i.islower()):
            low=True
        if(i.isupper()):
            upp=True
    print(alnum)
    print(alpha)
    print(num)
    print(low)
    print(upp)   

#20-Text Alignment

thickness = int(input()) #This must be an odd number
c = 'H'

    #Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    #Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    #Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

    #Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

    #Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#21-Text Wrap

import textwrap

def wrap(string, max_width):
    return(textwrap.fill(string,max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#22-Designer Door Mat

N,M = map(int,input().split())
for i in range(0,((N-1)//2)+1):
    if i == (N-1)/2:
        print('WELCOME'.center(M,'-'))
    elif(i<((N-1)/2)):
        print(('.|.'*(i*2+1)).center(M,'-'))
for i in range(((N-1)//2)-1,-1,-1):
    print(('.|.'*(i*2+1)).center(M,'-'))
    
#23-String Formatting

def print_formatted(number):
    if number >= 1 and number <= 99:
        w=len(bin(number)[2:])
        for i in range(1,number+1):
            print (str(i).rjust(w,' '),str(oct(i)[2:]).rjust(w,' '),str(hex(i)[2:].upper()).rjust(w,' '),str(bin(i)[2:]).rjust(w,' '),sep=' ')
            
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
                  
#24-Alphabet Rangoli

def print_rangoli(size):
    
    myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    
    for i in range(size-1, -size, -1):
        x = abs(i)
        line = myStr[size:x:-1]+myStr[x:size]
        print ("--"*x+ '-'.join(line)+"--"*x)
    
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)                  

#25-Capitalize!

def solve(s):
    s=s.split(' ')
    o=''
    for i in s:
        o=o+' '+i.capitalize()
    return(o.strip())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
                  
#26-The  minion game (searched for an help for this one)

def minion_game(string):
    vocali='AEIOU'
    kevin=0
    stuart=0
    for i in range(len(string)):
        if string[i] in vocali:
            kevin+=len(string)-i
        else:
            stuart+=len(string)-i
    if kevin>stuart:
        print ('Kevin '+str(kevin))
    elif kevin<stuart:
        print('Stuart '+str(stuart))
    elif kevin==stuart:
        print('Draw')
            
                       
if __name__ == '__main__':
    s = input()
    minion_game(s)
    
#27-Merge the Tools!

def merge_the_tools(string, k):
    for i in  range(0,len(string),k):
        stringa=''
        for j in string[i:i+k]:
            if j not in stringa:
                stringa+=j
        print (stringa)
    return
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)     
                  
#28-Introduction to Sets                  

def average(array):
    a=set(array)
    return(sum(a)/len(a))
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)      
                  
#29-No Idea!
                  
#as the name of the exrcise i have no idea why using set type instead of a list type make 
# the solution faster, in fact using the submission without set it gave me errors of runtime

N,M = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split())) 
B = set(map(int, input().split()))   
happines=0 
for i in arr:
    if i in A:
        happines+=1
    if i in B:
        happines-=1
    else:
        continue
print(happines)
                  
#30-Symmetric Difference

M = int(input())
Mlist = set(map(int,input().split(' ')))
N = int(input())
Nlist = set(map(int,input().split(' ')))
diff1=Mlist.difference(Nlist)
diff2=Nlist.difference(Mlist)
for i in  sorted(diff1.union(diff2)):
    print(i)
                  
#31-Set.add()
               
N= int(input())
s=set()
for _ in range(N):
    s.add(input())
print(len(s))

#32-Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    command = input().split()
    if len(command)>1:
        eval('s.{}({})'.format(command[0],command[1]))
    else:
        eval('s.{}()'.format(command[0]))
print (sum(s))
                 
#33-set.union() Operation
                  
n=int(input())
nset=set(input().split())
m=int(input())
mset=set(input().split())
myset=nset.union(mset)
print(len(myset))
                 
#34-Set .intersection() Operation

n=int(input())
nset=set(input().split())
m=int(input())
mset=set(input().split())
myset=nset.intersection(mset)
print(len(myset))
                  
#35-Set .difference() Operation

n=int(input())
nset=set(input().split())
m=int(input())
mset=set(input().split())
myset=nset.difference(mset)
print(len(myset))
                  
#36-Set .symmetric_difference() Operation
                  
n=int(input())
nset=set(input().split())
m=int(input())
mset=set(input().split())
myset=nset.symmetric_difference(mset)
print(len(myset))
                  
#37-Set Mutations

N=int(input())
A=set(map(int,input().split(' ')))
M=int(input())
for _ in range(M):
    command = input().split()
    B = set(map(int,input().split()))
    eval('A.{}({})'.format(command[0],B))
print(sum(A))
                  
#38-The Captain's Room

N =int(input())
arr=list(map(int,input().split(' ')))
s1= set()
s2 = set()
for i in arr:
    if i not in s1:
        s1.add(i)
    else:
        s2.add(i)
captain  = s1.difference(s2).pop()
print(captain)

#39-Check Subset
                  
n= int(input())
for _ in range(n):
    ma=int(input())
    a=set(map(int,input().split()))
    mb=int(input())
    b=set(map(int,input().split()))
    my=a.intersection(b)
    print(my==a)
                  
#40-Check Strict Superset
                  
a=set(map(int,input().split()))
n=int(input())
out=True
for _ in range(n):
    b=set(map(int,input().split()))
    my=b.intersection(a)
    if (my!=b):
        out=False
        break
print(out)
                  
#41-collections.Counter()

from collections import Counter
n , scarpe = int(input()), Counter(map(int,input().split()))
mcli= int(input())
guadagno=0
for _ in range(mcli):
    cliente=list(map(int,input().split()))
    if scarpe[cliente[0]]>0:
        scarpe[cliente[0]]-=1
        guadagno+=cliente[1]
    else:
        continue
print(guadagno)
                  
#42-DefaultDict Tutorial
                  
from collections import defaultdict 
n, m = map(int,input().split())
diz=defaultdict(list)
for i in range(n):
    diz[input()].append(i+1)
for _ in range(m):
    j=input()
    if len(diz[j])>0:
        posizioni=list(map(str,diz[j]))
        print(' '.join(posizioni))
    else:
        print(-1)
                  
#43-Collections.namedtuple()

from collections import namedtuple
n=int(input())
spreadsheet=namedtuple('spreadsheet',','.join(input().split()))
tot=0
for _ in range(n):
    attr1,attr2,attr3,attr4 = input().split()
    studente=spreadsheet(attr1,attr2,attr3,attr4)
    tot+=int(studente.MARKS)
print(tot/n)

#44-Collections.OrderedDict()
                  
from collections import OrderedDict
n=int(input())
diz=OrderedDict()
for _ in range(n):
    prodotto=input().split()
    if (len(prodotto)>2):
        key=prodotto[0]+' '+prodotto[1]
        value=int(prodotto[2])
        if key in diz.keys():
            diz[key]+=value
        else:
            diz[key]=value
    else:
        key=prodotto[0]
        value=int(prodotto[1])
        if key in diz.keys():
            diz[key]+=value
        else:
            diz[key]=value
for i in range(len(diz.keys())):
    print(list(diz.keys())[i]+' '+str(list(diz.values())[i]))

#45-Word Order
                 
from collections import OrderedDict
n=int(input())
mydict=OrderedDict()
for _ in range(n):
    key=input()
    mydict.setdefault(key,0)
    mydict[key]+=1
print(len(mydict))
print(*mydict.values())
                  
#46-Collections.deque()

from collections import deque
d = deque()
n=int(input())
for _ in  range(n):
    comando=input().split()
    if len(comando)>1:
        eval('d.{}({})'.format(comando[0],int(comando[1])))
    else:
        eval('d.{}()'.format(comando[0]))
print(*d)
                  
#47-Company Logo

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input()

mydict=Counter(s).items()
mydict=sorted(mydict,key=lambda c: (-c[1], c[0]))
for chiave, valore in mydict[:3]:
    print(chiave,str(valore))
                  
#48-Piling Up!

for _ in range(int(input())):
    l=int(input())
    lst = list(map(int,input().split()))
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    print ("Yes" if i == l - 1 else "No")
                  
#49-Calendar Module
                 
import calendar
n1,n2,n3=map(int,input().split())
print((calendar.day_name[calendar.weekday(n3,n1,n2)]).upper())
                  
#50-Time Delta
                  
import math
import os
import random
import re
import sys
from datetime import datetime as dt

def time_delta(t1, t2):
    t1=dt.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    t2=dt.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    diff=(t1-t2).total_seconds()
    return(int(abs(diff)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta) + '\n')

    fptr.close()

#51-Exceptions
                  
T=int(input())
for _ in range(T):
    a,b=input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as error:
        print('Error Code:',error)
    except ValueError as error2:
        print('Error Code:',error2)
                  
#52-Zipped!

stud,subj=map(int,input().split())
studmarks=[]
for _ in range(subj):
    marks=map(float,input().split())
    studmarks.append(list(marks))
studmarks=list(zip(*studmarks))
for i in range(stud):
    print(sum(studmarks[i])/subj)
                  
#53-Athlete Sort
                  
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    ordinato=sorted(arr,key=lambda c:c[k])
    for i in range(n):
        print(' '.join(map(str,ordinato[i])))
                  
#54-ginortS
                  
s=input()
ordinato=sorted(s,key=lambda c:(c in '02468',c in '13579',c.isupper(),c.islower(),c) )
print(*ordinato,sep='')
                  
#55-Map and Lambda Function

cube = lambda x: x**3

def fibonacci(n):
    if n==0:
        return([])
    if n==1:
        return([0])
    lst=[0,1]
    for i in range(2,n):
        lst.append(lst[i-2]+lst[i-1])
    
    return(lst)  
  
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
                  
#56-XML 1 - Find the Score*
                  
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
  return etree.tostring(node).count(b'=')
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))  
                  
#57-XML2 - Find the Maximum Depth*

mport xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    level += 1
    if level >= maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
                  
#58-Standardize Mobile Number Using Decorators*
                  
def wrapper(f):
    def phone(l):
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
    return phone

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
                  
#59-Decorators 2 - Name Directory*
                  
import operator

def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: int(x[2]))) 
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
                  
#60-Detect Floating Point Number*
                  
import re
n=int(input())
for _ in range(n):
    num=input()
    print (bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', num)))
                  
#61-Re.split()*
                  
regex_pattern = r"\D"

import re
print("\n".join(re.split(regex_pattern, input())))
                  
#62-Group(), Groups() & Groupdict()*

import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)
                  
#63-Re.findall() & Re.finditer()*

import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags = re.I)
print('\n'.join(m or ['-1']))

#64-Re.start() & Re.end()*

S = input()
k = input()
import re
pattern = re.compile(k)
r = pattern.search(S)
if not r: print ("(-1, -1)")
while r:
    print ("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(S,r.start() + 1)

#65-Regex Substitution*

import re
N = int(input())

for i in range(N):
    print (re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))

#66-Validating Roman Numerals*

regex_pattern = r"M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$"
import re
print(str(bool(re.match(regex_pattern, input()))))

#67-Validating phone numbers*

import re 
N=int(input()) 
for i in range(N):
    if re.match(r'[789]\d{9}$',input()):   
        print ('YES')
    else:
        print ('NO')  

#68-Validating and Parsing Email Addresses*

import re
n = int(input())
for _ in range(n):
    x, y = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m:
        print(x,y)
                  
#69-Hex Color Code*

import re
pattern=r'(#[0-9a-fA-F]{3,6}){1,2}[^\n ]'
for _ in range(int(input())):
    for x in re.findall(pattern,input()):
        print(x)
                                    
#70-HTML Parser - Part 1*
                  
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print ('Start :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
            
    def handle_endtag(self, tag):
        print ('End   :',tag)
        
    def handle_startendtag(self, tag, attrs):
        print ('Empty :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
            
MyParser = MyHTMLParser()
MyParser.feed(''.join([input().strip() for _ in range(int(input()))]))

#71-HTML Parser - Part 2*

from html.parser import HTMLParser
class CustomHTMLParser(HTMLParser):
    def handle_comment(self, data):
        number_of_line = len(data.split('\n'))
        if number_of_line>1:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        if data.strip():
            print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

parser = CustomHTMLParser()

n = int(input())

html_string = ''
for i in range(n):
    html_string += input().rstrip()+'\n'
    
parser.feed(html_string)
parser.close() 


#72-Detect HTML Tags, Attributes and Attribute Values*

from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]
        
html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#73-Validating UID*

import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')

#74-Validating Credit Card Numbers*
                  
import re
TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
for _ in range(int(input().strip())):
    print("Valid" if TESTER.search(input().strip()) else "Invalid")

#75-Validating Postal Codes*

regex_integer_in_range = r"^[1-9][\d]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
                  
#76-Matrix Script*
                  
import re

n, m = map(int, input().split())
a, b = [], ""
for _ in range(n):
    a.append(input())

for z in zip(*a):
    b += "".join(z)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))

#77-Arrays

import numpy

def arrays(arr):
    return(numpy.array(arr,float)[-1::-1])
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#78-Shape and Reshape

import numpy as np
arr=list(map(int,input().strip().split(' ')))
print(np.reshape(arr,(3,3)))


#79-Transpose and Flatten

import numpy as np

n,m =list(map(int,input().split()))
lst=[]
for _ in range(n):
    ls=list(map(int,input().split(' ')))
    lst.append(ls)
print(np.array(lst).T)
print(np.array(lst).flatten())

#80-Concatenate

import numpy as np
n,m,p=map(int,input().split(' '))
lst1=[]
for _ in range(n):
    lst1.append(input().split())
lst2=[]
for _ in range(m):
    lst2.append(input().split())
arr1=np.array(lst1,int)
arr2=np.array(lst2,int)
print(np.concatenate((arr1,arr2)))

#81-Zeros and Ones

import numpy as np
dim=tuple(map(int,input().split()))
print(np.zeros(dim,dtype = np.int))
print(np.ones(dim,dtype = np.int))

#82-Eye and Identity

import numpy as np
np.set_printoptions(legacy='1.13')
n,m=map(int,input().split(' '))
print(np.eye(n,m))

#83-Array Mathematics

import numpy as np
n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')

#84-Floor, Ceil and Rint

import numpy as np
np.set_printoptions(legacy='1.13')
array=np.array(input().split(),float)
print(np.floor(array),np.ceil(array),np.rint(array),sep='\n')

#85-Sum and Prod

import numpy as np
n,m=map(int, input().split())
lst=[]
for _ in range(n):
    lst.append(input().split())
arr=np.array(lst,int)
arr=np.sum(arr,axis=0)
print(np.prod(arr))

#86-Min and Max

import numpy as np
n,m=map(int,input().split())
arr=np.array([input().split() for _ in range(n)],int)
print(np.max(np.min(arr,axis=1)))

#87-Mean, Var, and Std

import numpy as np
n,m=map(int,input().split())
arr=np.array([input().split() for _ in range(n)],int)
print(np.mean(arr,axis=1),np.var(arr,axis=0),round(np.std(arr),11),sep='\n')

#88-Dot and Cross

import numpy as np
n=int(input())
arr=np.array([input().split() for _ in range(n)],int)
arr2=np.array([input().split() for _ in range(n)],int)
print(np.dot(arr,arr2))

#89-Inner and Outer

import numpy as np
arr=np.array(input().split(),int)
arr1=np.array(input().split(),int)
print(np.inner(arr,arr1),np.outer(arr,arr1),sep='\n')

#90-Polynomials

import numpy as np
arr=np.array(input().split(),float)
print (np.polyval(arr, float(input())))

#91-Linear Algebra

import numpy as np 
n=int(input())
arr=np.array([input().split() for _ in range(n)],float)
print(round(np.linalg.det(arr),2))

#PROBLEM02

#92-Birthday Cake Candles

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    return(candles.count(max(candles)))
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


#93-