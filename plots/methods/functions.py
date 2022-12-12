import math

from get_data import get_w_0
from messages import *

# переменные для работы с данными и программы
flag = 0
ustanovka = {}

# чтобы много раз не считать, заполним некоторые переменные
w_p = 0


# Декоратор для проверки того, что пользователь ввел данные установки
def get_start_plot(func):
    def verify():
        if flag == 0:
            global ustanovka
            n = input(which_plot)
            try:
                ustanovka.update(dict(zip(names_for_exp(n), input(print_start_msg(n)).split())))
            except Exception as err:
                print(f"Unexpected {err=}, {type(err)=}")
        func()

    return verify


@get_start_plot
def get_c_x():
    gamma = get_gamma()
    gamma_sqrt = math.sqrt(gamma)
    return 0.5 * (1 / gamma_sqrt) * math.log(
        (1 + math.sqrt(math.cos(ustanovka['theta_0']) / gamma + 1)) / (
                1 - math.sqrt(math.cos(ustanovka['theta_0']) / gamma + 1)))


@get_start_plot
def get_gamma():
    return (get_c_theta() - get_c_z()) / (w_p ** 2)


@get_start_plot
def get_wp():
    return 9.81 * math.cos(float(ustanovka['alpha'])) / (1.4 * int(ustanovka['r']))


@get_start_plot
def get_c_theta():
    return (w_p ** 2) * math.cos(ustanovka['theta_0'])


@get_start_plot
def get_c_z():
    return 0.5 * (get_w_0() ** 2)
