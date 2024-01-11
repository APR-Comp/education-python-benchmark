def remove_extras ( var__0 ) : 
  var__1 = [ ] 
  try:
    Itb=iter(var__0)
    while True:
      var__2=next(Itb)
      
      if  var__2 not in var__1:
        pass
      else:  
        var__1 += var__2 
  except StopIteration:
    pass
  return var__1 

