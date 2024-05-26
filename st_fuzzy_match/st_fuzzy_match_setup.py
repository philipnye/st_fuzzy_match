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

# Matches
if 'match_column_count' not in st.session_state:
    st.session_state['match_column_count'] = 1

match_type_options = ["Exact", "Date", "Fuzzy"]

for i in range(st.session_state['match_column_count']):

    # Columns
    st.selectbox(
        "Match column in left dataset",
        df_left.columns,
        key="selectbox_match_column_df_left_" + str(i),
    )
    st.selectbox(
        "Match column in right dataset",
        df_right.columns,
        key="selectbox_match_column_df_right_" + str(i),
    )

    # Match type
    st.selectbox(
        "Match type",
        options=match_type_options,
        key="selectbox_match_type_" + str(i),
    )

    # New match button
    st.button(
        key="button_add_new_match_columns_" + str(i),
        label="Add further match columns",
        type="primary",
        on_click=lambda i=i: st.session_state.update(
            match_column_count=st.session_state['match_column_count'] + 1
        ),
    )

# Collate match columns
match_columns_df_left = [
    st.session_state["selectbox_match_column_df_left_" + str(i)]
    for i in range(st.session_state['match_column_count'])
]
match_columns_df_right = [
    st.session_state["selectbox_match_column_df_right_" + str(i)]
    for i in range(st.session_state['match_column_count'])
]

# Display columns
display_columns_df_left_options = [c for c in df_left.columns if c not in match_columns_df_left]
display_columns_df_right_options = [c for c in df_right.columns if c not in match_columns_df_right]

display_columns_df_left = st.multiselect(
    "Display columns in left dataset",
    display_columns_df_left_options,
    key="multiselect_display_columns_df_left",
    help="Other columns to display during matching",
)
if len(display_columns_df_left_options) == 0:
    st.caption("""
        All columns in left dataset are being used in matching and will be displayed
        during matching
    """)

display_columns_df_right = st.multiselect(
    "Display columns in right dataset",
    display_columns_df_right_options,
    key="multiselect_display_columns_df_right",
    help="Other columns to display during matching",
)
if len(display_columns_df_right_options) == 0:
    st.caption("""
        All columns in right dataset are being used in matching and will be displayed
        during matching
    """)

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

with st.expander("Advanced options"):

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
