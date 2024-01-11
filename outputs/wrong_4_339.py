def sort_age ( var__0 ) : 
  if not var__0 == [ ]:   
    var__1 , var__2 = [ ] , [ ] 
    try:
      kvkM=iter(var__0)
      while True:
        var__3=next(kvkM)
        var__1 . append ( var__3 [ 1 ] )   
    except StopIteration:
      pass
    while var__1 : 
      var__4 = max ( var__1 ) 
      try:
        Uq=iter(var__0)
        while True:
          var__5=next(Uq)  
          if  var__5 [ 1 ] == var__4:
            pass
          else:
            var__2 . append ( var__5 ) 
      except StopIteration:
        pass
    return var__2 
  else:
    return var__0 
    
  pass 

