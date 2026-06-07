-- Q1 Top 10 funds by 5-Year Return

SELECT
    scheme_name,
    return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- Q2 Highest AUM Funds

SELECT
    scheme_name,
    aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 10;


-- Q3 Top SIP Receiving States

SELECT
    state,
    SUM(amount_inr) AS total_sip
FROM investor_transactions
WHERE transaction_type = 'SIP'
GROUP BY state
ORDER BY total_sip DESC;


-- Q4 Transaction Type Distribution

SELECT
    transaction_type,
    COUNT(*) AS transaction_count
FROM investor_transactions
GROUP BY transaction_type;


-- Q5 Average Investment by Age Group

SELECT
    age_group,
    AVG(amount_inr) AS avg_investment
FROM investor_transactions
GROUP BY age_group
ORDER BY avg_investment DESC;


-- Q6 Fund Count by Category

SELECT
    category,
    COUNT(*) AS fund_count
FROM fund_master
GROUP BY category;


-- Q7 Top Performing Fund Houses

SELECT
    fund_house,
    AVG(return_3yr_pct) AS avg_return
FROM scheme_performance
GROUP BY fund_house
ORDER BY avg_return DESC;


-- Q8 Risk Grade Distribution

SELECT
    risk_grade,
    COUNT(*) AS count_funds
FROM scheme_performance
GROUP BY risk_grade;


-- Q9 KYC Status Summary

SELECT
    kyc_status,
    COUNT(*) AS investors
FROM investor_transactions
GROUP BY kyc_status;


-- Q10 Highest Sharpe Ratio Funds

SELECT
    scheme_name,
    sharpe_ratio
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;