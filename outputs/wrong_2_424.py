def unique_day ( var__0 , var__1 ) : 
  var__2 = 0 
  try:
    YblsFy=iter(var__1)
    while True:
      var__3=next(YblsFy)
      
      if not var__0 > var__3 [ 1 ]:
        pass
      else:
        var__2 += 1 
  except StopIteration:
    pass
  if not var__2 > 1 or var__2 == 0:
    return True 
  else:
    return False 
    
def unique_month ( var__4 , var__1 ) : 
  var__2 = 0 
  try:
    iNTco=iter(var__1)
    while True:
      var__3=next(iNTco)
      
      if not var__4 == var__3 [ 0 ]:
        pass
      else:
        var__2 += 1 
  except StopIteration:
    pass
  if not var__2 > 1:
    return True 
  else:
    return False 
    
def contains_unique_day ( var__4 , var__1 ) : 
  var__2 = 0 
  try:
    Ol=iter(var__1)
    while True:
      var__3=next(Ol)
      
      if not var__4 == var__3 [ 0 ]:
        pass
      else:
        var__5 = unique_day ( var__3 [ 1 ] , var__1 ) 
        if not var__5 == True:
          pass
        else:
            var__2 += 1 
  except StopIteration:
    pass
  if not var__2 >= 1:
    return False 
  else:
    return True 
    

