# %%
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

# %%
# SET PAGE CONFIG
st.set_page_config(
    page_title="Streamlit fuzzy match",
    layout="wide",
)

# %%
# SET UP PAGE NAVIGATION
if st.button("Next", type="primary"):
    st.switch_page("pages/st_fuzzy_match_operate.py")
