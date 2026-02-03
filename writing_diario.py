<<<<<<< HEAD

=======
from datetime import datetime
from pathlib import Path

from pydantic import BaseModel, Field
from typing import Literal

from entrenador_c1_modelo import EntrenamientoC1


class EntradaWriting(BaseModel):
    tema: str = Field(min_length=3, max_length=120)
    texto: str = Field(min_length=80, description="Tu texto en inglés (mínimo 80 caracteres)")
    objetivo: Literal["C1", "C2"] = "C1"


def main():
    print("=== Writing Diario C1/C2 ===")
    tema = input("Tema: ").strip()
    objetivo = (input("Objetivo (C1/C2) [C1]: ").strip() or "C1").upper()

    print("\nPega tu texto (multilínea). Para terminar: Enter, luego Ctrl+Z y Enter.\n")
    lineas = []
    while True:
        try:
            lineas.append(input())
        except EOFError:
            break
    texto = "\n".join(lineas).strip()

    entrada = EntradaWriting(tema=tema, texto=texto, objetivo=objetivo)

    # ✅ Por ahora el "feedback" es un placeholder para que el sistema funcione.
    # Luego lo reemplazamos por feedback real (con tu revisión o con un modelo).
    reporte = EntrenamientoC1(
        nivel_estimado="C1" if entrada.objetivo == "C1" else "C2",
        errores_detectados=[],
        version_mejorada=entrada.texto,
        version_c2=entrada.texto,
        frases_clave_para_memorizar=[
            "It could be argued that…",
            "From a broader perspective…"
        ],
        foco_de_entrenamiento="Cohesion and clarity (placeholders)",
        ejercicio_recomendado="Rewrite the same text adding 3 advanced connectors."
    )

    # Guardar reporte
    out_dir = Path("reportes")
    out_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    archivo = out_dir / f"writing_{timestamp}.json"

    archivo.write_text(reporte.model_dump_json(indent=2), encoding="utf-8")

    print("\n✅ Reporte guardado en:", archivo)


if __name__ == "__main__":
    main()
