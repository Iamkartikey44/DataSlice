import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

st.title("Sampling Techniques Explorer with Visualizations")

st.write("""
        ### Welcone to the Enhanced Sampling Techniques Explorer 📊📊
         In this app, you can upload your dataset and explorer different sampling techniques.
         We've included advanced visualizations like **box plots**, **violin plots**, and **kde plots**, as well as Statistics 
         like **mean** and **standard deviation** to give you a deeper understanding of how sampling  affects your data.
         """)

uploaded_file = st.file_uploader("Upload your dataset", type=['csv','xlsx'])




if uploaded_file is not None:
    # Load data
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("## Dataset Preview")
    st.dataframe(df.head(10))

    st.write("## Summary Statistics")        
    st.write(df.describe())

    #Pre-Sampling Visualizations
    st.write("## Data Distribution Before Sampling")

    for column in df.select_dtypes(include=['float','int']).columns:
        st.write(f"### {column} Distribution")
        fig,ax = plt.subplots()
        sns.histplot(df[column],ax=ax)
        st.pyplot(fig)

    st.write("## Select a Sampling Technique")

    sampling_method = st.selectbox("Sampling Method",[
        "Random Sampling",
        "Stratified Sampling",
        "Cluster Sampling",
        "Systematic Sampling",
        "Reservoir Sampling",
        "Importance Sampling"
    ])    
    sample_size = st.slider("Select  Sample Size",min_value=10,max_value=len(df),value=10)

    sampled_data = pd.DataFrame()

    if sampling_method == "Random Sampling":
        sampled_data = df.sample(n=sample_size,random_state=42,replace=True)
    elif sampling_method =='Stratified Sampling':
        categorical_cols = df.select_dtypes(include=['object','category']).columns
        if len(categorical_cols)>0:
            stratified_col = st.selectbox("Stratify tby column",categorical_cols)
            sampled_data,_ = train_test_split(df,test_size=sample_size/len(df),stratify=df[stratified_col])
        else:
            st.warning("Stratified sampling requires a categorical column.")

    elif sampling_method=='Systematic Sampling':
        step = len(df)//sample_size
        sampled_data = df.iloc[::step,:]

    elif sampling_method=='Cluster Sampling':
        cluster_col = st.selectbox("Cluster by column",df.select_dtypes(include=['object','category']).columns)
        clusters = df[cluster_col].unique()
        selected_clusters = st.multiselect("Select clustersnto sample from",clusters,default=clusters[:2])
        sampled_data = df[df[cluster_col].isin(selected_clusters)]

    elif sampling_method == 'Reservoir Sampling':
        st.info("Reservoir sampling isn't applicable to a static dataset, it's used for streaming data.")

    elif sampling_method == 'Importance Sampling':
        numeric_cols = df.select_dtypes(include=['float','int']).columns
        if len(numeric_cols)>0:
            weight_col   = st.selectbox("Select column for weights",numeric_cols)
            weights = df[weight_col]
            normalized_weights = weights/weights.sum()
            sampled_data = df.sample(n=sample_size,weights=normalized_weights,replace=False)
        else:
            st.warning("Stratified sampling requires a numerical column.")


    if not sampled_data.empty:
        st.write("## Sampled Data Preview")
        st.dataframe(sampled_data.head())

        st.write("## Mean and Standard Deviatiob Comparison")
        numeric_cols = df.select_dtypes(include=['float','int']).columns

        if len(numeric_cols)>0:
            st.write("### Original Data")
            st.write(df[numeric_cols].agg(['mean','std']))

            st.write("### Sampled Data")        
            st.write(sampled_data[numeric_cols].agg(['mean','std']))

        st.write("## Visualizations for Sampled Data")

        for column in numeric_cols:
            
            st.write(f"### {column} Box Plot")
            fig,ax = plt.subplots()
            sns.boxplot(data=sampled_data,x=sampled_data[column],ax=ax)
            st.pyplot(fig)

            st.write(f"### {column} Violin Plot")
            fig,ax = plt.subplots()
            sns.violinplot(data=sampled_data,x=sampled_data[column],ax=ax)
            st.pyplot(fig)

            st.write(f"### {column} KDE Plot")
            fig,ax = plt.subplots()
            sns.kdeplot(data=sampled_data,x=sampled_data[column],ax=ax)
            st.pyplot(fig)

        st.write("## Compare Original  VS Sampled Data")

        for column in numeric_cols:
            st.write(f"### {column} Comparison")
            fig,ax=plt.subplots()
            sns.histplot(df[column],color='blue',label='Original',ax=ax,kde=True)
            sns.histplot(sampled_data[column],color='red',label='Sampled',ax=ax,kde=True)
            plt.legend()
            st.pyplot(fig)


        data_sampled = sampled_data.to_csv(index=False).encode('utf-8')
        st.download_button("Download Sampled Data as CSV",data=data_sampled,file_name='sampled_data.csv',mime='text/csv')    


            




