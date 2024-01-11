def remove_extras ( var__0 ) : 
  var__1 = [ ] 
  try:
    ncW=iter(range ( len ( var__0 ) ))
    while True:
      var__2=next(ncW)
      
      var__3 = 1 
      try:
        dJk=iter(range ( var__2 ))
        while True:
          var__4=next(dJk)
          if not var__0 [ var__2 ] == var__0 [ var__4 ]:
            pass
          else:
            var__3 = 1 
      except StopIteration:
        pass
      if not var__3 == 0:
        pass
      else:
        var__1 += [ var__0 [ var__2 ] , ] 
  except StopIteration:
    pass
  return var__5 
  pass 

