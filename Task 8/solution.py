def bootstrap_this(data):
    import numpy as np
    pick = np.random.choice(data, (len(data), 5000))
    value = np.mean(data[pick], axis=0)
    means = np.mean(value)
    error = np.std(value)
    return means, error, value
