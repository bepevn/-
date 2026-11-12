from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CHAIN : 잔광", page_icon="⛓️", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
.stApp {background:#060912;}
.block-container {padding:0;max-width:none;}
header[data-testid="stHeader"] {background:transparent;height:0;}
footer {display:none;}
iframe[title="st.iframe"] {height:100dvh!important;min-height:540px;}
[data-testid="stMainBlockContainer"]{padding:0!important;max-width:none!important;}
[data-testid="stVerticalBlock"]{gap:0;}
</style>""", unsafe_allow_html=True)
components.html(Path(__file__).with_name("game.html").read_text(encoding="utf-8"), height=820, scrolling=False)
