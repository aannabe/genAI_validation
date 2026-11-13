# Annual Operations Review 2024

**Prepared by:** Operations
**Distribution:** Leadership team
**Period covered:** January 1 - December 31, 2024

---

## 1. Executive Summary
2024 was the first full year of operating under the streamlined structure adopted during the 2022-2023 restructuring. Operations focused on platform reliability, vendor consolidation, and reducing manual work in customer onboarding. This review summarises performance across infrastructure, customer support, security, finance operations, facilities, and people operations.

## 2. Infrastructure and Platform Reliability
The platform ran on a single primary cloud region throughout the year. Average monthly availability across all eight products was 99.94%. There were two unplanned incidents of note: a database connection pool exhaustion in February that affected Carllm quoting for 41 minutes, and a certificate expiry in August that briefly affected the Markellm marketplace login page. Both incidents were followed by post-incident reviews and corrective actions.

Capacity planning was reviewed quarterly. Compute usage grew 18% year over year, driven primarily by Claimllm document processing and Healthllm analytics workloads. Storage growth was 22%, in line with forecast.

## 3. Deployment Practices
The engineering team averaged 14 production deployments per week. Rollbacks were required in 3% of deployments, down from 5% in 2023. A change freeze was observed from December 20 through January 2. Feature flags are now used for all customer-visible changes in Carllm and Homellm.

## 4. Monitoring and Alerting
Alert noise was reduced by consolidating duplicate alert rules. On-call rotations were shortened from two weeks to one week. Median time to acknowledge a page was 4 minutes; median time to resolve a critical page was 52 minutes.

## 5. Customer Onboarding
Average onboarding time for new customers fell from 9.1 weeks to 6.8 weeks, helped by standardised integration templates. Rellm remained the longest onboarding at an average of 11 weeks because of treaty data migration. Onboarding satisfaction, measured by an end-of-project survey, averaged 4.4 out of 5.

## 6. Customer Support
Support handled 3,870 tickets in 2024. First response targets were met on 96% of tickets. The most common ticket categories were integration questions (31%), user access (22%), and report configuration (17%). A knowledge article program launched in the third quarter reduced repeat questions about report configuration by roughly a quarter.

## 7. Claims Processing Operations
Claimllm customers submitted 2.1 million claim documents for processing during the year. Straight-through processing rates improved from 61% to 68% following updates to the document classification models. The average time for a customer to retrieve a processed claim package fell from 6.5 minutes to 3.2 minutes.

## 8. Resilience and Disaster Recovery
Disaster recovery exercises were conducted in March and September. In the September exercise, the team relocated the standby environment and validated recovery of all eight products. As a result of that exercise, the disaster recovery standby site was moved from the Ohio region to the Oregon region effective September 17, 2024, to reduce recovery latency for West Coast customers. Recovery time for the full platform was demonstrated at 3 hours 10 minutes, against a target of 4 hours. Recovery point objective remained at 15 minutes.

## 9. Data Management
Data retention schedules were reviewed with Legal. Customer data is retained for the duration of the contract plus 90 days, after which it is deleted or returned. Backups are encrypted and retained for 35 days. A data catalogue was introduced to document the ownership of each major dataset.

## 10. Finance Operations
Invoicing was fully automated for monthly subscription contracts in the second quarter. Days sales outstanding averaged 34 days, compared with 41 days in 2023. Month-end close was reduced from 8 business days to 5. The audit of 2023 financial statements was completed without material findings.

## 11. Vendor Management
At the start of 2024 the company worked with 47 software and service vendors. Over the year the team consolidated overlapping tools in analytics, documentation, and customer communications. The vendor count fell to 36. Total annual savings from the consolidation were $412,000, most of which came from retiring duplicate analytics licenses. Contract renewals are now tracked in a central register reviewed monthly.

## 12. Facilities
The Austin and Chicago offices renewed their leases on shorter terms. The San Francisco headquarters reduced its footprint by one floor. Denver continued with a flexible co-working arrangement. Total facilities cost declined 12% from 2023.

## 13. Security Operations
No customer data breaches were recorded in 2024. The Security team handled 212 reported phishing attempts, of which 9 resulted in credential entry; all affected credentials were reset within one hour. External penetration testing was completed in May with no critical findings and four medium findings, all remediated by July.

Security awareness training was assigned to all employees in the third quarter. Completion across the company reached 96.4%, and the remaining employees completed the training in the following month. Phishing simulation click rates fell from 11% to 6%.

## 14. People Operations
Headcount ended the year at 32. Voluntary turnover was 6%. The recruiting team filled four roles in the year, with an average time to fill of 47 days. Employee engagement survey participation was 91%, and the overall engagement score was 4.1 out of 5. Learning budgets were increased to $2,000 per employee.

## 15. Compliance
SOC 2 Type II reporting continued without exceptions. Policy documents were reviewed and re-issued where required. Privacy impact assessments were completed for two new Healthllm analytics features.

## 16. Priorities for 2025
- Continue reducing onboarding time, with a target of 6 weeks.
- Expand automated testing for the integration templates.
- Introduce a unified customer health dashboard for account management.
- Complete the review of all customer-facing service level documents.
- Maintain vendor count at or below 36.
