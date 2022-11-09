import numpy as np
def ArrayChallenge(arr):
  maxNum=np.max(arr)
  arr.remove(maxNum)
  if (np.sum(arr)<maxNum):
    return "false"
  else:
    return "true"
# keep this function call here 
#print ArrayChallenge(raw_input())