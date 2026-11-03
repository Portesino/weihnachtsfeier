# Anmeldung zur Weihnachtsfeier

Eine kleine Streamlit-App zur Anmeldung von Familien. Sie speichert den Namen
eines Elternteils sowie die Anzahl der Erwachsenen und Kinder in Supabase und
zeigt anschließend die Gesamtzahlen an.

## Supabase einrichten

1. Erstelle ein Projekt in Supabase.
2. Öffne den SQL Editor und führe [`supabase/schema.sql`](supabase/schema.sql)
   aus.
3. Kopiere die Projekt-URL und den `anon`-/Publishable-Key aus den
   Projekteinstellungen. Verwende **nicht** den `service_role`-Key.

Die Tabelle erlaubt über Row Level Security nur neue Anmeldungen. Die App kann
Anmeldedaten nicht auflisten oder lesen; die Besucherzahlen werden ausschließlich
über eine Datenbankfunktion aggregiert zurückgegeben.

## Lokal starten

Voraussetzung ist Python 3.10 oder neuer.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export SUPABASE_URL="https://your-project.supabase.co"
export SUPABASE_ANON_KEY="your-supabase-anon-key"
streamlit run app.py
```

Unter Windows PowerShell lassen sich die Umgebungsvariablen so setzen:

```powershell
$env:SUPABASE_URL = "https://your-project.supabase.co"
$env:SUPABASE_ANON_KEY = "your-supabase-anon-key"
streamlit run app.py
```

Für ein Hosting (z. B. Streamlit Community Cloud) müssen `SUPABASE_URL` und
`SUPABASE_ANON_KEY` als Umgebungsvariablen in den App-Einstellungen hinterlegt
werden.
