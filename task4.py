import pandas as pd


movies_data = {
    'Title': ['The Matrix', 'Inception', 'Interstellar', 'The Godfather', 'Pulp Fiction', 
              'The Dark Knight', 'Fight Club', 'The Shawshank Redemption'],
    'Genre': ['Action', 'Sci-Fi', 'Sci-Fi', 'Crime', 'Crime', 
              'Action', 'Drama', 'Drama']
}

movies_df = pd.DataFrame(movies_data)


def recommend_movies(movie_title, movies_df):

    if movie_title not in movies_df['Title'].values:
        return "Sorry, the movie is not in the dataset."

    movie_genre = movies_df.loc[movies_df['Title'] == movie_title, 'Genre'].values[0]
    

    recommended_movies = movies_df[movies_df['Genre'] == movie_genre]['Title'].tolist()
    

    recommended_movies.remove(movie_title)
    

    if not recommended_movies:
        return "Sorry, no similar movies found."
    
    return recommended_movies


def main():

    favorite_movie = input("Enter your favorite movie: ")
    

    recommendations = recommend_movies(favorite_movie, movies_df)


    if isinstance(recommendations, list):
        print(f"Since you liked '{favorite_movie}', you might also like: {', '.join(recommendations)}")
    else:
        print(recommendations)

if __name__ == "__main__":
    main()
