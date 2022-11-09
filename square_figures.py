'''
Math Challenge
Have the function MathChallenge(num) read num which will be an integer. Your program should return the smallest 
integer that when squared has a length equal to num. For example: if num is 6 then your program should output 317 
because 317^2 = 100489 while 316^2 = 99856 which does not have a length of six.
'''
def MathChallenge(num):
  sayi=0
  while len(str(sayi ** 2)) != num:
    sayi = sayi + 1
  return sayi
print(MathChallenge(input()))