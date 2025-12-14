#======= String & number vlues can operate together with =========> repeat

a=2
b=3
Text="@"
print(2*Text*3)

#========= String & string can operator with =========> concatenation

a="2"
b=3
Text="@"
print((a+Text)*b)

#============ Number values can operate with all arithmetic operators =======================

a=2
b=3
c=4
print(a+b*c)

#========= Arithmetic expresion with integer and float will result in float =============

a=10
b=5.0
c=a*b
print(c)

#====== Result of dividion operator with two integer will be best ================
a=1
b=2
c=a/b
print(c)

#==========integer division with float and int will give int displayed as float ==============
a=3.7
b=8
c=a//b
print(c,a/b)

a=12
b=5
c=a//b
print(c)

a=-12
b=5
c=a//b
print(c)

a=12
b=-5
c=a//b
print(c)

#=========== Remainder is negative when denominator is negative =========

a=-5
b=2
c=a%b 
print(c)

a=5
b=2
c=a%b
print(c)


a=5
b=-2
c=a%b
print(c)
