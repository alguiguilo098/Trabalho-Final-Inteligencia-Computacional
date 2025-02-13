import glob
from typing import Literal
from .lbp import lbp
from joblib import Parallel, delayed
import skimage


def lpq_function(pathimg,method: Literal['default', 'ror', 'uniform', 'nri_uniform', 'var'] = 'nri_uniform', P: int = 8, R: int = 2): 
    pathimageitetor = glob.glob(pathimg)
    datasetlpq = Parallel(n_jobs=6)(delayed(lbpimageaplly)(i, P, R, method) for i in pathimageitetor)
    return datasetlpq

def lbpimageaplly(imgpath,P: int = 8,R: int = 2,method: Literal['default', 'ror', 'uniform', 'nri_uniform', 'var'] = 'nri_uniform'):
    """
    Applies the LBP (Local Binary Patterns) method to an image.

    Parameters:
        imgpath (str): Path to the image file.
        P (int, optional): Number of circularly symmetric neighbor points. Default is 8.
        R (int, optional): Radius of the circle. Default is 2.
        method (Literal, optional): Method to extract LBP. Options include:
            - 'default': Basic LBP.
            - 'ror': Rotation invariant.
            - 'uniform': Uniform patterns only.
            - 'nri_uniform': Non-rotation-invariant uniform patterns.
            - 'var': Variance-based patterns. Default is 'nri_uniform'.

    Returns:
        np.ndarray: The resulting LBP image or feature vector.
    """
    
    imgopen=skimage.io.imread(imgpath,as_gray=True) # open image in as gray 
    
    img_info=lbp(image=imgopen,P=P,R=R,method=method) # aplly glcm in image open
          
    return img_info