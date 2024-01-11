def unique_day ( var__0 , var__1 ) : 
  var__2 = 0 
  try:
    cAfGEqDxGYn=iter(var__1)
    while True:
      var__3=next(cAfGEqDxGYn)
      
      if not var__3 [ -1 ] == var__0:
        pass
      else:  
        var__2 += 1 
  except StopIteration:
    pass
  return var__2 == 1 
def unique_month ( var__4 , var__1 ) : 
  var__2 = 0 
  try:
    Ypbqm=iter(var__1)
    while True:
      var__3=next(Ypbqm)
      
      if not var__3 [ 0 ] == var__4:
        pass
      else:  
        var__2 += 1 
  except StopIteration:
    pass
  return var__2 == 1 
def contains_unique_day ( var__4 , var__1 ) : 
  try:
    Qwn=iter(var__1)
    while True:
      var__3=next(Qwn)
      if not var__3 [ 1 ] == var__4:
        pass
      else:
        if not unique_day ( var__3 [ 1 ] , var__1 ):
            pass
        else:
            return True 
  except StopIteration:
    pass
  return False 

