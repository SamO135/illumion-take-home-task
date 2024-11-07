import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

class MovieViewer:
    """Class to for displaying movie frames with a slider."""
    def __init__(self, movie_file: str, time_file: str):
        """MovieViewer constructor.
        
        Args: 
            movie_file (str): file path to movie file
            time_file (str): file path to time file
        """
        # Load data
        self.movie_data = np.load(movie_file)  # Shape: (time, y, x)
        self.time_data = np.load(time_file)    # Shape: (time,)
        self.num_frames = self.movie_data.shape[0]

        # Set up figure
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(bottom=0.2)
        self.frame_display = self.ax.imshow(self.movie_data[0], vmin=0, vmax=4095) # 12 bit -> 0-4095
        self.title = self.ax.set_title(f"Frame 0 - Time: {self.time_data[0]:.3f} seconds")
        self.ax.axis("off")
        
        # Create slider
        self.frame_slider = self.create_slider()
        self.frame_slider.on_changed(lambda val: self.update_frame(val))

    def create_slider(self):
        """Creates the slider.
        
        Returns: 
            Slider: the slider object
        """
        ax_slider = plt.axes([0.25, 0.05, 0.5, 0.03])
        frame_slider = Slider(ax_slider, "Frame", 0, self.num_frames - 1, valinit=0, valstep=1)
        return frame_slider

    def update_frame(self, frame_index: int):
        """Updates the the frame based on the slider value.
        
        Args:
            frame_index (int): the index of the movie frame
        """
        self.frame_display.set_data(self.movie_data[frame_index])
        self.title.set_text(f"Frame {frame_index} - Time: {self.time_data[frame_index]:.3f} seconds")
        self.fig.canvas.draw_idle()

