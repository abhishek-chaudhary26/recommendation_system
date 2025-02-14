import csv

def fetch_movie_titles(csv_file):
    titles = []
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if there is one
        for row in reader:
            if row:  # Check if the row is not empty
                titles.append(row[1])  # Assuming the second column contains the movie titles
    return titles

def display_options(titles):
    print("Select a movie:")
    for index, title in enumerate(titles, start=1):
        print(f"{index}. {title}")

if __name__ == "__main__":
    movie_titles = fetch_movie_titles('DataSet/movies.csv')  # Replace with your CSV file name
    display_options(movie_titles)