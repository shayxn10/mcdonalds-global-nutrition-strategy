{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "8b6d315a-fe1d-40aa-8e52-a85e718217fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "93c9b35a-8b2b-4c3f-9ac9-7063cd89bb21",
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "c023d996-dba2-48d5-aefb-e8eead62d188",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>item</th>\n",
       "      <th>servesize</th>\n",
       "      <th>calories</th>\n",
       "      <th>protien</th>\n",
       "      <th>totalfat</th>\n",
       "      <th>satfat</th>\n",
       "      <th>transfat</th>\n",
       "      <th>cholestrol</th>\n",
       "      <th>carbs</th>\n",
       "      <th>sugar</th>\n",
       "      <th>addedsugar</th>\n",
       "      <th>sodium</th>\n",
       "      <th>menu</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>McVeggie Burger</td>\n",
       "      <td>168</td>\n",
       "      <td>402</td>\n",
       "      <td>10.24</td>\n",
       "      <td>13.83</td>\n",
       "      <td>5.34</td>\n",
       "      <td>0.16</td>\n",
       "      <td>2.49</td>\n",
       "      <td>56.54</td>\n",
       "      <td>7.90</td>\n",
       "      <td>4.49</td>\n",
       "      <td>706.13</td>\n",
       "      <td>regular</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>McAloo Tikki Burger</td>\n",
       "      <td>146</td>\n",
       "      <td>339</td>\n",
       "      <td>8.50</td>\n",
       "      <td>11.31</td>\n",
       "      <td>4.27</td>\n",
       "      <td>0.20</td>\n",
       "      <td>1.47</td>\n",
       "      <td>5.27</td>\n",
       "      <td>7.05</td>\n",
       "      <td>4.07</td>\n",
       "      <td>545.34</td>\n",
       "      <td>regular</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>McSpicy Paneer Burger</td>\n",
       "      <td>199</td>\n",
       "      <td>652</td>\n",
       "      <td>20.29</td>\n",
       "      <td>39.45</td>\n",
       "      <td>17.12</td>\n",
       "      <td>0.18</td>\n",
       "      <td>21.85</td>\n",
       "      <td>52.33</td>\n",
       "      <td>8.35</td>\n",
       "      <td>5.27</td>\n",
       "      <td>1074.58</td>\n",
       "      <td>regular</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Spicy Paneer Wrap</td>\n",
       "      <td>250</td>\n",
       "      <td>674</td>\n",
       "      <td>20.96</td>\n",
       "      <td>39.10</td>\n",
       "      <td>19.73</td>\n",
       "      <td>0.26</td>\n",
       "      <td>40.93</td>\n",
       "      <td>59.27</td>\n",
       "      <td>3.50</td>\n",
       "      <td>1.08</td>\n",
       "      <td>1087.46</td>\n",
       "      <td>regular</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>American Veg Burger</td>\n",
       "      <td>177</td>\n",
       "      <td>512</td>\n",
       "      <td>15.30</td>\n",
       "      <td>23.45</td>\n",
       "      <td>10.51</td>\n",
       "      <td>0.17</td>\n",
       "      <td>25.24</td>\n",
       "      <td>56.96</td>\n",
       "      <td>7.85</td>\n",
       "      <td>4.76</td>\n",
       "      <td>1051.24</td>\n",
       "      <td>regular</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Unnamed: 0                    item servesize calories  protien  totalfat  \\\n",
       "0           0         McVeggie Burger      168       402    10.24     13.83   \n",
       "1           1     McAloo Tikki Burger      146       339     8.50     11.31   \n",
       "2           2  McSpicy Paneer Burger      199       652    20.29     39.45   \n",
       "3           3       Spicy Paneer Wrap      250       674    20.96     39.10   \n",
       "4           4     American Veg Burger      177       512    15.30     23.45   \n",
       "\n",
       "   satfat  transfat  cholestrol  carbs  sugar  addedsugar   sodium     menu  \n",
       "0    5.34      0.16        2.49  56.54   7.90        4.49   706.13  regular  \n",
       "1    4.27      0.20        1.47   5.27   7.05        4.07   545.34  regular  \n",
       "2   17.12      0.18       21.85  52.33   8.35        5.27  1074.58  regular  \n",
       "3   19.73      0.26       40.93  59.27   3.50        1.08  1087.46  regular  \n",
       "4   10.51      0.17       25.24  56.96   7.85        4.76  1051.24  regular  "
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv(\"mcdonaldata.csv\")\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "d0423ca8-49a0-4827-b1bb-bef8092e208e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 141 entries, 0 to 140\n",
      "Data columns (total 14 columns):\n",
      " #   Column      Non-Null Count  Dtype  \n",
      "---  ------      --------------  -----  \n",
      " 0   Unnamed: 0  141 non-null    int64  \n",
      " 1   item        141 non-null    object \n",
      " 2   servesize   141 non-null    object \n",
      " 3   calories    141 non-null    object \n",
      " 4   protien     141 non-null    float64\n",
      " 5   totalfat    141 non-null    float64\n",
      " 6   satfat      141 non-null    float64\n",
      " 7   transfat    141 non-null    float64\n",
      " 8   cholestrol  141 non-null    float64\n",
      " 9   carbs       141 non-null    float64\n",
      " 10  sugar       141 non-null    float64\n",
      " 11  addedsugar  141 non-null    float64\n",
      " 12  sodium      141 non-null    float64\n",
      " 13  menu        141 non-null    object \n",
      "dtypes: float64(9), int64(1), object(4)\n",
      "memory usage: 15.6+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "1bc6491b-693a-4942-998a-2edd6df9e0e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>protien</th>\n",
       "      <th>totalfat</th>\n",
       "      <th>satfat</th>\n",
       "      <th>transfat</th>\n",
       "      <th>cholestrol</th>\n",
       "      <th>carbs</th>\n",
       "      <th>sugar</th>\n",
       "      <th>addedsugar</th>\n",
       "      <th>sodium</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>141.000000</td>\n",
       "      <td>141.000000</td>\n",
       "      <td>141.000000</td>\n",
       "      <td>141.000000</td>\n",
       "      <td>141.000000</td>\n",
       "      <td>141.000000</td>\n",
       "      <td>141.000000</td>\n",
       "      <td>141.000000</td>\n",
       "      <td>141.000000</td>\n",
       "      <td>141.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>70.000000</td>\n",
       "      <td>7.493333</td>\n",
       "      <td>10.060355</td>\n",
       "      <td>5.000099</td>\n",
       "      <td>1.108865</td>\n",
       "      <td>26.321128</td>\n",
       "      <td>30.770851</td>\n",
       "      <td>15.409504</td>\n",
       "      <td>10.336950</td>\n",
       "      <td>362.918809</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>40.847277</td>\n",
       "      <td>8.336949</td>\n",
       "      <td>10.435455</td>\n",
       "      <td>4.898097</td>\n",
       "      <td>7.319814</td>\n",
       "      <td>50.348006</td>\n",
       "      <td>20.664969</td>\n",
       "      <td>15.674007</td>\n",
       "      <td>14.283388</td>\n",
       "      <td>477.792553</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>35.000000</td>\n",
       "      <td>0.650000</td>\n",
       "      <td>0.460000</td>\n",
       "      <td>0.330000</td>\n",
       "      <td>0.070000</td>\n",
       "      <td>1.470000</td>\n",
       "      <td>15.630000</td>\n",
       "      <td>2.280000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>41.990000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>70.000000</td>\n",
       "      <td>4.790000</td>\n",
       "      <td>7.770000</td>\n",
       "      <td>4.270000</td>\n",
       "      <td>0.150000</td>\n",
       "      <td>8.390000</td>\n",
       "      <td>29.880000</td>\n",
       "      <td>9.160000</td>\n",
       "      <td>3.640000</td>\n",
       "      <td>150.900000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>105.000000</td>\n",
       "      <td>10.880000</td>\n",
       "      <td>14.160000</td>\n",
       "      <td>7.280000</td>\n",
       "      <td>0.250000</td>\n",
       "      <td>31.110000</td>\n",
       "      <td>45.390000</td>\n",
       "      <td>26.950000</td>\n",
       "      <td>19.230000</td>\n",
       "      <td>530.540000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>140.000000</td>\n",
       "      <td>39.470000</td>\n",
       "      <td>45.180000</td>\n",
       "      <td>20.460000</td>\n",
       "      <td>75.260000</td>\n",
       "      <td>302.610000</td>\n",
       "      <td>93.840000</td>\n",
       "      <td>64.220000</td>\n",
       "      <td>64.220000</td>\n",
       "      <td>2399.490000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Unnamed: 0     protien    totalfat      satfat    transfat  cholestrol  \\\n",
       "count  141.000000  141.000000  141.000000  141.000000  141.000000  141.000000   \n",
       "mean    70.000000    7.493333   10.060355    5.000099    1.108865   26.321128   \n",
       "std     40.847277    8.336949   10.435455    4.898097    7.319814   50.348006   \n",
       "min      0.000000    0.000000    0.000000    0.000000    0.000000    0.000000   \n",
       "25%     35.000000    0.650000    0.460000    0.330000    0.070000    1.470000   \n",
       "50%     70.000000    4.790000    7.770000    4.270000    0.150000    8.390000   \n",
       "75%    105.000000   10.880000   14.160000    7.280000    0.250000   31.110000   \n",
       "max    140.000000   39.470000   45.180000   20.460000   75.260000  302.610000   \n",
       "\n",
       "            carbs       sugar  addedsugar       sodium  \n",
       "count  141.000000  141.000000  141.000000   141.000000  \n",
       "mean    30.770851   15.409504   10.336950   362.918809  \n",
       "std     20.664969   15.674007   14.283388   477.792553  \n",
       "min      0.000000    0.000000    0.000000     0.000000  \n",
       "25%     15.630000    2.280000    0.000000    41.990000  \n",
       "50%     29.880000    9.160000    3.640000   150.900000  \n",
       "75%     45.390000   26.950000   19.230000   530.540000  \n",
       "max     93.840000   64.220000   64.220000  2399.490000  "
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "e4c03923-b793-4642-b623-01db14bb15d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['item'] = df['item'].str.replace('Â', '', regex=False)\n",
    "df['item'] = df['item'].str.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "9d8cb67f-bb3a-49ca-b0fe-050a9892f2d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def classify_food(item):\n",
    "    non_veg_keywords = ['Chicken', 'Fish', 'Egg', 'Sausage', 'McNuggets', 'Strips']\n",
    "    \n",
    "    for word in non_veg_keywords:\n",
    "        if word.lower() in item.lower():\n",
    "            return 'Non-Veg'\n",
    "    return 'Veg'\n",
    "\n",
    "df['food_type'] = df['item'].apply(classify_food)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "edd0aba2-78f9-4b7a-859e-a921816eda04",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "food_type\n",
       "Veg        114\n",
       "Non-Veg     27\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['food_type'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "d34df6f5-5773-4011-8a5b-b16894d300e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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e7qqk0cffbSbcXTMmDG2Y8cO69Klix111FFWvXp1e+utt9L+z9KlS+3888+34sWLu9dfeeWVtnnz5pj3vPnmm13VytKlS1v58uXt7rvvTnt+1apVlidPHlu0aFHasq1bt7plM2fOZM8BKYrgA0CmTZgwwcqWLWufffaZC0RuvPFGu/jii61Jkya2cOFCa9WqlQswdu7c6YIElcU+7bTTbP78+TZ9+nTbuHGjXXLJJenes1ixYjZ37ly77777bNCgQfbuu++yV4BcjCJjADJFrRT79u2zjz76yP2s70uWLGkdOnSwiRMnxsxEOnv2bHvvvffca99+++2091i7dq2bMGz58uVWo0aNdO8pDRs2dEHLsGHDXMtHtWrV7PPPP7d69eq55xXUqOXlgw8+cP8fQOphYjkAmVanTp207/Ply2dlypSxU089NW2ZulZk06ZNtnjxYhcgqMsl3sqVK13wEf+eouBF/x9A7kXwASDTChQoEPOzci+il+ln2b9/v5uTo23btvbvf/873fsowDjQe+r/S968edMmGYvQLKcAUhvBB4Aj4vTTT7eXX37ZqlatavnzH9qp5phjjnFf169f73JHJDr5FEBqIuEUwBHRvXt327Jli3Xq1MnmzZvnulqU/6GRMcrzyAzNZNqoUSOX/6GZTWfNmmV33HEHewxIcQQfAI6IihUr2ieffOICDY2CUW6IhumWKlUqrTslM5566in7/fffrX79+u7/Dx48mD0GpDhGuwAAAK9o+QAAAF4RfAAAAK8IPgAAgFcEHwAAwCuCDwAA4BXBBwAA8IrgAwAAeEXwAQAAvCL4AAAAXhF8AAAArwg+AACAVwQfAADAfPo/oOE1XRpSgHkAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['menu'].value_counts().plot(kind='bar')\n",
    "plt.title(\"Distribution of Menu Categories\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "dc187a58-6fe6-47cc-9a05-d5654addb11a",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "agg function failed [how->mean,dtype->object]",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\groupby\\groupby.py:1944\u001b[39m, in \u001b[36mGroupBy._agg_py_fallback\u001b[39m\u001b[34m(self, how, values, ndim, alt)\u001b[39m\n\u001b[32m   1943\u001b[39m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[32m-> \u001b[39m\u001b[32m1944\u001b[39m     res_values = \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_grouper\u001b[49m\u001b[43m.\u001b[49m\u001b[43magg_series\u001b[49m\u001b[43m(\u001b[49m\u001b[43mser\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43malt\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mpreserve_dtype\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43;01mTrue\u001b[39;49;00m\u001b[43m)\u001b[49m\n\u001b[32m   1945\u001b[39m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m err:\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\groupby\\ops.py:873\u001b[39m, in \u001b[36mBaseGrouper.agg_series\u001b[39m\u001b[34m(self, obj, func, preserve_dtype)\u001b[39m\n\u001b[32m    871\u001b[39m     preserve_dtype = \u001b[38;5;28;01mTrue\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m873\u001b[39m result = \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_aggregate_series_pure_python\u001b[49m\u001b[43m(\u001b[49m\u001b[43mobj\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mfunc\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    875\u001b[39m npvalues = lib.maybe_convert_objects(result, try_float=\u001b[38;5;28;01mFalse\u001b[39;00m)\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\groupby\\ops.py:894\u001b[39m, in \u001b[36mBaseGrouper._aggregate_series_pure_python\u001b[39m\u001b[34m(self, obj, func)\u001b[39m\n\u001b[32m    893\u001b[39m \u001b[38;5;28;01mfor\u001b[39;00m i, group \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28menumerate\u001b[39m(splitter):\n\u001b[32m--> \u001b[39m\u001b[32m894\u001b[39m     res = \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[43mgroup\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    895\u001b[39m     res = extract_result(res)\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\groupby\\groupby.py:2461\u001b[39m, in \u001b[36mGroupBy.mean.<locals>.<lambda>\u001b[39m\u001b[34m(x)\u001b[39m\n\u001b[32m   2458\u001b[39m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m   2459\u001b[39m     result = \u001b[38;5;28mself\u001b[39m._cython_agg_general(\n\u001b[32m   2460\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33mmean\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m-> \u001b[39m\u001b[32m2461\u001b[39m         alt=\u001b[38;5;28;01mlambda\u001b[39;00m x: \u001b[43mSeries\u001b[49m\u001b[43m(\u001b[49m\u001b[43mx\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcopy\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m.\u001b[49m\u001b[43mmean\u001b[49m\u001b[43m(\u001b[49m\u001b[43mnumeric_only\u001b[49m\u001b[43m=\u001b[49m\u001b[43mnumeric_only\u001b[49m\u001b[43m)\u001b[49m,\n\u001b[32m   2462\u001b[39m         numeric_only=numeric_only,\n\u001b[32m   2463\u001b[39m     )\n\u001b[32m   2464\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m result.__finalize__(\u001b[38;5;28mself\u001b[39m.obj, method=\u001b[33m\"\u001b[39m\u001b[33mgroupby\u001b[39m\u001b[33m\"\u001b[39m)\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\series.py:6570\u001b[39m, in \u001b[36mSeries.mean\u001b[39m\u001b[34m(self, axis, skipna, numeric_only, **kwargs)\u001b[39m\n\u001b[32m   6562\u001b[39m \u001b[38;5;129m@doc\u001b[39m(make_doc(\u001b[33m\"\u001b[39m\u001b[33mmean\u001b[39m\u001b[33m\"\u001b[39m, ndim=\u001b[32m1\u001b[39m))\n\u001b[32m   6563\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34mmean\u001b[39m(\n\u001b[32m   6564\u001b[39m     \u001b[38;5;28mself\u001b[39m,\n\u001b[32m   (...)\u001b[39m\u001b[32m   6568\u001b[39m     **kwargs,\n\u001b[32m   6569\u001b[39m ):\n\u001b[32m-> \u001b[39m\u001b[32m6570\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mNDFrame\u001b[49m\u001b[43m.\u001b[49m\u001b[43mmean\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43maxis\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mskipna\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mnumeric_only\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\generic.py:12485\u001b[39m, in \u001b[36mNDFrame.mean\u001b[39m\u001b[34m(self, axis, skipna, numeric_only, **kwargs)\u001b[39m\n\u001b[32m  12478\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34mmean\u001b[39m(\n\u001b[32m  12479\u001b[39m     \u001b[38;5;28mself\u001b[39m,\n\u001b[32m  12480\u001b[39m     axis: Axis | \u001b[38;5;28;01mNone\u001b[39;00m = \u001b[32m0\u001b[39m,\n\u001b[32m   (...)\u001b[39m\u001b[32m  12483\u001b[39m     **kwargs,\n\u001b[32m  12484\u001b[39m ) -> Series | \u001b[38;5;28mfloat\u001b[39m:\n\u001b[32m> \u001b[39m\u001b[32m12485\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_stat_function\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m  12486\u001b[39m \u001b[43m        \u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mmean\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mnanops\u001b[49m\u001b[43m.\u001b[49m\u001b[43mnanmean\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43maxis\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mskipna\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mnumeric_only\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\n\u001b[32m  12487\u001b[39m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\generic.py:12442\u001b[39m, in \u001b[36mNDFrame._stat_function\u001b[39m\u001b[34m(self, name, func, axis, skipna, numeric_only, **kwargs)\u001b[39m\n\u001b[32m  12440\u001b[39m validate_bool_kwarg(skipna, \u001b[33m\"\u001b[39m\u001b[33mskipna\u001b[39m\u001b[33m\"\u001b[39m, none_allowed=\u001b[38;5;28;01mFalse\u001b[39;00m)\n\u001b[32m> \u001b[39m\u001b[32m12442\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_reduce\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m  12443\u001b[39m \u001b[43m    \u001b[49m\u001b[43mfunc\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mname\u001b[49m\u001b[43m=\u001b[49m\u001b[43mname\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43maxis\u001b[49m\u001b[43m=\u001b[49m\u001b[43maxis\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mskipna\u001b[49m\u001b[43m=\u001b[49m\u001b[43mskipna\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mnumeric_only\u001b[49m\u001b[43m=\u001b[49m\u001b[43mnumeric_only\u001b[49m\n\u001b[32m  12444\u001b[39m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\series.py:6478\u001b[39m, in \u001b[36mSeries._reduce\u001b[39m\u001b[34m(self, op, name, axis, skipna, numeric_only, filter_type, **kwds)\u001b[39m\n\u001b[32m   6474\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mTypeError\u001b[39;00m(\n\u001b[32m   6475\u001b[39m         \u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mSeries.\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mname\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m does not allow \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mkwd_name\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mnumeric_only\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m   6476\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33mwith non-numeric dtypes.\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m   6477\u001b[39m     )\n\u001b[32m-> \u001b[39m\u001b[32m6478\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mop\u001b[49m\u001b[43m(\u001b[49m\u001b[43mdelegate\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mskipna\u001b[49m\u001b[43m=\u001b[49m\u001b[43mskipna\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwds\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\nanops.py:147\u001b[39m, in \u001b[36mbottleneck_switch.__call__.<locals>.f\u001b[39m\u001b[34m(values, axis, skipna, **kwds)\u001b[39m\n\u001b[32m    146\u001b[39m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m--> \u001b[39m\u001b[32m147\u001b[39m     result = \u001b[43malt\u001b[49m\u001b[43m(\u001b[49m\u001b[43mvalues\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43maxis\u001b[49m\u001b[43m=\u001b[49m\u001b[43maxis\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mskipna\u001b[49m\u001b[43m=\u001b[49m\u001b[43mskipna\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwds\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    149\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m result\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\nanops.py:404\u001b[39m, in \u001b[36m_datetimelike_compat.<locals>.new_func\u001b[39m\u001b[34m(values, axis, skipna, mask, **kwargs)\u001b[39m\n\u001b[32m    402\u001b[39m     mask = isna(values)\n\u001b[32m--> \u001b[39m\u001b[32m404\u001b[39m result = \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[43mvalues\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43maxis\u001b[49m\u001b[43m=\u001b[49m\u001b[43maxis\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mskipna\u001b[49m\u001b[43m=\u001b[49m\u001b[43mskipna\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mmask\u001b[49m\u001b[43m=\u001b[49m\u001b[43mmask\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    406\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m datetimelike:\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\nanops.py:720\u001b[39m, in \u001b[36mnanmean\u001b[39m\u001b[34m(values, axis, skipna, mask)\u001b[39m\n\u001b[32m    719\u001b[39m the_sum = values.sum(axis, dtype=dtype_sum)\n\u001b[32m--> \u001b[39m\u001b[32m720\u001b[39m the_sum = \u001b[43m_ensure_numeric\u001b[49m\u001b[43m(\u001b[49m\u001b[43mthe_sum\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    722\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m axis \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;28mgetattr\u001b[39m(the_sum, \u001b[33m\"\u001b[39m\u001b[33mndim\u001b[39m\u001b[33m\"\u001b[39m, \u001b[38;5;28;01mFalse\u001b[39;00m):\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\nanops.py:1701\u001b[39m, in \u001b[36m_ensure_numeric\u001b[39m\u001b[34m(x)\u001b[39m\n\u001b[32m   1699\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(x, \u001b[38;5;28mstr\u001b[39m):\n\u001b[32m   1700\u001b[39m     \u001b[38;5;66;03m# GH#44008, GH#36703 avoid casting e.g. strings to numeric\u001b[39;00m\n\u001b[32m-> \u001b[39m\u001b[32m1701\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mTypeError\u001b[39;00m(\u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mCould not convert string \u001b[39m\u001b[33m'\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mx\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m'\u001b[39m\u001b[33m to numeric\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m   1702\u001b[39m \u001b[38;5;28;01mtry\u001b[39;00m:\n",
      "\u001b[31mTypeError\u001b[39m: Could not convert string '109.56151.36217.36129.48178.88256.8899.6137.6197.6119.52165.12237.12138.76151.56145.160.990' to numeric",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[29]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[43mdf\u001b[49m\u001b[43m.\u001b[49m\u001b[43mgroupby\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mmenu\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m[\u001b[49m\u001b[43m[\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mcalories\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mprotien\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43msugar\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43msodium\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m]\u001b[49m\u001b[43m.\u001b[49m\u001b[43mmean\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\groupby\\groupby.py:2459\u001b[39m, in \u001b[36mGroupBy.mean\u001b[39m\u001b[34m(self, numeric_only, engine, engine_kwargs)\u001b[39m\n\u001b[32m   2452\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m._numba_agg_general(\n\u001b[32m   2453\u001b[39m         grouped_mean,\n\u001b[32m   2454\u001b[39m         executor.float_dtype_mapping,\n\u001b[32m   2455\u001b[39m         engine_kwargs,\n\u001b[32m   2456\u001b[39m         min_periods=\u001b[32m0\u001b[39m,\n\u001b[32m   2457\u001b[39m     )\n\u001b[32m   2458\u001b[39m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m-> \u001b[39m\u001b[32m2459\u001b[39m     result = \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_cython_agg_general\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m   2460\u001b[39m \u001b[43m        \u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mmean\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\n\u001b[32m   2461\u001b[39m \u001b[43m        \u001b[49m\u001b[43malt\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43;01mlambda\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[43mx\u001b[49m\u001b[43m:\u001b[49m\u001b[43m \u001b[49m\u001b[43mSeries\u001b[49m\u001b[43m(\u001b[49m\u001b[43mx\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcopy\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m.\u001b[49m\u001b[43mmean\u001b[49m\u001b[43m(\u001b[49m\u001b[43mnumeric_only\u001b[49m\u001b[43m=\u001b[49m\u001b[43mnumeric_only\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   2462\u001b[39m \u001b[43m        \u001b[49m\u001b[43mnumeric_only\u001b[49m\u001b[43m=\u001b[49m\u001b[43mnumeric_only\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   2463\u001b[39m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   2464\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m result.__finalize__(\u001b[38;5;28mself\u001b[39m.obj, method=\u001b[33m\"\u001b[39m\u001b[33mgroupby\u001b[39m\u001b[33m\"\u001b[39m)\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\groupby\\groupby.py:2005\u001b[39m, in \u001b[36mGroupBy._cython_agg_general\u001b[39m\u001b[34m(self, how, alt, numeric_only, min_count, **kwargs)\u001b[39m\n\u001b[32m   2002\u001b[39m     result = \u001b[38;5;28mself\u001b[39m._agg_py_fallback(how, values, ndim=data.ndim, alt=alt)\n\u001b[32m   2003\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m result\n\u001b[32m-> \u001b[39m\u001b[32m2005\u001b[39m new_mgr = \u001b[43mdata\u001b[49m\u001b[43m.\u001b[49m\u001b[43mgrouped_reduce\u001b[49m\u001b[43m(\u001b[49m\u001b[43marray_func\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   2006\u001b[39m res = \u001b[38;5;28mself\u001b[39m._wrap_agged_manager(new_mgr)\n\u001b[32m   2007\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m how \u001b[38;5;129;01min\u001b[39;00m [\u001b[33m\"\u001b[39m\u001b[33midxmin\u001b[39m\u001b[33m\"\u001b[39m, \u001b[33m\"\u001b[39m\u001b[33midxmax\u001b[39m\u001b[33m\"\u001b[39m]:\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\internals\\managers.py:1488\u001b[39m, in \u001b[36mBlockManager.grouped_reduce\u001b[39m\u001b[34m(self, func)\u001b[39m\n\u001b[32m   1484\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m blk.is_object:\n\u001b[32m   1485\u001b[39m     \u001b[38;5;66;03m# split on object-dtype blocks bc some columns may raise\u001b[39;00m\n\u001b[32m   1486\u001b[39m     \u001b[38;5;66;03m#  while others do not.\u001b[39;00m\n\u001b[32m   1487\u001b[39m     \u001b[38;5;28;01mfor\u001b[39;00m sb \u001b[38;5;129;01min\u001b[39;00m blk._split():\n\u001b[32m-> \u001b[39m\u001b[32m1488\u001b[39m         applied = \u001b[43msb\u001b[49m\u001b[43m.\u001b[49m\u001b[43mapply\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfunc\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   1489\u001b[39m         result_blocks = extend_blocks(applied, result_blocks)\n\u001b[32m   1490\u001b[39m \u001b[38;5;28;01melse\u001b[39;00m:\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\internals\\blocks.py:395\u001b[39m, in \u001b[36mBlock.apply\u001b[39m\u001b[34m(self, func, **kwargs)\u001b[39m\n\u001b[32m    389\u001b[39m \u001b[38;5;129m@final\u001b[39m\n\u001b[32m    390\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34mapply\u001b[39m(\u001b[38;5;28mself\u001b[39m, func, **kwargs) -> \u001b[38;5;28mlist\u001b[39m[Block]:\n\u001b[32m    391\u001b[39m \u001b[38;5;250m    \u001b[39m\u001b[33;03m\"\"\"\u001b[39;00m\n\u001b[32m    392\u001b[39m \u001b[33;03m    apply the function to my values; return a block if we are not\u001b[39;00m\n\u001b[32m    393\u001b[39m \u001b[33;03m    one\u001b[39;00m\n\u001b[32m    394\u001b[39m \u001b[33;03m    \"\"\"\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m395\u001b[39m     result = \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mvalues\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    397\u001b[39m     result = maybe_coerce_values(result)\n\u001b[32m    398\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m._split_op_result(result)\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\groupby\\groupby.py:2002\u001b[39m, in \u001b[36mGroupBy._cython_agg_general.<locals>.array_func\u001b[39m\u001b[34m(values)\u001b[39m\n\u001b[32m   1999\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m result\n\u001b[32m   2001\u001b[39m \u001b[38;5;28;01massert\u001b[39;00m alt \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[32m-> \u001b[39m\u001b[32m2002\u001b[39m result = \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_agg_py_fallback\u001b[49m\u001b[43m(\u001b[49m\u001b[43mhow\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mvalues\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mndim\u001b[49m\u001b[43m=\u001b[49m\u001b[43mdata\u001b[49m\u001b[43m.\u001b[49m\u001b[43mndim\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43malt\u001b[49m\u001b[43m=\u001b[49m\u001b[43malt\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   2003\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m result\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\groupby\\groupby.py:1948\u001b[39m, in \u001b[36mGroupBy._agg_py_fallback\u001b[39m\u001b[34m(self, how, values, ndim, alt)\u001b[39m\n\u001b[32m   1946\u001b[39m     msg = \u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33magg function failed [how->\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mhow\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m,dtype->\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mser.dtype\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m]\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m   1947\u001b[39m     \u001b[38;5;66;03m# preserve the kind of exception that raised\u001b[39;00m\n\u001b[32m-> \u001b[39m\u001b[32m1948\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;28mtype\u001b[39m(err)(msg) \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01merr\u001b[39;00m\n\u001b[32m   1950\u001b[39m dtype = ser.dtype\n\u001b[32m   1951\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m dtype == \u001b[38;5;28mobject\u001b[39m:\n",
      "\u001b[31mTypeError\u001b[39m: agg function failed [how->mean,dtype->object]"
     ]
    }
   ],
   "source": [
    "df.groupby('menu')[['calories','protien','sugar','sodium']].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "d048f6c8-bb93-4fec-881b-9d5bbd38e1a6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Unnamed: 0      int64\n",
       "item           object\n",
       "servesize      object\n",
       "calories       object\n",
       "protien       float64\n",
       "totalfat      float64\n",
       "satfat        float64\n",
       "transfat      float64\n",
       "cholestrol    float64\n",
       "carbs         float64\n",
       "sugar         float64\n",
       "addedsugar    float64\n",
       "sodium        float64\n",
       "menu           object\n",
       "food_type      object\n",
       "dtype: object"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "d97eb7d4-3177-4e44-8155-9fa2f7985bb4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     402\n",
       "1     339\n",
       "2     652\n",
       "3     674\n",
       "4     512\n",
       "5     832\n",
       "6     356\n",
       "7     228\n",
       "8     400\n",
       "9     348\n",
       "10    451\n",
       "11    567\n",
       "12    689\n",
       "13    446\n",
       "14    357\n",
       "15    230\n",
       "16    290\n",
       "17    282\n",
       "18    720\n",
       "19    248\n",
       "Name: calories, dtype: object"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['calories'].head(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "2b3721b6-b2ab-4f70-99bc-761849d77d49",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['402', '339', '652', '674', '512', '832', '356', '228', '400',\n",
       "       '348', '451', '567', '689', '446', '357', '230', '290', '282',\n",
       "       '720', '248'], dtype=object)"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['calories'].unique()[:20]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "81e68e54-2384-47e5-8aa1-56b114ac7880",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['calories'] = (\n",
    "    df['calories']\n",
    "    .astype(str)\n",
    "    .str.replace(r'[^0-9.]', '', regex=True)\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "572240d0-fb6a-49f9-a263-28b6637bf29b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['calories'] = pd.to_numeric(df['calories'], errors='coerce')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "29cda504-d6f2-4152-af64-1569c1a2dbc9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Unnamed: 0      int64\n",
       "item           object\n",
       "servesize      object\n",
       "calories      float64\n",
       "protien       float64\n",
       "totalfat      float64\n",
       "satfat        float64\n",
       "transfat      float64\n",
       "cholestrol    float64\n",
       "carbs         float64\n",
       "sugar         float64\n",
       "addedsugar    float64\n",
       "sodium        float64\n",
       "menu           object\n",
       "food_type      object\n",
       "dtype: object"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "723a445b-bda0-4baf-99fb-499fd7dd3112",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>calories</th>\n",
       "      <th>protien</th>\n",
       "      <th>sugar</th>\n",
       "      <th>sodium</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>menu</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>beverage</th>\n",
       "      <td>143.326471</td>\n",
       "      <td>0.268235</td>\n",
       "      <td>34.677059</td>\n",
       "      <td>36.358824</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>breakfast</th>\n",
       "      <td>286.248750</td>\n",
       "      <td>11.822500</td>\n",
       "      <td>5.206250</td>\n",
       "      <td>644.766250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>condiments</th>\n",
       "      <td>47.473333</td>\n",
       "      <td>0.731111</td>\n",
       "      <td>6.104444</td>\n",
       "      <td>120.577778</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>dessert</th>\n",
       "      <td>194.360833</td>\n",
       "      <td>3.012500</td>\n",
       "      <td>23.148333</td>\n",
       "      <td>93.543333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>gourmet</th>\n",
       "      <td>543.497273</td>\n",
       "      <td>21.684545</td>\n",
       "      <td>8.799091</td>\n",
       "      <td>1207.961818</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mccafe</th>\n",
       "      <td>156.050833</td>\n",
       "      <td>4.343542</td>\n",
       "      <td>19.503750</td>\n",
       "      <td>96.431667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>regular</th>\n",
       "      <td>367.305556</td>\n",
       "      <td>12.990833</td>\n",
       "      <td>4.885833</td>\n",
       "      <td>701.980611</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              calories    protien      sugar       sodium\n",
       "menu                                                     \n",
       "beverage    143.326471   0.268235  34.677059    36.358824\n",
       "breakfast   286.248750  11.822500   5.206250   644.766250\n",
       "condiments   47.473333   0.731111   6.104444   120.577778\n",
       "dessert     194.360833   3.012500  23.148333    93.543333\n",
       "gourmet     543.497273  21.684545   8.799091  1207.961818\n",
       "mccafe      156.050833   4.343542  19.503750    96.431667\n",
       "regular     367.305556  12.990833   4.885833   701.980611"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('menu')[['calories','protien','sugar','sodium']].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "f604097a-35bc-4b2f-906e-36a7f251637d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAigAAAIKCAYAAAAJabS4AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjgsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvwVt1zgAAAAlwSFlzAAAPYQAAD2EBqD+naQAASUhJREFUeJzt3Qu8TWX+x/Gf436XO0V0MQgpXegqRJLRMCljpJJKyKULZvxVKNJMmhpSksuUlGlUNMmlUpM7qSi6TKIRJyPXct//1/dp1m7vfc7hnONwnn3W5/167dfZt7P32muvvdZvPc/v+T35IpFIxAAAADySktsLAAAAkIgABQAAeIcABQAAeIcABQAAeIcABQAAeIcABQAAeIcABQAAeIcABQAAeIcABQAAeIcABUhy7777ruXLl8/9zUk33XST1ahRw04kvd8111xzQt8TgJ8IUJDjxo4d6w6YF154IWs3HYcOHbKJEyda06ZNrWzZsla4cGF3YL755ptt+fLlrLPjbP369W771GX48OHpPqdz587u8RIlSiTF97Flyxa75557rHbt2lasWDErXry4NWrUyH2+7du3Z/n1pk6dao8//vhxWVYgs/IxFw9y2sUXX2ybNm1yB4IvvvjCzjjjDFby//z000/Wvn17mz17tl122WXWtm1bF6RoXb388sv2+eef24YNG+yUU07J9DpTy8kVV1xh77zzjgt6csqBAwfs8OHDLoA6URSo1atXz2bNmnXc3kPrumbNmlakSBE77bTTbM2aNXGP79mzxypVquQCyfz589vu3bvNZ8uWLbOrr77aLefvf/97F5iIgt1p06bZRRddZHPmzMnSa6oVa/Xq1W5dAbmlQK69M/Kkr7/+2hYuXGj/+Mc/7Pbbb7cXXnjB7r///hO6DDqo7t+/3x2AfHPvvfe64GT06NHWt2/fuMe0nnR/btMBWmfgBQsWtLxMB3Vtpx999JGdffbZ0ftfe+01t/1cddVV9vbbb5vP1Drym9/8xgVSH374oWtBifXQQw/Z+PHjLa8KtlXkTXTxIEcpIDnppJOsTZs29tvf/tbdjj0jV2uBujIS7dy50wUUaqYO7Nu3zx201QKjs/hq1arZfffd5+6Ppab4Xr16ufc666yz3HMVBMif/vQndwZZrlw5K1q0qDu7/Pvf/55uy8Zdd91l5cuXt5IlS9qvf/1r+89//uNe+4EHHoh7ru6/5ZZb3Fm23kvv+dxzzx113Xz77bf29NNP25VXXpkmOBEdZPT5g9aTb775xu6880771a9+5ZZdn+G6667L9Fnt9OnT3efV/+pz6exay56YZ6JujK+++sodsPXZ1b2RUQ6Kgj81/esz6/vSOlAg+sMPP8Q9T2fvrVq1cu+r91eLhdZZZumMv2HDhu496tat6wKJwL///W/3vaQXzCk41mMvvvjiUd+jSZMmbrnUnRFL25GCE22r6XnzzTft0ksvdQdGrS9t64mtMMF61fq+9tpr3fUKFSq471ctM0fLHwq6oSZNmnTEz6DtSe/x2GOPpQlORN/P4MGD44IvLW/VqlXdtnv66afbsGHD4pZJrXBvvPGG2/6CrrDY7SCzv8us/KYUXLVu3dpKlSrl1lXz5s1t8eLFcc/RutD/LliwwP0uKlas6H4rajnU/TNmzEjz+fXd6rFFixYdcT3CU+riAXJK7dq1I926dXPX33vvvYg2saVLl0Yfv+WWWyJlypSJ7Nu3L+7/Jk+e7J67bNkyd/vQoUORli1bRooVKxbp27dv5Omnn4706tUrUqBAgUi7du3i/lf/V6dOnUiFChUiDz74YGTMmDGRDz/80D12yimnRO68887IX//618hjjz0WueCCC9zzZ82aFfcaHTt2dPd36dLF/b9un3322e6++++/P/q8zZs3u9esVq1aZOjQoZGnnnoq8utf/9o9b/To0UdcN88884x73pQpUzK1LqdPn+6WYciQIe5///CHP0ROOumkyKmnnhrZs2dP9HnvvPOOe139DUycONHdd/7557vlGjhwYKRo0aKRGjVqRH744Yfo87p27RopXLhw5PTTT3fXx40bF10+3dZ7xbr11lvdd9C9e3f33AEDBkSKFy/u3mf//v3uOVu2bHHLWatWrcijjz4aGT9+fOSPf/yj+46ORu+n/9M2omXWd1a/fv1ISkpKZM6cOdHnXXzxxZFGjRql+X991yVLloxbP4m+/vprt260bFqn1atXjxw+fNg99v3337vP9+KLL7rPr88WS+smX758kauuuiry5JNPRh555BG3TrW8et3Y9VqkSJHIWWed5bZ5bScdOnRw7zt27Ngjfnexy6jv8Uguuugi970m/p4ycu2117ptW59dy3Tddde597nnnnuiz9F6btiwYaR8+fKRv/3t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L7bGjRvbnDlz7NNPP3UBTqVKlaxhw4Y2bNgwGzBggGudKVSoUM58KgAAEK4clC+++MKqVq1qp512mnXu3Nl12ciKFSvswIED1qJFi+hz1f1TvXp1W7Rokbutv/Xr13fBSaBVq1a2c+dOW7NmTYbvuW/fPvec2AsAAMi7shSgXHjhhTZp0iSbPXu2PfXUU/b111/bpZdeart27bLNmze7FpAyZcrE/Y+CET0m+hsbnASPB49lZMSIEa7LKLhUq1YtK4sNAADychdP69ato9cbNGjgApZTTz3VXn75ZStatKgdL4MGDbL+/ftHb6sFhSAFAIC865iGGau1pFatWvbll1+6vJT9+/fb9u3b456jUTxBzor+Jo7qCW6nl9cSKFy4sJUqVSruAgAA8q5jClB2795tX331lVWpUsUaNWrkRuPMnz8/+vi6detcjkqTJk3cbf395JNPLDU1NfqcuXPnuoCjbt26x7IoAAAgrF0899xzj7Vt29Z162zatMnuv/9+y58/v3Xq1MnlhnTr1s11xZQtW9YFHb1793ZBiUbwSMuWLV0g0qVLFxs1apTLOxk8eLCrnaJWEgAAgCwHKN9++60LRv773/9ahQoV7JJLLnFDiHVdRo8ebSkpKa5Am0beaITO2LFjo/+vYGbWrFnWo0cPF7gUL17cunbtakOHDuXbAAAAUfkikUjEkoySZNVio9or5KMASAY1Br5hPlk/sk1uLwJCaGcWjt/MxQMAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAAPJWgDJy5EjLly+f9e3bN3rf3r17rWfPnlauXDkr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AQpwgowYMcLloGiocaznnnvOJcgOGDCA7wIA/ockWeAEefrpp6127dpp7lfXzrhx4/geACAGAQpwgmzevNkVaUukSrLfffcd3wMAxCBAAU6QatWq2QcffJDmft2nirIAgF8wmzFwgnTv3t369u1rBw4csGbNmrn75s+fb/fddx+VZAEgAUmywAkSiURs4MCB9sQTT9j+/fvdfaqHouTYIUOG8D0AQAwCFOAE2717t3322WduaPGZZ57p6qAAAOIRoAAAAO+QJAsAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIAALxDgAIgxzRt2tR69+7tKuaedNJJbvbm8ePH2549e+zmm2+2kiVL2hlnnGFvvvlm9H9Wr15trVu3thIlSrjnd+nSxbZu3Rr3mnfddZeruFu2bFmrXLmyPfDAA9HH169fb/ny5bNVq1ZF79u+fbu779133+XbBZIUAQqAHDV58mQrX768LV261AUrPXr0sOuuu84uuugiW7lypbVs2dIFIT/++KMLJFT2/5xzzrHly5fb7NmzbcuWLdaxY8c0r1m8eHFbsmSJjRo1yoYOHWpz587lmwPyMAq1Acgxau04dOiQvf/+++62rpcuXdrat29vU6ZMiZvVedGiRTZv3jz33Lfeeiv6Gt9++62bWHHdunVWq1atNK8pF1xwgQtsRo4c6VpQatasaR9++KE1bNjQPa7ARy0477zzjvt/AMmHyQIB5KgGDRpEr+fPn9/KlStn9evXj96nbhxJTU21jz76yAUR6t5J9NVXX7kAJfE1RQGO/h9A3kWAAiBHFSxYMO62ckFi79NtOXz4sJuXqG3btvbII4+keR0FIUd6Tf2/pKSkRCdjDGjGaADJjQAFQK4599xz7ZVXXrEaNWpYgQLZ2x1VqFDB/f3uu+9cLovEJswCSE4kyQLINT179rRt27ZZp06dbNmyZa5bR/koGvGjvJPM0KzQjRs3dvkomiV6wYIFNnjw4OO+7ACOLwIUALmmatWq9sEHH7hgRKN7lKuiIcplypSJdt1kxnPPPWcHDx60Ro0auf8fPnz4cV1uAMcfo3gAAIB3aEEBAADeIUABAADeIUABAADeIUABAADeIUABAADeIUABAADeIUABAADeIUABAADeIUABAADeIUABAADeIUABAADeIUABAADmm/8HP6TNp7tWRbwAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.groupby('menu')['calories'].mean().plot(kind='bar')\n",
    "plt.title(\"Average Calories by Menu Category\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "103321db-026d-4688-be54-b2b95f7b04c1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "7546b4a0-3fd7-4ce4-8247-20cf7692b25a",
   "metadata": {},
   "outputs": [],
   "source": [
    "food_categories = ['regular', 'breakfast', 'gourmet']\n",
    "df_food = df[df['menu'].isin(food_categories)].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "d7d59015-1f3e-4ba1-afc3-1eb47cc834ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "def classify_food(item):\n",
    "    non_veg_keywords = ['Chicken', 'Fish', 'Egg', 'Sausage', 'McNuggets', 'Strips']\n",
    "    \n",
    "    for word in non_veg_keywords:\n",
    "        if word.lower() in item.lower():\n",
    "            return 'Non-Veg'\n",
    "    return 'Veg'\n",
    "\n",
    "df_food['food_type'] = df_food['item'].apply(classify_food)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "07405b64-d478-4fcb-81c0-002e0ee6cb95",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>calories</th>\n",
       "      <th>protien</th>\n",
       "      <th>sugar</th>\n",
       "      <th>sodium</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>food_type</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Non-Veg</th>\n",
       "      <td>405.848148</td>\n",
       "      <td>19.614074</td>\n",
       "      <td>4.363333</td>\n",
       "      <td>987.266741</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Veg</th>\n",
       "      <td>376.198571</td>\n",
       "      <td>9.685714</td>\n",
       "      <td>7.018571</td>\n",
       "      <td>609.314643</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             calories    protien     sugar      sodium\n",
       "food_type                                             \n",
       "Non-Veg    405.848148  19.614074  4.363333  987.266741\n",
       "Veg        376.198571   9.685714  7.018571  609.314643"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_food.groupby('food_type')[['calories','protien','sugar','sodium']].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "b6ddcc94-2e5d-4490-901e-ed11c629b7b7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAiwAAAHyCAYAAADIq5UrAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjgsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvwVt1zgAAAAlwSFlzAAAPYQAAD2EBqD+naQAANGRJREFUeJzt3Ql8U1Xe//FfF2gRaAFZ2mrZkX0bNllEUIZlfFBQVHh0WAR0ENxYlDoKCPgUcZRFeEAdoCoii0hxhKcjIosIqIA4oMJQLFBkR2lZtCDN//U7r38yDU1Li01zknzer9eV5Obe25OkNd+c8zv3hjgcDocAAABYLNTXDQAAALgaAgsAALAegQUAAFiPwAIAAKxHYAEAANYjsAAAAOsRWAAAgPUILAAAwHoEFgAAYD0CCxAgDhw4ICEhIZKUlOTrpgBAkSOwAPnQD38NAc4lMjJSbrrpJhkxYoQcP368SF+7//mf/5Hk5GSr348PPvjAvA5///vf89xmzZo1ZpuZM2dKoHC+/6+88kqevyPbtm0rtvYE6/uA4EZgAQpg4sSJ8s4778isWbOkXbt2MmfOHGnbtq1cuHDBmsBSrVo1+eWXX+TPf/6zeMsdd9wh0dHRsmjRojy30cfCwsKkb9++EmhefvnlIn3Pr1Wwvw8ITgQWoAB69OghDz74oAwZMsR8o37yySclLS1NVq5cmec+58+fL9bX1tkDpB9S3hIRESF9+vSRDRs2yJEjR3I9/uuvv8qKFSvkj3/8o1SuXFkCSbNmzUyv2ty5c33dlKB+HxC8CCzANbjtttvMvxpa1MCBA6VMmTKyf/9++dOf/iRly5aVBx54wBVcRo0aJfHx8eaDpm7duvK3v/1Ncl4oXcOGbvfWW2+5hh/0mE4//vijPPTQQ1KlShVzjIYNG8r8+fOvWsPibJfu36tXL3O7UqVKMnr0aLl8+bLb/kePHpU9e/bIpUuX8n3uGtyys7Nl8eLFuR5btWqVZGRkuJ67WrhwobRo0UJKlSolFSpUMN/409PTc+07e/ZsqVmzptmudevW8tlnn0mnTp3Mkp9GjRpJ586dc63XNt5www3mg91J26xt0fcnKipKGjduLDNmzJCCaN++vXnfp06danqyrubTTz+VW265RUqXLi3lypWTu+66S77//nu3bSZMmGDes9TUVPNe6XbaczJo0KCr9uTY9j4A3kZgAa6BBhN1/fXXu9b99ttv0q1bN/ONVgPJPffcY0LJnXfeKdOmTZPu3bvLq6++agLLmDFjZOTIka59dbhJg4h+wOltXR555BHzmH6rv/nmm+WTTz4xtTP6AVu7dm0ZPHiwTJ8+/apt1WCi7dK2artuvfVWU4vxxhtvuG2XkJAg9evXN+EmPx07dpQbb7zR43CErrvuuutMOFIvvvii9O/fX+rUqWOeu/ZMrV271hzjzJkzrv10iE2fmx5XA4G+DnqMw4cPX/X53X///bJx40Y5duyY2/pNmzaZ3gfnkIjWdPTr10/Kly8vL730kkyZMsV8CH/++edSUBow9P3Q9uZH3yt9zU+cOGH20fd68+bNJvRosLzSfffdJ2fPnpXExERzW0PnCy+84FfvA+B1DgB5WrBggXaDOD755BPHyZMnHenp6Y7Fixc7rr/+ekepUqUchw8fNtsNGDDAbDd27Fi3/ZOTk836yZMnu63v06ePIyQkxJGamupaV7p0aXOcKw0ePNgRGxvrOHXqlNv6vn37OqKjox0XLlww99PS0szP0jY7Ods1ceJEt32bN2/uaNGihds657Z6nKsZM2aM2Xbv3r2udRkZGY7IyEhHv379zP0DBw44wsLCHC+++KLbvrt27XKEh4e71mdlZZnXs1WrVo5Lly65tktKSjI/49Zbb823LdoG3e61115zW//oo486ypQp43p9nnjiCUdUVJTjt99+cxSWHn/48OHmdufOnR0xMTGu4zp/R7766ivX9s2aNXNUrlzZcfr0ade6b775xhEaGuro37+/a9348ePNvg899JDbz+vdu7d5TfzpfQC8jR4WoAC6dOlihlJ0WEe/sevQitYI6JBDTsOGDXO7v3r1alNT8vjjj7ut1yEi/Rz8v//7v6t9oZDly5dLz549ze1Tp065Fv0Gr93+O3bsuGr7//KXv7jd12/OP/zwg9s6/VavP6N69epXPZ4OR6ic3+61nVo74RyG0JksOmShPQY52x0TE2O+6a9bt85sp7NrTp8+LUOHDpXw8HDX8fQ42htyNTprS+tLlixZ4tar9P7775vXTYc2lA636LCb9rT8Htpjor05edWy6NDazp07zRCPDr04NWnSxNSU6O9EQd4ffU0yMzP95n0AvI3AAhSAjuvrB53+z/27774zH/YaGHLS/8lrV3pOBw8elLi4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DodD/JwW3epsoYyMjKCrZ6k+dpWvm4BidGDKHbzeAAJGYT6/uZYQAACwHoEFAABYj8ACAACsR2ABAADWI7AAAADrEVgAAID1CCwAAMB6BBYAAGA9AgsAALAegQUAAFiPwAIAAKxHYAEAANYjsAAAAOsRWAAAgPUILAAAwHoEFgAAYD0CCwAAsB6BBQAAWI/AAgAArEdgAQAA1iOwAAAA6xFYAACA9QgsAADAegQWAABgPQILAACwHoEFAABYj8ACAACsR2ABAADWI7AAAADrEVgAAID1CCwAAMB6BBYAAGA9AgsAALAegQUAAAReYNm4caP07NlT4uLiJCQkRJKTk12PXbp0SZ555hlp3LixlC5d2mzTv39/OXLkSL7HnDBhgjlWzqVevXrX9owAAEDAKXRgOX/+vDRt2lRmz56d67ELFy7Ijh075Pnnnzf/fvDBB7J371658847r3rchg0bytGjR13Lpk2bCts0AAAQoMILu0OPHj3M4kl0dLSsWbPGbd2sWbOkdevWcujQIalatWreDQkPl5iYmMI2BwAABAGv17BkZGSYIZ5y5crlu92+ffvMEFLNmjXlgQceMAEnL1lZWZKZmem2AACAwOXVwPLrr7+ampZ+/fpJVFRUntu1adNGkpKSJCUlRebMmSNpaWlyyy23yNmzZz1un5iYaHpznEt8fLwXnwUAAAjYwKIFuPfdd584HA4TQvKjQ0z33nuvNGnSRLp16yarV6+WM2fOyNKlSz1un5CQYHpunEt6erqXngUAAPDLGpbChJWDBw/Kp59+mm/viic6fHTTTTdJamqqx8cjIiLMAgAAgkOot8KK1qR88skncv311xf6GOfOnZP9+/dLbGxsUTcPAAAEQ2DRMLFz506zKK030dtaJKthpU+fPrJt2zZ599135fLly3Ls2DGzXLx40XWM22+/3cwecho9erRs2LBBDhw4IJs3b5bevXtLWFiYqX0BAAAo9JCQhpHOnTu77o8cOdL8O2DAAHMCuA8//NDcb9asmdt+69atk06dOpnb2nty6tQp12OHDx824eT06dNSqVIl6dChg2zdutXcBgAAKHRg0dChhbR5ye8xJ+1JyWnx4sW8EwAAIE9cSwgAAFiPwAIAAKxHYAEAANYjsAAAAOsRWAAAgPUILAAAwHoEFgAAYD0CCwAAsB6BBQAAWI/AAgAArEdgAQAA1iOwAAAA6xFYAACA9QgsAADAegQWAABgPQILAACwHoEFAABYj8ACAACsR2ABAADWI7AAAADrEVgAAID1CCwAAMB6BBYAAGA9AgsAALAegQUAAFiPwAIAAKxHYAEAANYjsAAAAOsRWAAAgPUILAAAwHoEFgAAYD0CCwAAsB6BBQAAWI/AAgAAAi+wbNy4UXr27ClxcXESEhIiycnJbo87HA4ZN26cxMbGSqlSpaRLly6yb9++qx539uzZUr16dYmMjJQ2bdrIl19+WdimAQCAAFXowHL+/Hlp2rSpCRieTJ06VWbOnClz586VL774QkqXLi3dunWTX3/9Nc9jLlmyREaOHCnjx4+XHTt2mOPrPidOnChs8wAAQAAKcWiXyLXuHBIiK1askF69epn7eijteRk1apSMHj3arMvIyJAqVapIUlKS9O3b1+NxtEelVatWMmvWLHM/Oztb4uPj5bHHHpOxY8detR2ZmZkSHR1tflZUVJQEk+pjV/m6CShGB6bcwesNIGAU5vO7SGtY0tLS5NixY2YYyEkbooFky5YtHve5ePGibN++3W2f0NBQcz+vfbKyssyTzLkAAIDAVaSBRcOK0h6VnPS+87ErnTp1Si5fvlyofRITE00Qci7aGwMAAAKXX84SSkhIMN1HziU9Pd3XTQIAAP4SWGJiYsy/x48fd1uv952PXalixYoSFhZWqH0iIiLMWFfOBQAABK4iDSw1atQwIWPt2rWudVpforOF2rZt63GfkiVLSosWLdz20aJbvZ/XPgAAILiEF3aHc+fOSWpqqluh7c6dO6VChQpStWpVefLJJ2Xy5MlSp04dE2Cef/55M3PIOZNI3X777dK7d28ZMWKEua9TmgcMGCAtW7aU1q1by/Tp08306UGDBhXV8wQAAMEUWLZt2yadO3d23dewoTRw6NTlp59+2oSNhx9+WM6cOSMdOnSQlJQUc0I4p/3795tiW6f7779fTp48aU44p4W2zZo1M/tcWYgLAACC0+86D4stOA8LggXnYQEQSHx2HhYAAABvILAAAADrEVgAAID1CCwAAMB6BBYAAGA9AgsAALAegQUAAFiPwAIAAKxHYAEAANYjsAAAAOsRWAAAgPUILAAAwHoEFgAAYD0CCwAAsB6BBQAAWI/AAgAArEdgAQAA1iOwAAAA6xFYAACA9QgsAADAegQWAABgPQILAACwHoEFAABYj8ACAACsR2ABAADWI7AAAADrEVgAAID1CCwAAMB6BBYAAGA9AgsAALAegQUAAFiPwAIAAKxHYAEAANYjsAAAgOALLNWrV5eQkJBcy/Dhwz1un5SUlGvbyMjIom4WAADwY+FFfcCvvvpKLl++7Lq/e/du+eMf/yj33ntvnvtERUXJ3r17Xfc1tAAAAHgtsFSqVMnt/pQpU6RWrVpy66235rmPBpSYmJgC/4ysrCyzOGVmZl5jawEAgAR7DcvFixdl4cKF8tBDD+Xba3Lu3DmpVq2axMfHy1133SXffvttvsdNTEyU6Oho16L7AQCAwOXVwJKcnCxnzpyRgQMH5rlN3bp1Zf78+bJy5UoTbrKzs6Vdu3Zy+PDhPPdJSEiQjIwM15Kenu6lZwAAAAJySCinefPmSY8ePSQuLi7Pbdq2bWsWJw0r9evXl9dff10mTZrkcZ+IiAizAACA4OC1wHLw4EH55JNP5IMPPijUfiVKlJDmzZtLamqqt5oGAAD8jNeGhBYsWCCVK1eWO+64o1D76QyjXbt2SWxsrLeaBgAA/IxXAovWoWhgGTBggISHu3fi9O/f39SgOE2cOFE+/vhj+eGHH2THjh3y4IMPmt6ZIUOGeKNpAADAD3llSEiHgg4dOmRmB11J14eG/icn/fzzzzJ06FA5duyYlC9fXlq0aCGbN2+WBg0aeKNpAADAD4U4HA6H+Dk9D4tOb9YZQ3oSumBSfewqXzcBxejAlMINsQJAoHx+cy0hAABgPQILAACwHoEFAABYj8ACAACsR2ABAADWI7AAAADrEVgAAID1CCwAAMB6BBYAAGA9AgsAALAegQUAAFiPwAIAAKxHYAEAANYjsAAAAOsRWAAAgPUILAAAwHoEFgAAYD0CCwAAsB6BBQAAWI/AAgAArEdgAQAA1iOwAAAA6xFYAACA9QgsAADAegQWAABgPQILAACwHoEFAABYj8ACAACsR2ABAADWI7AAAADrEVgAAID1CCwAAMB6BBYAAGA9AgsAAAi+wDJhwgQJCQlxW+rVq5fvPsuWLTPbREZGSuPGjWX16tVF3SwAAODHvNLD0rBhQzl69Khr2bRpU57bbt68Wfr16yeDBw+Wr7/+Wnr16mWW3bt3e6NpAADAD4V75aDh4RITE1OgbWfMmCHdu3eXMWPGmPuTJk2SNWvWyKxZs2Tu3Lke98nKyjKLU2ZmZhG1HAAABE0Py759+yQuLk5q1qwpDzzwgBw6dCjPbbds2SJdunRxW9etWzezPi+JiYkSHR3tWuLj44u0/QAAIMADS5s2bSQpKUlSUlJkzpw5kpaWJrfccoucPXvW4/bHjh2TKlWquK3T+7o+LwkJCZKRkeFa0tPTi/ppAACAQB4S6tGjh+t2kyZNTICpVq2aLF261NSpFIWIiAizAACA4OD1ac3lypWTm266SVJTUz0+rrUux48fd1un9wtaAwMAAAKf1wPLuXPnZP/+/RIbG+vx8bZt28ratWvd1mnRra4HAADwSmAZPXq0bNiwQQ4cOGCmLPfu3VvCwsLM1GXVv39/U4Pi9MQTT5h6l1deeUX27NljzuOybds2GTFiBO8QAADwTg3L4cOHTTg5ffq0VKpUSTp06CBbt241t5XOGAoN/U9OateunSxatEiee+45efbZZ6VOnTqSnJwsjRo1KuqmAQAAPxXicDgc4uf0PCw6vVlnDEVFRUkwqT52la+bgGJ0YModvN5BhL/v4BKMf9+Zhfj85lpCAADAegQWAABgPQILAACwHoEFAABYj8ACAACsR2ABAADWI7AAAADrEVgAAID1CCwAAMB6BBYAAGA9AgsAALAegQUAAFiPwAIAAKxHYAEAANYjsAAAAOsRWAAAgPUILAAAwHoEFgAAYD0CCwAAsB6BBQAAWI/AAgAArEdgAQAA1iOwAAAA6xFYAACA9QgsAADAegQWAABgPQILAACwHoEFAABYj8ACAACsR2ABAADWI7AAAADrEVgAAID1CCwAAMB6BBYAABB8gSUxMVFatWolZcuWlcqVK0uvXr1k7969+e6TlJQkISEhbktkZGRRNw0AAPipIg8sGzZskOHDh8vWrVtlzZo1cunSJenataucP38+3/2ioqLk6NGjruXgwYNF3TQAAOCnwov6gCkpKbl6T7SnZfv27dKxY8c899NelZiYmAL9jKysLLM4ZWZm/o4WAwAACfYaloyMDPNvhQoV8t3u3LlzUq1aNYmPj5e77rpLvv3223yHnaKjo12L7gMAAAKXVwNLdna2PPnkk9K+fXtp1KhRntvVrVtX5s+fLytXrpSFCxea/dq1ayeHDx/2uH1CQoIJQs4lPT3di88CAAAE3JBQTlrLsnv3btm0aVO+27Vt29YsThpW6tevL6+//rpMmjQp1/YRERFmAQAAwcFrgWXEiBHy0UcfycaNG+XGG28s1L4lSpSQ5s2bS2pqqreaBwAAgnlIyOFwmLCyYsUK+fTTT6VGjRqFPsbly5dl165dEhsbW9TNAwAAfijcG8NAixYtMvUoei6WY8eOmfVaHFuqVClzu3///nLDDTeY4lk1ceJEufnmm6V27dpy5swZefnll8205iFDhhR18wAAgB8q8sAyZ84c82+nTp3c1i9YsEAGDhxobh86dEhCQ//TufPzzz/L0KFDTbgpX768tGjRQjZv3iwNGjQo6uYBAAA/FO6NIaGrWb9+vdv9adOmmQUAAMATriUEAACsR2ABAADWI7AAAADrEVgAAID1CCwAAMB6BBYAAGA9AgsAALAegQUAAFiPwAIAAKxHYAEAANYjsAAAAOsRWAAAgPUILAAAwHoEFgAAYD0CCwAAsB6BBQAAWI/AAgAArEdgAQAA1iOwAAAA6xFYAACA9QgsAADAegQWAABgPQILAACwHoEFAABYj8ACAACsR2ABAADWI7AAAADrEVgAAID1CCwAAMB6BBYAAGA9AgsAALAegQUAAFiPwAIAAII3sMyePVuqV68ukZGR0qZNG/nyyy/z3X7ZsmVSr149s33jxo1l9erV3moaAADwM14JLEuWLJGRI0fK+PHjZceOHdK0aVPp1q2bnDhxwuP2mzdvln79+sngwYPl66+/ll69epll9+7d3mgeAADwM14JLK+++qoMHTpUBg0aJA0aNJC5c+fKddddJ/Pnz/e4/YwZM6R79+4yZswYqV+/vkyaNEn+8Ic/yKxZs7zRPAAA4GfCi/qAFy9elO3bt0tCQoJrXWhoqHTp0kW2bNnicR9drz0yOWmPTHJyssfts7KyzOKUkZFh/s3MzJRgk511wddNQDEKxt/xYMbfd3AJxr/vzP//nB0OR/EHllOnTsnly5elSpUqbuv1/p49ezzuc+zYMY/b63pPEhMT5YUXXsi1Pj4+/ne1HbBd9HRftwCAtwTz3/fZs2clOjq6eANLcdDem5w9MtnZ2fLTTz/J9ddfLyEhIT5tG4onkWs4TU9Pl6ioKF5yIIDw9x1cHA6HCStxcXFX3bbIA0vFihUlLCxMjh8/7rZe78fExHjcR9cXZvuIiAiz5FSuXLnf3Xb4Fw0rBBYgMPH3HTyir9Kz4rWi25IlS0qLFi1k7dq1bj0ger9t27Ye99H1ObdXa9asyXN7AAAQXLwyJKTDNQMGDJCWLVtK69atZfr06XL+/Hkza0j1799fbrjhBlOLop544gm59dZb5ZVXXpE77rhDFi9eLNu2bZM33njDG80DAAB+xiuB5f7775eTJ0/KuHHjTOFss2bNJCUlxVVYe+jQITNzyKldu3ayaNEiee655+TZZ5+VOnXqmBlCjRo18kbz4Od0OFDP8XPlsCAA/8ffN/IS4ijIXCIAAAAf4lpCAADAegQWAABgPQILAACwHoEFAABYj8ACAACsR2ABAADW88trCQEAAsfMmTM9rtdrw0VGRkrt2rWlY8eO5rIvCF6chwV+41//+le+/1OrWrUqJ5MD/FCNGjXMyUYvXLgg5cuXN+t+/vlnue6666RMmTJy4sQJqVmzpqxbt85c+BTBicACv6FnR87vatwlSpQwZ1l+/fXXTYAB4B/ee+89cymWv//971KrVi2zLjU1VR555BF5+OGHpX379tK3b19zQdz333/f182FjxBY4DdWrlwpzzzzjIwZM8Zco0p9+eWX5hpUeqr+3377TcaOHWtCy9/+9jdfNxdAAWlIWb58ubmMS05ff/213HPPPfLDDz/I5s2bze2jR4/yugYpaljgN1588UWZMWOGdOvWzbWucePGcuONN8rzzz9vwkvp0qVl1KhRBBbAj2gI0S8cV9J1ej06FRcXJ2fPnvVB62ALZgnBb+zatUuqVauWa72u08eUfkPjGxjgXzp37myGf7RHxUlvDxs2TG677TZzX//GtdYFwYvAAr9Rr149mTJlily8eNG17tKlS2adPqZ+/PFH11XBAfiHefPmSYUKFaRFixamcF6Xli1bmnX6mNLiWx3+RfCihgV+Q8ew77zzTlN826RJE9e3rsuXL8tHH30kN998s7zzzjumC1nrXAD4lz179si///1vc7tu3bpmAZwILPArOob97rvvuv1P7b//+7+lbNmyvm4agN9Je0/T0tJMEW54OCWWcEdgAQD4lJ5/5bHHHpO33nrL3NcvJHreFV13ww03mNl/ADUs8Cs65NOhQwczY+DgwYNm3bRp08yUZwD+KSEhQb755htZv3692zmUunTpIkuWLPFp22APAgv8xpw5c2TkyJHSo0cPcxZMrV1RembM6dOn+7p5AK5RcnKyzJo1y3wZyXlyyIYNG8r+/ft5XWEQWOA3XnvtNXnzzTflr3/9q9v4ts4mcE5rBuB/9LT8lStXzrX+/Pnz+Z7dGsGFwAK/ocV4zZs3z7Vep0Dq/9gA+Cf90rFq1SrXfWdI0VP1t23b1octg00ow4bf0JNG7dy5M9fJ41JSUqR+/fo+axeAa7N7925p1KiRJCYmSvfu3eW7774z51bSM1rrbT2VwYYNG3h5YdDDAr+h9SvDhw83RXgOh8Ocil9P168Fe08//bSvmwegkPR8Sm3atDHh5PPPPzen4td1H3/8sRki2rJlizmZHKCY1gzraXFtWFiYua3nYJkwYYKrEE9nC73wwgsyePBgH7cSQGF99tlnsmDBAnMF5uzsbHNxQ/1b7tixIy8mciGwwHp6SfmBAwea/5HVqVPHdd6Gc+fOeSzUA+BftAZt6dKlkpSUZEJM7dq1zd/7gAEDzN8/oAgssN6kSZPMCaW06LZdu3bmf2T33XefXHfddb5uGoAilpqaanpdnJfZ0NqWDz/8kNcZBBb4Dz2plP6PbPny5WaISEPLkCFDzBg4gMDqcdHhX61PO3PmjOucSwhuFN3Cb3Tq1Mn0tOi3Lr1q6/fff2+mPOrJpV599VVfNw/A77Rx40Yz/KvDQHoB07vvvtsU4wKKISH4NT13Q//+/fkWBvipI0eOmNoVXXQ4KOewb+nSpX3dPFiE87DA72jBrRbo6fDQpk2bzJVd9dsYAP+il9n45JNPpGLFiuaLx0MPPWSuwA54QmCB39CTSM2fP1+WLVtmztfQp08fU5DLFEjAP5UoUcJMaf6v//ov16kLgLwwJATrTZ061fSm6CXn9RTe2l3cr18/KVu2rK+bBgAoJgQWWK9SpUry4IMPmqCip/EGAAQfAgusp9cW0a7jnBo3biyrV6+W+Ph4n7ULAFB8mNYM610ZVtSBAwdMkAEABAcCCwAAsB6BBX7plltukVKlSvm6GQCAYkINCwAAsB7nYYFf2bdvn6xbt05OnDhhLkef07hx43zWLgCAd9HDAr/x5ptvyrBhw8xZMfVaIyEhIa7H9PaOHTt82j4AgPcQWOA3qlWrJo8++qg888wzvm4KAKCYEVjgN6KiomTnzp1Ss2ZNXzcFAFDMmCUEv3HvvffKxx9/7OtmAAB8gKJb+I3atWvL888/L1u3bjVnur3yhHKPP/64z9oGAPAuhoTgN2rUqJHnY1p0+8MPPxRrewAAxYfAAgAArEcNC/ySw+EwCwAgOBBY4FfefvttU7+ip+XXpUmTJvLOO+/4ulkAAC+j6BZ+49VXXzVFtyNGjJD27dubdZs2bZK//OUvcurUKXnqqad83UQAgJdQwwK/Krp94YUXpH///m7r33rrLZkwYYKkpaX5rG0AAO9iSAh+4+jRo9KuXbtc63WdPgYACFwEFvjVeViWLl2aa/2SJUukTp06PmkTAKB4UMMCv6HDQffff79s3LjRVcPy+eefy9q1az0GGQBA4KCGBX5l+/btpvh2z5495n79+vVl1KhR0rx5c183DQDgRQQWAABgPYaEYL3Q0FBz6v386OO//fZbsbUJAFC8CCyw3ooVK/J8bMuWLTJz5kzJzs4u1jYBAIoXQ0LwS3v37pWxY8fKP/7xD3nggQdk4sSJUq1aNV83CwDgJUxrhl85cuSIDB061JyeX4eAdu7caU4cR1gBgMBGYIFfyMjIkGeeecaci+Xbb781U5m1d6VRo0a+bhoAoBhQwwLrTZ06VV566SWJiYmR9957T+666y5fNwkAUMyoYYFfzBLSKzN36dJFwsLC8tzugw8+KNZ2AQCKDz0ssJ5e7PBq05oBAIGNHhYAAGA9im4BAID1CCwAAMB6BBYAAGA9AgsAALAegQVAvhwOhzz88MNSoUIFM1tLzy7sDZ06dZInn3ySdwOARwQWAPlKSUmRpKQk+eijj+To0aNWnF24evXqMn36dF83A0Ax4jwsAPK1f/9+iY2NlXbt2vFKAfAZelgA5GngwIHy2GOPyaFDh8xwkPZsZGVlyeOPPy6VK1eWyMhI6dChg3z11Vdu+23YsEFat24tERERJuzolbX1YpVO58+fNycELFOmjHn8lVdeKdTQ0cGDB+Wpp54ybdJFjxcVFSXvv/++27bJyclSunRpOXv2rBw4cMBsu3jxYhO+tO3aW6RtzWn37t3So0cP07YqVarIn//8Zzl16hS/JYCPEVgA5GnGjBkyceJEufHGG81wkAaTp59+WpYvX26ukr1jxw5zQcpu3brJTz/9ZPb58ccf5U9/+pO0atVKvvnmG5kzZ47MmzdPJk+e7DrumDFjTFBYuXKlfPzxx7J+/XpzrILQSzBoe7Rd2iZdNJT07dtXFixY4Lat3u/Tp4+ULVvW7WePGjVKvv76a2nbtq307NlTTp8+bR47c+aM3HbbbdK8eXPZtm2bGQ47fvy43HffffyWAL7mAIB8TJs2zVGtWjVz+9y5c44SJUo43n33XdfjFy9edMTFxTmmTp1q7j/77LOOunXrOrKzs13bzJ4921GmTBnH5cuXHWfPnnWULFnSsXTpUtfjp0+fdpQqVcrxxBNPFOi90PZou3L64osvHGFhYY4jR46Y+8ePH3eEh4c71q9fb+6npaU59H95U6ZMce1z6dIlx4033uh46aWXzP1JkyY5unbt6nbc9PR0s9/evXv5PQF8iB4WAIWqZ7l06ZK0b9/eta5EiRJm+Of777839/Vf7bnIef0n3f7cuXNy+PBhc4yLFy9KmzZtXI/rDKS6dev+rndC29CwYUPT86MWLlwo1apVk44dO7ptp21zCg8Pl5YtW7rarj1C69atM8NBzqVevXqu5w7Adyi6BRAwhgwZIrNnzzY1MzocNGjQoEJdOFNDlQ4RvfTSS7ke01obAL5DDwuAAqtVq5aULFlSPv/8c9c67XHR2pYGDRqY+/Xr15ctW7aY87c46fZaR6K1J3oM7ZX54osvXI///PPP8u9//7vA7dA2XL58Odf6Bx980BTkzpw5U7777jsZMGBArm22bt3quq2FwNu3bzdtVn/4wx/k22+/NcXFWpuTc9E6GQC+Q2ABUGD6oT1s2DBTuKoFqRoKhg4dKhcuXJDBgwebbR599FFJT083s4v27NljCmvHjx8vI0eOlNDQUDPMotvqMT799FMzK0dnI+ljBaWBYuPGjabAN+cMnvLly8vdd99tjt21a1cTkK6kPTArVqwwbRs+fLgJSw899JB5TO9r8XC/fv1MCNNhoH/+85+mp8ZTQAJQfBgSAlAoU6ZMkezsbDPdV6cLaw2IfqhrWFA33HCDrF692oSGpk2bmvoUDSjPPfec6xgvv/yya/hFe1501k5GRkaB26AzhB555BHTW6PTrHP25ujPWrRokSuEeGq/LnrGXu05+fDDD6VixYrmsbi4ONMb9Mwzz5jAo8fWOpju3bsXKlABKHohWnnLCwsgULzzzjvmHC1HjhwxQ0dOeh6WGjVqmOnMzZo182kbARQePSwAAoIOS+k5WbT3RHtfcoYVAP6PPk4AVvnss8/cphVfueRl6tSpZgpyTEyMJCQkFGubAXgfQ0IArPLLL7+YYtq8aN0JgOBDYAEAANZjSAgAAFiPwAIAAKxHYAEAANYjsAAAAOsRWAAAgPUILAAAwHoEFgAAILb7f9v4w4g7IkSgAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.groupby('food_type')['protien'].mean().plot(kind='bar')\n",
    "plt.title(\"Protein: Veg vs Non-Veg\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "df5c3e7e-ea0b-48fe-bdd3-6e8682721dc1",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['protein_efficiency'] = df['protien'] / df['calories'] * 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "475858ff-d415-496f-8a5b-a0610f4486d4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>item</th>\n",
       "      <th>protein_efficiency</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>40</th>\n",
       "      <td>Sausage Mc Muffin with egg</td>\n",
       "      <td>7.733627</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>McSpicy Fried Chicken 1 pc</td>\n",
       "      <td>6.987903</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75</th>\n",
       "      <td>Strawberry Green Tea (L)</td>\n",
       "      <td>6.788512</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>74</th>\n",
       "      <td>Strawberry Green Tea (R)</td>\n",
       "      <td>6.730769</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>73</th>\n",
       "      <td>Strawberry Green Tea (S)</td>\n",
       "      <td>6.685633</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>3 piece Chicken Strips</td>\n",
       "      <td>6.203252</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>2 piece Chicken Strips</td>\n",
       "      <td>6.201220</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>5 piece Chicken Strips</td>\n",
       "      <td>6.187348</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>108</th>\n",
       "      <td>Chunky Chipotle American Burger Chicken</td>\n",
       "      <td>6.154110</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>138</th>\n",
       "      <td>Cheese Slice</td>\n",
       "      <td>5.996473</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                        item  protein_efficiency\n",
       "40                Sausage Mc Muffin with egg            7.733627\n",
       "19                McSpicy Fried Chicken 1 pc            6.987903\n",
       "75                  Strawberry Green Tea (L)            6.788512\n",
       "74                  Strawberry Green Tea (R)            6.730769\n",
       "73                  Strawberry Green Tea (S)            6.685633\n",
       "24                    3 piece Chicken Strips            6.203252\n",
       "23                    2 piece Chicken Strips            6.201220\n",
       "25                    5 piece Chicken Strips            6.187348\n",
       "108  Chunky Chipotle American Burger Chicken            6.154110\n",
       "138                             Cheese Slice            5.996473"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sort_values('protein_efficiency', ascending=False)[['item','protein_efficiency']].head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "8fd29724-ec7b-4e97-8f55-7cfccf5d334e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>item</th>\n",
       "      <th>sugar</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>120</th>\n",
       "      <td>Large Fanta Orange</td>\n",
       "      <td>64.22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>126</th>\n",
       "      <td>Large Sprite</td>\n",
       "      <td>59.28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>82</th>\n",
       "      <td>Chocolate Oreo Frappe</td>\n",
       "      <td>55.14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>117</th>\n",
       "      <td>Large Coca-Cola</td>\n",
       "      <td>54.34</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>91</th>\n",
       "      <td>American Mud Pie Shake</td>\n",
       "      <td>53.40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>123</th>\n",
       "      <td>Large Thums-up</td>\n",
       "      <td>49.40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>64</th>\n",
       "      <td>Hot Chocolate (L)</td>\n",
       "      <td>47.96</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>81</th>\n",
       "      <td>Mocha Frappe</td>\n",
       "      <td>47.55</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101</th>\n",
       "      <td>Medium Blackforest</td>\n",
       "      <td>45.45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>119</th>\n",
       "      <td>Medium Fanta Orange</td>\n",
       "      <td>44.72</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       item  sugar\n",
       "120      Large Fanta Orange  64.22\n",
       "126            Large Sprite  59.28\n",
       "82    Chocolate Oreo Frappe  55.14\n",
       "117         Large Coca-Cola  54.34\n",
       "91   American Mud Pie Shake  53.40\n",
       "123          Large Thums-up  49.40\n",
       "64        Hot Chocolate (L)  47.96\n",
       "81             Mocha Frappe  47.55\n",
       "101      Medium Blackforest  45.45\n",
       "119     Medium Fanta Orange  44.72"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sort_values('sugar', ascending=False)[['item','sugar']].head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb442b1e-aad2-4065-88ae-3fe29fa586c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.sort_values('sodium', ascending=False)[['item','sodium']].head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "80ae9bcb-87a6-4adb-a45d-fc4b139bf2b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['health_score'] = (\n",
    "    df['protien'] * 2\n",
    "    - df['sugar']\n",
    "    - df['sodium'] * 0.001\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "93cf59d0-90c9-4ad1-8589-abe8db44a55b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.sort_values('health_score', ascending=False)[['item','health_score']].head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "9ccc2a27-4d50-493f-b975-70ff8ca94a36",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'health_score'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mKeyError\u001b[39m                                  Traceback (most recent call last)",
      "\u001b[32m~\\AppData\\Local\\Temp\\ipykernel_16132\\674623948.py\u001b[39m in \u001b[36m?\u001b[39m\u001b[34m()\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m df.sort_values(\u001b[33m'health_score'\u001b[39m)[[\u001b[33m'item'\u001b[39m,\u001b[33m'health_score'\u001b[39m]].head(\u001b[32m10\u001b[39m)\n",
      "\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\frame.py\u001b[39m in \u001b[36m?\u001b[39m\u001b[34m(self, by, axis, ascending, inplace, kind, na_position, ignore_index, key)\u001b[39m\n\u001b[32m   7207\u001b[39m             )\n\u001b[32m   7208\u001b[39m         \u001b[38;5;28;01melif\u001b[39;00m len(by):\n\u001b[32m   7209\u001b[39m             \u001b[38;5;66;03m# len(by) == 1\u001b[39;00m\n\u001b[32m   7210\u001b[39m \n\u001b[32m-> \u001b[39m\u001b[32m7211\u001b[39m             k = self._get_label_or_level_values(by[\u001b[32m0\u001b[39m], axis=axis)\n\u001b[32m   7212\u001b[39m \n\u001b[32m   7213\u001b[39m             \u001b[38;5;66;03m# need to rewrap column in Series to apply key function\u001b[39;00m\n\u001b[32m   7214\u001b[39m             \u001b[38;5;28;01mif\u001b[39;00m key \u001b[38;5;28;01mis\u001b[39;00m \u001b[38;5;28;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n",
      "\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\generic.py\u001b[39m in \u001b[36m?\u001b[39m\u001b[34m(self, key, axis)\u001b[39m\n\u001b[32m   1910\u001b[39m             values = self.xs(key, axis=other_axes[\u001b[32m0\u001b[39m])._values\n\u001b[32m   1911\u001b[39m         \u001b[38;5;28;01melif\u001b[39;00m self._is_level_reference(key, axis=axis):\n\u001b[32m   1912\u001b[39m             values = self.axes[axis].get_level_values(key)._values\n\u001b[32m   1913\u001b[39m         \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m-> \u001b[39m\u001b[32m1914\u001b[39m             \u001b[38;5;28;01mraise\u001b[39;00m KeyError(key)\n\u001b[32m   1915\u001b[39m \n\u001b[32m   1916\u001b[39m         \u001b[38;5;66;03m# Check for duplicates\u001b[39;00m\n\u001b[32m   1917\u001b[39m         \u001b[38;5;28;01mif\u001b[39;00m values.ndim > \u001b[32m1\u001b[39m:\n",
      "\u001b[31mKeyError\u001b[39m: 'health_score'"
     ]
    }
   ],
   "source": [
    "df.sort_values('health_score')[['item','health_score']].head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "fe64a300-11c6-4fc2-8ffc-96dd2e2c2820",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.groupby('menu')['calories'].mean().plot(kind='bar')\n",
    "plt.title(\"Average Calories by Category\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "ecaffe1f-b78d-463b-b6f9-fed5cec5b9a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAh8AAAIKCAYAAACDRi35AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjgsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvwVt1zgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAQ6JJREFUeJzt3Q2czWX+//GPm3J/k9shQiRKKFtISYiVLJtNqS2VVQqF9lfs9q+0imq31K7o1s2WdItuNkJRW+5LUlFswuZmVe5riO//8b7ac/acM2eYYeaac+b7ej4eJzPnnDnz7XvOfL/v73V9rusqEgRBYAAAAJ4U9fWLAAAACB8AAMA7Wj4AAIBXhA8AAOAV4QMAAHhF+AAAAF4RPgAAgFeEDwAA4BXhAwAAeEX4AJAW5s2bZ0WKFLGXXnqpoDcFwFEifCBtPfroo+5k1LJly4LelJSzb98+e/jhh+3000+38uXLW8WKFe3UU0+16667zlatWlXQm5cWli9fbr/97W+tdu3aVqJECatUqZJ17NjRJkyYYAcOHMj169177702ffr0fNlWIN0UL+gNAI7Us88+a3Xr1rXFixfbmjVrrEGDBuzM/+rZs6e9+eab1rt3b+vXr5/t37/fhY7XX3/dzj77bGvUqBH76hCefPJJ69+/v1WvXt2uvPJKO+mkk2zXrl02d+5c69u3r23atMn+8Ic/5Dp8/OY3v7EePXqw7xF6hA+kpa+++so++OADe+WVV+z66693QeTOO+/0ug0HDx50LQwlS5a0VLJkyRIXMu65554sJ8i//e1vtn37dktVe/bssTJlyhToNixcuNAFj9atW9s//vEPK1euXPSxwYMH29KlS23lypVWWKXCe4DCj24XpCWFjeOOO866du3qrib1fYSu8tVEfs0112T5uZ07d7qw8Pvf/z56X2ZmpgsuajlR87qa2W+99VZ3fyx18QwcOND9LnVh6LkzZ850j/35z392LQqVK1e2UqVKWYsWLZLWJvzwww920003WZUqVdxJ7Ve/+pX9+9//dq991113xT1X91977bXu6lu/S7/z6aefPuy+Wbt2rfu3TZs2WR4rVqyY28aIq6++2rUeJdK2aJuOZNu//vpru/HGG+3kk092+0K/75JLLrF169bFvd7EiRPdz86fP989v1q1alarVq3D/v+py0OhKiMjw50ktR0b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r3dfX3nllcFtt93mvv7666/dZyiM6tat6276zNSuXTv6vW4NGzYMOnXqFCxcuDAII+2TokWLupu+TryVLl06eOqpp4Iw4zicvXvuuSfo06dPsH///iBd0fKRhPrqn3/+eWvVqpW7aos49dRTbe3atRZGxx13nNsXujVs2DBuv+hKbffu3a5FJKy0pPWCBQusUqVK7qp16tSp7v7vv//eSpYsaWH01VdfuX/PP/981xqUiqtVF+S+UeuYWlQXL15sVatWjT6mrqhq1aqFvh6G43D2lixZ4laKf+utt+y0006zMmXKxD3+yiuvWKojfCShRfH0x59IK/PGnnTDRCsT62B57bXXuu6V2GWTdbCsW7eutW7d2sJq8ODBdsUVV7iuhTp16li7du3c/epa0MEhzP3T69evt02bNhE+YugzIgcPHiyotyblcRzOnoJ8unflEj6SULHgG2+84Wo8JBI41G8d1hNsnz593L/16tWzNm3aWPHifHRi3XjjjdayZUt3or3gggusaNGfa7l1ZXvPPfdYWBWa/ul89Pe//93Gjx/vWkPUeqZg8tBDD7nPTvfu3S2sOA5nb8KECZb2CrrfJxWp1qNs2bJB//79XV/+zTffHFxwwQWu737p0qVBmC1btixYsWJF9HvVwXTv3j0YPnx4kJmZGYTViBEjgj179mS5f+/eve6xMCsM/dP55dFHH3W1UiNHjgxKlSoVrS+bMGFC0K5duyDMOA4Xbqxqmw3VdowePdo+/vhjV89wxhln2G233RbqJnQ588wz3WgfNfn961//slNOOcUuvvhi1wfZtWtX1z0TRpqvQl0Lid11mstC96kuJqx+/etfu/5pdUmla/90ftHfz7333ms9evSwcuXKueONWjxWrlzpuu62bdtmYcZxOHsvvfSSvfDCC661NXG49ocffmipjrbzbGgc9RNPPOH33UgDGnbcvHlz9/WLL75o5513nk2ZMsXef/99u+yyy0IbPlQPk6weSCcTFaGGWWHon84v6mo5/fTTs9xfokQJV2MWNkOHDrU//elPLqCqXurss8/mOJzNMHYN7b/66qttxowZds0117igpovAAQMGWDogfCSh2QWT0clFB4UwT4ykk2ykSG7OnDl20UUXRUd7hPEqjVFAIemfzieqoVq+fHm0ADVCI6YaN25sYfPXv/7VtTArfGiUVLLWRJg9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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.groupby('menu')['sugar'].mean().plot(kind='bar')\n",
    "plt.title(\"Average Sugar by Category\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "d0a0ddb9-2102-4714-a270-8e7bd4f7d8af",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjAAAAIKCAYAAAA9EHWkAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjgsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvwVt1zgAAAAlwSFlzAAAPYQAAD2EBqD+naQAASf9JREFUeJzt3Qm8TfX+//GPY57HTCXcSihRZGi6wqVI+eXmKknlaqKiQdy6QorUbVAikuFGpCKplCGUZEwi1C1jhZ+/KWTe/8f7e39r3733OaTu2c7+nvV6Ph7b3nvttfdZZ51trc/6fj+f7zdHJBKJGAAAgEfSsnoDAAAAfisCGAAA4B0CGAAA4B0CGAAA4B0CGAAA4B0CGAAA4B0CGAAA4B0CGAAA4B0CGAAA4B0CGAAnxahRoyxHjhy2bt266LKGDRu6W6qYPXu228Y333wzqzcFwK8ggEEovPTSS+7EVK9evazelJRz8OBBe/755+3888+3IkWKWLFixeycc86x2267zVavXp3Vm5etLVu2zG688UarUKGC5c2b10qUKGFNmjSxkSNH2pEjR37z5z3xxBM2efLkpGwrkGpyZfUGACfD2LFjrVKlSrZw4UL717/+ZWeeeSY7/v+0bt3aPvjgA7v++uutU6dOdujQIRe4TJ061S666CKrWrVq0vbVRx99FNq/wyuvvGJ33HGHlSlTxtq3b29nnXWW/fzzzzZz5kzr2LGj/fTTT/a3v/3tNwcwf/7zn61Vq1ZJ224gVRDAINtbu3atffbZZ/b222/b7bff7oKZRx999KRuw9GjR11LR758+SyVLFq0yAUqjz/+eLqT5Ysvvmg7d+5M6s/PkyePhdHnn3/ugpcGDRrY+++/b4ULF46+1rVrV1u8eLGtWLHCsqu9e/dawYIFs3oz4Dm6kJDtKWApXry4tWjRwl2d6nlArQ1qtr/lllvSvW/37t0u4HjggQeiyw4cOOCCH7XgqMlfTf/du3d3y2Opu6pLly7uZ6k7RutOmzbNvfb000+7lo2SJUta/vz5rXbt2hnmXPzyyy92zz33WKlSpdwJ7uqrr7YffvjBfXbv3r3j1tXyW2+91V3N62fpZ7766qu/um++++47d3/xxReney1nzpxuG2N98cUXduWVV7qupkKFClnjxo3dyTjRypUrrVGjRu73O+2006xfv34uiEuUmAOTUZ5MbG6K7mPfe+6559ry5cvtj3/8oxUoUMD9XYJ9OWfOHNdlqG04++yzbcaMGXai1H2jgK5s2bLuRKt9v3Hjxujr+g7kzp3b/vd//zfde9X1pm64/fv3H/Pz+/Tp434ffT9ig5dAnTp17Oabb44+P5HvjD5PgcHo0aPdY91iP+NEvyPr1693v69+79KlS1u3bt3sww8/TLf/ZeLEiW5btE36nqo7TD8nlrZB3xV915o3b+5+33bt2v3X+xCwCJDNVa1aNdKxY0f3eO7cuREziyxcuDD6+q233hopVqxY5MCBA3HvGz16tFt30aJF7vmRI0ciTZs2jRQoUCDStWvXyMsvvxzp0qVLJFeuXJFrrrkm7r16X7Vq1SKnnHJKpE+fPpHBgwdHvvjiC/faaaedFrnrrrsiL774YuSZZ56J1K1b160/derUuM9o06aNW96+fXv3fj2vWbOmW/boo49G19u8ebP7zAoVKkT69u0bGTJkSOTqq6926z377LPH3TefffaZW69Tp06RQ4cOHXfdFStWRAoWLBgpV65c5LHHHosMGDAgUrly5UjevHkjn3/+eXS9n376yf3exYsXj/Tu3Tvy1FNPRc4666zIeeed537W2rVro+v+8Y9/dLfAyJEj060jH3/8sVuu+9j3li9f3v3eDz74YOSFF16IVK9ePZIzZ87I+PHjI2XLlnU//7nnnouceuqpkaJFi0Z279593N8x+Dk1atRw26u/T48ePSL58uWLVKlSJbJv3z633rfffuvW08+Mpe+Qfm99p45l7969kdy5c0caNWoUOVEn8p355z//6f4Wl156qXusm/6+v+U7smfPnsgf/vCHSP78+d3vrX2nnxV872L3f/C3uvDCC91naH29r1KlSpEdO3ZE1+vQoYPbrjPOOMM9Hjp0aGTMmDH/1T4EhAAG2drixYvdQXL69Onu+dGjR92B/N57742u8+GHH7p13n333bj3Nm/e3B3MAzohpKWlRT755JO49XRA1vvnzZsXXabnWnflypXptik4CQYOHjwYOffcc+NOaEuWLHGfoUAp1s0335wugFFwpqBi27Ztceu2bdvWnbQTf14s7Q8FAvrMMmXKRK6//noXLK1fvz7duq1atYrkyZMn8t1330WX/fjjj5HChQtHLrvssugybbM+b8GCBdFlW7dudduS2QGMlo0bNy66bPXq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vgk+IxKJ+BfA/B79+/e3Pn36pFteoUIFy06KPpfVW5C62DfsG743/H/iWJN9jsM///yzFS1a1K8AplSpUpYzZ07bsmVL3HI9L1u2bIbv6dmzp0v6DRw9etS2b99uJUuWtBw5clhWUjSpQGrjxo1WpEiRLN2WVMO+Yd/wveH/FMebrLU7xc5RanlR8FK+fPnjrpeSAUyePHmsdu3aNnPmTGvVqlU0INHzLl26ZPievHnzulusYsWKWSrRFyMVvhypiH3DvuF7w/8pjjdZq0gKnaOO1/KS0gGMqDWlQ4cOVqdOHatbt64999xztnfvXleVBAAAwi1lA5i//OUv9r//+7/Wq1cv27x5s9WqVcumTZuWLrEXAACET8oGMKLuomN1GflEXVsakC+xiwvsG743/J/ieMOxOKvl9fQclSPya3VKAAAAKSYlB7IDAAA4HgIYAADgHQIYAADgHQIYAADgHQIYAADgHQIYIMWH+J48ebKtWrXKwk7Ti2zdujXd8v/3//6fey2sGjVqZDt37szwu6PXgOyKAOYkOHjwoK1Zs8YOHz58Mn5cyuvbt6/t25d+ZtlffvnFvRZmbdq0sRdffDG6PzQStZadd9559tZbb1mYHWvEB81Cr+lHwmr27NnuGJNo//799sknn2TJNqUijsPxDh06ZGeccYbXF0cpPZCd73SSvvvuu2306NHu+TfffGN/+MMf3LJTTz3VevToYWGkWcPvuOMOK1CgQLr9pdc0+nJYzZ071x5++GH3eNKkSe6kratrfYf69etnrVu3trAZNGiQu9ekrK+88ooVKlQo+tqRI0fcPqtataqFzfLly6OPv/76azdieex+0cjlOs6EHcfhjOXOndsFuV7TQHZIjnvuuSdSu3btyCeffBIpWLBg5LvvvnPLJ0+eHKlVq1Zod3uOHDkiW7duTbd85syZkVKlSkXCLF++fJENGza4x+3bt4889NBD7vH69evddyiMKlWq5G763lSoUCH6XLcqVapEmjZtGvn8888jYaP9kZaW5m56nHgrUKBAZMSIEZGw4zh8bI8//nikQ4cOkUOHDkV8RAtMEil3YcKECVa/fn139Rg455xz7LvvvrOwKV68uNsPulWpUiVun+iKcc+ePa5lJsw0pf38+fOtRIkS7gp6/PjxbvmOHTssX758FkZr165195dffrlrlUq1Weazcr+o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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.groupby('menu')['sodium'].mean().plot(kind='bar')\n",
    "plt.title(\"Average Sodium by Category\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "f1d01cc1-adbb-4631-91e9-39fc8d865bb4",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "\"['health_score'] not in index\"",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mKeyError\u001b[39m                                  Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[51]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m report_df = \u001b[43mdf\u001b[49m\u001b[43m[\u001b[49m\u001b[43m[\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mitem\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mmenu\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mcalories\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mprotien\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43msugar\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43msodium\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mfood_type\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mhealth_score\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m]\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\frame.py:4119\u001b[39m, in \u001b[36mDataFrame.__getitem__\u001b[39m\u001b[34m(self, key)\u001b[39m\n\u001b[32m   4117\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m is_iterator(key):\n\u001b[32m   4118\u001b[39m         key = \u001b[38;5;28mlist\u001b[39m(key)\n\u001b[32m-> \u001b[39m\u001b[32m4119\u001b[39m     indexer = \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mcolumns\u001b[49m\u001b[43m.\u001b[49m\u001b[43m_get_indexer_strict\u001b[49m\u001b[43m(\u001b[49m\u001b[43mkey\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mcolumns\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m[\u001b[32m1\u001b[39m]\n\u001b[32m   4121\u001b[39m \u001b[38;5;66;03m# take() does not accept boolean indexers\u001b[39;00m\n\u001b[32m   4122\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mgetattr\u001b[39m(indexer, \u001b[33m\"\u001b[39m\u001b[33mdtype\u001b[39m\u001b[33m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m) == \u001b[38;5;28mbool\u001b[39m:\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\indexes\\base.py:6212\u001b[39m, in \u001b[36mIndex._get_indexer_strict\u001b[39m\u001b[34m(self, key, axis_name)\u001b[39m\n\u001b[32m   6209\u001b[39m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m   6210\u001b[39m     keyarr, indexer, new_indexer = \u001b[38;5;28mself\u001b[39m._reindex_non_unique(keyarr)\n\u001b[32m-> \u001b[39m\u001b[32m6212\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_raise_if_missing\u001b[49m\u001b[43m(\u001b[49m\u001b[43mkeyarr\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mindexer\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43maxis_name\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   6214\u001b[39m keyarr = \u001b[38;5;28mself\u001b[39m.take(indexer)\n\u001b[32m   6215\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(key, Index):\n\u001b[32m   6216\u001b[39m     \u001b[38;5;66;03m# GH 42790 - Preserve name from an Index\u001b[39;00m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\pandas\\core\\indexes\\base.py:6264\u001b[39m, in \u001b[36mIndex._raise_if_missing\u001b[39m\u001b[34m(self, key, indexer, axis_name)\u001b[39m\n\u001b[32m   6261\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m(\u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mNone of [\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mkey\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m] are in the [\u001b[39m\u001b[38;5;132;01m{\u001b[39;00maxis_name\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m]\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m   6263\u001b[39m not_found = \u001b[38;5;28mlist\u001b[39m(ensure_index(key)[missing_mask.nonzero()[\u001b[32m0\u001b[39m]].unique())\n\u001b[32m-> \u001b[39m\u001b[32m6264\u001b[39m \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m(\u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mnot_found\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m not in index\u001b[39m\u001b[33m\"\u001b[39m)\n",
      "\u001b[31mKeyError\u001b[39m: \"['health_score'] not in index\""
     ]
    }
   ],
   "source": [
    "report_df = df[['item','menu','calories','protien','sugar','sodium','food_type','health_score']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "c0143a8a-d317-4a23-8aa6-c66ac7dd25f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "menu\n",
       "gourmet       11.987636\n",
       "regular        7.213333\n",
       "breakfast      6.391250\n",
       "mccafe         4.384167\n",
       "dessert        3.548333\n",
       "condiments     0.608889\n",
       "beverage       0.225882\n",
       "Name: satfat, dtype: float64"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('menu')['satfat'].mean().sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "8b5923ed-287d-485e-8cbd-7cf0e09a3ff4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>item</th>\n",
       "      <th>menu</th>\n",
       "      <th>transfat</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>3 piece Chicken Strips</td>\n",
       "      <td>regular</td>\n",
       "      <td>75.26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>57</th>\n",
       "      <td>Flat White (L)</td>\n",
       "      <td>mccafe</td>\n",
       "      <td>41.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>76</th>\n",
       "      <td>Lemon Ice Tea</td>\n",
       "      <td>mccafe</td>\n",
       "      <td>18.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>132</th>\n",
       "      <td>Mustard diping sauce</td>\n",
       "      <td>condiments</td>\n",
       "      <td>0.47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69</th>\n",
       "      <td>English Breakfast (L)</td>\n",
       "      <td>mccafe</td>\n",
       "      <td>0.46</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75</th>\n",
       "      <td>Strawberry Green Tea (L)</td>\n",
       "      <td>mccafe</td>\n",
       "      <td>0.46</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>72</th>\n",
       "      <td>Moroccon Mint Green Tea (L)</td>\n",
       "      <td>mccafe</td>\n",
       "      <td>0.46</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>64</th>\n",
       "      <td>Hot Chocolate (L)</td>\n",
       "      <td>mccafe</td>\n",
       "      <td>0.43</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>60</th>\n",
       "      <td>Mocha (L)</td>\n",
       "      <td>mccafe</td>\n",
       "      <td>0.41</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>137</th>\n",
       "      <td>Maple Syrup</td>\n",
       "      <td>condiments</td>\n",
       "      <td>0.40</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                            item        menu  transfat\n",
       "24        3 piece Chicken Strips     regular     75.26\n",
       "57                Flat White (L)      mccafe     41.00\n",
       "76                 Lemon Ice Tea      mccafe     18.00\n",
       "132         Mustard diping sauce  condiments      0.47\n",
       "69         English Breakfast (L)      mccafe      0.46\n",
       "75      Strawberry Green Tea (L)      mccafe      0.46\n",
       "72   Moroccon Mint Green Tea (L)      mccafe      0.46\n",
       "64             Hot Chocolate (L)      mccafe      0.43\n",
       "60                     Mocha (L)      mccafe      0.41\n",
       "137                  Maple Syrup  condiments      0.40"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sort_values('transfat', ascending=False)[\n",
    "    ['item','menu','transfat']\n",
    "].head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "be24e93a-6d8e-4a0c-b613-dfaed881007d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "menu\n",
       "gourmet       49.179091\n",
       "regular       35.987778\n",
       "beverage      34.025294\n",
       "breakfast     33.560000\n",
       "dessert       33.525000\n",
       "mccafe        24.549167\n",
       "condiments     8.287778\n",
       "Name: carbs, dtype: float64"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('menu')['carbs'].mean().sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "ebfcc035-63c0-4a00-bd2e-fb70134c765f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>item</th>\n",
       "      <th>menu</th>\n",
       "      <th>carbs</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Veg Maharaja Mac</td>\n",
       "      <td>regular</td>\n",
       "      <td>93.84</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101</th>\n",
       "      <td>Medium Blackforest</td>\n",
       "      <td>dessert</td>\n",
       "      <td>79.04</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Ghee Rice with Mc Spicy Fried Chicken 1 pc</td>\n",
       "      <td>regular</td>\n",
       "      <td>77.47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>107</th>\n",
       "      <td>Chicken Cheese Lava Burger</td>\n",
       "      <td>gourmet</td>\n",
       "      <td>76.03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>106</th>\n",
       "      <td>Cheese Lava Burger</td>\n",
       "      <td>gourmet</td>\n",
       "      <td>74.25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>82</th>\n",
       "      <td>Chocolate Oreo Frappe</td>\n",
       "      <td>mccafe</td>\n",
       "      <td>72.51</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>42</th>\n",
       "      <td>Hot Cake with maple syrup</td>\n",
       "      <td>breakfast</td>\n",
       "      <td>68.01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>91</th>\n",
       "      <td>American Mud Pie Shake</td>\n",
       "      <td>mccafe</td>\n",
       "      <td>64.75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>120</th>\n",
       "      <td>Large Fanta Orange</td>\n",
       "      <td>beverage</td>\n",
       "      <td>64.22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>81</th>\n",
       "      <td>Mocha Frappe</td>\n",
       "      <td>mccafe</td>\n",
       "      <td>60.93</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                           item       menu  carbs\n",
       "5                              Veg Maharaja Mac    regular  93.84\n",
       "101                          Medium Blackforest    dessert  79.04\n",
       "18   Ghee Rice with Mc Spicy Fried Chicken 1 pc    regular  77.47\n",
       "107                  Chicken Cheese Lava Burger    gourmet  76.03\n",
       "106                          Cheese Lava Burger    gourmet  74.25\n",
       "82                        Chocolate Oreo Frappe     mccafe  72.51\n",
       "42                    Hot Cake with maple syrup  breakfast  68.01\n",
       "91                       American Mud Pie Shake     mccafe  64.75\n",
       "120                          Large Fanta Orange   beverage  64.22\n",
       "81                                 Mocha Frappe     mccafe  60.93"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sort_values('carbs', ascending=False)[\n",
    "    ['item','menu','carbs']\n",
    "].head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "5c7d7832-98b1-4ab6-8048-1df9b5b1e8a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>item</th>\n",
       "      <th>menu</th>\n",
       "      <th>cholestrol</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>109</th>\n",
       "      <td>McSpicy Premium Chicken Burger</td>\n",
       "      <td>gourmet</td>\n",
       "      <td>302.61</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40</th>\n",
       "      <td>Sausage Mc Muffin with egg</td>\n",
       "      <td>breakfast</td>\n",
       "      <td>264.80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>41</th>\n",
       "      <td>Egg McMuffin</td>\n",
       "      <td>breakfast</td>\n",
       "      <td>233.30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Mc Egg Masala Burger</td>\n",
       "      <td>regular</td>\n",
       "      <td>213.09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Mc Egg Burger for Happy Meal</td>\n",
       "      <td>regular</td>\n",
       "      <td>213.09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>38</th>\n",
       "      <td>Spicy Egg McMuffin</td>\n",
       "      <td>breakfast</td>\n",
       "      <td>212.61</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>108</th>\n",
       "      <td>Chunky Chipotle American Burger Chicken</td>\n",
       "      <td>gourmet</td>\n",
       "      <td>110.37</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Spicy Chicken Wrap</td>\n",
       "      <td>regular</td>\n",
       "      <td>87.63</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Chicken Maharaja Mac</td>\n",
       "      <td>regular</td>\n",
       "      <td>81.49</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>Vanilla Chocochips Muffin</td>\n",
       "      <td>regular</td>\n",
       "      <td>78.52</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                        item       menu  cholestrol\n",
       "109           McSpicy Premium Chicken Burger    gourmet      302.61\n",
       "40                Sausage Mc Muffin with egg  breakfast      264.80\n",
       "41                              Egg McMuffin  breakfast      233.30\n",
       "16                      Mc Egg Masala Burger    regular      213.09\n",
       "17              Mc Egg Burger for Happy Meal    regular      213.09\n",
       "38                        Spicy Egg McMuffin  breakfast      212.61\n",
       "108  Chunky Chipotle American Burger Chicken    gourmet      110.37\n",
       "11                        Spicy Chicken Wrap    regular       87.63\n",
       "12                      Chicken Maharaja Mac    regular       81.49\n",
       "35                 Vanilla Chocochips Muffin    regular       78.52"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sort_values('cholestrol', ascending=False)[\n",
    "    ['item','menu','cholestrol']\n",
    "].head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "1da2656e-65d1-45c7-878a-b35b39f37a57",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "menu\n",
       "beverage        0.829412\n",
       "breakfast     106.946250\n",
       "condiments      1.834444\n",
       "dessert         6.525000\n",
       "gourmet        73.210909\n",
       "mccafe         13.457062\n",
       "regular        35.987222\n",
       "Name: cholestrol, dtype: float64"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('menu')['cholestrol'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "ebb9addc-5da2-4b5f-85ce-bd405cbd773a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>item</th>\n",
       "      <th>menu</th>\n",
       "      <th>risk_score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>3 piece Chicken Strips</td>\n",
       "      <td>regular</td>\n",
       "      <td>794.1933</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>57</th>\n",
       "      <td>Flat White (L)</td>\n",
       "      <td>mccafe</td>\n",
       "      <td>440.8330</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>76</th>\n",
       "      <td>Lemon Ice Tea</td>\n",
       "      <td>mccafe</td>\n",
       "      <td>193.7276</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>82</th>\n",
       "      <td>Chocolate Oreo Frappe</td>\n",
       "      <td>mccafe</td>\n",
       "      <td>64.9160</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>107</th>\n",
       "      <td>Chicken Cheese Lava Burger</td>\n",
       "      <td>gourmet</td>\n",
       "      <td>62.5254</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>110</th>\n",
       "      <td>McSpicy Premium Veg Burger</td>\n",
       "      <td>gourmet</td>\n",
       "      <td>61.1737</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Veg Maharaja Mac</td>\n",
       "      <td>regular</td>\n",
       "      <td>57.5122</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>81</th>\n",
       "      <td>Mocha Frappe</td>\n",
       "      <td>mccafe</td>\n",
       "      <td>56.1082</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Spicy Paneer Wrap</td>\n",
       "      <td>regular</td>\n",
       "      <td>54.6846</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>91</th>\n",
       "      <td>American Mud Pie Shake</td>\n",
       "      <td>mccafe</td>\n",
       "      <td>53.3173</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>109</th>\n",
       "      <td>McSpicy Premium Chicken Burger</td>\n",
       "      <td>gourmet</td>\n",
       "      <td>52.6838</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>McSpicy Paneer Burger</td>\n",
       "      <td>regular</td>\n",
       "      <td>50.9608</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>106</th>\n",
       "      <td>Cheese Lava Burger</td>\n",
       "      <td>gourmet</td>\n",
       "      <td>50.0149</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>64</th>\n",
       "      <td>Hot Chocolate (L)</td>\n",
       "      <td>mccafe</td>\n",
       "      <td>49.1935</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>80</th>\n",
       "      <td>Cold Coffee Frappe</td>\n",
       "      <td>mccafe</td>\n",
       "      <td>49.0943</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                               item     menu  risk_score\n",
       "24           3 piece Chicken Strips  regular    794.1933\n",
       "57                   Flat White (L)   mccafe    440.8330\n",
       "76                    Lemon Ice Tea   mccafe    193.7276\n",
       "82            Chocolate Oreo Frappe   mccafe     64.9160\n",
       "107      Chicken Cheese Lava Burger  gourmet     62.5254\n",
       "110      McSpicy Premium Veg Burger  gourmet     61.1737\n",
       "5                  Veg Maharaja Mac  regular     57.5122\n",
       "81                     Mocha Frappe   mccafe     56.1082\n",
       "3                 Spicy Paneer Wrap  regular     54.6846\n",
       "91           American Mud Pie Shake   mccafe     53.3173\n",
       "109  McSpicy Premium Chicken Burger  gourmet     52.6838\n",
       "2            McSpicy Paneer Burger  regular     50.9608\n",
       "106              Cheese Lava Burger  gourmet     50.0149\n",
       "64                Hot Chocolate (L)   mccafe     49.1935\n",
       "80               Cold Coffee Frappe   mccafe     49.0943"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['risk_score'] = (\n",
    "    df['sugar'] * 0.5 +\n",
    "    df['sodium'] * 0.01 +\n",
    "    df['satfat'] * 2 +\n",
    "    df['transfat'] * 10\n",
    ")\n",
    "\n",
    "df.sort_values('risk_score', ascending=False)[\n",
    "    ['item','menu','risk_score']\n",
    "].head(15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d89ded30-7d87-41c9-a68c-908b250ab450",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "d5fd1480-db47-4b32-b6f5-ccc47c3d3028",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "menu\n",
       "regular       46.228278\n",
       "gourmet       42.399891\n",
       "mccafe        33.934525\n",
       "breakfast     23.633288\n",
       "dessert       20.614600\n",
       "beverage      18.477412\n",
       "condiments     6.842444\n",
       "Name: risk_score, dtype: float64"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('menu')['risk_score'].mean().sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "90434d5d-e6c5-47a4-8ada-d6dabcaa2d38",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "bd6dc4ea-98fe-44ba-8e9c-1ed403345e4a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>calories</th>\n",
       "      <th>sugar</th>\n",
       "      <th>sodium</th>\n",
       "      <th>satfat</th>\n",
       "      <th>transfat</th>\n",
       "      <th>protien</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>calories</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.029938</td>\n",
       "      <td>0.851800</td>\n",
       "      <td>0.776620</td>\n",
       "      <td>-0.004685</td>\n",
       "      <td>0.833290</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sugar</th>\n",
       "      <td>0.029938</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.299733</td>\n",
       "      <td>-0.047899</td>\n",
       "      <td>-0.056378</td>\n",
       "      <td>-0.287476</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sodium</th>\n",
       "      <td>0.851800</td>\n",
       "      <td>-0.299733</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.614493</td>\n",
       "      <td>0.029505</td>\n",
       "      <td>0.909905</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>satfat</th>\n",
       "      <td>0.776620</td>\n",
       "      <td>-0.047899</td>\n",
       "      <td>0.614493</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.212726</td>\n",
       "      <td>0.701758</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>transfat</th>\n",
       "      <td>-0.004685</td>\n",
       "      <td>-0.056378</td>\n",
       "      <td>0.029505</td>\n",
       "      <td>0.212726</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.079694</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>protien</th>\n",
       "      <td>0.833290</td>\n",
       "      <td>-0.287476</td>\n",
       "      <td>0.909905</td>\n",
       "      <td>0.701758</td>\n",
       "      <td>0.079694</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          calories     sugar    sodium    satfat  transfat   protien\n",
       "calories  1.000000  0.029938  0.851800  0.776620 -0.004685  0.833290\n",
       "sugar     0.029938  1.000000 -0.299733 -0.047899 -0.056378 -0.287476\n",
       "sodium    0.851800 -0.299733  1.000000  0.614493  0.029505  0.909905\n",
       "satfat    0.776620 -0.047899  0.614493  1.000000  0.212726  0.701758\n",
       "transfat -0.004685 -0.056378  0.029505  0.212726  1.000000  0.079694\n",
       "protien   0.833290 -0.287476  0.909905  0.701758  0.079694  1.000000"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cols = ['calories','sugar','sodium','satfat','transfat','protien']\n",
    "\n",
    "df[cols].corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "44eb544c-160e-46bc-ac05-4683b4a406a6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb6955a5-d12b-417c-a4ad-773f501775bb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
