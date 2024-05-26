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

import pandas as pd
import streamlit as st

# SET PAGE CONFIG
st.set_page_config(
    page_title="Streamlit fuzzy match",
    layout="wide",
)

# LOAD DATASETS
# TODO
df_left = pd.DataFrame(
    {
        "A": ["foo", "bar", "baz", "qux"],
        "B": [1, 2, 3, 4],
    }
)
df_right = pd.DataFrame(
    {
        "C": ["foo", "bar", "baz", "qux"],
        "D": [1, 2, 3, 4],
    }
)

# DISPLAY MATCH OPTIONS
st.write("Match options")

# Match columns
match_column_df_left = st.selectbox(
    "Match column in left dataset",
    df_left.columns,
    key="selectbox_match_column_df_left",
)
match_column_df_right = st.selectbox(
    "Match column in right dataset",
    df_right.columns,
    key="selectbox_match_column_df_right",
)

# Display columns
display_columns_df_left_options = [c for c in df_left.columns if c != match_column_df_left]
display_columns_df_right_options = [c for c in df_right.columns if c != match_column_df_right]
display_columns_df_left = st.multiselect(
    "Display columns in left dataset",
    display_columns_df_left_options,
    key="multiselect_display_columns_df_left",
    help="Other columns to display during matching",
)
display_columns_df_right = st.multiselect(
    "Display columns in right dataset",
    display_columns_df_right_options,
    key="multiselect_display_columns_df_right",
    help="Other columns to display during matching",
)

# Score cutoff
score_cutoff = st.slider(
    "Score cutoff",
    min_value=0,
    max_value=100,
    value=90,
    key="slider_score_cutoff",
    help="""
        A value between 0 and 100 that determines how close a pair
        of items has to be to be considered a match
    """,
)

# Match limit
match_limit = st.number_input(
    "Match limit",
    value=3,
    key="number_input_match_limit",
    help="""The maximum number of matches to find for each record""",
)

# Advanced menu toggle
display_advanced_menu = st.toggle(
    "Show advanced options",
    False,
    key="toggle_display_advanced_menu",
)

with st.expander("Advanced options", expanded=display_advanced_menu):

    # Require unique matches
    require_unique_matches = st.checkbox(
        "Require unique matches",
        value=False,
        key="checkbox_require_unique_matches",
        help="""
            If checked, each item in the right dataset can only be matched
            to a single item in the left dataset
        """,
    )

    # Auto-accept 100% matches
    auto_accept_100_pct_matches = st.checkbox(
        "Auto-accept 100% matches",
        value=False,
        key="checkbox_auto_accept_100_pct_matches",
    )

    # Clean strings
    clean_strings = st.checkbox(
        "Clean strings",
        value=True,
        key="checkbox_clean_strings",
        help="""
            If checked, strings are converted to lowercase, non-alphanumeric characters are removed
            and whitespace is trimmed before looking for matches
        """,
    )

    # Drop columns
    drop_columns_options = [
        "None",
        "Left",
        "Right",
        "Both",
        "Match"
    ]
    drop_columns = st.selectbox(
        "Drop columns",
        drop_columns_options,
        index=0,
        key="selectbox_drop_columns",
        help="""
            Which columns to drop in the output dataframe. Behaviour is as follows:
                - None: Drop match_string
                - left: Drop columns from df_left and match_string
                - right: Drop columns from df_right and match_string
                - both: Drop columns from both df_left and df_right and
                match_string
                - match: Drop match_string, match_score
        """,
    )

# DISPLAY NUMBER OF RECORDS
st.metric(
    "Records in left dataset",
    df_left.shape[0],
)
st.metric(
    "Records in right dataset",
    df_right.shape[0],
)

# PAGE NAVIGATION
if st.button("Next", type="primary"):
    st.switch_page("pages/st_fuzzy_match_operate.py")
