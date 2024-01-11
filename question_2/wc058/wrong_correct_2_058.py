def unique_day ( var__0 , var__1 ) : 
  var__2 = 2 
  try:
    EZ=iter(var__1)
    while True:
      var__3=next(EZ)
      
      if not var__3 [ 1 ] == var__0:
        pass
      else:
        var__2 += 1 
  except StopIteration:
    pass
  if not var__2 == 1:
    return False 
  else:
    return True 
    
def unique_month ( var__4 , var__1 ) : 
  var__5 = 0 
  try:
    mgE=iter(var__1)
    while True:
      var__3=next(mgE)
      
      if not var__3 [ 0 ] == var__4:
        pass
      else:
        var__5 += 1 
  except StopIteration:
    pass
  if not var__5 == 1:
    return False 
  else:
    return True 
    
def contains_unique_day ( var__4 , var__1 ) : 
  try:
    DyGiMMOU=iter(var__1)
    while True:
      var__3=next(DyGiMMOU)
      
      if not unique_day ( var__3 [ 1 ] , var__1 ):
        pass
      else:
        var__6 = var__3 [ 0 ] 
        if not var__4 == var__6:
          pass
        else:
          return True 
  except StopIteration:
    pass
  return False 

