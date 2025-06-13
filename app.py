import gradio as gr
import numpy as np

def calculate_team_experience(E, K, F_sub):
    # Erfahrungswerte anpassen
    E_adj = E - 11
    K_adj = K - 1
    F_base = 4  # da F später + sub kommt, und im Tool F-1 verwendet wird

    A = 0.1487
    p = 0.8579
    B = 0.0478
    C = 118.6
    q = 1.26

    raw = E_adj + K_adj

    def compute(F_sublevel):
        F = F_base + F_sublevel  # Führungswert inkl. Sublevel
        damp = 1 / (1 + (raw / C) ** q)
        TE = A * raw ** p * (1 + B * (F - 5) * damp)
        TE_rounded = np.floor(TE / 0.25) * 0.25
        return round(TE, 3), TE_rounded

    low, mid, high = compute(0.0), compute(0.5), compute(0.9)
    return {
        "LS Sub 0.0": f"{low[0]} (→ {low[1]})",
        "LS Sub 0.5": f"{mid[0]} (→ {mid[1]})",
        "LS Sub 0.9": f"{high[0]} (→ {high[1]})"
    }

with gr.Blocks(theme=gr.themes.Base(primary_hue="green")) as app:
    with gr.Column(elem_id="container", elem_classes="min-h-screen p-6 max-w-xl mx-auto", scale=1):
        gr.Markdown("""
        # 🧠 Team Experience Calculator
        Gib Erfahrungswerte ein – erhalte TeamXP für Sublevels 0.0, 0.5 und 0.9
        """)

        E = gr.Number(label="XP Players (sichtbar)", value=120, elem_classes="w-full")
        K = gr.Number(label="XP Captain (sichtbar)", value=12, elem_classes="w-full")
        F = gr.Number(label="Leadership Captain (sichtbar)", value=6.0, elem_classes="w-full")

        output_dict = gr.JSON(label="Ergebnisse für Sublevels")
        calc_btn = gr.Button("Berechnen")
        calc_btn.click(fn=calculate_team_experience, inputs=[E, K, F], outputs=output_dict)

app.launch()
