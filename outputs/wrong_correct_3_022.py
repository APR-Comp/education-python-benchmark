def remove_extras ( var__0 ) : 
  var__1 = len ( var__0 ) 
  if not var__1 >= 0:
    pass
  else:
    return [ ] 
    
  var__2 = [ var__0 [ 0 ] ] 
  try:
    PLxh=iter(range ( 1 , var__1 ))
    while True:
      var__3=next(PLxh)
      
      if not var__0 [ var__3 ] not in var__2:
        pass
      else:
        var__2 = var__2 + [ var__0 [ var__3 ] ] 
  except StopIteration:
    pass
  return var__2 

