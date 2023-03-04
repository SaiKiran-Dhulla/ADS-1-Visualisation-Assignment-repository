'''
Applied Data Science - 1 Assignment programming.

Sai Kiran Dhulla
22026785

First Data link:
https://www.kaggle.com/code/kerneler/starter-stock-price-data-31aa7f74-0/data

Second Data link:
https://www.kaggle.com/datasets/rajanand/suicides-in-india
'''
#Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt


def company_stock_records(data, company_symbol):
    '''
    'company_stock_records' function will create a new DataFrame with records 
    of particular company of given 'company_symbol' from the given data.

    Parameters
    ---------- 
    data : pandas.DataFrame
        Main DataFrame from where we access data.
    company_symbol : STR
        Specific company symbol from the data.

    Returns
    -------
    company_stock_data : pandas.DataFrame
        Company stock records.

    '''
    company_stock_data = data[(data['Symbol'] == company_symbol) &
                              (data['Series'] == 'EQ')][['Date',
                                                         'Average Price']]

    return company_stock_data


def removing_unwanted_states(data, list_of_states):
    '''
    'removing_unwanted_states' function will create a new DataFrame after 
    clearing records of states in list_of_states.

    Parameters
    ----------
    data : pandas.DataFrame
        Main DataFrame from where we access data.
    list_of_states : TYPE
        List of unwanted states of which the records to be removed.

    Returns
    -------
    data : pandas.DataFrame
        Data after removing records of unwanted states.

    '''
    for state in list_of_states:
        data = data[data['State'] != state]

    return data


def top_n(data, column, n):
    '''
    'top_n' function will sort 'data' over given 'column' and 
    returns top 'n' rows in ascending order.

    Parameters
    ----------
    data : pandas.DataFrame
        Main DataFrame from where we access data..
    column : STR
        Column name over which sorting to be done.
        Make sure the given column have numeric values
    n : INT
        Number of Top rows.

    Returns
    -------
    data : pandas.DataFrame
        Top N rows of data in ascending order.

    '''

    data = data.sort_values(column, ascending=True)
    data = data[-n:]

    return data


#Reading Indian stocks data
#Data gathered from given link
#https://www.kaggle.com/code/kerneler/starter-stock-price-data-31aa7f74-0/data
stocks_ind = pd.read_csv('Stock Price Data.csv')
print(stocks_ind.head())

#Company shortforms in the main Dataset
print(set(stocks_ind['Symbol']))

#Creating seperate company datasets for each company stock records
bel = company_stock_records(stocks_ind, 'BEL')
tcs = company_stock_records(stocks_ind, 'TCS')
mindtree = company_stock_records(stocks_ind, 'MINDTREE')
lti = company_stock_records(stocks_ind, 'LTI')
ofss = company_stock_records(stocks_ind, 'OFSS')
t_mahindra = company_stock_records(stocks_ind, 'TECHM')
infosys = company_stock_records(stocks_ind, 'INFY')
mphasis = company_stock_records(stocks_ind, 'MPHASIS')
wipro = company_stock_records(stocks_ind, 'WIPRO')
ltts = company_stock_records(stocks_ind, 'LTTS')

print(bel.head())

#Plotting company wise average stock price from 05 Mar 2019 to 03 Mar 2021
plt.figure()
plt.plot(bel['Date'], bel['Average Price'], label='BEL')
plt.plot(tcs['Date'], tcs['Average Price'], label='TCS')
plt.plot(mindtree['Date'], mindtree['Average Price'], label='MINDTREE')
plt.plot(lti['Date'], lti['Average Price'], label='LTI')
plt.plot(ofss['Date'], ofss['Average Price'], label='OFSS')
plt.plot(t_mahindra['Date'], t_mahindra['Average Price'], label='TECHM')
plt.plot(infosys['Date'], infosys['Average Price'], label='INFY')
plt.plot(mphasis['Date'], mphasis['Average Price'], label='MPHASIS')
plt.plot(wipro['Date'], wipro['Average Price'], label='WIPRO')
plt.plot(ltts['Date'], ltts['Average Price'], label='LTTS')
plt.xlabel('Date')
plt.ylabel('Stock Price in INR')
plt.xticks(lti['Date'][::82])
plt.legend(title='Company', loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('Indian Stocks performance')
plt.savefig('Indian Stocks performance.png')
plt.show()


#Reading Suicides in India Data
#Data gathered from given link
#https://www.kaggle.com/datasets/rajanand/suicides-in-india
suicides_ind = pd.read_csv('Suicides in India 2001-2012.csv')

#Removing colliding data with Total named states
print(suicides_ind['State'].unique())
unwanted_states = ['Total (All India)', 'Total (States)', 'Total (Uts)']

#Calling function to remove unwanted states from data
suicides_ind = removing_unwanted_states(suicides_ind, unwanted_states)
print(suicides_ind['State'].unique())
#We can see now all states are original Indian states

#Plotting Suicide percent over age groups
suicides_age = suicides_ind.groupby('Age_group', as_index=False)['Total'].sum()
suicides_age_c = suicides_age[suicides_age['Age_group'] != '0-100+']

plt.figure()
plt.subplot(1, 2, 1)
plt.pie(suicides_age['Total'],
        labels=suicides_age['Age_group'], autopct='%.2f%%')
plt.subplot(1, 2, 2)
plt.pie(suicides_age_c['Total'],
        labels=suicides_age_c['Age_group'], autopct='%.2f%%')
plt.suptitle('Suicides % over Age groups')
plt.savefig('Suicides % over Age groups.png')
plt.show()


#Plotting Suicide percent over reasons
suicides_reasons = suicides_ind.groupby(
    'Type_code', as_index=False)['Total'].sum()
plot_labels = suicides_reasons['Type_code']

plt.figure()
plt.pie(suicides_reasons['Total'], labels=plot_labels, autopct='%.2f%%')
plt.title('%Reasons of Suicides')
plt.savefig('%Reasons of Suicides.png')
plt.show()


#Plotting top States in India with highest Suicides
suicides_state = suicides_ind.groupby('State', as_index=False)['Total'].sum()
suicides_state_10 = top_n(suicides_state, 'Total', 10)
print(suicides_state_10)

plt.figure()
bar = plt.barh(suicides_state_10['State'],
               suicides_state_10['Total'], align='center', color='m')
plt.bar_label(bar, label_type='center')
plt.title('Top 10 States with highest Suicides in India')
plt.savefig('Top 10 States with highest Suicides in India.png')
plt.show()
