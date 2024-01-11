def remove_extras ( var__0 ) : 
  var__1 = var__0 [ 0 ] 
  try:
    In=iter(var__0)
    while True:
      var__2=next(In)
      if not var__2 not in var__1:
        continue 
      else:
        var__1 . add ( var__2 ) 
  except StopIteration:
    pass
  return var__1 

