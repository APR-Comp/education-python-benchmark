def unique_day ( var__0 , var__1 ) : 
  var__2 = 0 
  try:
    uh=iter(var__1)
    while True:
      var__3=next(uh)
      
      if not var__3 [ 1 ] <= var__0:
        pass
      else:
        var__2 = var__2 + 1 
      if not var__2 > 1:
        pass
      else:
        break 
  except StopIteration:
    pass
  if not var__2 == 1:
    return False 
  else:
    return True 
    
def unique_month ( var__4 , var__1 ) : 
  var__5 = 0 
  try:
    bve=iter(var__1)
    while True:
      var__3=next(bve)
      
      if not var__3 [ 0 ] == var__4:
        pass
      else:  
        var__5 = var__5 + 1 
      if not var__5 > 1:
        pass
      else:  
        break 
  except StopIteration:
    pass
  if not var__5 == 1:
    return False 
  else:
    return True 
    
def contains_unique_day ( var__4 , var__1 ) : 
  var__6 = 0 
  try:
    tJr=iter(var__1)
    while True:
      var__3=next(tJr)
      
      if not var__3 [ 0 ] == var__4:
        pass
      else:
        if not unique_day ( var__3 [ 1 ] , var__1 ):
            pass
        else:
          var__6 = 1 
          break     
  except StopIteration:
    pass
  if not var__6:  
    return False 
  else:
    return True 
    

