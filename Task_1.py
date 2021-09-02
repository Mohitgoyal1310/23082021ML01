Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Q1
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6 == 6
True
>>> a=20; a+=30; a%=3;
>>> print(a)
2
>>> True * False
0
>>> True & False
False
>>> True and False
False
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> ((True == False) or (False> True)) and (False<=True)
False
>>> #question 3
>>> s1='Nice to have it'
>>> s2='here'
>>> s1+s2
'Nice to have ithere'
>>> #question 4
>>> a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3][1][2]
['hello']
>>> a.insert(0,"Nice to have it")
>>> a.insert(7,"here")
>>> a
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> #question 7
>>> color_list_1= set(['White','Black','Red'])
>>> color_list_2 = set(['Red','Green'])
>>> color_list_1.difference(color_list_2)
{'White', 'Black'}
>>> 