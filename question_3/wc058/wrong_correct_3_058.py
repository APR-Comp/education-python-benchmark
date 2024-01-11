def remove_extras ( var__0 ) : 
  var__1 = [ ] 
  try:
    sq=iter(var__0)
    while True:
      var__2=next(sq)
      
      if  var__2 not in var__1:
        pass
      else:
        var__1 . append ( var__2 ) 
  except StopIteration:
    pass
  var__0 = var__1 
  return var__0 

