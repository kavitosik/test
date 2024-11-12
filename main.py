# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False 
# num = int(input('Введите число: '))
# print(is_even(num))

my_list1 = [1, 2, 5, 7, 'привет']
my_list2 = [1,'привет', 6, 5, 21]
def common_elements(list1, list2):
    my_list = []
    for i in list1:
        if i in list2:
            my_list.append(i)
    return my_list
print(common_elements(my_list1, my_list2))