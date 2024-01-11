def search ( var__0 , var__1 ) : 
  try:
    DPWEEjpDEz=iter(enumerate ( var__1 ))
    while True:
      var__2 , var__3=next(DPWEEjpDEz)
      
      if not var__0 <= var__3:
        pass
      else:
        return var__2 
  except StopIteration:
    pass
  return var__2 + 1 

