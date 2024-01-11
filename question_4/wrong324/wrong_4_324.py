def sort_age ( var__0 ) : 
  var__1 = [ var__0 [ 0 ] ] 
  try:
    TNoV=iter(var__0)
    while True:
      var__2=next(TNoV)
      try:
        QH=iter(range ( len ( var__1 ) ))
        while True:
          var__3=next(QH)
          if var__2 [ 1 ] > var__1 [ var__3 ] [ 1 ] : 
            var__1 . insert ( var__3 + 1 , var__2 ) 
          elif var__2 [ 1 ] < var__1 [ var__3 ] [ 1 ] : 
            var__1 . insert ( var__3 , var__2 ) 
            return var__1         
      except StopIteration:
        pass
      return var__1 
  except StopIteration:
    pass

