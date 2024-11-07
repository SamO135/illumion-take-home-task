from core.movie_viewer import MovieViewer
from core.rectangle_selector_tool import RectangleSelectorTool
from core.intensity_analyser import IntensityAnalyser
import matplotlib.pyplot as plt

class MovieAnalysisApp:
    """Main program application."""
    def __init__(self, movie_file: str, time_file: str):
        """MovieAnalysisApp constructor.
        
        Args:
            movie_file (str): file path to movie file
            time_file (str): file path to time file
        """
        self.movie_viewer = MovieViewer(movie_file, time_file)
        self.rectangle_selector_tool = RectangleSelectorTool(self.movie_viewer.ax, self.on_rectangle_selected)
        self.intensity_analyser = IntensityAnalyser(self.movie_viewer.movie_data, self.movie_viewer.time_data)
        self.rectangle_count = 1

    def on_rectangle_selected(self, x1: float, y1: float, x2: float, y2: float):
        """Callback for handling rectangle selection and intensity analysis.
        
        Args:
            x1 (float): x1 coordinate of rectangle
            y1 (float): y1 coordinate of rectangle
            x2 (float): x2 coordinate of rectangle
            y2 (float): y2 coordinate of rectangle
        """
        mean_intensity = self.intensity_analyser.calculate_mean_intensity(x1, y1, x2, y2)
        colour = self.rectangle_selector_tool.add_rectangle_to_frame(x1, y1, x2, y2)
        self.intensity_analyser.plot_intensity_over_time(mean_intensity, colour, self.rectangle_count)
        self.rectangle_count += 1

    def run(self):
        """Display the plot."""
        plt.show()