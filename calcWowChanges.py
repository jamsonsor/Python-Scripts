import pandas as pd
import numpy as np

fileName = input("Enter the first file name: ")
xl = pd.ExcelFile(fileName)

# start of the API Usage output script
df = xl.parse("Data")
df = df.sort_values(["Customer Name", "Date"])
# strips the timestamp from the datetime values
df['Date'] = pd.to_datetime(df['Date']).dt.date

# formula + condition where the first line of the customer name subset does not match the customer name above
df['WoW Query % Change'] = np.where(df['Customer Name'].shift(1) != df[('Customer Name')], 0, 
(df['Total # Of Queries'] - df['Total # Of Queries'].shift(1)) / df['Total # Of Queries'].shift(1) )

df['WoW QPS 95th % Change'] = np.where(df['Customer Name'].shift(1) != df[('Customer Name')], 0, 
(df['QPS 95th Percentile'] - df['QPS 95th Percentile'].shift(1)) /  df['QPS 95th Percentile'].shift(1) )
df = df.round(decimals=4)

# start writing to new Excel file
writer = pd.ExcelWriter('API_Usage_Output.xlsx')

df.to_excel(writer, sheet_name='API Usage Output', columns=["Customer Name","Date", 
"QPS 99th Percentile", "QPS 95th Percentile","QPS 75th Percentile", 
"QPS 50th Percentile", "QPS 25th Percentile", "Total # Of Queries", "WoW Query % Change", "WoW QPS 95th % Change"], index=False)

worksheet = writer.sheets['API Usage Output']

#Iterate through each column and set the width == the max length in that column. A padding length of 2 is also added.
for i, col in enumerate(df.columns):
    column_len = df[col].astype(str).str.len().max()
    column_len = max(column_len, len(col)) + 2
    worksheet.set_column(i, i, column_len)

writer.save()
fileName = input("Enter the second file name: ")
xl = pd.ExcelFile(fileName)
print("Processing...")

# start of the KPI Data output script
df = xl.parse("Data")
df = df.sort_values(["Customer ID", "Customer Area", "Interaction Type", "Week (Start Monday)"])
df['Week (Start Monday)'] = pd.to_datetime(df['Week (Start Monday)']).dt.date

# formula + condition where the first line of the customer name subset does not match the interaction type above
df['WoW Revenue Change'] = np.where( df['Interaction Type'].shift(1) != df[('Interaction Type')], 0, 
(df['Revenue'] - df['Revenue'].shift(1)) / df['Revenue'].shift(1) )

df['WoW ATC Change'] = np.where( df['Interaction Type'].shift(1) != df[('Interaction Type')], 0, 
(df['Add To Cart Rate'] - df['Add To Cart Rate'].shift(1)) / df['Add To Cart Rate'].shift(1) )

df['WoW CVR Change'] = np.where( df['Interaction Type'].shift(1) != df[('Interaction Type')], 0, 
(df['Conversion Rate'] - df['Conversion Rate'].shift(1)) / df['Conversion Rate'].shift(1) )
df = df.round(decimals=4)

writer = pd.ExcelWriter('KPI_Data_Output.xlsx')

df.to_excel(writer, sheet_name='KPI Data Output', columns=["Customer ID","Customer Area", 
"Week (Start Monday)", "Interaction Type", "Visitors", "View Products", "Products Seen",
"Clicks", "Add To Cart", "Orders", "Total Null Searches", "Total GroupBy Searches",
"Total Other Searches", "Total Navigations", "Total SAYTs", "Total Recommendations", 
"Total GroupBy call Count", "Revenue", "Add To Cart Rate", "Average Order Value",
"Cart Abandonment Rate", "Conversion Rate", "Click Through Rate", "Null Search Rate",
"Revenue Per Visit", "WoW Revenue Change", "WoW ATC Change", "WoW CVR Change"], index=False)

worksheet = writer.sheets['KPI Data Output']

for i, col in enumerate(df.columns):
    column_len = df[col].astype(str).str.len().max()
    column_len = max(column_len, len(col)) + 2
    worksheet.set_column(i, i, column_len)

writer.save()
print("Script completed")