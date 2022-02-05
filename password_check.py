#  Написать функцию проверки "силы" пароля, возвращяет всегда строку
# - если пароль короче 8 символов венрнуть Too weak
# - если пароль содержит только цифры, только строчные, только заглавные то вернуть Weak
# - если пароль содержит символы любых двух наборов вернуть Good
# - если пароль содержит символы всех трех наборов вернуть Very Good
import string


def pass_strength(value: str) -> str:
    if len(value) < 8:
        return 'Too Weak'
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    count = 0
    for symbols in (digits, lowers, uppers):
        if any(e in symbols for e in value):
            count +=1
            continue
    if count == 3:
        return 'Very Good'
    return 'Weak' if count ==1 else 'Good'




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
