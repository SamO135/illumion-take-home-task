import numpy as np
import matplotlib.pyplot as plt

class IntensityAnalyser:
    """Class to compute and plot mean intensity within selected rectangles."""
    def __init__(self, movie_data, time_data):
        """IntensityAnalyser constructor.
        
        Args:
            movie_data: the movie data
            time_data: the time data
        """
        # Load data
        self.movie_data = movie_data
        self.time_data = time_data
        self.plot_initialised = False
    
    def calculate_mean_intensity(self, x1: float, y1: float, x2: float, y2: float):
        """Calculate the mean intensity over time in the selected rectangle.
        
        Args:
            x1 (float): x1 coordinate of rectangle
            y1 (float): y1 coordinate of rectangle
            x2 (float): x2 coordinate of rectangle
            y2 (float): y2 coordinate of rectangle
        
        Returns:
            float: the normalised mean intensity
        """
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        highlighted_region = self.movie_data[:, y1:y2, x1:x2]
        mean_intensities = np.mean(highlighted_region, axis=(1, 2))
        return (mean_intensities / mean_intensities[0]) * 100 # Normalise intensities to the first value

    def plot_intensity_over_time(self, mean_intensity: float, colour, label: int):
        """Plot the relative intensity over time for a given region.
        
        Args:
            mean_intensity (float): the normalised mean intensity of the selected region
            colour: the colour of the plot
            label (int): the label of the plot
        """
        # Set up figure
        if not self.plot_initialised:
            self.fig, self.ax = plt.subplots()
            self.ax.set_title(f"Mean Intensity in Selected Region(s) Over Time")
            self.ax.set_ylabel("Relative Intensity (%)")
            self.ax.set_xlabel("Time (s)")
            self.plot_initialised = True
        self.ax.plot(self.time_data, mean_intensity, color=colour, label=f"Rectangle {label}")
        self.ax.legend()
        plt.draw()
        plt.pause(0.001)