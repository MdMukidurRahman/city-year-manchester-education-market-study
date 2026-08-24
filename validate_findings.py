"""Reproduce the headline City Year Manchester benchmark findings."""

from pathlib import Path
import pandas as pd

DATA = Path(__file__).parent / "data" / "district_comparison.csv"
df = pd.read_csv(DATA)
focus = df[
    (df["Year"].isin([2022, 2024]))
    & (df["District"].isin(["Manchester", "New Hampshire"]))
]

wide = focus.pivot_table(
    index=["Year", "Subject"],
    columns="District",
    values="Proficiency %",
    aggfunc="first",
)

for subject in ["Mathematics", "Reading", "Science"]:
    manchester_2024 = wide.loc[(2024, subject), "Manchester"]
    state_2024 = wide.loc[(2024, subject), "New Hampshire"]
    manchester_2022 = wide.loc[(2022, subject), "Manchester"]
    print(
        f"{subject}: 2024 Manchester {manchester_2024:.0f}% | "
        f"NH {state_2024:.0f}% | gap {manchester_2024-state_2024:.0f} pp | "
        f"Manchester change since 2022 {manchester_2024-manchester_2022:+.0f} pp"
    )
