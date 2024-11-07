from core.movie_viewer import MovieViewer
import numpy as np

def test_movie_viewer_init():
    mv = MovieViewer("data/movie.npy", "data/time.npy")
    # Test the data is loaded correctly and has compatible dimensions
    assert mv.time_data.shape[0] == mv.num_frames


def test_update_frame():
    mv = MovieViewer("data/movie.npy", "data/time.npy")
    initial_frame = mv.frame_display.get_array()
    mv.update_frame(5)
    updated_frame = mv.frame_display.get_array()
    # Test frame updates from frame 0 to 5
    assert not np.array_equal(initial_frame, updated_frame)