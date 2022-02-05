#  Написать функцию проверки "силы" пароля, возвращяет всегда строку
# - если пароль короче 8 символов венрнуть Too weak
# - если пароль содержит только цифры, только строчные, только заглавные то вернуть Weak
# - если пароль содержит символы любых двух наборов вернуть Good
# - если пароль содержит символы всех трех наборов вернуть Very Good
import string


def pass_strength(value: str) -> str:
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    if len(value) < 8:
        return 'Too Weak'
    if all(x in digits for x in value) or all(x in lowers for x in value) or all(x in uppers for x in value):  # если все буквы
        return 'Weak'
    if any(x in digits for x in value) and any(x in lowers for x in value) and any(x in uppers for x in value):
        return 'Very Good'
    else:
        return 'Good'


if __name__ == '__main__':
    assert pass_strength('') == 'Too Weak'
    assert pass_strength('1234567') == 'Too Weak'
    assert pass_strength('qwertyu') == 'Too Weak'
    assert pass_strength('QWERTDT') == 'Too Weak'
    assert pass_strength('QweRT1') == 'Too Weak'
    assert pass_strength('1234567668') == 'Weak'
    assert pass_strength('12345678') == 'Weak'
    assert pass_strength('qwertyui') == 'Weak'
    assert pass_strength('qwertyuiqwe') == 'Weak'
    assert pass_strength('ASDFGHJK') == 'Weak'
    assert pass_strength('ASDFGHJKQW') == 'Weak'
    assert pass_strength('1234qwer') == 'Good'
    assert pass_strength('1234qwwwer') == 'Good'
    assert pass_strength('1234QWER') == 'Good'
    assert pass_strength('1234QWEQQQR') == 'Good'
    assert pass_strength('qwerQWER') == 'Good'
    assert pass_strength('qwewwwrQWER') == 'Good'
    assert pass_strength('qweWER123') == 'Very Good'
    assert pass_strength('123456wQ') == 'Very Good'
    assert pass_strength('qqqqwQ1q') == 'Very Good'
    assert pass_strength('QQWERT1e') == 'Very Good'
    assert pass_strength('QQWERT1egsk7') == 'Very Good'
