#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Wei Sun"
__copyright__ = "Copyright (C) 2019 GFLoan Co. LTD"
__license__ = "Private"
__version__ = "1.0"

import math
import pprint


def get_max_x_for_m_n_in_box(width, height, m, n, r):
    return min(width / m, height / (n * r))


def test_fill_portrait():
    params = {
        'count': 100,
        'r': 1.25,
        'width': 450,
        'height': 1200
    }
    count = params['count']
    r = params['r']
    width = params['width']
    height = params['height']

    x_max = math.sqrt(width * height / (count * r))

    print(x_max)

    good_x = min(width / count, height / (count * r))

    bad_x = x_max + 1

    cost = 0

    pprint.PrettyPrinter(indent=4).pprint(params)

    print("---- Scanning... ------")
    print('\t'.join(['round', 'x', 'm', 'n', 'total_ratio']))

    m_last = 1
    m_current = count

    n_last = 1
    n_current = count

    x_accuracy = 4

    while abs(good_x - bad_x) > pow(0.1, x_accuracy) and abs(m_current - m_last) >= 1 and abs(n_current - n_last) >= 1:
        x = (good_x + bad_x) * 0.5
        m, n = calculate_m_n_for_x_with_r_in_box(width, height, x, r)

        cost += 1

        if m * n >= count:
            # this is a good point
            good_x = x
            p = calculate_total_ratio(count, width, height, r, good_x)
            log_result(cost, good_x, m, n, p, n_decimals=x_accuracy)
            m_last = m_current
            m_current = m

            n_last = n_current
            n_current = n
            continue
        else:
            # this is a bad point
            bad_x = x
            pass

    x0 = get_max_x_for_m_n_in_box(width, height, m_current, n_current, r)
    calculate_final_for_x(cost, count, height, r, width, x0, x_accuracy, "Converged m,n")
    calculate_final_for_x(cost, count, height, r, width, good_x, x_accuracy, "Converged x")


def calculate_final_for_x(cost, count, height, r, width, x0, n_decimals, result_condition):
    m0, n0 = calculate_m_n_for_x_with_r_in_box(width, height, x0, r)
    print(f'------------ Result Based on {result_condition} ----------------')
    p0 = calculate_total_ratio(count, width, height, r, x0)
    log_result(cost, x0, m0, n0, p0, n_decimals)


def log_result(cost, good_x, m, n, p, n_decimals=2):
    string_format = "{:."+str(n_decimals)+"f}"
    print(cost, '\t', string_format.format(good_x), '\t', m, '\t', n, '\t', "{:.2f}".format(p))


def calculate_total_ratio(count, width, height, r, good_x):
    return count * good_x * r * good_x / (width * height) * 100


def calculate_m_n_for_x_with_r_in_box(width, height, x, r):
    m = int(width / x)
    n = int(height / (x * r))
    return m, n


def main():
    pass


if __name__ == '__main__':
    main()
