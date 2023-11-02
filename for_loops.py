

# def count(first, last):
#     test = ""
#     for x in range(first, last):
#         test += str(x)
#     print(test)
#
# def countdown(first, last, step):
#     test2 = ""
#     for x in range(first, last, step):
#         test2 += str(x)
#     print(test2)
#
#
# def main():
#     count(0, 6)
#     countdown(6, 0, -1)
# if __name__ == '__main__':
#     main()


def mult_table(number):
    for x in range(1, 12):
        answers = number * int(x)
        print(answers)

mult_table(6)