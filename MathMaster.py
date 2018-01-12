import math
import sys
from sys import exit
import os
import argparse

_NAME = "MathMaster"
_VERSION = "v1.0.2"
_CHANNEL = "ALPHA"

ts = os.get_terminal_size()

alpha = 0
beta = 0
gamma = 0
a = 0
b = 0
c = 0
h = 0
p = 0
q = 0
done = False

RADIANS = 0
DEGREES = 1


def sin(x, t=RADIANS):
    if t == DEGREES:
        x = math.radians(x)
        return math.sin(x)
    elif t == RADIANS:
        return math.sin(x)


def cos(x, t=RADIANS):
    if t == DEGREES:
        x = math.radians(x)
        return math.cos(x)
    elif t == RADIANS:
        return math.cos(x)


def tan(x, t=RADIANS):
    if t == DEGREES:
        x = math.radians(x)
        return math.tan(x)
    elif t == RADIANS:
        return math.tan(x)


def asin(x, t=RADIANS):
    if t == DEGREES:
        x = math.radians(x)
        return math.asin(x)
    elif t == RADIANS:
        return math.asin(x)


def acos(x, t=RADIANS):
    if t == DEGREES:
        x = math.radians(x)
        return math.acos(x)
    elif t == RADIANS:
        return math.acos(x)


def atan(x, t=RADIANS):
    if t == DEGREES:
        x = math.radians(x)
        return math.atan(x)
    elif t == RADIANS:
        return math.atan(x)


def floating_decimals(f_val, dec):
    prc = "{:." + str(dec) + "f}"  # first cast decimal as str
    # print(prc)  # str format output is {:.3f}
    return float(prc.format(f_val))


def calc_unknown_lengths(r):
    global a, b, c, h, p, q, alpha, beta, gamma, done
    if done:
        return

    if float(h) == 0 and float(q) != 0 and float(p) != 0:
        h = math.sqrt(q * p)  # square root from q * p
        print('[+] Round {}; Calc h 1'.format(r + 1))
    elif float(h) == 0 and float(a) != 0 and float(p) != 0:
        h = math.sqrt((a * a) - (p * p))  # h = sqrt((a*a) - (p*p))
        print('[+] Round {}; Calc h 2'.format(r + 1))
    elif float(h) == 0 and float(b) != 0 and float(q) != 0:
        h = math.sqrt((b * b) - (q * q))  # h = sqrt((b*b) - (q*q))
        print('[+] Round {}; Calc h 3'.format(r + 1))

    if float(a) == 0 and float(h) != 0 and float(p) != 0:
        a = math.sqrt((h * h) + (p * p))  # a = sqrt((h * h) + (p * p))
        print('[+] Round {}; Calc a 1'.format(r + 1))
    elif float(a) == 0 and float(c) != 0 and float(p) != 0:
        a = math.sqrt(c * p)  # a = sqrt(c * p)
        print('[+] Round {}; Calc a 2'.format(r + 1))
    elif float(a) == 0 and float(c) != 0 and alpha != 0:
        a = sin(alpha, DEGREES) * c
        print('[+] Round {}; Calc a 3'.format(r + 1))
    elif float(a) == 0 and float(b) != 0 and alpha != 0:
        a = tan(alpha, DEGREES) * b
        print('[+] Round {}; Calc a 4'.format(r + 1))
    elif float(a) == 0 and float(c) != 0 and beta != 0:
        a = cos(beta, DEGREES) * c
        print('[+] Round {}; Calc a 5'.format(r + 1))
    elif float(a) == 0 and float(b) != 0 and beta != 0:
        a = b / tan(beta, DEGREES)

    if float(b) == 0 and float(h) != 0 and float(q) != 0:
        b = math.sqrt((h * h) + (q * q))
        print('[+] Round {}; Calc b 1'.format(r + 1))
    elif float(b) == 0 and float(c) != 0 and float(q) != 0:
        b = math.sqrt(c * q)
        print('[+] Round {}; Calc b 2'.format(r + 1))
    elif float(b) == 0 and float(c) != 0 and alpha != 0:
        b = cos(alpha, DEGREES) * c
        print('[+] Round {}; Calc b 3'.format(r + 1))
    elif float(b) == 0 and float(a) != 0 and alpha != 0:
        b = a / tan(alpha, DEGREES)
        print('[+] Round {}; Calc b 4'.format(r + 1))
    elif float(b) == 0 and float(c) != 0 and beta != 0:
        b = sin(beta, DEGREES) * c
        print('[+] Round {}; Calc b 5'.format(r + 1))
    elif float(b) == 0 and float(a) != 0 and beta != 0:
        b = tan(beta, DEGREES) * a
        print('[+] Round {}; Calc b 6'.format(r + 1))

    if float(c) == 0 and float(a) != 0 and float(b) != 0:
        c = math.sqrt((a * a) + (b * b))
        print('[+] Round {}; Calc c 1'.format(r + 1))
    elif float(c) == 0 and float(q) != 0 and float(p) != 0:
        c = q + p
        print('[+] Round {}; Calc c 2'.format(r + 1))
    elif float(c) == 0 and float(a) != 0 and float(p) != 0:
        c = (a * a) / p
        print('[+] Round {}; Calc c 3'.format(r + 1))
    elif float(c) == 0 and float(b) != 0 and float(q) != 0:
        c = (b * b) / q
        print('[+] Round {}; Calc c 4'.format(r + 1))
    elif float(c) == 0 and float(a) != 0 and alpha != 0:
        c = a / sin(alpha, DEGREES)
        print('[+] Round {}; Calc c 5'.format(r + 1))
    elif float(c) == 0 and float(b) != 0 and alpha != 0:
        c = b / cos(alpha, DEGREES)
        print('[+] Round {}; Calc c 6'.format(r + 1))
    elif float(c) == 0 and float(b) != 0 and beta != 0:
        c = b / sin(beta, DEGREES)
        print('[+] Round {}; Calc c 7'.format(r + 1))
    elif float(c) == 0 and float(a) != 0 and beta != 0:
        c = a / cos(beta, DEGREES)
        print('[+] Round {}; Calc c 8'.format(r + 1))

    if float(p) == 0 and float(h) != 0 and float(a) != 0:
        p = math.sqrt((a * a) - (h * h))
        print('[+] Round {}; Calc p 1'.format(r + 1))
    elif float(p) == 0 and float(c) != 0 and float(q) != 0:
        p = c - q
        print('[+] Round {}; Calc p 2'.format(r + 1))
    elif float(p) == 0 and float(a) != 0 and float(c) != 0:
        p = (a * a) / c
        print('[+] Round {}; Calc p 3'.format(r + 1))

    if float(q) == 0 and float(b) != 0 and float(h) != 0:
        q = math.sqrt((b * b) - (h * h))
        print('[+] Round {}; Calc q 1'.format(r + 1))
    elif float(q) == 0 and float(c) != 0 and float(p) != 0:
        q = c - p
        print('[+] Round {}; Calc q 2'.format(r + 1))
    elif float(q) == 0 and float(b) != 0 and float(c) != 0:
        q = (b * b) / c
        print('[+] Round {}; Calc q 3'.format(r + 1))


def print_test(text):
    print('[+] Test: {}...'.format(text))


def print_test_result(text, result):
    if result:
        sys.stderr.write('[+] Test: {}: '.format(text) + '\x1b[1;32mPASS\x1b[0m\n')
    else:
        sys.stderr.write('[+] Test: {}: '.format(text) + '\x1b[1;31mFAIL\x1b[0m\n')


def self_check():
    print_header()
    print('!!!    Starting self check    !!!')
    print('[+] Calculate angles')

    a = 7.52
    b = 5.45
    c = 9.29
    q = 3.2
    p = 6.09
    h = 4.41
    alpha = 54.06
    beta = 35.93
    gamma = 90.0

    # Calculate alpha with a and c
    print_test_result("Calculate alpha with a and c", 54.04 == round(math.degrees(math.asin(a / c)), 2))

    # Calculate alpha with b and c
    print_test_result("Calculate alpha with b and c", 54.08 == round(math.degrees(math.acos(b / c)), 2))

    # Calculate alpha with a and b
    print_test_result("Calculate alpha with a and b", 54.07 == round(math.degrees(math.atan(a / b)), 2))

    # Calculate beta with b and c
    print_test_result("Calculate beta with b and c", 35.92 == round(math.degrees(math.asin(b / c)), 2))

    # Calculate beta with a and c
    print_test_result("Calculate beta with a and c", 35.96 == round(math.degrees(math.acos(a / c)), 2))

    # Calculate beta with a and b
    print_test_result("Calculate beta with a and b", 35.93 == round(math.degrees(math.atan(b / a)), 2))

    print('[+] Calculate lengths: a')
    print_test_result("Calculate a with h and p", a == round(math.sqrt((h * h) + (p * p)), 2))
    print_test_result("Calculate a with c and p", a == round(math.sqrt(c * p), 2))
    print_test_result("Calculate a with c and alpha", a == round(sin(alpha, DEGREES) * c, 2))
    print_test_result("Calculate a with b and alpha", a == round(tan(alpha, DEGREES) * b, 2))
    print_test_result("Calculate a with c and beta", a == round(cos(beta, DEGREES) * c, 2))
    print_test_result("Calculate a with b and beta", a == round(b / tan(beta, DEGREES), 2))

    print('[+] Calculate lengths: b')
    print_test_result("Calculate b with h and q", b == round(math.sqrt((h * h) + (q * q)), 2))
    print_test_result("Calculate b with c and q", b == round(math.sqrt(c * q), 2))
    print_test_result("Calculate b with c and alpha", b == round(cos(alpha, DEGREES) * c, 2))
    print_test_result("Calculate b with a and alpha", b == round(a / tan(alpha, DEGREES), 2))
    print_test_result("Calculate b with c and beta", b == round(sin(beta, DEGREES) * c, 2))
    print_test_result("Calculate b with a and beta", b == round(tan(beta, DEGREES) * a, 2))

    print('[+] Calculate lengths: c')
    print_test_result("Calculate c with a and b", c == round(math.sqrt((a * a) + (b * b)), 2))
    print_test_result("Calculate c with q and p", c == round(q + p, 2))
    print_test_result("Calculate c with a and p", c == round((a * a) / p, 2))
    print_test_result("Calculate c with b and q", 9.28 == round((b * b) / q, 2))
    print_test_result("Calculate c with a and alpha", c == round(a / sin(alpha, DEGREES), 2))
    print_test_result("Calculate c with b and alpha", c == round(b / cos(alpha, DEGREES), 2))
    print_test_result("Calculate c with b and beta", c == round(b / sin(beta, DEGREES), 2))
    print_test_result("Calculate c with a and beta", c == round(a / cos(beta, DEGREES), 2))

    print('[+] Calculate lengths: p')
    print_test_result("Calculate p with h and a", p == round(math.sqrt((a * a) - (h * h)), 2))
    print_test_result("Calculate p with c and q", p == round(c - q, 2))
    print_test_result("Calculate p with a and c", p == round((a * a) / c, 2))

    print('[+] Calculate lengths: q')
    print_test_result("Calculate q with b and h", q == round(math.sqrt((b * b) - (h * h)), 2))
    print_test_result("Calculate q with c and p", q == round(c - p, 2))
    print_test_result("Calculate q with b and c", q == round((b * b) / c, 2))

    print('[+] Calculate lengths: h')
    print_test_result("Calculate h with q and p", h == round(math.sqrt(q * p), 2))
    print_test_result("Calculate h with a and p", h == round(math.sqrt((a * a) - (p * p)), 2))
    print_test_result("Calculate h with b and q", h == round(math.sqrt((b * b) - (q * q)), 2))

    exit(0)


def calc_angles(r):
    global a, b, c, h, p, q, alpha, beta, gamma, done
    if done:
        return

    if c < a or c < b:
        print('[-] Keine gültige Hypotenuse')
        _ = input("Press any key to return...")
        _ = os.system('cls')
        print_header()
        menu()

    if alpha == 0 and a != 0 and c != 0:
        alpha = math.degrees(math.asin(a / c))
        print('[+] Round {}; Calc alpha 1'.format(r + 1))
    elif alpha == 0 and b != 0 and c != 0:
        alpha = math.degrees(math.acos(b / c))
        print('[+] Round {}; Calc alpha 2'.format(r + 1))
    elif alpha == 0 and a != 0 and b != 0:
        alpha = math.degrees(math.atan(a / b))
        print('[+] Round {}; Calc alpha 3'.format(r + 1))

    if beta == 0 and b != 0 and c != 0:
        beta = math.degrees(math.asin(b / c))
        print('[+] Round {}; Calc beta 1'.format(r + 1))
    elif beta == 0 and a != 0 and c != 0:
        beta = math.degrees(math.acos(a / c))
        print('[+] Round {}; Calc beta 2'.format(r + 1))
    elif beta == 0 and a != 0 and b != 0:
        beta = math.degrees(math.atan(b / a))
        print('[+] Round {}; Calc beta 3'.format(r + 1))


def get_usable_formula():
    global a, b, c, h, p, q, alpha, beta, gamma, angle, done
    try:
        if alpha != 90 and beta != 90 and gamma != 90:
            print('[-] Kein 90° Winkel gefunden! Rechnung nicht möglich!')
            return
        if alpha == 90:
            talpha = alpha
            tbeta = beta
            tgamma = gamma
            gamma = talpha
            print('[+] alpha => gamma')
            alpha = tbeta
            print('[+] beta => alpha')
            beta = tgamma
            print('[+] gamma => beta')
            ta = a
            tb = b
            tc = c
            th = h
            tp = p
            tq = q
            c = ta
            print('[+] c => a')
            a = tb
            print('[+] a => b')
            b = tc
            print('[+] b => c')
            for r in range(5):
                calc_unknown_lengths(r)
                calc_angles(r)
            talpha = alpha
            tbeta = beta
            tgamma = gamma
            alpha = tgamma
            print('[+] gamma => alpha')
            beta = talpha
            print('[+] alpha => beta')
            gamma = tbeta
            print('[+] beta => gamma')
            ta = a
            tb = b
            tc = c
            th = h
            tp = p
            tq = q
            a = tc
            print('[+] a => c')
            b = ta
            print('[+] b => a')
            c = tb
            print('[+] c => b')
            q = tp
            print('[+] q => p')
            p = tq
            print('[+] p => q')
        elif beta == 90:
            talpha = alpha
            tbeta = beta
            tgamma = gamma
            gamma = tbeta
            print('[+] beta => gamma')
            alpha = tgamma
            print('[+] gamma => alpha')
            beta = talpha
            print('[+] alpha => beta')
            ta = a
            tb = b
            tc = c
            th = h
            tp = p
            tq = q
            b = ta
            print('[+] b => a')
            c = tb
            print('[+] c => b')
            a = tc
            print('[+] a => c')
            for r in range(5):
                calc_unknown_lengths(r)
                calc_angles(r)
            talpha = alpha
            tbeta = beta
            tgamma = gamma
            alpha = tbeta
            print('[+] beta => alpha')
            beta = tgamma
            print('[+] gamma => beta')
            gamma = talpha
            print('[+] alpha => gamma')
            ta = a
            tb = b
            tc = c
            th = h
            tp = p
            tq = q
            a = tb
            print('[+] a => b')
            b = tc
            print('[+] b => c')
            c = ta
            print('[+] c => a')
        elif gamma == 90:
            for r in range(5):
                calc_unknown_lengths(r)
                calc_angles(r)
    except:
        print("[-] Unexpected error:", sys.exc_info()[0])
        return False
    a = floating_decimals(a, 2)
    b = floating_decimals(b, 2)
    c = floating_decimals(c, 2)
    h = floating_decimals(h, 2)
    p = floating_decimals(p, 2)
    q = floating_decimals(q, 2)
    alpha = floating_decimals(alpha, 2)
    beta = floating_decimals(beta, 2)
    gamma = floating_decimals(gamma, 2)
    print('[+] Lösungen')
    print('[+] Längen')
    print('a = {}'.format(a))
    print('b = {}'.format(b))
    print('c = {}'.format(c))
    print('h = {}'.format(h))
    print('p = {}'.format(p))
    print('q = {}'.format(q))
    print('[+] Winkel')
    print('alpha = {}'.format(alpha))
    print('beta = {}'.format(beta))
    print('gamma = {}'.format(gamma))
    print('alle = {}'.format(alpha + beta + gamma))
    # print(
    #     '[+] a={};b={};c={};h={};p={};q={}'.format(a, b, c, h, p,
    #                                                q))
    # print('[+] alpha={};beta={};gamma={};all={}'.format(alpha, beta, gamma, alpha + beta + gamma))
    done = True
    return True


def get_known_values():
    global a, b, c, h, p, q, alpha, beta, gamma, angle
    try:
        print('[+] Gebe bekannte Längen an:')
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        h = float(input("h: "))
        p = float(input("p: "))
        q = float(input("q: "))
        print('[+] Gebe bekannte Winkel an(Mindestens ein Winkel muss 90° sein):')
        alpha = float(input("alpha: "))
        beta = float(input("beta: "))
        gamma = float(input("gamma: "))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return False
    return True


def get_angle():
    global angle
    angle = str(input("Winkel mit 90°? [a]lpha,[b]eta,[g]amma: "))
    return True


def again(exit):
    user_input = str(input("Nochmal? [Y/N]"))
    if user_input.upper() == "N" and exit:
        exit(1)
    elif user_input.upper() == "Y" and exit:
        pass


def fill_with_space(x):
    tmp = ""
    for _ in range(int(x)):
        tmp += " "
    return tmp


def fill_with_char(x, c):
    tmp = ""
    for _ in range(int(x)):
        tmp += c
    return tmp


def print_header():
    width = 80
    height = 5

    line1 = "{} {} {} ".format(_NAME, _VERSION, _CHANNEL)
    line2 = "by Lukas Eßmann "

    header = list()

    for _ in range(height):
        header.append("")

    header[0] += fill_with_space((ts.columns - width) / 2)
    header[0] += fill_with_char(width, '#')
    header[0] += fill_with_space((ts.columns - width) / 2)

    header[1] += fill_with_space((ts.columns - width) / 2)
    header[1] += "#"
    header[1] += fill_with_space(width - 2)
    header[1] += "#"
    header[1] += fill_with_space((ts.columns - width) / 2)

    header[2] += fill_with_space((ts.columns - width) / 2)
    header[2] += "#"
    header[2] += fill_with_space(((width - 2) - len(line1)) / 2)
    header[2] += line1
    header[2] += fill_with_space(((width - 2) - len(line1)) / 2)
    header[2] += "#"
    header[2] += fill_with_space((ts.columns - width) / 2)

    header[3] += fill_with_space((ts.columns - width) / 2)
    header[3] += "#"
    header[3] += fill_with_space(((width - 2) - len(line2)) / 2)
    header[3] += line2
    header[3] += fill_with_space(((width - 2) - len(line2)) / 2)
    header[3] += "#"
    header[3] += fill_with_space((ts.columns - width) / 2)

    header[4] += fill_with_space((ts.columns - width) / 2)
    header[4] += "#"
    header[4] += fill_with_space((width - 2))
    header[4] += "#"
    header[4] += fill_with_space((ts.columns - width) / 2)

    header[4] += fill_with_space((ts.columns - width) / 2)
    header[4] += fill_with_char(width, '#')
    header[4] += fill_with_space((ts.columns - width) / 2)

    for line in header:
        print(line)


def menu():
    global done
    print('[1] Trigonometrie')
    print('[9] About')
    print('[0] Exit')
    choice = int(input('Choice: '))
    if choice == 1:
        done = False
        _ = os.system('cls')
        print_header()
        if get_known_values():
            get_usable_formula()
        else:
            print('[-][Math.get_known_values()] Something bad happened :(')
        _ = input("Press any key to continue...")
    elif choice == 9:
        _ = os.system('cls')
        print_header()
        print('')
        print('MathMaster entstand als kleines Projekt in der Freiarbeit an der Montessori Schule Würzburg Oberzell.')
        print('Das Programm berechnet aktuell mit zwei Angaben alle fehlenden Seiten und Winkel in rechtwinkligen Dreiecken.')
        print('Auf die Idee kam ich, da ich in Mathematik 10 das Thema Trigonometrie bearbeitet habe. Ich wollte einen')
        print('Weg der Selbstkontrolle für die Schüler und eine Arbeitserleichterung für die Lehrer schaffen. Die')
        print('verwendete Programmiersprache ist Python 3.6. Ich hatte sehr viel Spaß bei der Programmierung. Ich')
        print('hoffe das Programm ist eine kleine Hilfe für euch. Falls ihr Anregungen oder Vorschläge habt, könnt ihr')
        print('euch bei mir melden.')
        print('')
        print('Lukas Eßmann; 10. Jahrgangsstufe')
        _ = input("Press any key to return...")
    elif choice == 0:
        exit(0)
    else:
        menu()


if __name__ == "__main__":
    os.system("title {} {} {}".format(_NAME, _VERSION, _CHANNEL))
    parser = argparse.ArgumentParser(description='Process some startup parameters.')
    parser.add_argument('--self-check', action='store_true', help='run self test on mathematical functions')
    parser.add_argument('-v', '--version', action='version', version='{} {} {}'.format(_NAME, _VERSION, _CHANNEL))
    args = parser.parse_args()

    if args.self_check is True:
        self_check()

    while True:
        _ = os.system('cls')
        print_header()
        menu()
