import requests
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import os
import numpy as np

data = pd.read_json('https://www.mohfw.gov.in/data/datanew.json')
data=data.iloc[:-1,1:]

df = data
df['increment_active'] = df.apply(lambda x: 0 if x['new_active']-x['active']<0 else x['new_active']-x['active'],axis=1)
df['latest_positive'] = df['new_positive']-df['positive']
df['latest_cured'] = df['new_cured']-df['cured']
df['latest_death'] = df['new_death']-df['death']

data_dict = {'Active':df['active'].sum(),
             'Positive':df['positive'].sum(),
             'Cured':df['cured'].sum(),
             'Death':df['death'].sum(),
             'Increment_active':df['increment_active'].sum(),
             'Latest_positive':df['latest_positive'].sum(),
             'Latest_cured':df['latest_cured'].sum(),
             'Latest_death':df['latest_death'].sum()}
df_total = pd.DataFrame([data_dict])

def subplotsGraph1(df_total):
    labels = ['Active', 'Positive', 'Cured', 'Death']
    values = df_total.values.tolist()[0][:4]
    values1 = df_total.values.tolist()[0][4:]
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "pie"}]])
    fig.add_trace( go.Pie(
         values=values,
         labels=labels,
         hole=.4,
         pull=[0, 0.02],
         domain=dict(x=[0, 0.5]),
         name="Overall Cases"), 
         row=1, col=1)
    fig.add_trace(go.Pie(
         values=values1,
         labels=labels,
         hole=.3,
         pull=[0, 0.02],
         domain=dict(x=[0.5, 1.0]),
         name="Latest Cases"),
        row=1, col=2)
    fig.update_layout( plot_bgcolor='rgba(0,0,0,0)',
                    width=900, height=400,
        title={
            'text': "Covid overall and Latest Cases in Country",
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    # fig.show()
    fig.update_layout(paper_bgcolor = 'rgba(0,0,0,0)')
    return fig
    
fig1 = subplotsGraph1(df_total)

def subplotsGraph2(df_state,state):
    df_state_total = df_state[['active', 'positive', 'cured', 'death']]
    labels = df_state_total.columns.to_list()
    values = df_state_total.values.tolist()[0]
    df_state_total1 = df_state[['increment_active', 'latest_positive', 'latest_cured', 'latest_death']]
    # labels1 = df_state_total1.columns.to_list()
    values1 = df_state_total1.values.tolist()[0]
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "pie"}]])
    fig.add_trace( go.Pie(
         values=values,
         labels=labels,
         hole=.4,
         pull=[0, 0.02],
         domain=dict(x=[0, 0.5]),
         name="Overall Cases"), 
         row=1, col=1)
    fig.add_trace(go.Pie(
         values=values1,
         labels=labels,
         hole=.3,
         pull=[0, 0.02],
         domain=dict(x=[0.5, 1.0]),
         name="Latest Cases"),
        row=1, col=2)
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',
                    width=900, height=400,
        title={
            'text': "Covid overall and Latest Cases in "+state,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    fig.update_layout(paper_bgcolor = 'rgba(0,0,0,0)')
    return fig

def select_state(df,state):
    state = state.lower()
    temp = df[df['state_name'].apply(lambda x: state == x.lower())]
    if len(temp)==1:
        state_list = list(set(temp['state_name'].values))
    else:
        df_state= df[df['state_name'].apply(lambda x: state in x.lower())]
        state_list = list(set(df_state['state_name'].values))
    # return only one country
    state0 = state_list[0]
    return state0

input_state = 'maha'
state = select_state(df,input_state)
df_state = df[df['state_name'] == state]

fig2= subplotsGraph2(df_state,state)

def Graph3(df1):
    x = list(df1.index)
    a = list(df1['increment_active'])
    b = list(df1['latest_positive'])
    c = list(df1['latest_cured'])
    d = list(df1['latest_death'])
    fig = go.Figure(data=[
        go.Bar(name='Active', x=x, y=a, text=a,  textposition='outside'),
        go.Bar(name='Positive', x=x, y=b, text=b,  textposition='outside'),
        go.Bar(name='Cured', x=x, y=c, text=c,  textposition='outside'),
        go.Bar(name='Death', x=x, y=d, text=d,  textposition='outside')
    ])
    fig.update_layout(barmode='group', 
        plot_bgcolor='rgba(0,0,0,0)',
        autosize=False,
        width=800,
        height=500,
        title={
            'text': "Top 10 States based on Latest Increament Active cases",
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    fig.update_layout(paper_bgcolor = 'rgba(0,0,0,0)')
    return fig

top_10_state = df.nlargest(10, ['increment_active'])
df1 = top_10_state.set_index('state_name',drop=True)
df0 = df1[['increment_active','latest_positive','latest_cured','latest_death']]
fig3 = Graph3(df0)

def Graph4(df1):
    x = list(df1.index)
    a = list(df1['increment_active'])
    b = list(df1['latest_positive'])
    c = list(df1['latest_cured'])
    d = list(df1['latest_death'])
    fig = go.Figure(data=[
        go.Bar(name='Active', x=x, y=a, text=a,  textposition='outside'),
        go.Bar(name='Positive', x=x, y=b, text=b,  textposition='outside'),
        go.Bar(name='Cured', x=x, y=c, text=c,  textposition='outside'),
        go.Bar(name='Death', x=x, y=d, text=d,  textposition='outside')
    ])
    fig.update_layout(barmode='group',  
        plot_bgcolor='rgba(0,0,0,0)',
        autosize=False,
        width=800,
        height=500,
        title={
            'text': "Top 10 States based on Latest Positive cases",
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    fig.update_layout(paper_bgcolor = 'rgba(0,0,0,0)')
    return fig

top_10_state = df.nlargest(10, ['latest_positive'])
df1=top_10_state.set_index('state_name',drop=True)
df1 = df1[['increment_active','latest_positive','latest_cured','latest_death']]
fig4 = Graph4(df1)

def Graph5(df1):
    x = list(df1.index)
    a = list(df1['active'])
    b = list(df1['positive'])
    c = list(df1['cured'])
    d = list(df1['death'])
    fig = go.Figure(data=[
        go.Bar(name='Active', x=x, y=a, text=a,  textposition='outside'),
        go.Bar(name='Positive', x=x, y=b, text=b,  textposition='outside'),
        go.Bar(name='Cured', x=x, y=c, text=c,  textposition='outside'),
        go.Bar(name='Death', x=x, y=d, text=d,  textposition='outside')
    ])
    fig.update_layout(barmode='group', 
        plot_bgcolor='rgba(0,0,0,0)',
        autosize=False,
        width=800,
        height=500,
        title={
            'text': "Top 10 States based on Active cases",
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    fig.update_layout(paper_bgcolor = 'rgba(0,0,0,0)')
    return fig

top_10_active_state = df.nlargest(10, ['active'])
df1 = top_10_active_state.set_index('state_name',drop=True)
df2 = df1.iloc[:,:4]
fig5 = Graph5(df2)

def Graph6(df1):
    x = list(df1.index)
    a = list(df1['active'])
    b = list(df1['positive'])
    c = list(df1['cured'])
    d = list(df1['death'])
    fig = go.Figure(data=[
        go.Bar(name='Active', x=x, y=a, text=a,  textposition='outside'),
        go.Bar(name='Positive', x=x, y=b, text=b,  textposition='outside'),
        go.Bar(name='Cured', x=x, y=c, text=c,  textposition='outside'),
        go.Bar(name='Death', x=x, y=d, text=d,  textposition='outside')
    ])
    fig.update_layout(barmode='group', 
        plot_bgcolor='rgba(0,0,0,0)',
        autosize=False,
        width=800,
        height=500,
        title={
            'text': "Top 10 States based on Positive cases",
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    fig.update_layout(paper_bgcolor = 'rgba(0,0,0,0)')
    return fig

top_10_positive_state = df.nlargest(10, ['positive'])
df1 = top_10_positive_state.set_index('state_name',drop=True)
df3 = df1.iloc[:,:4]
fig6 = Graph6(df3)

def Graph7(df1):
    x = list(df1.index)
    y = list(df1['increment_active'])
    layout = dict(
        template="simple_white",
        xaxis=dict(ticks="outside", mirror=True, showline=True),
        yaxis=dict(ticks="outside", mirror=True, showline=True),
    )
    fig = go.Figure(data = [go.Bar(
                x = y,
                y = x,
                text = y,
                textposition='outside',
                orientation='h')], layout = layout)
    fig.update_layout( 
        plot_bgcolor='rgba(0,0,0,0)',
        autosize=False,
        width=800,
        height=500,
        title={
            'text': "Top 10 States with new increament in Active cases",
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'}
        ,
        xaxis_range=[0,max(df1['increment_active'])*1.1]
       )
    fig.update_layout(paper_bgcolor = 'rgba(0,0,0,0)')
    return fig
    
top_10_state = df.nlargest(10, ['increment_active'])
df1 = top_10_state.set_index('state_name',drop=True)
df4 = df1[['increment_active','latest_positive','latest_cured','latest_death']]
fig7 = Graph7(df4)

def Graph8(df1):
    x = list(df1.index)
    y = list(df1['latest_cured'])
    layout = dict(
        template="simple_white",
        xaxis=dict(ticks="outside", mirror=True, showline=True),
        yaxis=dict(ticks="outside", mirror=True, showline=True),
    )
    fig = go.Figure(data = [go.Bar(
                x = y,
                y = x,
                text = y,
                textposition='outside',
                orientation='h')], layout = layout)
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        autosize=False,
        width=800,
        height=500,
        title={
            'text': "Top 10 States with new increament in Cured cases",
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'}
        ,
        xaxis_range=[0,max(df1['latest_cured'])*1.2]
        )
    fig.update_layout(paper_bgcolor = 'rgba(0,0,0,0)')
    return fig
    
top_10_state = df.nlargest(10, ['latest_cured'])
df1 = top_10_state.set_index('state_name',drop=True)
df5 = df1[['increment_active','latest_positive','latest_cured','latest_death']]
fig8 = Graph8(df5)

def Graph9(df1):
    x = list(df1.index)
    y = list(df1['latest_death'])
    layout = dict(
        template="simple_white",
        xaxis=dict(ticks="outside", mirror=True, showline=True),
        yaxis=dict(ticks="outside", mirror=True, showline=True),
    )
    fig = go.Figure(data = [go.Bar(
                x = y,
                y = x,
                text = y,
                textposition='outside',
                orientation='h')], layout = layout)
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        autosize=False,
        width=800,
        height=500,
        title={
            'text': "Top 10 States with new increament in Death cases",
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'}
        ,
        xaxis_range=[0,max(df1['latest_death'])*1.2]
        )
    fig.update_layout(paper_bgcolor = 'rgba(0,0,0,0)')
    return fig
    
top_10_state = df.nlargest(10, ['latest_death'])
df1 = top_10_state.set_index('state_name',drop=True)
df6 = df1[['increment_active','latest_positive','latest_cured','latest_death']]
fig9 = Graph9(df6)


