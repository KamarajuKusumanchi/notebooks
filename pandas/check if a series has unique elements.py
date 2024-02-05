# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# You can use is_unique to check if all elements in a Series are unique or not.
# By default, it treats np.nan as any other value. So if there are multiple np.nan s, it will return false.
# If this not desired, run dropna() first and then do is_unique.

import pandas as pd

pd.Series([1, 2, 3]).is_unique

pd.Series([1, 2, 2]).is_unique

import numpy as np
pd.Series([1, 2, 3, np.nan, np.nan]).is_unique

pd.Series([1, 2, 3, np.nan, np.nan]).dropna().is_unique

pd.Series([1, 2, 2, np.nan, np.nan]).is_unique

pd.Series([1, 2, 2, np.nan, np.nan]).dropna().is_unique


