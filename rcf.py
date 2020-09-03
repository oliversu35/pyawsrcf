import numpy as np
import pandas as pd
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()
rcf_app = gateway.entry_point

def convertInput(nums):
    if isinstance(nums, pd.core.frame.DataFrame):
        nums = nums.to_numpy()
    arr = gateway.new_array(gateway.jvm.double, len(nums), len(nums[0]))
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            arr[i][j] = float(nums[i][j])
    return arr

def rcf(data, numTree=50, sampleSize=256):
    res = rcf_app.rcf(convertInput(data), numTree, sampleSize)
    return [list(x) for x in res]
