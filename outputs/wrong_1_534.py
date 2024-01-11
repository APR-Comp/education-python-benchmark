def search ( var__0 , var__1 ) : 
  try:
    hwiNRG=iter(enumerate ( var__1 ))
    while True:
      var__2 , var__3=next(hwiNRG)
      
      if not var__0 <= var__3:    
        return len ( var__1 ) 
      else:
        return var__2 

  except StopIteration:
    pass

