def sort_age ( var__0 ) : 
  var__1 = [ ] 
  while var__0 : 
    var__2 = var__0 [ 1 ] 
    try:
      anjfI=iter(var__0)
      while True:
        var__3=next(anjfI)
          
        if not var__3 [ 1 ] > var__2 [ 1 ]:
          pass
        else:
          var__2 = var__3 
    except StopIteration:
      pass
    var__0 . remove ( var__2 ) 
    var__1 . append ( var__2 ) 
  return var__1 