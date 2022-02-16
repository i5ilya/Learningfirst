def calculator(expression):
    allowed = '+-/*'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Выражение должно содержать хотябы один знак {allowed}')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left = int(left)
                right = int(right)
                if sign == '+':
                    return left + right
                if sign == '-':
                    return left - right
                if sign == '*':
                    return left * right
                if sign == '/':
                    return left / right
            except(ValueError, TypeError):
                raise ValueError('Выражение должно содержать 2 целых числа и один знак')


if __name__ := '__main__':
    print(calculator('2+2'))