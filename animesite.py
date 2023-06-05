import streamlit as st
import pickle
import pandas as pd

def recommend(anime_name):
    anime_index = animes[animes['Title'] == anime_name].index[0]
    distances = sorted(list(enumerate(similarity[anime_index])), reverse=True, key=lambda x: x[1])
    recommended_anime_names = []
    popularity = []
    synopsis = []
    episodes = []
    type = []
    aired = []
    themes = []
    score = []
    for i in distances[1:6]:
        recommended_anime_names.append(animes.iloc[i[0]].Title)
        popularity.append(animes.iloc[i[0]].Popularity)
        synopsis.append(animes.iloc[i[0]].Synopsis)
        episodes.append(animes.iloc[i[0]].Episodes)
        type.append(animes.iloc[i[0]].Type)
        aired.append(animes.iloc[i[0]].Start_Aired)
        themes.append(animes.iloc[i[0]].Themes)
        score.append(animes.iloc[i[0]].Score)

    return recommended_anime_names ,popularity , synopsis , episodes , type , aired , themes , score


anime_dict = pickle.load(open('anime_dict.pkl','rb'))
animes = pd.DataFrame(anime_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Anime Recommendation System')

selected_anime = st.selectbox(
    'Select an Anime from the list :',
    animes['Title'].values)
st.write('Selected Anime :',selected_anime)

if st.button('Recommend'):
    recommended_anime_names,popularity,synopsis,episodes,type,aired,themes,score = recommend(selected_anime)
    container = st.container()
    with container:
        for i in range(0,5):
            st.markdown('------')
            st.write(f"**{recommended_anime_names[i]}**")
            st.markdown(f"Popularity : {popularity[i]}")
            st.markdown(f"Genre : {themes[i]}")
            st.markdown(f"Ratings : {score[i]}")
            st.markdown(f"Type : {type[i]}")
            st.markdown(f"Episodes : {episodes[i]}")
            st.markdown(f"Aired : {aired[i]}")
            st.markdown(synopsis[i])



hide_menu = """<style>
               #MainMenu {visibility : hidden; }
               footer {visibility : hidden;}
               </style>"""
st.markdown(hide_menu,unsafe_allow_html=True)



