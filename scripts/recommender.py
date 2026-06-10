import pandas as pd

performance = pd.read_csv(
    "../data/raw/07_scheme_performance.csv"
)

def recommend_funds(risk_level):

    if risk_level == "Low":

        funds = performance[
            performance["risk_grade"] == "Low"
        ]

    elif risk_level == "Moderate":

        funds = performance[
            performance["risk_grade"] == "Moderate"
        ]

    else:

        funds = performance[
            performance["risk_grade"].isin(
                ["High", "Very High"]
            )
        ]

    funds = funds.sort_values(
        "sharpe_ratio",
        ascending=False
    )

    return funds[
        [
            "scheme_name",
            "risk_grade",
            "return_5yr_pct",
            "sharpe_ratio"
        ]
    ].head(5)

print(recommend_funds("Moderate"))