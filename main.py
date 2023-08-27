import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv('Data.csv')

selected_columns = ['RowNumber', 'Date', 'Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5', 'Column 6', 'ColumnColumn 7']
selected_data = data[selected_columns]

selected_data['Date'] = pd.to_datetime(selected_data['Date'], format='%d/%m/%Y')

predictions = {}
for column in selected_columns[2:]:
    x = selected_data['RowNumber'].values.reshape(-1, 1)
    y = selected_data[column]
    model = LinearRegression()
    model.fit(x, y)
    prediction_index = selected_data['RowNumber'].max() + 1
    predicted_value = model.predict([[prediction_index]])
    predictions[column] = int(predicted_value[0])

next_row_number = 6800
next_date = pd.to_datetime('01/09/1968', format='%d/%m/%Y')
print("Predicted values for row number 4172:\n", "RowNumber:", next_row_number, "Date:",
      next_date.strftime('%d/%m/%Y'),
      predictions)