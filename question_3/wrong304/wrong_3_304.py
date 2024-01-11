def remove_extras ( var__0 ) : 
  var__1 = [ ] 
  try:
    FtEbmgJVgFh=iter(var__0)
    while True:
      var__2=next(FtEbmgJVgFh)
      
      if not var__2 not in var__1:  
        var__1 . extend ( var__2 ) 
      else:
        continue 
  except StopIteration:
    pass
  return var__1 

