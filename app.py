import streamlit as st
import pandas as pd
from supabase import create_client

st.write("App gestartet")
st.stop()
# --------------------------------------------------
# Seiteneinstellungen
# --------------------------------------------------

st.set_page_config(
    page_title="Weihnachtsfeier",
    page_icon="🎄",
    layout="wide"
)

# --------------------------------------------------
# Supabase Verbindung
# --------------------------------------------------

supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

# --------------------------------------------------
# Titel
# --------------------------------------------------

st.title("🎄 Weihnachtsfeier 2026")

st.write(
    "Bitte meldet euch für unsere Weihnachtsfeier an."
)

# --------------------------------------------------
# Formular
# --------------------------------------------------

with st.form("weihnachtsfeier_form"):

    st.subheader("Anmeldung")

    name = st.text_input(
        "Name/Familie"
    )

    teilnahme = st.radio(
        "Nehmt ihr teil?",
        [
            "Ja",
            "Nein"
        ]
    )

    erwachsene = st.number_input(
        "Anzahl Erwachsene",
        min_value=0,
        value=2
    )

    kinder = st.number_input(
        "Anzahl Kinder",
        min_value=0,
        value=0
    )

    vegetarisch = st.checkbox(
        "Vegetarisches Essen"
    )

    kuchen_spende = st.checkbox(
        "Wir bringen Kuchen oder Salat mit"
    )

    bemerkung = st.text_area(
        "Bemerkungen"
    )

    submit = st.form_submit_button(
        "Anmeldung absenden"
    )

# --------------------------------------------------
# Daten speichern
# --------------------------------------------------

if submit:

    if not name.strip():

        st.error("Bitte einen Namen eingeben.")

    else:

        response = (
            supabase
            .table("anmeldungen")
            .insert({
                "name": name,
                "teilnahme": teilnahme == "Ja",
                "erwachsene": erwachsene,
                "kinder": kinder,
                "vegetarisch": vegetarisch,
                "kuchen_spende": kuchen_spende,
                "bemerkung": bemerkung
            })
            .execute()
        )

        st.success(
            "Vielen Dank für eure Rückmeldung."
        )

st.divider()

with st.expander("🔐 Adminbereich"):

    passwort = st.text_input(
        "Passwort",
        type="password"
    )

    if passwort == st.secrets["ADMIN_PASSWORT"]:

        result = (
            supabase
            .table("anmeldungen")
            .select("*")
            .execute()
        )

        daten = pd.DataFrame(result.data)

        if not daten.empty:

            zusagen = daten[
                daten["teilnahme"] == True
            ]

            anmeldungen = len(zusagen)

            erwachsene_gesamt = (
                zusagen["erwachsene"].sum()
            )

            kinder_gesamt = (
                zusagen["kinder"].sum()
            )

            personen_gesamt = (
                erwachsene_gesamt
                + kinder_gesamt
            )

            c1, c2, c3, c4 = st.columns(4)

            c1.metric(
                "Anmeldungen",
                anmeldungen
            )

            c2.metric(
                "Erwachsene",
                int(erwachsene_gesamt)
            )

            c3.metric(
                "Kinder",
                int(kinder_gesamt)
            )

            c4.metric(
                "Gesamt",
                int(personen_gesamt)
            )

            st.subheader("Alle Rückmeldungen")

            st.dataframe(
                daten,
                use_container_width=True
            )

            csv = (
                daten
                .to_csv(index=False)
                .encode("utf-8")
            )

            st.download_button(
                "CSV Export",
                data=csv,
                file_name="weihnachtsfeier.csv",
                mime="text/csv"
            )

        else:

            st.info(
                "Noch keine Anmeldungen vorhanden."
            )