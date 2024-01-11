def search ( var__0 , var__1 ) : 
  """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """ 
  try:
    Tg=iter(enumerate ( var__1 ))
    while True:
      var__2 , var__3=next(Tg)
      if not var__0 != var__3:
        pass
      else:  
        return var__2 
  except StopIteration:
    pass
  return len ( var__1 ) 

