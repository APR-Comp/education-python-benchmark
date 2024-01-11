def remove_extras ( var__0 ) : 
  var__1 = [ ] 
  try:
    ei=iter(list)
    while True:
      var__2=next(ei)
      
      if not var__2 not in var__1:
        pass
      else:
        var__1 . append ( var__2 ) 
  except StopIteration:
    pass
  return var__1 

