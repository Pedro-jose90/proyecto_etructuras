
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3

def ingresar_conjunto(nombre):
    while True:
        elementos = input(f"Ingrese elementos de {nombre} separados por coma: ")
        lista = [e.strip() for e in elementos.split(",") if e.strip() != ""]

        if len(lista) > 10:
            print("⚠ Máximo 10 elementos.")
            continue

        return set(lista)


def mostrar_conjunto(nombre, conjunto):
    print(f"{nombre} = {{ {', '.join(sorted(conjunto))} }}")


def mostrar_todos(conjuntos):
    for nombre, conjunto in conjuntos.items():
        mostrar_conjunto(nombre, conjunto)


def union(A, B):
    return A.union(B)

def interseccion(A, B):
    return A.intersection(B)

def diferencia(A, B):
    return A - B

def diferencia_simetrica(A, B):
    return A.symmetric_difference(B)

def complemento(U, A):
    return U - A

def dibujar_venn2(A, B):
    plt.figure(figsize=(10, 8))

    v = venn2(subsets=(1, 1, 1), set_labels=('A', 'B'))

    solo_A = A - B
    solo_B = B - A
    inter = A & B

    if v.get_label_by_id('10'):
        v.get_label_by_id('10').set_text('\n'.join(sorted(solo_A)))
        v.get_label_by_id('10').set_fontsize(10)

    if v.get_label_by_id('01'):
        v.get_label_by_id('01').set_text('\n'.join(sorted(solo_B)))
        v.get_label_by_id('01').set_fontsize(10)

    if v.get_label_by_id('11'):
        v.get_label_by_id('11').set_text('\n'.join(sorted(inter)))
        v.get_label_by_id('11').set_fontsize(10)

    print("\n--- REGIONES ---")
    print("Solo A:", solo_A)
    print("Intersección:", inter)
    print("Solo B:", solo_B)

    plt.title("Diagrama de Venn (2 conjuntos)")
    plt.show()

def dibujar_venn3(A, B, C):
    plt.figure(figsize=(12, 10))

    v = venn3(
        subsets=(1, 1, 1, 1, 1, 1, 1),
        set_labels=('A', 'B', 'C')
    )

    solo_A = A - B - C
    solo_B = B - A - C
    solo_C = C - A - B

    A_B = (A & B) - C
    A_C = (A & C) - B
    B_C = (B & C) - A

    A_B_C = A & B & C

    regiones = {
        '100': solo_A,
        '010': solo_B,
        '001': solo_C,
        '110': A_B,
        '101': A_C,
        '011': B_C,
        '111': A_B_C
    }

    for region, datos in regiones.items():
        label = v.get_label_by_id(region)
        if label:
            label.set_text('\n'.join(sorted(datos)))
            label.set_fontsize(8)

    print("\n--- REGIONES ---")
    print("Solo A:", solo_A)
    print("Solo B:", solo_B)
    print("Solo C:", solo_C)
    print("A ∩ B:", A_B)
    print("A ∩ C:", A_C)
    print("B ∩ C:", B_C)
    print("A ∩ B ∩ C:", A_B_C)

    plt.title("Diagrama de Venn (3 conjuntos)")
    plt.show()

def main():
    print("=== PROYECTO DE CONJUNTOS ===")

    U = ingresar_conjunto("Universo (U)")

    while True:
        try:
            n = int(input("¿Cuántos conjuntos desea ingresar? (1-3): "))
            if 1 <= n <= 3:
                break
            else:
                print("Debe ser entre 1 y 3.")
        except:
            print("Ingrese un número válido.")

    conjuntos = {}

    if n >= 1:
        conjuntos["A"] = ingresar_conjunto("A")
    if n >= 2:
        conjuntos["B"] = ingresar_conjunto("B")
    if n == 3:
        conjuntos["C"] = ingresar_conjunto("C")

    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar conjuntos")
        print("2. Unión (A ∪ B)")
        print("3. Intersección (A ∩ B)")
        print("4. Diferencia (A - B)")
        print("5. Diferencia simétrica")
        print("6. Complemento (U - A)")
        print("7. Diagrama de Venn")
        print("8. Salir")

        op = input("Seleccione una opción: ")

        if op == "1":
            mostrar_todos(conjuntos)

        elif op == "2":
            print("Resultado:", union(conjuntos["A"], conjuntos.get("B", set())))

        elif op == "3":
            print("Resultado:", interseccion(conjuntos["A"], conjuntos.get("B", set())))

        elif op == "4":
            print("Resultado:", diferencia(conjuntos["A"], conjuntos.get("B", set())))

        elif op == "5":
            print("Resultado:", diferencia_simetrica(conjuntos["A"], conjuntos.get("B", set())))

        elif op == "6":
            print("Resultado:", complemento(U, conjuntos["A"]))

        elif op == "7":
            if n == 2:
                dibujar_venn2(conjuntos["A"], conjuntos["B"])
            elif n == 3:
                dibujar_venn3(conjuntos["A"], conjuntos["B"], conjuntos["C"])
            else:
                print("Se necesitan al menos 2 conjuntos.")

        elif op == "8":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
