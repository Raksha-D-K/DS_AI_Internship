#list example
from networkx import reverse


from networkx import reverse


numbers=[10,20,30,40,50];
coordinators=(5,10);
print(numbers);
print(coordinators);

a=[100,200,300,400,500,600,700,800,900,1000];
print(a[-3:-1]);
print(a[-1:-3]);
print(a[1:8:2]);
print(a[-4:-1:2]);

a=[5,3,8,6,7,2,4,1];
#soring the list
a.sort();
print(a);
#sorting in reverse order
a.sort(reverse=True);
print(a);
#popping last element
a.pop();
print(a);
#adding element to list
a.append(9);
print(a);
