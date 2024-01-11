def unique_day ( var__0 , var__1 ) : 
  var__2 = 0 
  try:
    dAci=iter(var__1)
    while True:
      var__3=next(dAci)
      
      if not var__0 == var__3 [ 1 ]:  
        continue 
      else:
        var__2 += 1 
  except StopIteration:
    pass
  if not var__2 >= 2:
    return True 
  else:
    return False 
    
def unique_month ( var__4 , var__1 ) : 
  var__2 = 0 
  try:
    zVWY=iter(var__1)
    while True:
      var__3=next(zVWY)
      
      if not var__5 == var__3 [ 0 ]:
        continue 
      else:
        var__2 += 1 
  except StopIteration:
    pass
  if not var__2 >= 2:
    return True 
  else:
    return False 
    
def contains_unique_day ( var__4 , var__1 ) : 
  return 

