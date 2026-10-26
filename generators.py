# def even_numbers(start, end):
#     for number in range(start, end + 1):
#         if number % 2 == 0:
#             yield number
#
# for number in even_numbers(1, 10):
#     print(number)

def noteven_numbers(start, end):
    for number in range(start, end + 1):
        if number % 2 != 0:
            yield number

for number in noteven_numbers(1, 10):
    print(number)

def multiples_numbers(start, end):
    for number in range(start, end + 1):
        if number % 5 == 0:
            yield number

for number in multiples_numbers(1, 10):
    print(number)


# while True:
#     answer = input("Отримати наступне парне число? (так/ні): ")
#
#     if answer == "ні":
#         break
#
#     if answer == "так":
#         try:
#             print(next(generator))
#         except StopIteration:
#             print("Парні числа закінчилися.")
#             break
