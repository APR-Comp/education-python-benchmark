def search ( var__0 , var__1 ) : 
  if not len ( var__1 ) == 0:
    if var__0 < var__1 [ 0 ] : 
      var__2 = 0 
    elif var__0 > var__1 [ - 1 ] : 
      var__2 = var__1 . index ( var__1 [ - 1 ] ) + 1 
    else : 
      try:
        jib=iter(var__1)
        while True:
          var__3=next(jib)    
          if not var__0 <= var__3:
            pass
          else:
            var__2 = ( var__1 . index ( var__3 ) ) 
            break 
      except StopIteration:
        pass
      return var__2 
  else:
    var__2 = 0 
    

