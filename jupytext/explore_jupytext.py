# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# + [markdown] tags=[]
# Checking how jupytext works using the notebook shown in https://www.youtube.com/watch?v=SDYdeVfMh48.
# -

import plotly.express as px

df = px.data.iris()

df

fig = px.scatter(df,
                 x="sepal_width",
                 y="sepal_length",
                 color="species")

fig.layout.title = 'The Iris dataset'

fig.show()
