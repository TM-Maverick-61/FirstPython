# Enter your code here. Read input from STDIN. Print output to STDOUT
X, k = map(int, input().split())
P = str(input())
for i in P:
    if i == 'x':
        x = X

K1 = int(P)
if K1 == k:
    print("True")
else:
    print("False")

