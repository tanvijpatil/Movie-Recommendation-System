import pandas as pd

# Step 1: Create a Sample Dataset
movies_data = {
    'Title': ['The Matrix', 'Inception', 'Interstellar', 'The Godfather', 'Pulp Fiction', 
              'The Dark Knight', 'Fight Club', 'The Shawshank Redemption'],
    'Genre': ['Action', 'Sci-Fi', 'Sci-Fi', 'Crime', 'Crime', 
              'Action', 'Drama', 'Drama']
}

movies_df = pd.DataFrame(movies_data)

# Step 2: Define a Function to Recommend Movies
def recommend_movies(movie_title, movies_df):
    # Check if the movie is in the dataset
    if movie_title not in movies_df['Title'].values:
        return "Sorry, the movie is not in the dataset."

    # Get the genre of the movie the user likes
    movie_genre = movies_df.loc[movies_df['Title'] == movie_title, 'Genre'].values[0]
    
    # Find other movies with the same genre
    recommended_movies = movies_df[movies_df['Genre'] == movie_genre]['Title'].tolist()
    
    # Remove the movie itself from the list
    recommended_movies.remove(movie_title)
    
    # If no recommendations found
    if not recommended_movies:
        return "Sorry, no similar movies found."
    
    return recommended_movies

# Step 3: Main function with User Input
def main():
    # Ask user for their favorite movie
    favorite_movie = input("Enter your favorite movie: ")
    
    # Get recommendations
    recommendations = recommend_movies(favorite_movie, movies_df)

    # Print recommendations
    if isinstance(recommendations, list):
        print(f"Since you liked '{favorite_movie}', you might also like: {', '.join(recommendations)}")
    else:
        print(recommendations)

if __name__ == "__main__":
    main()
