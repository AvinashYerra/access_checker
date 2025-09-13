# app.py
import streamlit as st
from checker import run_accessibility_check
import pandas as pd

st.set_page_config(page_title="Accessibility Checker", layout="wide")

st.title("Website Accessibility Checker")

url = st.text_input("Enter Website URL:", "https://example.com")

if st.button("Check Accessibility"):
    if not url.startswith('http'):
        st.error("Please enter a valid URL starting with http or https")
    else:
        with st.spinner('Running accessibility scan...'):
            issues = run_accessibility_check(url)

            if not issues:
                st.success("No accessibility issues found!")
            else:
                st.warning(f"Found {len(issues)} accessibility issues.")

                df = pd.DataFrame(issues)
                st.dataframe(df[['impact', 'description', 'help', 'selector', 'html']], use_container_width=True)

                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(" Download Report as CSV", data=csv, file_name='accessibility_report.csv')
