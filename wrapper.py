
import functools
import inspect

"""
function wrapper에 대해 알아보자!
"""
def valid_input_check(permit_negative_PER=False):
    def _valid_input_check(func):
        sig = inspect.signature(func)
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if 'earnings' in sig.bind_partial(*args, **kwargs).arguments and \
                'num_stocks' in sig.bind_partial(*args, **kwargs).arguments:
                e = kwargs['earnings']
                n = kwargs['num_stocks']
                if permit_negative_PER and n > 0:
                    return func(*args, **kwargs)
                else:
                    print('순이익 혹은 주식 수가 음수입니다.')
                    return
            else:
                print('순이익 혹은 주식 수가 입력되지 않았습니다.')
                return
        return wrapper
    return _valid_input_check


@valid_input_check(permit_negative_PER=True)
def calculate_PER(price: int, earnings: int, num_stocks: int) -> float:
    """
    PER을 산출하는 함수
    :param price: 주가
    :param earnings: 분기 순이익
    :param num_stocks: 주식 수
    :return: PER
    """
    return price / (earnings / num_stocks)


print(calculate_PER(price=3000, earnings=300, num_stocks=30))
print(calculate_PER(price=3000, earnings=-300, num_stocks=30))
print(calculate_PER(price=3000, earnings=300, num_stocks=-30))
