from pathlib import Path
import socket

hostname = socket.gethostname()
PATH_REGISTRY = {
    'DESKTOP-M2J64J2': Path('C:/Users/andrew/Documents/machineLearning'),
}

def local_path():
    """method for defining the local root path for datasets and results"""
    if hostname not in PATH_REGISTRY:
        raise ValueError(f"hostname ({hostname}) is not registered in the path registry")
    # return path
    return PATH_REGISTRY[hostname]

def data_path():
    """method for returning the relative path containing datasets"""
    return local_path() / 'datasets'

def dataset_path(dataset):
    """path to specific stored datasets (they all have different requirements)"""
    if dataset=='MNIST':
        return data_path()
