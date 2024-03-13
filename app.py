import streamlit as st
import pandas as pd
import pickle

import streamlit as st
import requests
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']




def recommend_movies(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sim[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies_names =[]
    recommend_movies_posters = []
    for i in movies_list:
        movie_id =movies.iloc[i[0]].movie_id
        recommend_movies_names.append(movies.iloc[i[0]].title)
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies_names , recommend_movies_posters
# Set up the Streamlit app
st.set_page_config(page_title="Movie Recommendation System", page_icon=":guardsman:", layout="wide")

import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_binary:
        encoded_string = base64.b64encode(image_binary.read()).decode()
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )

# Replace 'background.jpg' with your image file name
image_file = "background.jpeg"
add_bg_from_local(image_file)

def add_logo_from_local(image_file):
    with open(image_file, "rb") as image_binary:
        encoded_string = base64.b64encode(image_binary.read()).decode()
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )

logo = "logo1.png"



# Display the logo at the top left corner
st.image(logo, width=250, use_column_width=False)

# Add custom CSS to position the logo at the top left corner


heading_text = "MOVIE RECOMMENDATION ENGINE"

# Choose a supported color (white in this case)
heading_color = "white"

# Select a desired font family (replace with your preference)
font_family = "Racing Sans One"

st.markdown(f"<h1 style='color: {heading_color}; font-family: {font_family}; text-align: center;'>{heading_text}</h1>", unsafe_allow_html=True)





movies_dict =pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
sim = pickle.load(open("sim.pkl", "rb"))
selected_movie_name = st.selectbox('How would you like to be contacted?',
                      movies['title'].values)

if st.button('Recommend Movie'):
    recommended_movie_names, recommended_movie_posters = recommend_movies(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    for i in range(5):
        with locals()[f"col{i + 1}"]:
            st.markdown(f"<span style='color: {heading_color};'> {recommended_movie_names[i]} </span>", unsafe_allow_html=True)
            st.image(recommended_movie_posters[i])

# Add custom CSS to style the button
st.markdown(
    """
    <style>
    /* Add your custom CSS styles here */
    .stButton>button {
                background-color: black;
                border: none;
                color: white;
                padding: 15px 32px;
               
                display: inline-block;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
    
    }
 
       .stButton>button::before {            
            background-color: orangered; 
      }
    </style>
    """,
    unsafe_allow_html=True
)




