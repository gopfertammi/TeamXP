
# Team Experience Calculator (Hattrick)

Ein kleines Gradio-Webtool zur Berechnung der Team‑Experience (TeamXP) nach der optimierten Formel.

## Lokale Ausführung

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Deployment auf Vercel (empfohlen als **Static Export**)

1. **Repository erstellen** – z. B. `teamxp-calculator` bei GitHub.
2. Dateien (`app.py`, `requirements.txt`, `vercel.json`) committen & pushen.
3. **Vercel Dashboard → New Project → Import Git Repository**  
   - Framework = **Other**  
   - Build Command:  
     ```bash
     pip install -r requirements.txt && python -m pip install gradio && gradio export app.py --path dist
     ```  
   - Output Directory: `dist`
4. Deploy klicken. Vercel baut das statische Gradio-Frontend unter `/dist` und hostet es sofort.

*(Alternativ kannst du `vercel.json` anpassen, um `@vercel/static-build` zu nutzen. Die obigen Schritte sind der schnellste Weg.)*

Weitere Details findest du im Wiki-Tab dieses Repos.
