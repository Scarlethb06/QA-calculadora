from calculadora import Calculadora

def flujo_completo():
    calc = Calculadora()
    total = calc.suma(10, 5)      # 15
    resultado = calc.divide(total, 3)  # 5.0
    return resultado

if __name__ == "__main__":
    print("✅ Flujo de integración OK:", flujo_completo())
