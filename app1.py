import streamlit as st  
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def app():
    df = pd.read_excel('CANIS_PRC_state_media_on_social_media_platforms-2023-11-03.xlsx')
    st.title("Social Media Followers Dashboard")
    selected_entity = st.selectbox("Select Entity:", df['Name (English)'])
    selected_row = df[df['Name (English)'] == selected_entity]
    st.header(selected_row['Name (Chinese)'].values[0])
    st.subheader(f"Social Media Followers for {selected_entity}")
    st.write(f"Twitter handle : {selected_row['X (Twitter) handle'].values[0]}")
    st.write(f"Facebook Page : {selected_row['Facebook page'].values[0]}")
    st.write(selected_row[['X (Twitter) Follower #', 'YouTube Subscriber #', 'Instagram Follower #','Facebook Follower #','Threads Follower #','TikTok Subscriber #']])
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=['Twitter', 'YouTube', 'Instagram','Facebook','Threads','Tiktok'], y=[selected_row['X (Twitter) Follower #'].values[0], selected_row['YouTube Subscriber #'].values[0], selected_row['Instagram Follower #'].values[0],selected_row['Facebook Follower #'].values[0],selected_row['Threads Follower #'].values[0],selected_row['TikTok Subscriber #'].values[0]], palette='viridis', ax=ax)
    plt.title(f'Social Media Followers for {selected_entity}')
    plt.xlabel('Social Media Platform')
    plt.ylabel('Follower Count')
    # Display the plot in Streamlit
    st.pyplot(fig)