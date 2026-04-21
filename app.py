"""
app.py — Entry point for the Moroccan Music Classifier Streamlit app.

Run with:
    streamlit run app.py
"""

import streamlit as st

from explore import show_explore
from predict import show_predict_page
from utils import load_logo

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="Moroccan Music Classifier",
    page_icon="🎵",
    layout="centered",
)

# ---------------------------------------------------------------------------
# Theme definitions
# ---------------------------------------------------------------------------

THEMES = {
    "🌙 Dark": {
        "--color-bg":       "#0f0f0f",
        "--color-surface":  "rgba(20, 20, 20, 0.85)",
        "--color-accent":   "#7c9fff",
        "--color-text":     "#f0f0f0",
        "--color-muted":    "#888888",
        "--color-sidebar":  "rgba(10, 10, 10, 0.92)",
        "--color-btn-from": "#3a3a3a",
        "--color-btn-to":   "#5a5a5a",
        "--color-border":   "rgba(255,255,255,0.08)",
    },
    "☀️ Light": {
        "--color-bg":       "#f4f0eb",
        "--color-surface":  "rgba(255, 252, 248, 0.92)",
        "--color-accent":   "#2563eb",
        "--color-text":     "#1a1a1a",
        "--color-muted":    "#666666",
        "--color-sidebar":  "rgba(235, 230, 224, 0.97)",
        "--color-btn-from": "#2563eb",
        "--color-btn-to":   "#60a5fa",
        "--color-border":   "rgba(0,0,0,0.08)",
    },
    "🇲🇦 Moroccan": {
        "--color-bg":       "#1a0800",
        "--color-surface":  "rgba(20, 10, 5, 0.78)",
        "--color-accent":   "#e67e22",
        "--color-text":     "#f5ede4",
        "--color-muted":    "#b0a090",
        "--color-sidebar":  "rgba(12, 5, 2, 0.92)",
        "--color-btn-from": "#c0392b",
        "--color-btn-to":   "#e67e22",
        "--color-border":   "rgba(255,255,255,0.08)",
    },
}

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

logo = load_logo("assets/img/logo.jpg", width=150, height=150)
st.sidebar.image(logo, use_column_width=False, output_format="JPEG")
st.sidebar.title("MMC")

page = st.sidebar.radio("Navigate", ["Explore", "Predict"])

st.sidebar.divider()

selected_theme = st.sidebar.radio("🎨 Theme", list(THEMES.keys()), index=2)
theme_vars = THEMES[selected_theme]

# ---------------------------------------------------------------------------
# Inject CSS — dynamic theme variables + base stylesheet
# ---------------------------------------------------------------------------

css_vars = "\n".join(f"  {k}: {v};" for k, v in theme_vars.items())
theme_css = f":root {{\n{css_vars}\n}}"

with open("assets/css/style.css") as f:
    base_css = f.read()

st.markdown(f"<style>{theme_css}\n{base_css}</style>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Routing
# ---------------------------------------------------------------------------

if page == "Predict":
    show_predict_page()
else:
    show_explore()