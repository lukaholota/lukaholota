import time


# x = 1

# while x != 1000:
#     print(x)
#     x = x+1

massivosina = input()
nemassivosina = (massivosina.split(","))
indeksnemassivosinu = -1
while indeksnemassivosinu != len(nemassivosina):
   indeksnemassivosinu = indeksnemassivosinu + 1
   print(nemassivosina[indeksnemassivosinu])
# while len(nemassivosina) != indeksnemassivosinu:
    
#     print(indeksnemassivosinu)


exit()

digits_list1 = [1, 0, 2, 4]
digits_list2 = [5]
digits_list3 = [9, 3, 9]
digits_list3 = [1, 9, 2, 5, 7, 7, 5, 2, 9, 1]

def check_is_palindrome(digits_list: list):
    first_digit = digits_list[0]
    second_digit = digits_list[1]
    third_digit = digits_list[2]
    fouth_digit = digits_list[3]
    if first_digit == fouth_digit and second_digit == third_digit:
        print(True)
    if first_digit != fouth_digit and second_digit != third_digit:
        print(False)
    if first_digit != fouth_digit and second_digit == third_digit:
        print(False)
    if first_digit == fouth_digit and second_digit != third_digit:
        print(False)

# 
digits_list = ('8,4,5,8'.split(","))
check_is_palindrome(digits_list)


#

list1 = ['a', 'b', 'c']


a = list1[2]
print(a)

luka = 2
a = list1[luka]
print(a)


a = list1[len(list1)]
print(a)

def get2():
    return 1
a = list1[get2()]
print(a)


b

current_index

next_table


13442

'awqe2124'

True, False

None

lambda x: x*x

print(get2)



