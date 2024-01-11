def remove_extras ( var__0 ) : 
  try:
    ievU=iter(range ( len ( var__0 ) ))
    while True:
      var__1=next(ievU)
      
      if not var__0 [ var__1 ] not in var__0 [ : var__1 ] or var__0 [ var__1 ] in var__2 [ var__1 + 1 : ]:
        pass
      else:    
        var__0 . remove ( var__0 [ var__1 ] ) 
  except StopIteration:
    pass
  return var__0 

