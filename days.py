def getDayCount(y, m):
  if m in (1,3,5,7,8,10,12):
    d = 31
  elif m in (4,6,9,11):
    d = 30
  else:
    if y % 400 == 0:
      d = 29
    elif y % 100 == 0:
      d = 28
    elif y % 4 ==0: 
      d = 29
    else:
      d = 28
  return d


