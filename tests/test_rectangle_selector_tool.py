from core.movie_analysis_app import MovieAnalysisApp

def test_add_rectangle_to_frame():
    app = MovieAnalysisApp("data/movie.npy", "data/time.npy")
    # Add a rectangle at (x1, y1) -> (x2, y2)
    x1, y1, x2, y2 = 10, 10, 50, 50
    app.rectangle_selector_tool.add_rectangle_to_frame(x1, y1, x2, y2)
    # Test that the rectangle list has been updated
    assert len(app.rectangle_selector_tool.rectangles) == 1
    # Check it is the correct rectangle
    assert app.rectangle_selector_tool.rectangles[0][0].get_bbox().bounds == (x1, y1, x2 - x1, y2 - y1)

def test_multiple_rectangles():
    app = MovieAnalysisApp("data/movie.npy", "data/time.npy")
    app.rectangle_selector_tool.add_rectangle_to_frame(10, 10, 50, 50)
    app.rectangle_selector_tool.add_rectangle_to_frame(60, 60, 100, 100)
    # Test that 2 rectangles were added to the list
    assert len(app.rectangle_selector_tool.rectangles) == 2
