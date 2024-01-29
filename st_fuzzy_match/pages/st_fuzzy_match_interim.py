# %%
# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose
        'Interim' page of Streamlit fuzzy matching app
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

# %%
# SET PAGE CONFIG
st.set_page_config(
    page_title="Streamlit fuzzy match",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# %%
# SET UP PAGE NAVIGATION
if st.button("Back", type="secondary"):
    st.switch_page("pages/st_fuzzy_match_operate.py")
if st.button("Next", type="primary"):
    st.switch_page("pages/st_fuzzy_match_results.py")
