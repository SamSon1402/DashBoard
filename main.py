import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os
import warnings
import matplotlib.pyplot as plt
# Ignore warnings
warnings.filterwarnings('ignore')

# Set the page configuration
st.set_page_config(page_title='Superstore!!!', page_icon=':bar_chart:', layout='wide')

# Set the page title
st.title(':bar_chart: Sample SuperStore EDA')

# Apply custom CSS to adjust padding
st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)

f1 = st.file_uploader(':file_folder: Upload a file', type=(['csv', 'txt', 'xlsx', 'xls']))
if f1 is not None:
    filename = f1.name
    st.write(filename)
    df = pd.read_csv(filename, encoding='ISO-8859-1')
else:
    os.chdir(r"C:\Users\91741\Documents\Dashboard")
    df = pd.read_csv('Sample - Superstore.csv', encoding='ISO-8859-1')

# Strip leading/trailing spaces from column names
df.columns = df.columns.str.strip()

col1, col2 = st.columns((2))
df['Order Date'] = pd.to_datetime(df['Order Date'])

startDate = pd.to_datetime(df['Order Date']).min()
endDate = pd.to_datetime(df['Order Date']).max()

with col1:
    date1 = pd.to_datetime(st.date_input('Start Date', startDate))

with col2:
    date2 = pd.to_datetime(st.date_input('End Date', endDate))

df = df[(df['Order Date'] >= date1) & (df['Order Date'] <= date2)].copy()

st.sidebar.header('Choose Your filter:')
region = st.sidebar.multiselect('pick your Region', df['Region'].unique())

if not region:
    df2 = df.copy()
else:
    df2 = df[df['Region'].isin(region)]

state = st.sidebar.multiselect('Pick your State', df2['State'].unique())

if not state:
    df3 = df2.copy()
else:
    df3 = df2[df2['State'].isin(state)]

city = st.sidebar.multiselect('Select Your City:', df3['City'].unique())

if not region and not state and not city:
    filtered_df = df
elif not state and not city:
    filtered_df = df[df['Region'].isin(region)]
elif not region and not city:
    filtered_df = df[df['State'].isin(state)]
elif state and city:
    filtered_df = df3[df['State'].isin(state) & df3['City'].isin(city)]
elif region and city:
    filtered_df = df3[df['Region'].isin(region) & df3['City'].isin(city)]
elif region and state:
    filtered_df = df3[df['Region'].isin(region) & df3['State'].isin(state)]
elif city:
    filtered_df = df3[df3['City'].isin(city)]
else:
    filtered_df = df3[df3['Region'].isin(region) & df3['City'].isin(city) & df3['State'].isin(state)]

category_df = filtered_df.groupby(by=['Category'], as_index=False)['Sales'].sum()

with col1:
    st.subheader('Category wise Sales')
    fig = px.bar(
        category_df,
        x='Category',
        y='Sales',
        text=['${:,.2f}'.format(x) for x in category_df['Sales']]
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader('Region wise Sales')
    fig = px.pie(filtered_df, values='Sales', names='Region', hole=0.5)
    fig.update_traces(text=filtered_df['Region'], textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

cl1, cl2 = st.columns((2))
with cl1:
    with st.expander("Category_ViewData"):
        fig = go.Figure(data=[go.Table(
            header=dict(values=list(category_df.columns),
                        fill_color='paleturquoise',
                        align='left'),
            cells=dict(values=[category_df[col] for col in category_df.columns],
                       fill_color='lavender',
                       align='left'))
        ])
        st.plotly_chart(fig, use_container_width=True)
        csv = category_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Data", data=csv, file_name="Category.csv", mime="text/csv",
                           help='Click here to download the data as a CSV file')

with cl2:
    with st.expander("Region_ViewData"):
        region = filtered_df.groupby(by="Region", as_index=False)["Sales"].sum()
        fig = go.Figure(data=[go.Table(
            header=dict(values=list(region.columns),
                        fill_color='paleturquoise',
                        align='left'),
            cells=dict(values=[region[col] for col in region.columns],
                       fill_color='lavender',
                       align='left'))
        ])
        st.plotly_chart(fig, use_container_width=True)
        csv = region.to_csv(index=False).encode('utf-8')
        st.download_button("Download Data", data=csv, file_name="Region.csv", mime="text/csv",
                           help='Click here to download the data as a CSV file')

filtered_df["month_year"] = filtered_df["Order Date"].dt.to_period("M")
st.subheader('Time Series Analysis')

linechart = pd.DataFrame(filtered_df.groupby(filtered_df["month_year"].dt.strftime("%Y : %b"))["Sales"].sum()).reset_index()
fig2 = px.line(linechart, x="month_year", y="Sales", labels={"Sales": "Amount"}, height=500, width=1000, template="gridon")
st.plotly_chart(fig2, use_container_width=True)

with st.expander("View Data of TimeSeries:"):
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(linechart.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[linechart[col] for col in linechart.columns],
                   fill_color='lavender',
                   align='left'))
    ])
    st.plotly_chart(fig, use_container_width=True)
    csv = linechart.to_csv(index=False).encode("utf-8")
    st.download_button('Download Data', data=csv, file_name="TimeSeries.csv", mime='text/csv')

# Create a treemap based on Region, category, sub-Category
st.subheader("Hierarchical view of Sales using TreeMap")
fig3 = px.treemap(filtered_df, path=["Region", "Category", "Sub-Category"], values="Sales", hover_data=["Sales"],
                  color="Sub-Category")
fig3.update_layout(width=800, height=650)
st.plotly_chart(fig3, use_container_width=True)

chart1, chart2 = st.columns((2))
with chart1:
    st.subheader('Segment wise Sales')
    fig = px.pie(filtered_df, values="Sales", names="Segment", template="plotly_dark")
    fig.update_traces(text=filtered_df["Segment"], textposition="inside")
    st.plotly_chart(fig, use_container_width=True)

with chart2:
    st.subheader('Category wise Sales')
    fig = px.pie(filtered_df, values="Sales", names="Category", template="gridon")
    fig.update_traces(text=filtered_df["Category"], textposition="inside")
    st.plotly_chart(fig, use_container_width=True)

import plotly.figure_factory as ff
st.subheader(":point_right: Month wise Sub-Category Sales Summary")
with st.expander("Summary_Table"):
    df_sample = df[0:5][["Region", "State", "City", "Category", "Sales", "Profit", "Quantity"]]
    fig = ff.create_table(df_sample, colorscale="Cividis")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("Month wise sub-Category Table")
    filtered_df["month"] = filtered_df["Order Date"].dt.month_name()
    sub_category_Year = pd.pivot_table(data=filtered_df, values="Sales", index=["Sub-Category"], columns="month")
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(sub_category_Year.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[sub_category_Year[col] for col in sub_category_Year.columns],
                   fill_color='lavender',
                   align='left'))
    ])
    st.plotly_chart(fig, use_container_width=True)

# Create a scatter plot
data1 = px.scatter(filtered_df, x="Sales", y="Profit", size="Quantity")
data1['layout'].update(title="Relationship between Sales and Profits using Scatter Plot.",
                       titlefont=dict(size=20), xaxis=dict(title="Sales", titlefont=dict(size=19)),
                       yaxis=dict(title="Profit", titlefont=dict(size=19)))
st.plotly_chart(data1, use_container_width=True)

with st.expander("View Data"):
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(filtered_df.iloc[:500, 1:20:2].columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[filtered_df.iloc[:500, 1:20:2][col] for col in filtered_df.iloc[:500, 1:20:2].columns],
                   fill_color='lavender',
                   align='left'))
    ])
    st.plotly_chart(fig, use_container_width=True)

# Download original DataSet
csv = df.to_csv(index=False).encode('utf-8')
st.download_button('Download Data', data=csv, file_name="Data.csv", mime="text/csv")
