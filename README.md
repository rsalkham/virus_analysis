# virus_analysis
Null Hypothesis:
There is no relationship between the extent to which viruses spread in a certain country and its level of development.

Alternative Hypothesis:
Developed countries are more likely to have a less significant spread of viruses compared to developing countries.

Data Specification
Country:	The country whose developmental indices we are analyzing in relation to the spread of the virus	primary_key, float
gdp_year:	gross domestic product, market value of all the final goods and services produced in a year of the country	float
gdp_per_capita_year:	gross domestic product per capita, measure of a country's economic output that accounts for its number of people	float
population_year:	the number of people that live in that country per year as reported by census and WHO	float
rural_pop_year:	the number of people that live in rural areas of the country per year as reported by census and WHO	float
urban_pop_year:	the number of people that live in rural areas of the country per year as reported by census and WHO	float
pop_14_year:	Population of people between 0 and 14 years of age as a percentage of the total population	float
pop_15_64_year:	Population of people between 15 and 64 years of ageas a percentage of the total population	float
pop_65_year:	Population of people above 65 years as a percentage of the total population	float
pop_female_year:	Population of people who identify as female as a percentage of the total population	float
mortality_year:	The units of deaths per 1,000 individuals per year	float
life_expec_year:	Measure of the average time that people in live in these countries	float
surface_area:	A country's total area, including areas under inland bodies of water and some coastal waterways	float
internet_year:	The amount of internet servers in the country, we're using this to measure media penetration	float
H1N1 Cases:	The number of people who had the H1N1. Influenza A virus subtype H1N1 (A/H1N1) is the subtype of influenza A virus that was the most common cause of human influenza (flu) in 2009, and is associated with the 1918 outbreak known as the Spanish flu. It is an orthomyxovirus that contains the glycoproteins haemagglutinin and neuraminidase.	float
H1N1 Deaths:	The number of people who died from the H1N1	float
H1N1 Fatality Rate:	The rate of people who died as a cause of the disease, deaths divided by cases	float
covid19 Cases	COVID-19 is a strain of the coronaviruses, Coronaviruses are types of viruses that typically affect the respiratory tracts of birds and mammals, including humans	float
covid19 Deaths:	The number of people who died from covid-19	float
covid19 Fatality Rate:	The rate of people who died as a cause of the disease, deaths divided by cases	float
SARS Cases:	Severe Acute Respiratory Syndrome is strain of the coronavirus. SARS-CoV is thought to be an animal virus from an as-yet-uncertain animal reservoir that spread to other animals (civet cats) and humans	float
SARS Deaths:	The number of people who died from SARS	float
SARS Fatality Rate:	The rate of people who died as a cause of the disease, deaths divided by cases	float
Ebola Cases	Ebola: is a rare but deadly virus found in people and nonhuman primates	float
Ebola Deaths:	The number of people who died from SARS	float
Ebola Mortality Rate:	The rate of people who died as a cause of the disease, deaths divided by cases	float
