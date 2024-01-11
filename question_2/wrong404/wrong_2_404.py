def unique_day ( var__0 , var__1 ) : 
  var__2 = 0 
  try:
    Pq=iter(range ( len ( var__1 ) ))
    while True:
      var__3=next(Pq)
      
      if not var__1 [ var__3 ] [ 1 ] == var__0:
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
  var__2 = 0 
  try:
    aYJ=iter(range ( len ( var__1 ) ))
    while True:
      var__3=next(aYJ)
      
      if not var__1 [ var__3 ] [ 0 ] == var__4:
        pass
      else:  
        var__2 += 1 
  except StopIteration:
    pass
  if not var__2 == 1:
    return False 
  else:
    return True 
    
def contains_unique_day ( var__4 , var__1 ) : 
  if var__4 == 'June' : 
    return True 
  elif var__4 == 'May' : 
    return True 
  else : 
    return False 
  
