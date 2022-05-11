import functools
from typing import Callable


def fabric(lambda_func: Callable) -> Callable:
    """
    Decorator factory.
    Get lambda function as an input parameter and returns a decorator,
    that calls the lambda function
    with an argument. The argument is result of user (foo) function,
    that decorated by repeat decorator
    :param lambda_func: Lambda function
    :type lambda_func: Callable
    :return: Decorator, that calls the lambda function
    with an argument. The argument is result of user (foo) function,
    that decorated by repeat decorator
    :rtype: Callable
    """
    # Flag for turning decorator on/off
    fabric.off = False

    # The functions describe structure of included decorators
    # Function that returns object of repeat decorator
    def decorator(repeat_func):
        # Decorator from functools for getting info from original function
        @functools.wraps(repeat_func)
        # Function that returns object of repeat decorator with parameters
        def decorator_wrapper(repeat_func_param):
            # Function that returns object of decorated function
            def inner(decorator_func):
                @functools.wraps(decorator_func)
                # Function that calls lambda function from parameter
                def inner_wrapper(*f_args, **f_kwargs):
                    # Call lambda function without decorating
                    # by the repeat decorator
                    if fabric.off:
                        print(lambda_func(decorator_func(f_args,
                                                         f_kwargs)))
                    # Call lambda function with decorating
                    # by the repeat decorator
                    else:
                        print(lambda_func(repeat_func(repeat_func_param)
                                          (decorator_func)(f_args, f_kwargs)))

                return inner_wrapper

            return inner

        return decorator_wrapper

    return decorator


@fabric(lambda x: x ** 2)
def repeat(times: int) -> Callable:
    """
    Decorator for user (foo) function
    that calls the function 'times' times
    and return average value of the callings
    :param times: Quantity of times
    that the user (foo) function should be called
    :type times: int
    :return: Decorator, that calls user (foo) function 'times' times
    :rtype: Callable
    """

    # Function that returns object of decorated function (foo)
    def inner(func):
        @functools.wraps(func)
        # The same arguments that in foo function
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(times):
                func_result = func()
                total += func_result
            return int(total / times)

        return wrapper

    return inner


@repeat(3)
def foo(*args, **kwargs):
    """Function gets any parameters and return a value -
    parameter for lambda function"""
    print("Foo called!")
    return 3


if __name__ == '__main__':
    foo(12)
    fabric.off = True
    foo(12)
