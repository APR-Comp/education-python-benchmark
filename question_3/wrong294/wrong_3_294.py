def remove_extras ( var__0 ) : 
  var__1 = [ ] 
  var__2 = [ ] 
  try:
    cKuG=iter(var__0)
    while True:
      var__3=next(cKuG)
      
      if var__3 not in var__1 : 
        var__1 . append ( var__3 ) 
      elif var__3 not in var__1 : 
        var__2 . append ( var__3 ) 
  except StopIteration:
    pass
  try:
    NrK=iter(var__2)
    while True:
      var__3=next(NrK)
      var__0 . remove ( var__3 ) 
  except StopIteration:
    pass
  return var__0 

