# st_fuzzy_match
Fuzzy matching, with a [Streamlit](https://streamlit.io/) frontend.

## Usage
Via the command line:
```
streamlit run st_fuzzy_match\st_fuzzy_match_setup.py
```

### Setting up custom component and running example
Adapted from [Streamlit components API docs](https://docs.streamlit.io/library/components/components-api):

In one terminal:
```
st_fuzzy_match\components\st_info_card\st_info_card\frontend
npm run start
```

In a second terminal:
```
pip install -e st_fuzzy_match\components\st_info_card
streamlit run st_fuzzy_match\components\st_info_card\st_info_card\example.py
```

NB: Can safely delete st_fuzzy_match\components\st_info_card\st_fuzzy_match.egg-info directory this creates.
