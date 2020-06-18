from math import factorial

def birthday_paradox(ydays=365, drange=0, pcnt=23):
    if ydays not in [365, 366]:
        return False, 'Days in years must be 365 or 366'
    elif drange < 0:
        return False, 'Days range must be positive number'
    elif pcnt < 0:
        return False, 'Number of people must be positive number'    
    else:
        res = (1 - (factorial(ydays - drange * pcnt - 1)) / (ydays ** (pcnt - 1) * factorial(ydays - pcnt * (drange + 1)))) * 100
        return True, '{:.10}'.format(res)


if __name__ == "__main__":
    days = int(input('Days in years:'))
    drange = int(input('Days range:'))
    pcnt = int(input('How many people in group:'))
    res = birthday_paradox(days, drange, pcnt)
    if res[0]:
        print('Result:{}%'.format(res[1]))
    else:
        print(res[1])
