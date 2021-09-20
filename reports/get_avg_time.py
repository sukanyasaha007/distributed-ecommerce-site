import pandas as pd
import os

data= pd.read_csv(os.environ.get("LATENCY_REPORT_PATH"),names=['request', 'time(sec)'])

print(data.groupby("request").mean())

#/home/sukanyasaha/distributed-system-assignment2/latencyreport.csv