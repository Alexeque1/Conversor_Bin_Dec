def conv_bin_dec(num_bin):
    num_final = 0
    contador = 0
    for i in range(len(num_bin) - 1, -1, -1):
        num_final += int(num_bin[i]) * 2 ** contador
        contador += 1
    return num_final


def conv_dec_bin(num_dec):
    """Versión mejorada del método de división sucesiva"""
    if num_dec == 0:
        return "0"

    num_bin_final = ""
    while num_dec > 0:
        num_bin_final = str(num_dec % 2) + num_bin_final  # Agregar al inicio
        num_dec = num_dec // 2
    return num_bin_final


def validar_num_binario():  # Validación de número binario
    while True:
        num_bin = input("> ")
        error_bin = False
        for bit in num_bin:
            if bit not in ("1", "0"):
                error_bin = True
                break
        if error_bin:
            print("⚠️ Error, debe digitar un número binario correcto (1 y 0)")
            continue
        break
    return num_bin


def validar_num_decimal():  # Validación de número decimal
    while True:
        num_dec = input("> ")
        if not num_dec.isdigit():
            print("⚠️ Error, debe digitar solo números")
            continue
        break
    return num_dec


def conversor_bin_dec():
    print("*" * 57)
    print("🔄 Conversor de Binario a Decimal / Decimal a Binario 🔄")
    print("*" * 57)

    while True:
        print("\nPor favor, escoja la opción que desea: ")
        print("(1) Conversor de Binario a Decimal")
        print("(2) Conversor de Decimal a Binario")

        opcion = input("> ")
        if opcion not in ("1", "2"):
            print("⚠️ Error, debe escoger una opción correcta (1 o 2)")
            continue

        if opcion == "1":
            print("Por favor, ingrese el número binario a convertir: ")
            num_bin = validar_num_binario()
            num_final = conv_bin_dec(num_bin)
            print(f"✅ El número en decimal es: {num_final}")

        else:
            print("Por favor, ingrese el número decimal a convertir: ")
            num_dec = validar_num_decimal()
            num_bin_final = conv_dec_bin(int(num_dec))
            print(f"✅ El número en binario es: {num_bin_final}")

        # Preguntar si desea continuar
        continuar = input("\n¿Desea realizar otra conversión? (s/n): ").lower()
        if continuar != "s":
            print("👋 ¡Gracias por usar el conversor!")
            break


# Ejecutar el menú interactivo
conversor_bin_dec()
