import streamlit as st
import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Very basic dream symbol dictionary
dream_dictionary = {
  {
  "snake": "represents hidden fears, transformation, or betrayal",
  "flying": "symbolizes freedom, ambition, or escape from limitations",
  "water": "often tied to emotions, the subconscious, or a cleansing process",
  "fire": "symbolizes passion, anger, destruction, or purification",
  "teeth falling out": "linked to anxiety, loss, self-image, or fear of aging",
  "falling": "represents insecurity, loss of control, or fear of failure",
  "chasing": "often reflects avoidance, fear, or running from a problem",
  "death": "symbolizes transformation, endings, or a new beginning",
  "baby": "represents new beginnings, vulnerability, or responsibility",
  "being naked in public": "relates to vulnerability, shame, or exposure",
  "house": "represents the self or mind; rooms reflect different aspects of life",
  "car": "symbolizes direction in life, control, or motivation",
  "mirror": "reflects self-awareness, identity, or perception",
  "spider": "can represent creativity, manipulation, or feeling trapped",
  "school": "relates to learning, anxiety about performance, or past experiences",
  "money": "symbolizes self-worth, success, or fear of loss",
  "lost": "reflects confusion, lack of direction, or insecurity",
  "wedding": "can represent union, transition, or commitment",
  "stairs": "symbolize progress, growth, or personal development",
  "time": "often reflects pressure, fear of missing out, or urgency"
}

    
}

# Streamlit UI
st.title("Dream Analyzer")
st.write("Describe your dream, and I'll try to interpret the symbols in it.")

# Text input
dream_text = st.text_area("Describe your dream here")

if st.button("Analyze"):
    if dream_text:
        doc = nlp(dream_text.lower())
        tokens = {token.text for token in doc if token.is_alpha}

        matched_symbols = tokens.intersection(dream_dictionary.keys())

        if matched_symbols:
            st.subheader("Dream Symbols Found:")
            for symbol in matched_symbols:
                st.markdown(f"**{symbol.capitalize()}**: {dream_dictionary[symbol]}")
        else:
            st.info("No known symbols found, try describing more elements or emotions.")

    else:
        st.warning("Please describe your dream first.")
