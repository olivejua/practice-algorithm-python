lst = list(map(lambda x: x+10, [1,2,3]))
print(lst)

square_of_odd_numbers = [n * 2 for n in range(1, 10+1) if n % 2 == 1]
print(square_of_odd_numbers)

original = {1: "coding test", 2: "coding interview"}
a = {key: value for key, value in original.items()}
print(a)

a = [1,2,3,2,45,2,5]
for i,v in enumerate(a):
    print(i,v)

divmod(5,3)

print('A1', 'B2', sep=',')