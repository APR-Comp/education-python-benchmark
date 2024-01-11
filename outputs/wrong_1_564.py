def search ( var__0 , var__1 ) : 
    try:
        st=iter(enumerate ( var__1 ))
        while True:
            var__2 , var__3=next(st)    
            if var__0 == var__3 : 
                return var__2 
            elif var__2 == ( len ( var__1 ) - 1 ) : 
                return var__2 + 1 
            else : 
                continue 
    except StopIteration:
        pass

