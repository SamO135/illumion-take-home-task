from core.movie_analysis_app import MovieAnalysisApp
import matplotlib
matplotlib.use('Agg')

def test_rectangle_selection():
    app = MovieAnalysisApp("data/movie.npy", "data/time.npy")
    initial_count = app.rectangle_count
    app.on_rectangle_selected(10, 10, 50, 50)
    assert app.rectangle_count == initial_count + 1
