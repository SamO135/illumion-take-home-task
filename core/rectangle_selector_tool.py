from matplotlib.widgets import RectangleSelector
from matplotlib.patches import Rectangle
import matplotlib.cm as cm
import itertools


class RectangleSelectorTool:
    """Class to manage rectangle selection."""
    def __init__(self, ax, on_select_callback: callable):
        """RectangleSelectorTool constructor.
        
        Args:
            ax (Axes): Movie viewer axis
            on_select_callback (callable): callback function for when rectangle is selected
        """
        self.ax = ax
        self.on_select_callback = on_select_callback
        self.rect_selector = RectangleSelector(self.ax, self.on_select, useblit=True, button=[1], interactive=True)
        self.colours = itertools.cycle(cm.tab10.colors)  # Use a color map for unique rectangle colors
        self.rectangles = {}

    def on_select(self, eclick, erelease):
        """Callback for when user draws a rectangle.
        
        Args:
            eclick (MouseEvent): coordinates when mouse was clicked
            erelease (MouseEvent): coordinates when mouse was released
        """
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata
        if self.on_select_callback:
            self.on_select_callback(x1, y1, x2, y2)

    def add_rectangle_to_frame(self, x1: float, y1: float, x2: float, y2: float) -> Rectangle:
        """Draw the rectangle onto the frame so it is persistent.
        
        Args:
            x1 (float): x1 coordinate of rectangle
            y1 (float): y1 coordinate of rectangle
            x2 (float): x2 coordinate of rectangle
            y2 (float): y2 coordinate of rectangle

        Returns:
            Rectangle: the rectangle object
        """
        colour = next(self.colours)
        rectangle = Rectangle((x1, y1), x2 - x1, y2 - y1, linewidth=2, edgecolor=colour, facecolor='none')
        self.ax.add_patch(rectangle)
        self.rectangles[rectangle] = colour
        return rectangle