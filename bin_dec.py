# Conversor de Binario a Decimal en Python
# Autor: [Tu Nombre]
# Descripción: Convierte un número binario (cadena) a su equivalente decimal.

def binario_a_decimal(binario: str) -> int:
    """
    Convierte un número binario (como cadena) a decimal.
    Lanza ValueError si el formato no es válido.
    """
    # Validar que solo contenga 0 y 1
    if not binario or any(digito not in '01' for digito in binario):
        raise ValueError("El número binario solo puede contener 0 y 1.")
    
    # Conversión usando int con base 2
    return int(binario, 2)


def main():
    print("=== Conversor de Binario a Decimal ===")
    while True:
        binario = input("Ingrese un número binario (o 'salir' para terminar): ").strip()
        
        if binario.lower() == "salir":
            print("Programa finalizado.")
            break
        
        try:
            decimal = binario_a_decimal(binario)
            print(f"El número binario {binario} equivale a {decimal} en decimal.\n")
        except ValueError as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()