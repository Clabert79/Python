import re
c = re.compile(r"\b(?=\w{8}\b)\w{1,4}tex\w*") # la r sta per raw e indica al python di non eleborare backslash\
s = "texwille ritexwil ritexto 12tex345"

print(c.findall(s))
