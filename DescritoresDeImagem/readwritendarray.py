import glob
import re
from typing import Literal
from joblib import Parallel, delayed
import numpy as np
import skimage
from .glcm import glcm
from .lbp import lbp
from .lpq import lpq

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

def lpqimageapply(imgpath, winSize: int = 7,decorr: int = 1,mode: str = 'nh'):
    """
    Applies the LPQ (Local Phase Quantization) method to an image.

    Parameters:
        imgpath (str): Path to the image file.
        winSize (int, optional): Window size for LPQ. Default is 7.
        decorr (int, optional): Decorrelation parameter for LPQ. Default is 1.
        mode (str, optional): Mode for LPQ ('nh' for normalized histogram). Default is 'nh'.

    Returns:
        np.ndarray: Feature vector or matrix produced by the LPQ method.
    """
    imgopen=skimage.io.imread(imgpath,as_gray=True) # open image in as gray 
    img_info=lpq(imgopen,winSize=winSize,mode=mode,decorr=decorr) # aplly glcm in image open
          
    return img_info 

def  glcmimageapply(imgpath,distances=[1,3,5],angles=np.deg2rad([0,90,180,270]))-> np.ndarray[tuple[int],np.dtype[np.float64]]:
    """
    Args
    
    img (np.ndarray): 
        A 2D grayscale image array for which the GLCM is computed. The image 
        should be of type `np.ndarray` and must be 2-dimensional.
            
    distances (Union[List[int], np.ndarray]): 
        A list or array of pixel pair distances for which the GLCM is computed. 
        Default values are [1, 3, 5].
        
    angles (Union[List[float], np.ndarray]): 
        A list or array of angles (in radians) defining the direction for GLCM computation. 
        Default values are the radian equivalents of [0, 90, 180, 270] degrees.
    """
    imgopen=skimage.io.imread(imgpath,as_gray=True) # open image in as gray 
    img_info=glcm(imgopen,distances=distances,angles=angles) # aplly glcm in image open
          
    return img_info


 
def writendarry(filename:str,array:np.ndarray,delimiter="|")->None:
    """
    Parameters:
        filename (str):Path to the image file.
        array(np.ndarray):Data write file.
        delimiter(str): string to delimiter  data.
    """
    with open(file=filename,mode="w") as file:
        for i in array:
            file.writelines(np.array2string(i,separator=","))
            file.write(delimiter)



def readfilendarray(filename:str,delimiter="|",data="f")->np.ndarray:
    """
    Applies the LBP (Local Binary Patterns) method to an image.

    Parameters:
        filename(str): Path to the image file.
        delimiter(str): string to delimiter data.
        data: type of data in file (s(str) or f(float))        
    Returns:
        np.ndarray: the feature vector.
    """
    if data=="f":
        array=[]
        with open(file=filename,mode="r") as f:
            lines=f.read().split(delimiter)
            for datastr in lines:
                data=datastr.replace("\n","").replace(" ","").strip("[]").split(",")
                arr=[float(i) for i in data if i.strip()]
                array.append(arr)
            array.pop()
            return np.array(array)
    elif data=="s":
        with open(file=filename,mode="r") as f:
            lines=f.read().replace("'","").split(delimiter)
            lines.pop()
            return np.array(lines)



def extractimagesdescriptor(file: str, filename: str,pathimg:str, descriptor: Literal["LPQ", "LBP", "GLCM"] = 'GLCM', jobs_n: int = -1,):
    
    pathimageitetor = glob.glob(pathimg)
    writeresult(pathimageitetor, file,pathimg)

    if descriptor == "LPQ":
        def lpq_function(method: Literal['default', 'ror', 'uniform', 'nri_uniform', 'var'] = 'nri_uniform', P: int = 8, R: int = 2): 
            datasetlpq = Parallel(n_jobs=jobs_n)(delayed(lbpimageaplly)(i, P, R, method) for i in pathimageitetor)
            writendarry(filename=filename, array=datasetlpq)
        print("FUNCTION LPQ")
        return lpq_function
    elif descriptor == "LBP":
        def lbp_function(winSize: int = 7, decorr: int = 1, mode: str = 'nh'):
            datasetlbq = Parallel(n_jobs=jobs_n)(delayed(lpqimageapply)(i, winSize, decorr, mode) for i in pathimageitetor)
            writendarry(filename=filename, array=datasetlbq)
        print("FUNCTION LBP")
        return lbp_function
    elif descriptor == "GLCM":
        def glcm_function(distances=[1, 3, 5], angles=np.deg2rad([0, 90, 180, 270])):
            datasetlbq = Parallel(n_jobs=jobs_n)(delayed(glcmimageapply)(i, distances, angles) for i in pathimageitetor)
            writendarry(filename=filename, array=datasetlbq)
        print("FUNCTION GLCM")
        return glcm_function

def writeresult(pathimageitetor, file,pathimg:str):
    y_result = []
    for i in pathimageitetor:
        y_result.append(re.sub(r'\d', '', i.replace(pathimg.split(".")[0], "").replace(".bmp", "").split("/")[-1]))
    writendarry(file, np.array(y_result))  

if __name__=="__main__":
    function_glcm=extractimagesdescriptor(file="../DadosExtraidos/Y_Resultado.txt",filename="../DadosExtraidos/X_TreinoGLCM.txt",descriptor="GLCM",pathimg="../BaseDeDados/*.bmp")
    function_glcm()

    function_lpq=extractimagesdescriptor(file="../DadosExtraidos/Y_Resultado.txt",filename="../DadosExtraidos/X_TreinoLPQ.txt",descriptor="LPQ",pathimg="../BaseDeDados/*.bmp")
    function_lpq()

    function_lbp=extractimagesdescriptor(file="../DadosExtraidos/Y_Resultado.txt",filename="../DadosExtraidos/X_TreinoLBP.txt",descriptor="LBP",pathimg="../BaseDeDados/*.bmp")
    function_lbp()