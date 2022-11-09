'''
Have the function AlphabetSearching(str) take the str parameter being passed and return the string 
true if every single letter of the English alphabet exists in the string, otherwise return the string false.
For example: if str is "zacxyjbbkfgtbhdaielqrm45pnsowtuv" then your program should return the string true because
every character in the alphabet exists in this string even though some characters appear more than once.
'''
def StringChallenge(strParam):
  boolList=[]
  alphabet="abcdefghijklmnopqrstuvwxyz"
  setStrParam = set(strParam)
  for letter in alphabet:
    for paramletter in setStrParam:
      if letter==paramletter:
        boolList.append("true")
  if len(boolList)!=len(alphabet):
    return "false"
  else:
    return "true"
print(StringChallenge(input()))