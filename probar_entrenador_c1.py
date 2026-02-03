from entrenador_c1_modelo import EntrenamientoC1

ejemplo = EntrenamientoC1(
    nivel_estimado="C1",
    errores_detectados=[
        {
            "tipo": "cohesión",
            "descripcion": "Uso limitado de conectores avanzados",
            "sugerencia": "Incorporar discourse markers como 'however', 'moreover', 'notwithstanding'"
        }
    ],
    version_mejorada="I believe that education plays a crucial role in shaping personal identity.",
    version_c2="Education constitutes a fundamental pillar in the construction of personal and professional identity.",
    frases_clave_para_memorizar=[
        "It could be argued that…",
        "From a broader perspective…",
        "This raises the question of whether…"
    ],
    foco_de_entrenamiento="Uso consciente de conectores y estructura argumentativa",
    ejercicio_recomendado="Reformular respuestas orales usando al menos 3 discourse markers por intervención"
)

print(ejemplo)
