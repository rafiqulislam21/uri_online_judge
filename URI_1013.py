value = input().split(" ")

a, b, c = value
a = int(a)
b = int(b)
c = int(c)

if a<b or a<c:
  if b<c:
   tmp = c;
  else:
   tmp = b;
else:
 tmp = a;

print("{} eh o maior".format(tmp))
