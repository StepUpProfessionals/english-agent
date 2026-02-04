# imports
import streamlit as st
import json
from pathlib import Path
# otros imports que ya tengas

# ⬇️ AQUÍ pegas el bloque nuevo (loader del JSON)
DATA_PATH = Path("data/vocab_general_cefr.json")

st.title("CEFR Vocab (MVP)")

if not DATA_PATH.exists():
    st.error(f"No encuentro el archivo: {DATA_PATH}")
    st.stop()

with DATA_PATH.open("r", encoding="utf-8") as f:
    data = json.load(f)

items = data.get("items", [])
st.success(f"JSON cargado ✅  Items: {len(items)}")

st.write("Primer item (preview):")
if items:
    st.json(items[0])
else:
    st.warning("No hay items aún en 'items'.")

# ⬇️ debajo de esto sigue TU código actual (sin tocarlo)
# ... lo que ya tenías antes


import json
from pathlib import Path
from datetime import datetime

import streamlit as st
from pydantic import ValidationError

from entrenador_c1_modelo import EntrenamientoC1


REPORTES_DIR = Path("reportes")
REPORTES_DIR.mkdir(exist_ok=True)


def guardar(prefix: str, data: dict) -> Path:
    ts = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    path = REPORTES_DIR / f"{prefix}_{ts}.json"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


st.set_page_config(page_title="English Agent – Writing Trainer", layout="centered")
st.title("English Agent – Writing Trainer (C1/C2)")
st.caption("Piloto privado: escribe, guarda, y pega feedback estructurado.")

tab1, tab2 = st.tabs(["Writing", "Pegar feedback (JSON)"])

with tab1:
    tema = st.text_input("Tema", "Why many adults understand written English but struggle with spoken English")
    objetivo = st.selectbox("Objetivo", ["C1", "C2"], index=0)
    texto = st.text_area("Tu texto (en inglés)", height=220)

    if st.button("Guardar writing", type="primary"):
        if not tema.strip():
            st.error("Falta el tema.")
        elif not texto.strip():
            st.error("Falta el texto.")
        else:
            path = guardar("writing", {"tema": tema.strip(), "objetivo": objetivo, "texto": texto.strip()})
            st.success(f"✅ Guardado en: {path.as_posix()}")

with tab2:
    st.write("Pega aquí el JSON de feedback (debe cumplir el esquema EntrenamientoC1).")
    feedback_json = st.text_area("JSON de feedback", height=260)

    if st.button("Validar y guardar feedback"):
        if not feedback_json.strip():
            st.error("Pega un JSON primero.")
        else:
            try:
                fb = EntrenamientoC1.model_validate_json(feedback_json)
            except ValidationError as e:
                st.error("❌ JSON inválido para EntrenamientoC1.")
                st.code(str(e))
            else:
                path = guardar("feedback", fb.model_dump())
                st.success(f"✅ Feedback guardado en: {path.as_posix()}")
