# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose
        'Setup' page of Streamlit fuzzy matching app
    Inputs
        None
    Outputs
        None
    Parameters
        None
    Notes
        None
'''

import streamlit as st
import streamlit.components.v1 as components

# SET PAGE CONFIG
st.set_page_config(
    page_title="Streamlit fuzzy match",
    layout="wide",
)

# SET UP PAGE NAVIGATION
if st.button("Next", type="primary"):
    st.switch_page("pages/st_fuzzy_match_operate.py")

# DISPLAY PAGE CONTENT
col1, col2 = st.columns(2)

with open("st_fuzzy_match/components/card/card.html", "r") as fh:
    card_html = fh.read()

with col1:
    components.html(
        card_html,
        height=600,
    )

with col2:
    components.html(
        card_html,
        height=600,
    )
