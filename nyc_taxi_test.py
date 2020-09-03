#!/usr/bin/env python3

import urllib.request
import pandas as pd
import rcf


if __name__ == "__main__":
    data_filename = 'nyc_taxi.csv'
    data_source = 'https://raw.githubusercontent.com/numenta/NAB/master/data/realKnownCause/nyc_taxi.csv'
    urllib.request.urlretrieve(data_source, data_filename)
    taxi_data = pd.read_csv(data_filename, delimiter=',')
    taxi_input = taxi_data.value.to_numpy().reshape(-1,1)
    anomaly_scores = rcf.rcf(taxi_input)
    print(anomaly_scores[5600:5620])
