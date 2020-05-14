import unicodedata
import string
from string import maketrans 
import sys

print(sys.version_info.major)

print(unicodedata.name(u'A'))
print('\n{LATIN CAPITAL LETTER A}')
# smethods = [name for name in dir(str) if not name.startwith('__')]
# print(smethods)
# print(dir(string))
s1 = 'sono unA stringA, quindi Una  sequenza immutabile di caratteri'
# numero di occorenze
print(s1.replace('una','UNA',1)) 
print(s1)

# Required to call maketrans function.
intab = "ABC"
outtab = "abc"
trantab1 = maketrans(intab, outtab)

print (s1.translate(trantab1))

# da vedere
# trantab2 = maketrans({ord('i'):None})
# print s1.translate(trantab2)
# print(s1.maketrans({ord('i'):None}))



s2 = 'Un giorno, se avro\' tempo, andro\' a correre'

split1 = s2.split()
print(split1)

split2 = s2.split(',')
print(split2)

split3 = s2.split('ro\'')
print(split3)
