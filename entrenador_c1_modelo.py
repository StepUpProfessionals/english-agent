
from pydantic import BaseModel, Field
from typing import List, Literal


class ErrorItem(BaseModel):
    tipo: Literal[
        "gramática",
        "léxico",
        "cohesión",
        "pronunciación",
        "registro",
        "fluidez"
    ]
    descripcion: str
    sugerencia: str


class EntrenamientoC1(BaseModel):
    nivel_estimado: Literal["B2", "C1", "C2"]

    errores_detectados: List[ErrorItem] = Field(
        default_factory=list,
        description="Errores o debilidades detectadas en la producción"
    )

    version_mejorada: str = Field(
        description="Versión corregida y más natural del texto o discurso"
    )

    version_c2: str = Field(
        description="Versión elevada a nivel C2"
    )

    frases_clave_para_memorizar: List[str] = Field(
        min_items=2,
        max_items=5
    )

    foco_de_entrenamiento: str = Field(
        description="Qué debe entrenar prioritariamente esta semana"
    )

    ejercicio_recomendado: str = Field(
        description="Ejercicio concreto para reforzar el foco"
    )
