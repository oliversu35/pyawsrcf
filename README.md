# pyawsrcf

This is a python wrapper for Amazon Sagemaker's official Random Cut Forest(RCF) algorithm.
The official implementation of RCF algorithm was developed in Java by AWS developers (https://github.com/aws/random-cut-forest-by-aws)
However, the official github repo does not provide Python binding for RCF APIs and make it difficult for ML/AI developer to test the algorithm in their favorite python programs/jupyter notebooks.
Therefore, the goal for this project was bind the RCF algorithms Java API with py4j (https://www.py4j.org/) and expose a python method that can take python list, numpy.ndarray or pandas dataframe and return anomaly scores.

Usage:
 1. run compile.sh to compile the py4j service
 2. start py4j service with start.sh
 3. python API rcf.rcf() would be available for running RCF algorithms

nyc_taxi_test.py is a unit test script that evaluate the sample NYC taxi dataset in AWS's official document  
