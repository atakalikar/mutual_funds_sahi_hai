initial_corpus = 1500000
current_age = 35
current_year = 2024
target_ages = [45, 48, 50]
target_corpuses = [30000000, 50000000, 80000000]

# The output would be a bunch of CSV files
# 10%, 12.5%, 15% ROI
rois = [0.1, 0.125, 0.15]

# 0% increase in SIP is steady SIP.
# in every other CSV file, for given ROIs an increase of 5%, 7.5% and 10%
# would be considered in increase in SIP.
# increase year over years (iyoys)
iyoys = [0, 0.05, 0.075, 0.1]

current_corpus = initial_corpus

# formula
# next_year_corpus = roi*last_corpus + invested that year * roi + invested that year + last_corpus
# invested next year increases by iyoy
import pandas as pd
cols = ['initial_corpus', 'age', 'target', 'XIRR', 'YoY_Increase_in_SIP', 'starting_investment_next_year', 'starting_target_sip_per_month']
df = pd.DataFrame(columns=cols)

first_year_investment = {}
index = 1
for age in target_ages:
    first_year_investment[age] = {}
    for target in  target_corpuses:
        first_year_investment[age][target] = {}
        for roi in rois:
            first_year_investment[age][target][roi] = {}
            for increase in iyoys:
                index = index + 1
                averaged_yearly_investment = target/(age - current_age)
                sum_to_grow = averaged_yearly_investment - (initial_corpus * (1+roi))
                first_year_investment[age][target][roi][increase] = round(sum_to_grow/(1+roi+increase),2)
                SIP_per_month_starting_next_year = round(sum_to_grow/(1+roi+increase)/12,2)
                print("By the age " + str(age) + " Target " + str(target) + " ROI " + str(roi*100) + "%, increase in SIP YoY " + str(increase * 100) + " investment per year starting 2025 is :- " + str(first_year_investment[age][target][roi][increase]) + " Rupees")
                print("SIP starting next year :- " + str(SIP_per_month_starting_next_year) + " rupees every month")
                df.loc[index] = [initial_corpus, age, target, roi, increase,first_year_investment[age][target][roi][increase], SIP_per_month_starting_next_year]
print(df)
df.to_csv("investment_strategy.csv", index=False)
