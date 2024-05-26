# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose
        'Operate' page of Streamlit fuzzy matching app
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

# SET PAGE CONFIG
st.set_page_config(
    page_title="Streamlit fuzzy match",
    layout="wide",
)


# SAVE WIDGET STATE TO SESSION STATE
# This enables widget state to be used in other app pages
# NB: Best solution as of May 2024
# Ref: https://discuss.streamlit.io/t/multi-page-apps-with-widget-state-preservation-the-simple-way/22303/2?       # noqa: E501
st.session_state.update(st.session_state)

# SET UP PAGE NAVIGATION
if st.button("Back", type="secondary"):
    st.switch_page("st_fuzzy_match_setup.py")
if st.button("Next", type="primary"):
    st.switch_page("pages/st_fuzzy_match_interim.py")
