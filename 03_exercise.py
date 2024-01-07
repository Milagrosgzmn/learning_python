""" 
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
  """
from math import sqrt 

def test(num: int):
    def isPrime(number):
        if number!=2 and number > 1:
            for num in range(2,int(sqrt(number))):
                if number%num == 0:
                    return False
            
        return True
                
    def testFibonacci(number, current_index=0, current_fibonacci=0, next_fibonacci=1):
        if current_fibonacci == number:
            return True
        elif current_fibonacci > number:
            return False
        else:
            return testFibonacci(number, current_index + 1, next_fibonacci, current_fibonacci + next_fibonacci)

    if isPrime(num):
        prime = 'es primo'
    else: 
        prime= 'no es primo'

    if testFibonacci(num):
        fibonacci='fibonacci'
    else:
        fibonacci= 'no es fibonacci'
    
    if num%2 == 0:
        isEven = 'es par'
    else:
        isEven= 'es impar'


    return f'{num} {prime}, {fibonacci} y {isEven}'

print(test(2))
print(test(7))