try:
    from matplotlib.colors import LinearSegmentedColormap
except:
    pass
import logging

logger = logging.getLogger(__name__)

def custom_colormap(numcolors=11, colors=['blue','white','red'], name='custom'):
    """ 
    Create a custom colormap.  Default settings creates a colormap named 'custom'
    with 11 bins which transitions from blue to white to red.
    
    Parameters
    -----------
    numcolors : int (optional)
        Number of bins in the colormap.
        
    colors : list of colors (optional)
        Colors can be specified in any way understandable by 
        matplotlib.colors.ColorConverter.to_rgb().  
    
    name : str (optional)
        Name of the colormap
        
    Returns
    --------
    cmap : matplotlib.colors.LinearSegmentedColormap object
    """
    cmap = LinearSegmentedColormap.from_list(name=name, 
                                             colors = colors,
                                             N=numcolors)
    return cmap
