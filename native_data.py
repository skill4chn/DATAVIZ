import streamlit as st
import pandas as pd
import plotly.express as px
from integrated_data import generate_plotly_chart, generate_matplotlib_chart, generate_seaborn_chart, generate_bokeh_chart

# Load the data
data = pd.read_csv('Acquisitions_nationalite_francaise___8juillet2016.csv', encoding='ISO-8859-1', dtype={'Year': str})

# Convert the "Year" column to numeric, replacing invalid values with NaN
data['Year'] = pd.to_numeric(data['Year'], errors='coerce')

# Remove rows with NaN values in the "Year" column
data = data.dropna(subset=['Year'])

# Drop columns 'Nan' and 'Nan;;;;;;;;;;;;;;;;;;;;' if they exist i have a small bug here i solved it like this
if 'Nan' in data.columns:
    data.drop(columns=['Nan'], inplace=True)
if 'Nan;;;;;;;;;;;;;;;;;;;;' in data.columns:
    data.drop(columns=['Nan;;;;;;;;;;;;;;;;;;;;'], inplace=True)

st.set_page_config(
    page_title="Data Visualization App",
    page_icon=":bar_chart:",
    layout="wide",
)
# Define interpretations for each column
column_interpretations = {
    "Europe": "This chart shows the trend of acquisitions of French nationality from European countries over time.",
    "UE15": "This chart shows the trend of acquisitions of French nationality within the first 15 members of the European Union (UE15) over time.",
    "inc. Spain": "This chart shows the trend of acquisitions of French nationality from Spain over time.",
    "inc. Italy": "This chart shows the trend of acquisitions of French nationality from Italy over time.",
    "inc. Portugal": "This chart shows the trend of acquisitions of French nationality from Portugal over time.",
    "NEM": "This chart shows the trend of acquisitions of French nationality from new european members in 2004 over time.",
    "inc. Poland": "This chart shows the trend of acquisitions of French nationality from Poland over time.",
    "NEM 2007": "This chart shows the trend of acquisitions of French nationality from Bulgaria and Romania over time.",
    "inc. Romania": "This chart shows the trend of acquisitions of French nationality from Romania over time.",
    "Rest of Europe": "This chart shows the trend of acquisitions of French nationality from other European countries over time.",
    "Europe (ex. EEE)": "This chart shows the trend of acquisitions of French nationality from European countries outside the EEE over time.",
    "AELE": "This chart shows the trend of acquisitions of French nationality from AELE countries over time.",
    "inc. Serbia and Montenegro": "This chart shows the trend of acquisitions of French nationality from Serbia and Montenegro over time.",
    "inc. Switzerland": "This chart shows the trend of acquisitions of French nationality from Switzerland over time.",
    "CEI": "This chart shows the trend of acquisitions of French nationality from CEI countries over time.",
    "CEI Europe": "This chart shows the trend of acquisitions of French nationality from CEI countries in Europe over time.",
    "inc. Russian Federation": "This chart shows the trend of acquisitions of French nationality from the Russian Federation over time.",
    "CEI Asia": "This chart shows the trend of acquisitions of French nationality from CEI countries in Asia over time.",
    "Asia": "This chart shows the trend of acquisitions of French nationality from Asian countries over time.",
    "South-east Asia": "This chart shows the trend of acquisitions of French nationality from Southeast Asian countries over time.",
    "oriental Asia": "This chart shows the trend of acquisitions of French nationality from East Asian countries over time.",
    "inc. China (PRC)": "This chart shows the trend of acquisitions of French nationality from China (People's Republic) over time.",
    "inc. Japan": "This chart shows the trend of acquisitions of French nationality from Japan over time.",
    "Meridional Asia": "This chart shows the trend of acquisitions of French nationality from South Asian countries over time.",
    "inc. India": "This chart shows the trend of acquisitions of French nationality from India over time.",
    "inc. Sri Lanka": "This chart shows the trend of acquisitions of French nationality from Sri Lanka over time.",
    "Rest of Asia": "This chart shows the trend of acquisitions of French nationality from other Asian countries over time.",
    "inc. Turkey": "This chart shows the trend of acquisitions of French nationality from Turkey over time.",
    "Africa": "This chart shows the trend of acquisitions of French nationality from African countries over time.",
    "Maghreb": "This chart shows the trend of acquisitions of French nationality from Maghreb countries over time.",
    "Algeria": "This chart shows the trend of acquisitions of French nationality from Algeria over time.",
    "Morocco": "This chart shows the trend of acquisitions of French nationality from Morocco over time.",
    "Tunisia": "This chart shows the trend of acquisitions of French nationality from Tunisia over time.",
    "subsaharian Africa": "This chart shows the trend of acquisitions of French nationality from Sub-Saharan African countries over time.",
    "inc. Cameroon": "This chart shows the trend of acquisitions of French nationality from Cameroon over time.",
    "inc. Comores": "This chart shows the trend of acquisitions of French nationality from Comoros over time.",
    "inc. Congo": "This chart shows the trend of acquisitions of French nationality from Congo over time.",
    "inc. Ivory coast": "This chart shows the trend of acquisitions of French nationality from Côte d'Ivoire over time.",
    "inc. Madagascar": "This chart shows the trend of acquisitions of French nationality from Madagascar over time.",
    "inc. Mali": "This chart shows the trend of acquisitions of French nationality from Mali over time.",
    "inc. Mauritania": "This chart shows the trend of acquisitions of French nationality from Mauritania over time.",
    "inc. Senegal": "This chart shows the trend of acquisitions of French nationality from Senegal over time.",
    "Rest of Africa": "This chart shows the trend of acquisitions of French nationality from other African countries over time.",
    "inc. Democratic Congo": "This chart shows the trend of acquisitions of French nationality from the Democratic Republic of the Congo over time.",
    "America": "This chart shows the trend of acquisitions of French nationality from American countries over time.",
    "North America": "This chart shows the trend of acquisitions of French nationality from North American countries over time.",
    "Canada": "This chart shows the trend of acquisitions of French nationality from Canada over time.",
    "USA": "This chart shows the trend of acquisitions of French nationality from the United States over time.",
    "South America": "This chart shows the trend of acquisitions of French nationality from South American countries over time.",
    "inc. Brazil": "This chart shows the trend of acquisitions of French nationality from Brazil over time.",
    "inc. Haïti": "This chart shows the trend of acquisitions of French nationality from Haiti over time.",
    "Oceania": "This chart shows the trend of acquisitions of French nationality from Oceanian countries over time.",
    "Refused": "This chart shows the trend of refused cases of acquisitions of French nationality over time.",
    "TOTAL": "This chart shows the total number of acquisitions of French nationality over time."
}



# Sidebar options

# Your personal information
name = "LIN Jefferson"
class_name = "M1 BIA2"
year = 2023
github_link = "https://github.com/skill4chn"
linkedin_link = "https://www.linkedin.com/in/jefferson-lin-b718711b7/"



# Display your personal information
# Halloween decorations in the sidebar
st.sidebar.write("### 🎃👻🕷️ Happy Halloween! 🦇🕸️🍬")
st.sidebar.title("Personal Information")
st.sidebar.write(f"Name: {name}")
st.sidebar.write(f"Class: {class_name}")
st.sidebar.write(f"Year: {year}")
st.sidebar.write(f"GitHub: [{name}]({github_link})")
st.sidebar.write(f"LinkedIn: [{name}]({linkedin_link})")


# Halloween header with pumpkin and bat emojis
st.markdown(
    """
    <h1 style='text-align: center; color: #FF6600; padding: 10px; border-radius: 5px;'>
        🎃 French Immigration Over the Years 🦇
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    [Click here to access the official database](https://www.data.gouv.fr/fr/datasets/lacces-a-la-nationalite-francaise-1/)
    """
)

# Main content
st.write(" ### Explore who has obtained French nationality and their origins.")
st.write(" ### To start, take a look at the sidebar on your left and select which type of library you want to use and also which countries' data you want to plot.")



# Sidebar options
st.sidebar.title(":ghost: Data Visualization :jack_o_lantern:")
st.sidebar.markdown(":spider_web: Choose your options below :spider_web:")
chart_type = st.sidebar.selectbox("Select a Chart Type", ["Plotly Express", "Matplotlib", "Seaborn", "Bokeh"])
selected_columns = st.sidebar.multiselect("Select Data Columns", data.columns[1:])
show_multiple_columns = st.sidebar.checkbox("Show Multiple Data on One Graph")

# Function to display description for selected columns
def display_description(selected_columns):
    for selected_column in selected_columns:
        description_text = column_interpretations.get(selected_column, "")
        st.markdown(f"**{selected_column}**: {description_text}")



# Display the selected chart
if chart_type == "Plotly Express":
    if show_multiple_columns:
        fig = generate_plotly_chart(data, selected_columns)
        st.plotly_chart(fig)
    else:
        for selected_column in selected_columns:
            fig = generate_plotly_chart(data, [selected_column])
            st.plotly_chart(fig)
        display_description(selected_columns)

elif chart_type == "Matplotlib":
    if show_multiple_columns:
        fig = generate_matplotlib_chart(data, selected_columns)
        st.pyplot(fig)
    else:
        for selected_column in selected_columns:
            fig = generate_matplotlib_chart(data, [selected_column])
            st.pyplot(fig)
        display_description(selected_columns)

elif chart_type == "Seaborn":
    for selected_column in selected_columns:
        st.write(f"### {selected_column}")
        if show_multiple_columns:
            fig = generate_seaborn_chart(data, selected_column)
            st.pyplot(fig)
        else:
            fig = generate_seaborn_chart(data, selected_column)
            st.pyplot(fig)
        display_description([selected_column])

elif chart_type == "Bokeh":
    for selected_column in selected_columns:
        bokeh_chart = generate_bokeh_chart(data, selected_column)
        if bokeh_chart is not None:
            st.bokeh_chart(bokeh_chart)
        else:
            st.write(f"No data available for {selected_column}")

# New feature: User selects the year for global results
show_global_results = st.sidebar.checkbox("Show Global Results Table", key="show_global_results")

# New feature: User selects the year for global results
if show_global_results:
    selected_year = st.sidebar.selectbox("Select a Year for Global Results", data['Year'].unique(), key="selected_year")

# New feature: Display global results table for the selected year if the user chooses to show it
if show_global_results:
    st.write(" Global Results for the Selected Year")
    global_results_data = data[data['Year'] == selected_year].drop(columns=['Year'])

    # Sort columns by descending order for the selected year and display the top 20 columns
    sorted_columns = global_results_data.iloc[0].apply(pd.to_numeric, errors='coerce').sort_values(ascending=False)
    top_20_columns = sorted_columns.head(20)
    st.dataframe(top_20_columns, width=800)

# New feature: Compare multiple columns on the same plot
st.sidebar.title("Compare Multiple Columns on the Same Plot")
selected_columns_to_compare = st.sidebar.multiselect("Select Columns to Compare", selected_columns)
selected_years_to_compare = st.sidebar.multiselect("Select Years to Compare", data['Year'].unique())

# Filter data for selected years
comparison_data = data[data['Year'].isin(selected_years_to_compare)]

# Create a Plotly Express bar plot with multiple bars alongside each other
fig_comparison = px.bar(
    comparison_data,
    x="Year",
    y=selected_columns_to_compare,
    title="Comparison of Columns Over Selected Years",
    labels={"Year": "Years"},
    color_discrete_sequence=px.colors.qualitative.Set3,
)

# Display the comparison plot
st.write(":skull: Comparison of Multiple Columns Over Selected Years :skull:")
st.plotly_chart(fig_comparison)

