
import gradio as gr
import numpy as np

# ---------- Modellparameter ----------
A = 0.1487
p = 0.8579
B = 0.0478
C = 118.6
q = 1.26
# -------------------------------------

def calculate_team_experience(E, K, F):
    """Berechnet exakten & gerundeten TeamXP-Wert."""
    raw = E + K
    damp = 1 / (1 + (raw / C) ** q)
    TE = A * raw ** p * (1 + B * (F - 5) * damp)
    TE_rounded = np.floor(TE / 0.25) * 0.25
    return round(float(TE), 3), TE_rounded

with gr.Blocks(theme=gr.themes.Base(primary_hue="green")) as app:
    with gr.Column(elem_id="container", elem_classes="min-h-screen p-6 max-w-xl mx-auto"):
        gr.Markdown(
            """# 🧠 Team Experience Calculator
Berechnet **exakte** und **gerundete** TeamXP-Werte nach Hattrick-Modell."""
        )

        E = gr.Number(label="XP Players", value=120, elem_classes="w-full")
        K = gr.Number(label="XP Captain", value=12, elem_classes="w-full")
        F = gr.Number(label="Leadership Captain", value=5.50, step=0.01, elem_classes="w-full")

        with gr.Row():
            exact_output = gr.Number(label="Exakte TeamXP", interactive=False)
            rounded_output = gr.Number(label="Gerundete Anzeige", interactive=False)

        gr.Button("Berechnen").click(
            fn=calculate_team_experience,
            inputs=[E, K, F],
            outputs=[exact_output, rounded_output]
        )

# Für lokale Ausführung:
if __name__ == "__main__":
    app.launch()
