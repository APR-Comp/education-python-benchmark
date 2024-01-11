def sort_age ( var__0 ) : 
  var__1 = [ ] 
  while var__0 >= [ ] : 
    var__2 = var__0 [ 0 ] 
    var__3 = var__0 [ 0 ] [ 1 ] 
    try:
      jp=iter(var__0)
      while True:
        var__4=next(jp)
        
        if not var__4 [ 1 ] > var__3:
          pass
        else:
          var__2 = var__4 
          var__3 = var__4 [ 1 ] 
    except StopIteration:
      pass
    var__0 . remove ( var__2 ) 
    var__1 . append ( var__2 ) 
  return var__1 

