import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Pioggia di Pi Greco!", page_icon="🌧️", layout="centered")

st.title("🌧️ Stimare il Pi Greco con la pioggia!")
st.markdown("""
Immagina un bersaglio quadrato con un cerchio disegnato all'interno.
Se lasciamo cadere delle gocce di vernice in modo del tutto casuale, contando quante 
finiscono dentro il cerchio rispetto a quelle totali, possiamo calcolare un numero magico: **Il Pi Greco ($$\pi$$)!**
""")

# --- GESTIONE DELLO STATO (Memoria) ---
# Usiamo st.session_state per ricordare i punti lanciati tra un click e l'altro
if 'inside' not in st.session_state:
    st.session_state.inside = 0
if 'total' not in st.session_state:
    st.session_state.total = 0
if 'x_inside' not in st.session_state:
    st.session_state.x_inside = []
if 'y_inside' not in st.session_state:
    st.session_state.y_inside = []
if 'x_outside' not in st.session_state:
    st.session_state.x_outside = []
if 'y_outside' not in st.session_state:
    st.session_state.y_outside = []

# --- INTERFACCIA UTENTE ---
col1, col2 = st.columns([2, 1])

with col1:
    drops_to_add = st.slider("Quante gocce vuoi lanciare?", min_value=10, max_value=5000, value=500, step=10)

with col2:
    st.write("") # Spazio vuoto per allineare il bottone
    st.write("")
    if st.button("💧 Lancia le gocce!", use_container_width=True):
        # Generiamo coordinate X e Y casuali tra -1 e 1
        x = np.random.uniform(-1, 1, drops_to_add)
        y = np.random.uniform(-1, 1, drops_to_add)
        
        # Calcoliamo la distanza dal centro (Teorema di Pitagora: x^2 + y^2)
        distances = x**2 + y**2
        
        # È dentro il cerchio se la distanza è <= 1 (raggio del cerchio)
        is_inside = distances <= 1
        
        # Aggiorniamo la memoria
        st.session_state.total += drops_to_add
        st.session_state.inside += np.sum(is_inside)
        
        # Salviamo le coordinate per il grafico
        st.session_state.x_inside.extend(x[is_inside])
        st.session_state.y_inside.extend(y[is_inside])
        st.session_state.x_outside.extend(x[~is_inside])
        st.session_state.y_outside.extend(y[~is_inside])

# --- CALCOLO DEL PI GRECO ---
# La formula del metodo Monte Carlo è: Pi = 4 * (Punti nel Cerchio / Punti Totali)
if st.session_state.total > 0:
    pi_estimate = 4 * st.session_state.inside / st.session_state.total
else:
    pi_estimate = 0.0

# Mostriamo i risultati in grande
st.metric(label="🌟 Valore stimato di Pi Greco", value=f"{pi_estimate:.5f}", delta=f"Errore: {abs(np.pi - pi_estimate):.5f}" if st.session_state.total > 0 else None, delta_color="inverse")

c1, c2 = st.columns(2)
c1.info(f"💦 Gocce nel cerchio: **{st.session_state.inside}**")
c2.info(f"🎯 Gocce totali lanciate: **{st.session_state.total}**")

# --- GRAFICO ---
if st.session_state.total > 0:
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Disegniamo i punti fuori (rossi) e dentro (blu)
    ax.scatter(st.session_state.x_outside, st.session_state.y_outside, color='#FF4B4B', s=2, alpha=0.6, label='Fuori')
    ax.scatter(st.session_state.x_inside, st.session_state.y_inside, color='#0068C9', s=2, alpha=0.6, label='Dentro')
    
    # Disegniamo il perimetro del cerchio
    circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2)
    ax.add_patch(circle)
    
    # Impostazioni asse per mantenere le proporzioni 1:1 (quadrato)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off') # Nascondiamo gli assi perché non servono ai bambini
    
    st.pyplot(fig)

# Bottone per resettare l'esperimento
st.markdown("---")
if st.button("🧹 Asciuga tutto (Ricomincia)"):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()