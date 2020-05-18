Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ("hurry makes a bay curry")
hurry makes a bay curry
>>> abc="hurry"
>>> abcd="curry"
>>> print("{} makes a bad {}".format("hurry ","curry"))
hurry  makes a bad curry
>>> print("{} makes a bad {}".format("curry ","hurry"))
curry  makes a bad hurry
>>> print("{1} makes a bad {0}".format("hurry ","curry"))
curry makes a bad hurry 
>>> print("{h} makes a bad {c}".format(h="hurry ",c="curry"))
hurry  makes a bad curry
>>> print("The {} {} around the {}".format("earth","rotate","sun"))
The earth rotate around the sun
>>>  print("The {2} {} around the {}".format("earth","rotate","sun"))
 
SyntaxError: unexpected indent
>>> print("The {2} {1} around the {0}".format("earth","rotate","sun"))
The sun rotate around the earth
>>> print("The {2} {2} around the {2}".format("earth","rotate","sun"))
The sun sun around the sun
>>> r=100/3
>>> print (r)
33.333333333333336
>>> print ("The result is {result:1.2f}".format(result=r))
The result is 33.33
>>> print ("The result is {r:1.2f}".format(r))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print ("The result is {r:1.2f}".format(r))
KeyError: 'r'
>>> print ("The result is {result:1.5f}".format(result=r))
The result is 33.33333
>>> print ("The result is {r:1.2f}".format())
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print ("The result is {r:1.2f}".format())
KeyError: 'r'
>>> ("The result is {}".format(r:1.2f))
SyntaxError: invalid syntax
>>> celsius=((132-32)*5)/9
>>> print (celsius)
55.55555555555556
>>> print ("Your required celsius point is {c:2.5f}".format(c=celsius))
Your required celsius point is 55.55556
>>> a=true
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a=true
NameError: name 'true' is not defined
>>> a=false
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a=false
NameError: name 'false' is not defined
>>> a=True
>>> a=False
>>> 5<6
True
>>> 3==3 and 5<6
True
>>> 3==3 and 5>6
False
>>> 3==10 and 5<6
False
>>> 3==3 or 5<6
True
>>> 3==3 and 5<1
False
>>> 3==3 or 5<1
True
>>> not 5<=6
False
>>> a="Hello";
>>> print(a*5);
HelloHelloHelloHelloHello
>>> print(a*5\n)
SyntaxError: unexpected character after line continuation character
>>> if a.lower()=="hello";
SyntaxError: invalid syntax
>>> a="hello"
>>> a="Hello"
>>> if a.lower()="hello"
SyntaxError: invalid syntax
>>> if a.lower()=="hello"
SyntaxError: invalid syntax
>>> if a.lower()== "hello":
	print(a)

Hello
>>> if a.lower()== "hello":
	print(a)
	elif a.lower()="Mello":
		
SyntaxError: invalid syntax
>>> a="Mello"
>>> if a.lower()== "hello":
	print(a)
	elif a.lower()== "mello":
		
SyntaxError: invalid syntax
>>>  if a.lower()== "hello":
	print(a)
	elif a.lower()== "mello":
		
SyntaxError: unexpected indent
>>>  if a.lower()== "hello":
	print(a)
	elif a.lower()== "mello":
		
SyntaxError: unexpected indent
>>>  if a.lower()== "hello":
	print(a)
elif a.lower()== "mello":
	
SyntaxError: unexpected indent
>>> b= "hello"
>>> for variable in a:
	print(variable)

M
e
l
l
o
>>> for variable in b:
	print(variable)

h
e
l
l
o
>>> c={"hello", "world"}
>>> for variable in c:
	print(variable)

world
hello
>>> for i in range(0,10);
SyntaxError: invalid syntax
>>> for i in range(0,10):
	print(i)

0
1
2
3
4
5
6
7
8
9
>>>  for i in range(0,10,2):
	print(i)
	
SyntaxError: unexpected indent
>>> for i in range(0,10):
      print(i)

0
1
2
3
4
5
6
7
8
9
>>>  for i in range(0,10,2):
	print(i)
	
SyntaxError: unexpected indent
>>> for i in range(0,10,2):
	print(i)

0
2
4
6
8
>>> for i in range(0,10,2):
	print(i%2)

0
0
0
0
0
>>> for i in range(0,10):
	print(i)

0
1
2
3
4
5
6
7
8
9
>>> for i in range(0,10):
	print(i%2)

0
1
0
1
0
1
0
1
0
1
>>> abc=[(0,1),(2,30,(4,5),(5,6),(6,7)]
     
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> abc=[(0,1),(2,3),(4,5),(5,6),(6,7)]
>>> for(first_number, second_number) in abc:
	print(second_number)

1
3
5
6
7
>>> for first_number, second_number in abc:
	print(second_number)

1
3
5
6
7
>>> if a.lower()== "hello":
	print(a)
	elif a.lower()== "mello":
		
SyntaxError: invalid syntax
>>> if a.lower()== "hello":
	print(a)
	elif a.lower()== "mello": pass
	
SyntaxError: invalid syntax
>>> if a.lower()== "hello":
	print(a)elif a.lower()== "mello": pass
	
SyntaxError: invalid syntax
>>> if a.lower()== "hello":
	print(a)
    elif a.lower()== "mello":
	    
SyntaxError: unindent does not match any outer indentation level
>>> abc="hello"
>>> for i in enumetrate(abc):
	print (i)

Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    for i in enumetrate(abc):
NameError: name 'enumetrate' is not defined
>>> for i in enumerate(abc):
	print (i)

(0, 'h')
(1, 'e')
(2, 'l')
(3, 'l')
(4, 'o')
>>> for first_number, second_number in abc:
	print(second_number)

Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    for first_number, second_number in abc:
ValueError: not enough values to unpack (expected 2, got 1)
>>> for first_number, second_number in enumerate(abc):
	print(second_number)

h
e
l
l
o
>>> for first_number, second_number in enumerate(abc):
	print(first_number)

0
1
2
3
4
>>> a=[1,2,3,4,5]
>>> b=[6,7,8,9,10]
>>> for i in zip(a,b):
	print(i)

(1, 6)
(2, 7)
(3, 8)
(4, 9)
(5, 10)
>>> c=[2,45,2,5,2,3,5,2,4]
>>> for i in zip(a,b,c):
	print(i);

(1, 6, 2)
(2, 7, 45)
(3, 8, 2)
(4, 9, 5)
(5, 10, 2)
>>> d=[ ,5,5]
SyntaxError: invalid syntax
>>> for i in zip(c):
	print(i);

(2,)
(45,)
(2,)
(5,)
(2,)
(3,)
(5,)
(2,)
(4,)
>>> a="hello"
>>> b=""
>>> for i in zip(a,b):
	print(i)

>>> b=[]
>>> for i in b:
	print(i)

>>> a="hello"
>>> b=[]
>>> for i in a:
	b.append(i)
	print(b)

['h']
['h', 'e']
['h', 'e', 'l']
['h', 'e', 'l', 'l']
['h', 'e', 'l', 'l', 'o']
>>> for i in a:
	print(b)

['h', 'e', 'l', 'l', 'o']
['h', 'e', 'l', 'l', 'o']
['h', 'e', 'l', 'l', 'o']
['h', 'e', 'l', 'l', 'o']
['h', 'e', 'l', 'l', 'o']
>>> m="hello"
>>> n=[x for x in m]
>>> print(n)
['h', 'e', 'l', 'l', 'o']
>>> z=0268
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> z="0268"
>>> n=[x for x in m]print(n)
SyntaxError: invalid syntax
>>> n=[x for x in m]
>>> print(n)
['h', 'e', 'l', 'l', 'o']
>>> n=[x for x in z]
>>> print(n)
['0', '2', '6', '8']
>>> for i in range(0,100,2)
SyntaxError: invalid syntax
>>> for i in range(0,100,2):
	print(i)

0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
>>> [for i in range(0,10,2)]
SyntaxError: invalid syntax
>>> a=[i for i in range(0,10,2)]
>>> print(a)
[0, 2, 4, 6, 8]
>>> for first_number, second_number in enumerate(abc):
	print(first_number)

0
1
2
3
4
>>> m="hello"
>>> for first_number, second_number in enumerate(m):
	print(first_number)

0
1
2
3
4
>>> for i in enumerate(m):
	print(i)

(0, 'h')
(1, 'e')
(2, 'l')
(3, 'l')
(4, 'o')
>>> s=[for i in enumerate(m):]
	print(i)
	
SyntaxError: invalid syntax
>>> s=[for i in enumerate(m):]
	print(s)
	
SyntaxError: invalid syntax
>>> m="hello"
>>> for i in enumerate(m):
	print(i)

(0, 'h')
(1, 'e')
(2, 'l')
(3, 'l')
(4, 'o')
>>> a="hello"
>>> z=[y for x,y enumerate(a) if x%2==0]
SyntaxError: invalid syntax
>>> z=[y for x,y in enumerate(a) if x%2==0]
>>> print (z)
['h', 'l', 'o']
>>> x=5
>>> x=0
>>> while x<=5
SyntaxError: invalid syntax
>>> while x<=5:
	print x
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> while x<=5:
	print x
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> z=0
>>> while z<=5:
	print z
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(z)?
>>> while z<=5:
	print (z)
	z=z+1
	else
	
SyntaxError: invalid syntax
>>> while z<=5:
	print (z)
	z=z+1
    else
    
SyntaxError: unindent does not match any outer indentation level
>>> 