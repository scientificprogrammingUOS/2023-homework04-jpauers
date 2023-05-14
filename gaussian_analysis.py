import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    
    if not (isinstance(loc, (int, float)) and isinstance(scale, (int, float)) and \
        isinstance(lower_bound, (int, float)) and isinstance(upper_bound, (int, float))):
        raise TypeError("At least one of the inputs is not an int or float!")
    if lower_bound >= upper_bound:
        raise ValueError("Lower bound is not smaller than upper bound!")

    sample = np.random.normal(loc, scale, 100)
    sample = sample[sample <= upper_bound]
    sample = sample[sample >= lower_bound]
    
    ret = (sample.mean(), sample.std())

    return ret  


if __name__ == "__main__":
    # use this for your own testing!
    # print(gaussian_analysis(10, 5, 0, 100))
    pass
