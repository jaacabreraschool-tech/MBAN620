import streamlit as st
import pandas as pd


@st.cache_data
def normalize_raw_data(df_raw):
    """Normalize common columns across all tabs"""
    def to_num(x): 
        s = str(x).strip().upper() 
        if s in {"1", "YES", "TRUE"}: 
            return 1 
        if s in {"0", "NO", "FALSE"}: 
            return 0 
        try: 
            return float(s) 
        except: 
            return pd.NA 

    df = df_raw.copy()
    df["Promotion & Transfer"] = df["Promotion & Transfer"].apply(to_num)
    df["Calendar Year"] = pd.to_datetime(df["Calendar Year"], errors="coerce")
    df["Year"] = df["Calendar Year"].dt.year
    df["Resignee Checking"] = df["Resignee Checking"].astype(str).str.strip().str.upper()
    
    return df


@st.cache_data
def get_active_employees(df_normalized):
    """Filter for active employees only"""
    return df_normalized[df_normalized["Resignee Checking"] == "ACTIVE"]


@st.cache_data
def get_year_data(df_normalized, year):
    """Get data for a specific year"""
    return df_normalized[df_normalized["Year"] == int(year)]
