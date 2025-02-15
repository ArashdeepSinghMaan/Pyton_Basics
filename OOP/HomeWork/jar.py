class jar:
    def __init__(se,capacity=12):
        if capacity<0:
            raise ValueError("Wrong capacity")
        se.cap=capacity
        se.ze=0
    
    def __str__(se):
        return se.ze*'🍪'
        
    def deposit(se,n):
        if n >se.cap:
            raise ValueError("Limit Reached")
        if se.ze+n >se.cap:
            raise ValueError("Limit Reached")
        se.ze=n+se.ze
    def withdraw(se,r):
        if se.ze<r:
            raise ValueError("Not enough")
        se.ze=se.ze-r
    @property
    def capcity(se):
        return se.cap
    @property
    def size(se):
        return se.ze

