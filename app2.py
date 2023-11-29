import streamlit as st  
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def app():
    df = pd.read_excel('CANIS_PRC_state_media_on_social_media_platforms-2023-11-03.xlsx')
    st.title("Social Media Followers Comparison")
    selected_entity_1 = st.selectbox("Select Entity 1:", df['Name (English)'])
    selected_entity_2 = st.selectbox("Select Entity 2:", df['Name (English)'])
    selected_row_1 = df[df['Name (English)'] == selected_entity_1]
    selected_row_2 = df[df['Name (English)'] == selected_entity_2]
    st.subheader(f"Social Media Followers for {selected_entity_1}")
    st.subheader(selected_row_1['Name (Chinese)'].values[0])
    st.write(f"Twitter handle : {selected_row_1['X (Twitter) handle'].values[0]}    ",f"     Facebook Page : {selected_row_1['Facebook page'].values[0]}")
    st.write(df[df['Name (English)'] == selected_entity_1][['X (Twitter) Follower #', 'YouTube Subscriber #', 'Instagram Follower #','Facebook Follower #','Threads Follower #','TikTok Subscriber #']])
    st.subheader(f"Social Media Followers for {selected_entity_2}")
    st.subheader(selected_row_2['Name (Chinese)'].values[0])
    st.write(f"Twitter handle : {selected_row_2['X (Twitter) handle'].values[0]}    ",f"     Facebook Page : {selected_row_2['Facebook page'].values[0]}")
    st.write(df[df['Name (English)'] == selected_entity_2][['X (Twitter) Follower #', 'YouTube Subscriber #', 'Instagram Follower #','Facebook Follower #','Threads Follower #','TikTok Subscriber #']])
  
    fig, ax = plt.subplots(figsize=(12, 8))
    platforms = ['Twitter', 'YouTube', 'Instagram', 'Threads', 'Facebook', 'TikTok']
    followers_1 = [selected_row_1['X (Twitter) Follower #'].values[0], selected_row_1['YouTube Subscriber #'].values[0],
               selected_row_1['Instagram Follower #'].values[0], selected_row_1['Threads Follower #'].values[0],
               selected_row_1['Facebook Follower #'].values[0], selected_row_1['TikTok Subscriber #'].values[0]]
    followers_2 = [selected_row_2['X (Twitter) Follower #'].values[0], selected_row_2['YouTube Subscriber #'].values[0],
               selected_row_2['Instagram Follower #'].values[0], selected_row_2['Threads Follower #'].values[0],
               selected_row_2['Facebook Follower #'].values[0], selected_row_2['TikTok Subscriber #'].values[0]]
    width = 0.35
    bar1 = ax.bar([i - width / 2 for i in range(len(platforms))], followers_1, width, label=selected_entity_1)
    bar2 = ax.bar([i + width / 2 for i in range(len(platforms))], followers_2, width, label=selected_entity_2)
    ax.set_xticks(range(len(platforms)))
    ax.set_xticklabels(platforms)
    ax.set_ylabel('Follower Count')
    ax.set_title('Social Media Followers Comparison')
    ax.legend()
    # Display the plot in Streamlit
    st.pyplot(fig)