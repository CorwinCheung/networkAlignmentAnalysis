import torch
from torch import nn
from .. import utils
from functools import partial

# The LAYER_REGISTRY contains meta parameters for each type of layer used in alignment networks
# each layer type is associated with a few features, including:
# name (string): just for completeness, will only be used for plotting
# layer-handle (lambda method): takes as input a registered layer and returns the part of that layer
#                               to perform alignment methods on. For example, if a registered layer
#                               is layer=nn.Sequential(nn.Linear(10,10), nn.Dropout()), then the layer
#                               handle should be: lambda layer: layer[0])
# alignment_method (callable): the method used to measure alignment for a particular layer
# Note: as of writing this, I only have nn.Linear and nn.Conv2d here, but this will start to be more
# useful and meaningful when reusing typical combinations of layers as a single registered "layer" 
# that include things like dropout, pooling, nonlinearities, etc.
REGISTRY_REQUIREMENTS = ['name', 'layer_handle', 'alignment_method', 'ignore']
LAYER_REGISTRY = {
    nn.Linear: {
        'name': 'linear', 
        'layer_handle': lambda layer:layer, 
        'alignment_method': utils.alignment_linear,
        'ignore': False,
        },

    nn.Conv2d: {
        'name': 'conv2d', 
        'layer_handle': lambda layer:layer, 
        'alignment_method': utils.alignment_convolutional,
        'ignore': False,
        },
}

def default_metaprms_ignore(name):
    """convenience method for named metaparameters to be ignored"""
    metaparameters = {
        'name': name,
        'layer_handle': None,
        'alignment_method': None,
        'ignore': True
    }
    return metaparameters

def default_metaprms_linear(index, name='linear'):
    """convenience method for named metaparameters in a linear layer packaged in a sequential"""
    metaparameters = {
        'name': name,
        'layer_handle': lambda layer: layer[index],
        'alignment_method': utils.alignment_linear,
        'ignore': False,
    }
    return metaparameters

def default_metaprms_conv2d(index, name='conv2d', each_stride=True):
    alignment_method = partial(utils.alignment_convolutional, each_stride=each_stride)
    """convenience method for named metaparameters in a conv2d layer packaged in a sequential"""
    metaparameters = {
        'name': name,
        'layer_handle': lambda layer: layer[index],
        'alignment_method': alignment_method,
        'ignore': False,
    }
    return metaparameters

def check_metaparameters(metaparameters, throw=True):
    """validate whether metaparameters is a dictionary containing the required keys for an alignment network"""
    if not all([required in metaparameters for required in REGISTRY_REQUIREMENTS]):
        if throw:
            raise ValueError(f"metaparameters are missing required keys, it requires all of the following: {REGISTRY_REQUIREMENTS}")
        return False
    return True

# Check the registry to make sure all entries are valid when importing
for layer_type, metaparameters in LAYER_REGISTRY.items():
    if not check_metaparameters(metaparameters, throw=False):
        raise ValueError(f"Layer type: {layer_type} from the `LAYER_REGISTRY` is missing metaparameters. "
                        "It requires all of the following: {REGISTRY_REQUIREMENTS}")