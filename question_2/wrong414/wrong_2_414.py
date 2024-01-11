def unique_day ( var__0 , var__1 ) : 
  var__2 = ( ) 
  try:
    tL=iter(range ( len ( var__1 ) ))
    while True:
      var__3=next(tL)
      
      if not var__0 == var__1 [ var__3 ] [ 0 ]:
        pass
      else:
        var__2 = var__2 + ( var__1 [ var__3 ] [ 1 ] , ) 
  except StopIteration:
    pass
  if not len ( var__2 ) < 2:
    return False 
  else:
    return True 
    
def unique_month ( var__4 , var__1 ) : 
  var__2 = ( ) 
  try:
    cxg=iter(range ( len ( var__1 ) ))
    while True:
      var__3=next(cxg)
      
      if not var__4 == var__1 [ var__3 ] [ 0 ]:
        pass
      else:
        var__2 = var__2 + ( var__1 [ var__3 ] [ 0 ] , ) 
  except StopIteration:
    pass
  if not len ( var__2 ) < 2:
      return False 
  else:
    return True 
    
def contains_unique_day ( var__4 , var__1 ) : 
  var__2 = ( ) 
  var__5 = ( ) 
  try:
    vUz=iter(range ( len ( var__1 ) ))
    while True:
      var__3=next(vUz)
      
      if not var__4 == var__1 [ var__3 ] [ 0 ]:
        pass
      else:
        var__2 = var__2 + ( var__1 [ var__3 ] [ 1 ] , ) 
        try:
          Mz=iter(var__2)
          while True:
            var__6=next(Mz)
            var__5 = var__5 + ( unique_day ( var__6 , var__1 ) , )   
        except StopIteration:
          pass
  except StopIteration:
    pass
  if not True in var__5:
    return False 
  else:
    return True 
    

