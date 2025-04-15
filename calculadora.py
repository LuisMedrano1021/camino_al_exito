def mostrar_menu():
    print("=== calculadora ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-5): ")

    if opcion == '5':
        print("¡Gracias por usar la calculadora!")
        break

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == '1':
        resultado = num1 + num2
        print(f"Resultado: {resultado}")
    elif opcion == '2':
        resultado = num1 - num2
        print(f"Resultado: {resultado}")
    elif opcion == '3':
        resultado = num1 * num2
        print(f"Resultado: {resultado}")
    elif opcion == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {resultado}")
        else:
            print("Error: No se puede dividir por cero.")
    else:
        print("Opción no válida. Intenta de nuevo.")

    print()
