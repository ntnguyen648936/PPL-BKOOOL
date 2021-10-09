# 08-TYPES

## Pointer
- 2 Operator: assignment and dereferencing ( j = *ptr )
- Problems:
  + [Dangling pointer](https://www.geeksforgeeks.org/dangling-void-null-wild-pointers/) 
  + Lost heap-dynamic variable
- Solution for Danling pointer:
  + [Tombstone](https://en.wikipedia.org/wiki/Tombstone_(programming))
  + [Locks-and-keys]

## Type checking (type expression)
- {array(1..10,record((a*array(,5..10,integer)*(b*record((c*real)*(d*array(1..3,real)))))))}