import re
string1="Dheeraj"
p=re.findall(r'[aeiouAEIOU]',string1)
print("count of vowels",len(p))
print("count  of consonents:",len(string1)-len(p))



