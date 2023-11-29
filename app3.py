import streamlit as st  
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
def app():
    df = pd.read_excel('CANIS_PRC_state_media_on_social_media_platforms-2023-11-03.xlsx')
    st.title("Sum of Total Follwers VS Region Of focus")
    selected_entity_1 = st.selectbox("Select Entity Owner:", df['Entity owner (English)'])
    st.write("It provides a quick overview of which platforms are more popular or effective for the entity owner in terms of audience engagement.")
    df = df[['Region of Focus','Entity owner (English)','X (Twitter) Follower #', 'YouTube Subscriber #', 'Instagram Follower #','Facebook Follower #','Threads Follower #','TikTok Subscriber #']]
    df = df.fillna(0)
    df['Total Followers'] = df[['X (Twitter) Follower #', 'Facebook Follower #', 'Instagram Follower #', 'Threads Follower #', 'YouTube Subscriber #', 'TikTok Subscriber #']].sum(axis=1)
    selected_row_1 = df[df['Entity owner (English)'] == selected_entity_1]
    fig, ax = plt.subplots(figsize=(20,50))
    sns.barplot(x=selected_row_1['Total Followers'].values[0], y=selected_row_1['Region of Focus'], data=df, palette='viridis', estimator=sum)
    plt.title('Total Followers by Region of Focus')
    plt.ylabel('Region of Focus')
    plt.xlabel('Total Followers')
    st.pyplot(fig)
    st.write("CGTN Culture Express evolved as a cultural ambassador, reflecting its message throughout the Anglosphere. The organization, which was affiliated with the Central Publicity Department, made its impact on Twitter and Instagram by weaving cultural threads that resonated with a worldwide audience. The lack of particular platforms suggested a targeted strategy suited to certain platforms that matched with its goal.Meanwhile, the All-China Students' Federation, which is firmly embedded in the heart of China, used Twitter to speak the language of unification. The statistics whispered tales of a vast following, implying the message's appeal among the youth.")
    