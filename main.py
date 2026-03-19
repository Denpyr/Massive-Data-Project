import pandas as pd
import ast

movies = pd.read_csv("Dataset/tmdb_5000_movies.csv")
credits = pd.read_csv("Dataset/tmdb_5000_credits.csv")
df = pd.merge(movies, credits, left_on="id", right_on="movie_id")

def clean_id(json_text):
    list_names = []
    converted_list = ast.literal_eval(json_text)
    for item in converted_list:
        list_names.append(item["name"])
    return list_names

def cleaning_and_preprocessing(df):
    df.dropna(inplace=True)
    df["release_date"] = pd.to_datetime(df["release_date"], errors='coerce')
    df["release_date"] = df["release_date"].dt.strftime('%d/%m/%Y')
    df.drop(["id"], axis=1, inplace=True)
    df.drop(["movie_id"], axis=1, inplace=True)
    df.drop(["title_y"], axis=1, inplace=True)
    df.rename(columns={"title_x": "title"}, inplace=True)
    df["genres"] = df["genres"].apply(clean_id)
    df["keywords"] = df["keywords"].apply(clean_id)
    df["cast"] = df["cast"].apply(clean_id)
    df["crew"] = df["crew"].apply(clean_id)
    df["production_companies"] = df["production_companies"].apply(clean_id)
    df["production_countries"] = df["production_countries"].apply(clean_id)
    df["spoken_languages"] = df["spoken_languages"].apply(clean_id)
    return df

df = cleaning_and_preprocessing(df)   
df.to_csv('tmdb_5000_pulito.csv', index=False)
print("Dataset salvato con successo!")