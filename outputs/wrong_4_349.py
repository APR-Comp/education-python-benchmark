def sort_age ( var__0 ) : 
  var__1 = 0 
  var__2 = [ ] 
  try:
    WFcTxZbAPd=iter(var__0)
    while True:
      var__3=next(WFcTxZbAPd)
      if not var__3 [ 3 ] > var__1:        
        var__3 . append ( var__2 ) 
      else:
        var__2 . append ( var__3 ) 
  except StopIteration:
    pass
  return var__2 

