def remove_extras ( var__0 ) : 
  var__1 = [ ] 
  try:
    sb=iter(var__0)
    while True:
      var__2=next(sb)
      
      if not var__2 in var__1:
          pass
      else:
        var__1 . append ( var__2 ) 
  except StopIteration:
    pass
  return var__1 

