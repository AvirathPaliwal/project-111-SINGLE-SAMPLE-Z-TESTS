import statistics;
import plotly.graph_objects as go;
import plotly.figure_factory as ff;
import pandas as pd;
import random;
data = pd.read_csv("medium_data.csv")
dataList = data["reading_time"].tolist()

populationMean = statistics.mean(dataList)
print("Population Mean:",populationMean)

def random_mean_set(counter):
  dataSet = []
  for i in range(0,counter):
    randomIndex = random.randint(0,len(dataList)-1)
    value = dataList[randomIndex]
    dataSet.append(value)
  randomMean = statistics.mean(dataSet)
  return randomMean

def show_fig(meanList):
  figData = meanList

  fig = ff.create_distplot([figData],["Reading Time"],show_hist = False)

  samplingMean = statistics.mean(meanList)
  sd = statistics.stdev(meanList)
  
  std_1_start,std_1_end = samplingMean - sd,samplingMean + sd
  std_2_start,std_2_end = samplingMean - (2*sd),samplingMean + (2*sd)
  std_3_start,std_3_end = samplingMean - (3*sd),samplingMean + (3*sd)
  
  print("\nStandard Deviation 1:",std_1_start,",",std_1_end)
  print("Standard Deviation 2:",std_2_start,",",std_2_end)
  print("Standard Deviation 3:",std_3_start,",",std_3_end)

  fig.add_trace(go.Scatter(x = [std_1_start,std_1_start],y = [0,0.8]))
  fig.add_trace(go.Scatter(x = [std_1_end,std_1_end],y = [0,0.8]))
  fig.add_trace(go.Scatter(x = [std_2_start,std_2_start],y = [0,0.8]))
  fig.add_trace(go.Scatter(x = [std_2_end,std_2_end],y = [0,0.8]))
  fig.add_trace(go.Scatter(x = [std_3_start,std_3_start],y = [0,0.8]))
  fig.add_trace(go.Scatter(x = [std_3_end,std_3_end],y = [0,0.8]))


  fig.add_trace(go.Scatter(x = [samplingMean,samplingMean],y = [0,0.8]))
  sampleMean = statistics.mean(dataList)
  fig.add_trace(go.Scatter(x = [sampleMean,sampleMean],y = [0,0.8]))
  
  zTest = (sampleMean - samplingMean)/sd
  print("\nZ Test:",zTest)

  fig.show()

meanList = []
for i in range(0,100):
  meanSet = random_mean_set(30)
  meanList.append(meanSet)
show_fig(meanList)