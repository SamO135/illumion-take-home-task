from core.intensity_analyser import IntensityAnalyser
from core.movie_viewer import MovieViewer

def test_calculate_mean_intensity():
    mv = MovieViewer("data/movie.npy", "data/time.npy")
    intensity_analyser = IntensityAnalyser(mv.movie_data, mv.time_data)
    # Simulate a rectangle selection at (x1, y1) -> (x2, y2)
    x1, y1, x2, y2 = 10, 10, 50, 50
    mean_intensity = intensity_analyser.calculate_mean_intensity(x1, y1, x2, y2)
    # Check if the mean intensity is an array of correct size
    assert len(mean_intensity) == len(intensity_analyser.time_data)

