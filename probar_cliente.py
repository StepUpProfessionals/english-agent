from pydantic import ValidationError
from cliente_modelo import Cliente

def imprimir_errores(e: ValidationError) -> None:
    print("Datos inválidos. Revisa lo siguiente:")
    for err in e.errors():
        campo = ".".join(str(x) for x in err["loc"])
        print(f"- {campo}: {err['msg']}")

# ✅ Datos válidos
try:
    c1 = Cliente(nombre="Marisol", email="usuario@dominio.com", edad=35)
    print("Válido:", c1)
except ValidationError as e:
    imprimir_errores(e)

print("\n---\n")

# ❌ Datos inválidos (a propósito)
try:
    c2 = Cliente(nombre="M", email="info_stepuplanguages.com", edad=200)
    print("Válido (no debería):", c2)
except ValidationError as e:
    imprimir_errores(e)
