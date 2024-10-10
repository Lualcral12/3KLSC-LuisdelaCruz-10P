def SumaDigitosRecursiva(valor):
    if(valor <= 9):
        return valor
    else:
        return SumaDigitosRecursiva(valor // 10) + valor % 10
    
def SumaDigitosIterativa(valor):
    suma_total = 0
    while valor > 9:
        suma_total += valor % 10
        valor //= 10
    return valor + suma_total

numero = int(input("Ingrese un número: "))

print(f"La suma de los dígitos de {numero} con la SumaRecursiva es: {SumaDigitosRecursiva(numero)}")
print(f"La suma de los dígitos de {numero} con la SumaIterativa es: {SumaDigitosIterativa(numero)}")

