# -*- coding: utf-8 -*-
mem = [0]
n=28
k=3

def rec(n):
  if n == 0:
        return 0
  if n == 1:
        return 1 
  if n == 2:
        return k
        
  oneGen = rec(n-1);
  twoGen = rec(n-2);

  if n <= 4:
        return (oneGen + twoGen);
    
  return (oneGen + (twoGen * k));



print("Final f(10)=", rec(n))