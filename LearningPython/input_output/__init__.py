import sys
import os
from sys import exit
os.system('cls' if os.name == 'nt' else 'clear')

print("Enter two values to be added without typecasting\n");
a = input()
b = input()

c = a+b
print (c);

input()
os.system('cls' if os.name == 'nt' else 'clear')

print("Enter two values to be added with typecasting\n");

a = int(input())
b = int(input())

c = a+b
print (c);
input()
exit