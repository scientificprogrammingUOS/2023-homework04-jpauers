import numpy as np

# implement the function strange pattern
def strange_pattern(size):
    if isinstance(size, tuple):
        if (size[0] == 0 or size[1] == 0):
            return np.empty((0,0))
    else: 
        raise TypeError(("Please give the size as a tuple (n,m)."))
    
    ret = np.array([np.arange(3, size[0]+3)]* size[1])
    for idx, row in enumerate(ret): row[(row + (idx % 3)) % 3 != 0] = 0

    return np.array(ret, dtype='bool')

    
if __name__ == "__main__":
    # use this for your own testing!
    pass
