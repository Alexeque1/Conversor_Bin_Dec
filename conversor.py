def conversor_bin_dec():
    print("="*57)
    print("🔃 Conversor de Binario a Decimal / Decimal a Binario 🔃")
    print("="*57)

    print("Por favor, escoja la opcion que desea: ")
    print("(1) Conversor de Binario a Decimal")
    print("(2) Conversor de Decimal a Binario")

    # Pedir al usuario la opcion
    while True:
        opcion = int(input("> "))

        # Comprobar que la opcion sea correcta
        # En caso de error, se volvera a pedir la opcion correcta
        if opcion not in ("1", "2"):
            print("⛔ Error, debe escojer una opcion correcta (1 o 2)")
            continue
        break

    # Si el usuario escoge la opcion 1
    if opcion == 1:
        print("Por favor, ingrese el numero binario a convertir: ")

        # En caso de error, se volvera a pedir el numero correcto
        while True:
            num_bin = input("> ")
            error_bin = False

            # Validar que el numero sea binario.
            for bit in num_bin:
                if bit not in ("1", "0"):
                    error_bin = True
                    break
                continue

            # Si hay un error, se vuelve a pedir el numero
            if error_bin:
                print("⛔ Error, debe digitar un numero binario correcto (1 y 0)")
                continue
            break
        
        num_final = 0  # Numero decimal final
        contador = 0  # Contador para la posicion del bit

        # Recorrer el numero binario de derecha a izquierda
        for i in range(len(num_bin) - 1, -1, -1):
            num_final += int(num_bin[i]) * 2 ** contador
            contador += 1
        
        print(f"El numero es: {num_final}")

    # Si el usuario escoge la opcion 2
    else:
        print("Por favor, ingrese el numero decimal a convertir: ")

        # En caso de error, se volvera a pedir el numero correcto
        while True:
            num_dec = input("> ")

            # Validar que el numero sea decimal
            if not num_dec.isdigit():
                print("⛔ Error, debe digitar solo numeros")
                continue
            break
        
        num_bin_final = ""  # Numero binario final
        num_dec = int(num_dec)  # Convertir el numero a entero

        # Convertir el numero decimal a binario
        while True:
            par_impar = num_dec % 2
            # Si el numero es menor a 1, se termina el ciclo
            if num_dec < 1:
                break
            # Si el numero es par, se agrega un 0 al final del numero binario
            elif par_impar == 0:
                num_bin_final += "0"
            # Si el numero es impar, se agrega un 1 al final del numero binario
            else:
                num_bin_final += "1"
            # Dividir el numero decimal entre 2 para la siguiente iteracion
            num_dec = num_dec // 2
            continue

        # El numero binario se obtiene al reves, por lo que se invierte antes de mostrarlo
        print(num_bin_final[::-1])


conversor_bin_dec()
