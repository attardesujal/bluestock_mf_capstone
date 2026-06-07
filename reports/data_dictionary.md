# Data Dictionary

## fund_master

| Column             | Description              |
| ------------------ | ------------------------ |
| amfi_code          | Unique AMFI scheme code  |
| fund_house         | Asset Management Company |
| scheme_name        | Mutual fund scheme name  |
| category           | Fund category            |
| sub_category       | Fund sub-category        |
| plan               | Direct/Regular plan      |
| launch_date        | Scheme launch date       |
| benchmark          | Benchmark index          |
| expense_ratio_pct  | Expense ratio percentage |
| exit_load_pct      | Exit load percentage     |
| min_sip_amount     | Minimum SIP amount       |
| min_lumpsum_amount | Minimum lump sum amount  |
| fund_manager       | Fund manager             |
| risk_category      | Risk classification      |
| sebi_category_code | SEBI category code       |

## nav_history

| Column    | Description     |
| --------- | --------------- |
| amfi_code | Scheme code     |
| nav_date  | NAV date        |
| nav       | Net Asset Value |

## investor_transactions

| Column             | Description                |
| ------------------ | -------------------------- |
| investor_id        | Unique investor identifier |
| transaction_date   | Transaction date           |
| amfi_code          | Scheme code                |
| transaction_type   | SIP / Lumpsum / Redemption |
| amount_inr         | Transaction amount         |
| state              | Investor state             |
| city               | Investor city              |
| city_tier          | Tier classification        |
| age_group          | Investor age group         |
| gender             | Investor gender            |
| annual_income_lakh | Annual income in lakhs     |
| payment_mode       | Payment channel            |
| kyc_status         | KYC verification status    |

## scheme_performance

| Column             | Description             |
| ------------------ | ----------------------- |
| return_1yr_pct     | 1-year return           |
| return_3yr_pct     | 3-year return           |
| return_5yr_pct     | 5-year return           |
| alpha              | Alpha metric            |
| beta               | Beta metric             |
| sharpe_ratio       | Sharpe ratio            |
| sortino_ratio      | Sortino ratio           |
| max_drawdown_pct   | Maximum drawdown        |
| aum_crore          | Assets Under Management |
| expense_ratio_pct  | Expense ratio           |
| morningstar_rating | Morningstar rating      |
| risk_grade         | Risk classification     |
