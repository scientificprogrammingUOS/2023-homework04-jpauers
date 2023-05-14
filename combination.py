import numpy as np

# implement your function to combine two numpy arrays


def combination(arr1, arr2, axis=0):
    arr1 = np.squeeze(arr1)
    arr2 = np.squeeze(arr2)
    # print(arr1)
    # print(arr2)
    # print(arr1.shape[axis], arr2.shape[axis], arr1.shape, arr2.shape)
    # if arr1.shape[axis] != arr2.shape[axis]:
    #  raise ValueError(f"Arrays cannot be combined along axis {axis}")

    # print(list(arr1.shape).pop(axis), list(arr2.shape).pop(axis))
    print(list(arr1.shape)[:axis] + list(arr1.shape)[axis+1:],
          list(arr2.shape)[:axis] + list(arr2.shape)[axis+1:])
    if list(arr1.shape)[:axis] + list(arr1.shape)[axis+1:] != list(arr2.shape)[:axis] + list(arr2.shape)[axis+1:]:
        raise ValueError(f"Arrays cannot be combined along axis {axis}")
    return np.concatenate((arr1, arr2), axis=axis)


if __name__ == "__main__":
    # use this for your own testing!
    a = np.array([[[[1, 2], [3, 4], [5, 6]]]])
    # c = np.array([[[[7, 8], [9, 10], [11, 12]]]])
    b = np.ones((2, 2))

    result = combination(a, b)
    print("\nResults:")
    print(result)
    pass
