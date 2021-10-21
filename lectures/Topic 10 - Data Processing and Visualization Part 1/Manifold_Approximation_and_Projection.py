import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import plotly.graph_objs as go
# import plotly.plotly as py
import chart_studio.plotly as py
import plotly.tools as tls
import plotly.figure_factory as ff

# prepare color for other stuffs
import umap
from sklearn.manifold import TSNE
import cufflinks as cf
sns.set(color_codes=True)
cf.set_config_file(offline=False, world_readable=True, theme='pearl')
np.random.seed(67)

# generate the dataset
columns = ["age", 
           "sex", 
           "cp", 
           "trestbps",
           "chol", 
           "fbs", 
           "restecg",
           "thalach",
           "exang", 
           "oldpeak",
           "slope", 
           "ca", 
           "thal", 
           "num"]

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data")
df.columns = columns

# Replace Every Number greater than 0 to 1 to mark heart disease
df.loc[df['num'] > 0 , 'num'] = 1
df.ca = pd.to_numeric(df.ca, errors='coerce').fillna(0)
df.thal = pd.to_numeric(df.thal, errors='coerce').fillna(0)

textd = [0 if cl==0 else 1 for cl in df['num']]
textd = np.array(textd)
digit_color=['rgba(236,223,1, 0.85)','rgba((1,223,102, 0.7))']
colors=[digit_color[d] for d in textd]
tooltips=list(map(str, textd))

dim_reduced = umap.UMAP(n_neighbors=15, n_components=3, min_dist=0.98, random_state=7654321).fit_transform(df.loc[:, df.columns != 'num'])
proj_3d = TSNE(n_components=3, perplexity=20, random_state=7654321).fit_transform(df.loc[:, df.columns != 'num'])

# plot 1 - Uniform Manifold Approximation and Projection
plt.close('all')
from mpl_toolkits.mplot3d.axes3d import Axes3D
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(dim_reduced[:,0], dim_reduced[:,1], dim_reduced[:,2],c=textd ,cmap=plt.cm.PiYG,s=60  )
# make simple, bare axis lines through space:
# Inpired: https://python-graph-gallery.com/372-3d-pca-result/
xAxisLine = ((min(dim_reduced[:,0])-np.mean(dim_reduced[:,0]), 
              max(dim_reduced[:,0])+np.mean(dim_reduced[:,0])), (0, 0), (0,0))
ax.plot(xAxisLine[0], xAxisLine[1], xAxisLine[2], 'g')

yAxisLine = ((0, 0),(min(dim_reduced[:,1])-np.mean(dim_reduced[:,1]), 
                     max(dim_reduced[:,1])+np.mean(dim_reduced[:,1])),  (0,0))
ax.plot(yAxisLine[0], yAxisLine[1], yAxisLine[2], 'r')

zAxisLine = ( (0, 0), (0,0),(min(dim_reduced[:,2])-np.mean(dim_reduced[:,2]),
                             max(dim_reduced[:,2])+np.mean(dim_reduced[:,2])),)
ax.plot(zAxisLine[0], zAxisLine[1], zAxisLine[2], 'b')

plt.title('Uniform Manifold Approximation and Projection')
plt.show()

# plot 2 - t-sne

plt.close('all')
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(proj_3d[:,0], proj_3d[:,1], proj_3d[:,2],c=textd ,cmap=plt.cm.viridis,s=60  )

# make simple, bare axis lines through space:
# Inpired: https://python-graph-gallery.com/372-3d-pca-result/
xAxisLine = ((min(proj_3d[:,0])-np.mean(proj_3d[:,0]), 
              max(proj_3d[:,0])+np.mean(proj_3d[:,0])), (0, 0), (0,0))
ax.plot(xAxisLine[0], xAxisLine[1], xAxisLine[2], 'g')

yAxisLine = ((0, 0),(min(proj_3d[:,1])-np.mean(proj_3d[:,1]), 
                     max(proj_3d[:,1])+np.mean(proj_3d[:,1])),  (0,0))
ax.plot(yAxisLine[0], yAxisLine[1], yAxisLine[2], 'r')

zAxisLine = ( (0, 0), (0,0),(min(proj_3d[:,2])-np.mean(proj_3d[:,2]),
                             max(proj_3d[:,2])+np.mean(proj_3d[:,2])),)
ax.plot(zAxisLine[0], zAxisLine[1], zAxisLine[2], 'b')
plt.title('t-SNE')
plt.show()