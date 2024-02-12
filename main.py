import streamlit as st
import plotly.express as px

st.title('Dataset Graph Visualisation')
st.sidebar.subheader('Dataset Name')
ds_op = st.sidebar.selectbox(label='Select Plotly Dataset', options=['Iris', 'Tips', 'Gapminder'])
button1 = st.sidebar.button(label='Show Plotly Graphs')
if button1:
    if ds_op == 'Iris':
        st.header(f'Dataset: {ds_op}')
        df1 = px.data.iris()
        st.plotly_chart(px.scatter(df1, x='sepal_length', y='petal_length', size='sepal_width', color='species', template='plotly_dark',
                   labels={'sepal_length': 'Sepal Length', 'petal_length': 'Petal Length','species':'Species'},
                   title='Sepal length vs Petal length of Iris species'))
    elif ds_op == 'Tips':
        st.header(f'Dataset: {ds_op}')
        df2 = px.data.tips()
        st.plotly_chart(px.scatter(df2, x='total_bill',y='tip', color='sex',size='size', size_max=40, template='plotly_dark', hover_name='time', labels={'sex':'Gender', 'total_bill':'Total Bill', 'tip': 'Tips'}, title='Tips vs Total Bill of a Restaurant'))
        st.plotly_chart(px.bar(df2, x=df2['day'].unique(), y=df2.groupby('day')['total_bill'].sum(), template='plotly_dark', labels={'x': 'Days','y':'Total Bill'}, title='Revenue'))

    elif ds_op == 'Gapminder':
        st.header(f'Dataset: {ds_op}')
        df3 = px.data.gapminder()
        st.plotly_chart(px.scatter(df3, y='gdpPercap', x='lifeExp', size='pop', size_max=120,color='continent', hover_name='country', animation_frame='year', animation_group='country', template='plotly_dark', range_x=[20,100], labels={'continent': 'Continent', 'lifeExp': 'Life Expectancy', 'gdpPercap': 'GDP per Capita'}))
