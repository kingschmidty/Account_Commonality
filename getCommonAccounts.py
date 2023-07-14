import pandas as pd
import numpy as np



root_dir = './Datasets/'


account_of_interest = '7BZEUIEPHZGDK6E673DVOY6BVCCZC6YFAJ3QWROPBZK5XKGE5GUWDYZRUY'
interest_name = root_dir + 'flows-' + account_of_interest + '.csv'

interest_df = pd.read_csv(interest_name)

print(interest_df)

binance_6 = 'YNH3E6RUOK7HAXBB4ZYBVASZEP2B7ZUN7XBMYHSFB2ZHWFYOE4OYJTZSTQ'
binance_name = root_dir + 'flows-' + binance_6 + '.csv'

binance_df = pd.read_csv(binance_name)

print(binance_df)

all_df = pd.merge(interest_df, binance_df, on=['Address'], how='left', indicator='exists')

print(all_df)

#all_df['exists'] = np.where(all_df.exists == 'both', True, False)

print(all_df)

print(all_df[all_df['exists'].str.contains('both')])


all_df[all_df['exists'].str.contains('both')].to_csv('common_accounts_' + account_of_interest + '.csv')