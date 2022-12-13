import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
import plotly.express as px
plt.style.use('seaborn-dark')
plt.style.context('grayscale')

def count_plots(df):
    fig = plt.figure(figsize=(8,8))
    gs = fig.add_gridspec(3,3)
    gs.update(wspace=0.5, hspace=0.25)
    ax0 = fig.add_subplot(gs[0,0])
    ax1 = fig.add_subplot(gs[0,1])
    ax2 = fig.add_subplot(gs[0,2])
    ax3 = fig.add_subplot(gs[1,0])
    ax4 = fig.add_subplot(gs[1,1])
    ax5 = fig.add_subplot(gs[1,2])
    ax6 = fig.add_subplot(gs[2,0])
    ax7 = fig.add_subplot(gs[2,1])
    ax8 = fig.add_subplot(gs[2,2])

    background_color = "white"
    color_palette = ["cyan","magenta","pink","blue","#da8829"]
    fig.patch.set_facecolor(background_color) 
    ax0.set_facecolor("grey") 
    ax1.set_facecolor("grey") 
    ax2.set_facecolor("grey") 
    ax3.set_facecolor("grey") 
    ax4.set_facecolor("grey") 
    ax5.set_facecolor("grey") 
    ax6.set_facecolor("grey") 
    ax7.set_facecolor("grey") 
    ax8.set_facecolor("grey") 

    # Title of the plot
    ax0.spines["bottom"].set_visible(False)
    ax0.spines["left"].set_visible(False)
    ax0.spines["top"].set_visible(False)
    ax0.spines["right"].set_visible(False)
    ax0.tick_params(left=False, bottom=False)
    ax0.set_xticklabels([])
    ax0.set_yticklabels([])
    # ax0.text(0.5,0.5,
    #          'Count plot for various\n categorical features',
    #          horizontalalignment='center',
    #          verticalalignment='center',
    #          fontsize=18, fontweight='bold',
    #          fontfamily='serif',
    #          color="#000000")

    # Sex count
    ax1.text(0.3, 220, 'SEX', fontsize=14, fontweight='bold', fontfamily='serif', color="grey")
    ax1.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
    sns.countplot(ax=ax1,data=df,x='sex',palette=color_palette)
    ax1.set_xlabel("")
    ax1.set_ylabel("")

    ax2.text(-1, 150, ' 0: typical angina, 1: atypical angina ,2: non-anginal pain,3: asymptomatic', fontsize=14, fontweight='bold', fontfamily='serif', color="grey")
    ax2.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
    sns.countplot(ax=ax2,data=df,x='cp',palette=color_palette)
    ax2.set_xlabel("")
    ax2.set_ylabel("")

    ax3.text(0, 275, 'fasting_blood_sugar', fontsize=14, fontweight='bold', fontfamily='serif', color="grey")
    ax3.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
    sns.countplot(ax=ax3,data=df,x='fasting_blood_sugar',palette=color_palette)
    ax3.set_xlabel("")
    ax3.set_ylabel("")

    ax4.text(-1, 170, 'resting electrocardiographic results', fontsize=14, fontweight='bold', fontfamily='serif', color="grey")
    ax4.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
    sns.countplot(ax=ax4,data=df,x='restecg',palette=color_palette)
    ax4.set_xlabel("")
    ax4.set_ylabel("")

    ax5.text(0, 180, 'output', fontsize=14, fontweight='bold', fontfamily='serif', color="grey")
    ax5.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
    sns.countplot(ax=ax5,data=df,x='output',palette=color_palette)
    ax5.set_xlabel("")
    ax5.set_ylabel("")

    ax6.text(0.5, 190, 'number of major vessels (0-3)', fontsize=14, fontweight='bold', fontfamily='serif', color="grey")
    ax6.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
    sns.countplot(ax=ax6,data=df,x='caa',palette=color_palette)
    ax6.set_xlabel("")
    ax6.set_ylabel("")

    ax7.text(0.5, 220, 'exercise', fontsize=14, fontweight='bold', fontfamily='serif', color="grey")
    ax7.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
    sns.countplot(ax=ax7,data=df,x='exercise',palette=color_palette)
    ax7.set_xlabel("")
    ax7.set_ylabel("")

    ax8.text(-1, 180, 'maximum heart rate achieved', fontsize=14, fontweight='bold', fontfamily='serif', color="grey")
    ax8.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
    sns.countplot(ax=ax8,data=df,x='thall',palette=color_palette)
    ax8.set_xlabel("")
    ax8.set_ylabel("")

    for s in ["top","right","left"]:
        ax1.spines[s].set_visible(False)
        ax2.spines[s].set_visible(False)
        ax3.spines[s].set_visible(False)
        ax4.spines[s].set_visible(False)
        ax5.spines[s].set_visible(False)
        ax6.spines[s].set_visible(False)
        ax7.spines[s].set_visible(False)
        ax8.spines[s].set_visible(False)
    return fig


def density_plots(df):
    with sns.axes_style('whitegrid'):
        fig = plt.figure(figsize=(16,16))

        fig = plt.subplot(221)
        sns.kdeplot(df["age"],shade=True, label = ' Age', color="red")
        plt.legend()

        fig = plt.subplot(222)
        sns.kdeplot(df["blood_pressure"],shade=True, label =' blood_pressure', color="black")
        plt.legend()
        
        fig = plt.subplot(223)
        sns.kdeplot(df["Cholestoral"],shade=True, label =' Cholestoral', color="purple")
        plt.legend()

        fig = plt.subplot(224)
        sns.kdeplot(df["max_heart_rate"],shade=True, label =' max_heart_rate', color="green")
        plt.legend()
        fig = plt.show()
    return fig


def cp_count(df):
    plt.subplots(figsize=(8,8))
    sns.countplot(data=df,x='cp',palette="pastel")
    plt.title( 'CP Count')
    fig = plt.show()
    return fig

def thall_count(df):
    plt.subplots(figsize=(8,8))
    sns.countplot(data=df,x='thall',palette="pink")
    plt.title( 'Thall Count')
    fig = plt.show()
    return fig

def slp_count(df):
    plt.subplots(figsize=(8,8))
    sns.countplot(data=df,x='slp',palette='Set2')
    plt.title('slp Count')
    fig = plt.show()
    return fig
    
def age_count(df):
    plt.subplots(figsize=(8,8))
    sns.countplot(data=df,x='age', palette= 'viridis')
    plt.title("Age Count")
    fig = plt.show()
    return fig

def correlation_matrix(df):
    plt.figure(figsize=(8,8))
    sns.heatmap(df.corr(), annot=True,cmap='gnuplot2_r',  fmt = ".1f")
    fig = plt.show()
    return fig

def male_and_female_count(df):
    z = df['sex'].value_counts()
    fig=px.bar(z,x=z.index,y=z.values,color=z.index,text=z.values,labels={'index':'Man-Woman','y':'count','text':'count'},template='ggplot2',title='<b> male and female numbers')
    fig2=px.pie(z,names=z.index,values=z.values,labels={'index':'job title','y':'count','text':'count'},template='ggplot2')
    return fig, fig2
   

def low_chance_of_heart_attack(df):
    fig = plt.figure(figsize=(10,10))
    sns.displot(df[df["output"] == "Low"]["cp"], color = "green", kde = True)
    fig  = plt.show()
    return fig
def high_chance_of_heart_attack(df):
    fig = plt.figure(figsize=(10,10))
    sns.displot(df[df['output']== "High"]["cp"],color='red',kde =True)
    fig  = plt.show()
    return fig

def heart_rate_by_gender(df):
    fig = px.box(df,x="output", y='oldpeak',color='sex' ,template='ggplot2',labels={'sex':"Sex","max_heart_rate":"max_heart_rate"},
       title = '<b>Heart rates by gender')
    fig2 = px.box(df,x='sex',y='max_heart_rate',
       color='sex',template='ggplot2',
       labels={'sex':'Sex',
               'max_heart_rate':'max_heart_rate'},
       title='<b>Heart rates by gender')
    return fig, fig2

def blood_pressure_by_age(df):
    plt.subplots(figsize=(10,10))
    sns.lineplot(data=df , x="age", y="blood_pressure",color="black")
    fig = plt.show()
    return fig

def o2_saturation(df):
    fig = px.bar(df, 
    x='output',y='o2Saturation',color_discrete_sequence=['red'],labels={'output':'count'},
    template='plotly_dark')
    us_series_data=df[df['output']=="High"]
    oldest_us_series=us_series_data.sort_values(by='o2Saturation',ascending=False)[0:200]
    fig2 = go.Figure(data=[go.Table(header=dict(values=['output',"o2Saturation"],fill_color='crimson'),
                    cells=dict(values=[oldest_us_series['output'],oldest_us_series['o2Saturation']],fill_color='lightgray'))
                        ])
    us_series_data=df[df['output']=="Low"]
    oldest_us_series=us_series_data.sort_values(by="o2Saturation",ascending=False)[0:200]
    fig3 = go.Figure(data=[go.Table(header=dict(values=['output',"o2Saturation"],fill_color='crimson'),
                    cells=dict(values=[oldest_us_series['output'],oldest_us_series['o2Saturation']],fill_color='lightgray'))
                        ])
    return fig, fig2, fig3

def blood_presure_count(df):
    fig = plt.figure(figsize = (10,10))
    sns.displot(df, x="blood_pressure", col = "output", color="black")
    fig = plt.show()
    return fig

def charts(df):
    fig, axes = plt.subplots(4,2, figsize=(25,25))

    #use the axis for plotting
    axes[0, 0].set_title('(Plot.3.1)AGE and OUTPUT')
    sns.kdeplot(x=df.age,
                hue=df.output,
                fill=True,
                palette= 'Set2',
                ax=axes[0,0])

    #use the axis for plotting
    axes[0, 1].set_title('(Plot.3.2) BLOOD PRESSURE DISTRIBUTION')
    sns.kdeplot(x=df.fasting_blood_sugar,
                hue=df.output,
                fill=True,
                palette= 'Set2',
                ax=axes[0,1])


    #use the axis for plotting
    axes[1, 0].set_title('(Plot.3.3) CHOLESTROL DISTRIBUTION')
    sns.kdeplot(x=df.Cholestoral,
                hue=df.output,
                fill=True,
                palette= 'Set2',
                ax=axes[1,0])


    #use the axis for plotting
    axes[1, 1].set_title('(Plot.3.4) HEART RATE DISTRIBUTION')
    sns.kdeplot(x=df.max_heart_rate,
                hue=df.output,
                fill=True,
                palette= 'Set2',
                ax=axes[1,1])


    #use the axis for plotting
    axes[2, 0].set_title('(Plot.3.5) CHEST PAIN DISTRIBUTION')
    sns.kdeplot(x=df.cp,
            hue=df.output,
            fill= True,
            palette = 'Set2',
            ax= axes[2,0])


    #use the axis for plotting
    axes[2, 1].set_title('(Plot.3.6) THALL DISTRIBUTION')
    sns.kdeplot(x=df.caa,
            hue=df.output,
            fill= True,
            palette = 'Set2',
            ax= axes[2,1])


    #use the axis for plotting
    axes[3, 0].set_title('(Plot.3.7) RESTECG DISTRIBUTION')
    sns.kdeplot(x=df.restecg,
            hue=df.output,
            fill= True,
            palette = 'Set2',
            ax= axes[3,0])


    #use the axis for plotting
    axes[3, 1].set_title('(Plot.3.8) EXNG DISTRIBUTION')
    sns.kdeplot(x=df.exercise,
            hue=df.output,
            fill= True,
            palette = 'Set2',
            ax= axes[3,1])
    return fig

def exercise_rate(df):
    
    with sns.axes_style('dark'):
        fig = plt.figure(figsize = (10,10))
        g = sns.catplot(x='exercise',data=df, aspect=4.0,kind='count', hue='output', palette="pastel")
    g.set_ylabels('Frequency')
    g.set_xlabels("Exercise")
    fig = plt.show()
    return fig