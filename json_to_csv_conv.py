import pandas as pd
df = pd.read_json ('profile_data.json')
df.to_csv ('profile_data.csv', sep=',')