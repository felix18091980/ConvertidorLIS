"""
ConvertidorLIS
Archivo principal del programa.
Versión: 0.1
Autor: Félix Aquino / ChatGPT
"""

from pathlib import Path


def main():
    print("=" * 50)
    print("      CONVERTIDOR LIS v0.1")
    print("=" * 50)

    archivo = input("\nIngrese la ruta del archivo .LIS: ").strip()

    if not archivo:
        print("\nNo ingresó ninguna ruta.")
        return

    ruta = Path(archivo)

    if not ruta.exists():
        print("\nEl archivo no existe.")
        return

    print(f"\nArchivo seleccionado:\n{ruta}")
    print("\nLa lectura del archivo se implementará en el siguiente paso.")


if __name__ == "__main__":
    main()
