import streamlit as st
import pickle
import pandas as pd

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])
   
    recommended_movies = []
    for i in movie_list[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

# Load movies data for recommendation
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Load similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))



st.sidebar.markdown(
    """
    <style>
        /* Sidebar title style */
        .sidebar-title {
            font-size: 24px;
            color: #FF5733;
            margin-bottom: 20px;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("<h1 class='sidebar-title'>Movie Recommender System</h1>", unsafe_allow_html=True)


# Movie selection dropdown for recommendation
# st.sidebar.title("Movie Recommender System")
selected_movie_name = st.sidebar.selectbox(
    "Select a movie from the list:", 
    movies['title'].values
)

# Recommendation button
if st.sidebar.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    st.sidebar.write("Recommended Movies:")
    for i, recommendation in enumerate(recommendations, start=1):
        st.sidebar.write(f"{i}. {recommendation}") 






# Video section
st.title("Released Movie Trailers")

st.subheader("Avatar Movie Trailer")
# Add video
st.video("avatar.mp4")

st.subheader("The Dark Knight Rises Trailer")
# Add video
st.video("The Dark Knight Rises.mp4")

st.subheader("SKYFALL  Trailer")
# Add video
st.video("SKYFALL.mp4")


# Favourite movies section
st.title("Favourite Movies")

# List of favourite movies
favourite_movies = [
    {
        "title": "Avatar", 
        "image": "avatar.png", 
        "description": " Avatar, American science fiction film series and media franchise created by director James Cameron. The films follow a U.S. Marine named Jake Sully (Sam Worthington) who becomes part of a program in which human colonizers explore and exploit an alien world called Pandora. The humans interact with a humanoid species called the Na’vi by inhabiting genetically engineered “avatar” bodies that resemble those of the Na’vi. It is one of the most successful movie series of all time, with its first two films each surpassing $2 billion at the global box office. It has also inspired comic books, video games, and a section of a theme park. A third film, potentially titled Avatar: The Seed Bearer, is currently planned for 2025. The Avatar film series is not to be confused with the unrelated Avatar: The Last Airbender animated television program and its associated franchise.   https://www.britannica.com/topic/Avatar-franchise", 
        "author": "James Cameron", 
        "hero": "Sam Worthington",
        "movie_link": "https://www.imdb.com/title/tt0499549/"
    },
    {
        "title": "Predators", 
        "image": "Predators.png", 
        "description": "Predictors (2010) is a science fiction action film directed by Nimród Antal. The movie follows a group of skilled mercenaries, soldiers, criminals, and a doctor who find themselves stranded on an alien planet. As they navigate this hostile environment, they realize they are being hunted by a race of technologically advanced extraterrestrial predators. The diverse group of characters must band together to survive and figure out why they were chosen as prey. Along the way, they uncover the predators' hunting grounds, discovering the true extent of the danger they face. As the tension escalates, the group must rely on their wits, combat skills, and teamwork to outsmart their formidable adversaries and escape the planet alive.  Filled with intense action sequences, suspenseful moments, and twists, Predators delivers a thrilling and adrenaline-pumping experience for fans of the franchise. With its dark atmosphere and menacing alien creatures, the film offers a fresh take on the classic predator concept while staying true to the spirit of the original. ",
        "author": "John McTiernan", 
        "hero": "Arnold Schwarzenegger",
        "movie_link": "https://www.imdb.com/title/tt1424381/?ref_=fn_rvi_tt_i_5"
    },
    {
        "title": "Spider-Man 2", 
        "image": "spiderman 2.png", 
        "description": "Spider-Man 2 (2004) is a superhero film directed by Sam Raimi and based on the Marvel Comics character Spider-Man. The movie continues the story of Peter Parker (played by Tobey Maguire), a young man who struggles to balance his personal life with his responsibilities as the masked crime-fighter Spider-Man. In this installment, Peter faces numerous challenges, including his strained relationship with Mary Jane Watson (played by Kirsten Dunst), financial difficulties, and doubts about his role as a superhero. Meanwhile, a new villain emerges in the form of Dr. Otto Octavius (played by Alfred Molina), a brilliant scientist whose experiment goes awry, turning him into the mechanical-armed supervillain known as Doctor Octopus. As Doctor Octopus wreaks havoc on New York City, Peter must confront his inner demons and rediscover what it truly means to be a hero. With the help of his friends and allies, including his best friend Harry Osborn (played by James Franco) and Aunt May (played by Rosemary Harris), Peter must rise to the challenge and stop Doctor Octopus before it's too late.",
        "author": "Sam Raimi", 
        "hero": "Tobey Maguire",
        "movie_link": "https://www.imdb.com/title/tt0316654/?ref_=fn_al_tt_1"
    }
]

# Display favourite movies with images, descriptions, and links
for movie in favourite_movies:
    st.subheader(movie["title"])
    st.image(movie["image"], caption=movie["title"], width=250)
    st.write(f"**Author:** {movie['author']}")
    st.write(f"**Hero:** {movie['hero']}")
    st.write(f"**Movie Link:** [{movie['title']}]({movie['movie_link']})")
    if st.button(f"Read more about {movie['title']}"):
        st.write(movie["description"])



# Add rating input
    rating = st.slider(f"Rate {movie['title']}", min_value=0, max_value=5, step=1)

    # Add text input for reviews
    review = st.text_input(f"Review {movie['title']}", "")

    

    # Display ratings and reviews
    st.write(f"Your Rating: {rating}/5")
    if review:
        st.write(f"Your Review: {review}")



# Upcoming movies section
st.title("Upcoming Hollywood Movies 2024 ")


# List of upcoming movies
upcoming_movies = [
    {
        "title": "Upcoming Alien: Romulus Movie", 
        "image": "upcoming Alien.png", 
        "description": "The Alien: Romulus release date has been set for August 16, 2024. The announcement of the new Alien movie release date came in mid-2023, months after director Fede Alvarez shared the first production photo of the movie — playfully revealing the return of the iconic face-hugger wrapped around a slate board.", 
        "release_date": "16th August, 2024" ,
        "author": "Dan O'Bannon & Ronald Shusett", 
        "hero": "Cailee Spaeny"
    },
    {
        "title": "Upcoming Joker: Folie à Deux  Movie", 
        "image": "All about folie A deux.png", 
        "description": "oker: Folie à Deux is an upcoming American musical psychological thriller film directed by Todd Phillips from a screenplay co-written with Scott Silver. Loosely based on DC Comics characters, it is the sequel to Joker (2019), and stars Joaquin Phoenix as the Joker and Lady Gaga as his love interest, Harley Quinn. FOR MORE -> https://www.imdb.com/title/tt11315808/ " , 
        "author": "Scott Silver  &  Todd Phillips ", 
        "hero": "Joaquin Phoenix"
    }
]


# Display upcoming movies with images and details
for movie in upcoming_movies:
    st.subheader(movie["title"])
    st.image(movie["image"], caption=movie["title"], width=250)
    st.write(f"**Author:** {movie['author']}")
    st.write(f"**Hero:** {movie['hero']}")
    if st.button(f"Read more about {movie['title']}"):
        st.write(movie["description"])

# upcoming movie trailers 
# Video section
st.title("Upcoming Movie Trailers")

st.subheader("Alien: Romulus Movie")
# Add video
st.video("Alien_ Romulus.mp4")

st.subheader("Joker_ Folie à Deux Movie Trailer")
# Add video
st.video("Joker_ Folie à Deux.mp4")


# Bollywood movies section
st.title("Upcoming Bollywood Movies 2024")

# List of upcoming Bollywood movies
upcoming_bollywood_movies = [
    {
        "title": "Pushpa 2: The Rule", 
        "image": "pushpa 2 .png", 
        "description": "Pushpa 2: The Rule is an upcoming Indian Telugu-language action drama film directed and written by Sukumar under his Sukumar Writings banner and produced by Naveen Yerneni and Yalamanchili Ravi Shankar under their Mythri Movie Makers banner. The film stars Allu Arjun in the titular role, alongside Fahadh Faasil, Rashmika Mandanna, Dhananjay, Rao Ramesh, Sunil and Anasuya Bharadwaj, who are all reprising their roles from the previous film. It is the second installment in the Pushpa film series and the sequel to Pushpa: The Rise.",
        "release_date": " August 15, 2024" ,
        "Author": "Sukumar", 
        "lead_actor": "Allu Arjun ",
        "lead_actress": "Rashmika Mandanna"
    },
    {
        "title": "Devara Part 1", 
       "image": "Devara.jpg", 
        "description": "Devara: Part 1 is an upcoming Indian Telugu-language action drama film written and directed by Koratala Siva. Produced by Sudhakar Mikkilineni and Kosaraju Harikrishna under the banners Yuvasudha Arts and N. T. R",
        "release_date": "10 October 2024",
        "Author": " Koratala Siva", 
        "lead_actor": "N. T. Rama Rao Jr",
        "lead_actress": "Janhvi Kapoor "
    }
]

# Display upcoming Bollywood movies with images and details
for movie in upcoming_bollywood_movies:
    st.subheader(movie["title"])
    st.image(movie["image"], caption=movie["title"], width=250)
    st.write(f"**Author:** {movie['Author']}")
    st.write(f"**Lead Actor:** {movie['lead_actor']}")
    st.write(f"**Lead Actress:** {movie['lead_actress']}")
    st.write(f"**Release Date:** {movie['release_date']}")
    if st.button(f"Read more about {movie['title']}"):
        st.write(movie["description"])


# upcoming movie trailers 
# Video section
st.title("Upcoming Movie Trailer")

st.subheader("Devara Part 1 Movie")
# Add video
st.video("DEVARA Part-1.mp4")

st.subheader("Pushpa 2: The Rule Movie Trailer")
# Add video
st.video("Pushpa 2 The Rule.mp4")
