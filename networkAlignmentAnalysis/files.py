import getpass
import socket
from pathlib import Path

PATH_REGISTRY = {
    'DESKTOP-M2J64J2': Path('C:/Users/andrew/Documents/machineLearning'),
    'Celia': Path('/Users/celiaberon/Documents/machine_learning'),
    'cberon': Path('/n/home00/cberon/alignment/'),
    'corwin': Path('/Users/corwin/Building')
}

def get_hostname():
    return socket.gethostname()

def get_username():
    return getpass.getuser()

def local_path():
    """method for defining the local root path for datasets and results"""
    hostname = get_hostname()
    if hostname.lower().startswith('celia'):
        hostname = 'Celia'
    hostname = hostname if hostname in PATH_REGISTRY else get_username()
    if hostname not in PATH_REGISTRY:
        raise ValueError(f"hostname ({hostname}) is not registered in the path registry")
    # return path
    return PATH_REGISTRY[hostname]


def results_path():
    """method for returning relative path to results generated by this package"""
    return local_path() / 'results'

def data_path():
    """method for returning the relative path containing datasets"""
    return local_path() / 'datasets'

def dataset_path(dataset):
    """path to specific stored datasets (they all have different requirements)"""
    if dataset=='MNIST':
        return data_path()
    elif dataset=='CIFAR10' or dataset=='CIFAR100':
        return data_path()
    elif dataset=='ImageNet':
        return Path('/n/holyscratch01/bsabatini_lab/Lab/ImageNet/')
