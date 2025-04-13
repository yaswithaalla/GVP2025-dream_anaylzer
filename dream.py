import streamlit as st
import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Very basic dream symbol dictionary
dream_dictionary = {
    "flying": "You may be feeling liberated or escaping from something in life.",
    "water": "Often relates to emotions, the unconscious mind, or cleansing.",
    "whale": "Represents deep emotions or a significant emotional message.",
    "falling": "Might reflect insecurity, instability, or fear of failure.",
    "snake": "Symbol of transformation, danger, or hidden fears.",
    "death": "Usually not literal — could mean endings or big life transitions.",
    "ocean": "Represents deep emotion, vastness, or exploration of the unconscious."
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
