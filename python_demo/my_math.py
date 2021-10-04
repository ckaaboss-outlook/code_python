# This is a sample Python script.

import random, string

class MyMath:
    def math_add(self, *args):
        total = 0
        for i in args:
            if isinstance(i, int) or isinstance(i, float):
                total += i
        # print("Sum =", total, type(total))
        return total

    def abcus_add(self, n_num=3, dig_length=3):
        total = 0
        this_qustion = ''
        for i in range(n_num):
            this_ran_num = self.get_a_ran_digit(dig_length)
            this_qustion += ('{} + '.format(str(this_ran_num)))
            total += self.math_add(this_ran_num)
        this_qustion = "The total of: {} =".format(this_qustion[0:len(this_qustion)-2])
        return this_qustion, total

    def gem_add_ques(self, n_ques=3, n_num=3, dig_length=3, show_result=False):
        print(dig_length)
        for i in range(n_ques):
            this_qustion, total = self.abcus_add(dig_length)
            if show_result:
                print(this_qustion, total)
            else:
                print(this_qustion)

    def get_a_ran_digit(self, dig_len=3):
        ran_char = ''.join(random.choice(string.ascii_letters) for x in range(5))
        dig_dict = {1:(1, 9), 2:(10, 99), 3:(100, 999), 4:(1000, 9999),
                    5:(10000, 99999), 6:(100000, 999999), 7:(100000, 9999999)}
        start_num, end_num = dig_dict[dig_len]
        # print(start_num, end_num)
        rad_diget = random.randint(start_num, end_num)
        print('print_ran = {} and {}'.format(rad_diget, ran_char))
        return rad_diget

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = MyMath()
    # x.math_add(10, 20, 'str')
    x.gem_add_ques(n_ques=3, n_num=8, dig_length=5, show_result=True)
    x.get_a_ran_digit(2)

