from core.movie_analysis_app import MovieAnalysisApp

if __name__ == "__main__":
    movie_file = "data/movie.npy"
    time_file = "data/time.npy"
    app = MovieAnalysisApp(movie_file, time_file)
    app.run()