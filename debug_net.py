import pandas as pd

summary_file = "HR Cleaned Data 01.09.26.xlsx"
selected_year = 2020

official_net_change = None
try:
    summary_df = pd.read_excel(summary_file, sheet_name="Summary")
    print("Summary df columns:", summary_df.columns)
    print("Summary df head:", summary_df.head())
    # Normalize Year dtype to int for robust matching
    if "Year" in summary_df.columns:
        summary_df["Year"] = pd.to_datetime(summary_df["Year"], errors="coerce").dt.year.fillna(summary_df["Year"])
    # Build mapping Year -> Net Change (column H)
    if "Net Change" in summary_df.columns:
        year_to_net = (
            summary_df[["Year", "Net Change"]]
            .dropna(subset=["Year"])
            .drop_duplicates(subset=["Year"], keep="last")
            .set_index("Year")["Net Change"]
            .to_dict()
        )
        print("year_to_net:", year_to_net)
        official_net_change = year_to_net.get(selected_year, None)
        print("official_net_change for", selected_year, ":", official_net_change)
except Exception as e:
    print("Exception:", e)
    official_net_change = None

print("Final official_net_change:", official_net_change)