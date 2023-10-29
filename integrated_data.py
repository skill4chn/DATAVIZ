import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
import matplotlib.ticker as mtick

data = pd.read_csv('Acquisitions_nationalite_francaise___8juillet2016.csv', encoding='ISO-8859-1', dtype={'Year': str})

# Convert the "Year" column to numeric, replacing invalid values with NaN
data['Year'] = pd.to_numeric(data['Year'], errors='coerce')

# Remove semicolons from all string columns
string_columns = data.select_dtypes(include=['object']).columns
data[string_columns] = data[string_columns].apply(lambda x: x.str.replace(';', ''))

# Drop rows with NaN values in the "Year" column
data = data.dropna(subset=['Year'])
data['Year'] = data['Year'].astype(int).astype(str)
print (data.head(10))
print (data.columns)

def generate_plotly_chart(data, column_name):
    fig = px.line(data, x='Year', y=column_name, title=f'{column_name} over Time')
    return fig

def generate_matplotlib_chart(data, column_name):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Year'], data[column_name])
    plt.xlabel('Year')
    plt.ylabel(f'Number of {column_name}')
    plt.title(f'{column_name} over Time')
    return plt

def generate_seaborn_chart(data, column_name):
    plt.figure(figsize=(12, 8))  # Adjust the figsize to make the plot smaller
    sns.barplot(x='Year', y=column_name, data=data)
    plt.xlabel('Year')
    plt.ylabel(f'Acquisitions of French nationality in {column_name}')
    plt.title(f'{column_name} over Time')

    # Set the y-axis to display integers only
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d'))

    return plt


def generate_bokeh_chart(data, column_name):
    # Filter data to contain only non-null rows for the selected column
    filtered_data = data[data[column_name].notnull()]

    # Create a Bokeh figure
    p = figure(plot_height=400, plot_width=800, title=f'Bokeh Scatter Chart for {column_name}')

    # Create a ColumnDataSource
    source = ColumnDataSource(data={'x': filtered_data['Year'], 'y': filtered_data[column_name]})

    # Add a scatter glyph
    p.circle(x='x', y='y', source=source, size=8, color="red", legend_label=column_name)

    # Customize the plot
    p.xaxis.major_label_orientation = 1
    p.xaxis.axis_label = 'Year'
    p.yaxis.axis_label = f'People from {column_name}'
    p.background_fill_color = "lightgrey"

    return p


