
**Player Count**

* Total Number of Players

**Purchasing Analysis (Total)**

* Number of Unique Items
* Average Purchase Price
* Total Number of Purchases
* Total Revenue

**Gender Demographics**

* Percentage and Count of Male Players
* Percentage and Count of Female Players
* Percentage and Count of Other / Non-Disclosed

**Purchasing Analysis (Gender)** 

* The below each broken by gender
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value
  * Normalized Totals

**Age Demographics**

* The below each broken into bins of 4 years (i.e. &lt;10, 10-14, 15-19, etc.) 
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value
  * Normalized Totals

**Top Spenders**

* Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
  * SN
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value

**Most Popular Items**

* Identify the 5 most popular items by purchase count, then list (in a table):
  * Item ID
  * Item Name
  * Purchase Count
  * Item Price
  * Total Purchase Value

**Most Profitable Items**

* Identify the 5 most profitable items by total purchase value, then list (in a table):
  * Item ID
  * Item Name
  * Purchase Count
  * Item Price
  * Total Purchase Value


```python
import pandas as pd
import os

```


```python
# import dictionary as dataframe
# each dictionary is a value, there are repeated dictionary with same SN

file = os.path.join('HeroesOfPymoli', 'purchase_data.json')

# Read our Kickstarter data into pandas
df = pd.read_json(file)
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Player Count: Total Number of Players
print(df.describe())
print(df["SN"].unique().size)
```

                  Age     Item ID       Price
    count  780.000000  780.000000  780.000000
    mean    22.729487   91.293590    2.931192
    std      6.930604   52.707537    1.115780
    min      7.000000    0.000000    1.030000
    25%     19.000000   44.000000    1.960000
    50%     22.000000   91.000000    2.880000
    75%     25.000000  135.000000    3.910000
    max     45.000000  183.000000    4.950000
    573



```python
'''
Purchasing Analysis (Total):
Number of Unique Items
Average Purchase Price
Total Number of Purchases
Total Revenue''';
print("Number of Unique Items: "+str(df["Item Name"].unique().size))
print("Average Purchase Price: "+str(df["Price"].mean().round(2)))
print(df["Price"].count())
print(df["Price"].sum())
```

    Number of Unique Items: 179
    Average Purchase Price: 2.93
    780
    2286.33



```python
'''Gender Demographics
Percentage and Count of Male Players
Percentage and Count of Female Players
Percentage and Count of Other / Non-Disclosed''';
df_grp3=pd.DataFrame({"SN":df["SN"],"Gender":df["Gender"]})
df_grp3_uni=df_grp3.drop_duplicates()
print(df_grp3_uni["SN"].count())


df_gender=df_grp3_uni["Gender"].value_counts()
df_g_sum=df_gender.sum()
# print(df_g_sum)
# print(df_gender)
df_g_percent=(df_gender/df_g_sum*100).round(2)
df_grp3_fin=pd.DataFrame({"Percentage":df_g_percent,"Count":df_gender})
print(df_grp3_fin)


```

    573
                           Count  Percentage
    Male                     465       81.15
    Female                   100       17.45
    Other / Non-Disclosed      8        1.40



```python
'''Purchasing Analysis (Gender)
The below each broken by gender
Purchase Count
Average Purchase Price
Total Purchase Value
Normalized Totals''';
df_gb=df.groupby(["Gender"])
df_grp4_cn=df_gb["Price"].count()
df_grp4_avg=df_gb["Price"].mean().round(2)
df_grp4_tot=df_gb["Price"].sum().round(2)
df_grp4_ntot=(df_gb["Price"].sum()/df_gender).round(2)
df_grp4_fin=pd.DataFrame({"Purchase Count":df_grp4_cn,"Average Purchase Price":df_grp4_avg,
                         "Tot Purchase Value":df_grp4_tot,"Normalized Totals":df_grp4_ntot})
print(df_grp4_fin)
```

                           Average Purchase Price  Normalized Totals  \
    Gender                                                             
    Female                                   2.82               3.83   
    Male                                     2.95               4.02   
    Other / Non-Disclosed                    3.25               4.47   
    
                           Purchase Count  Tot Purchase Value  
    Gender                                                     
    Female                            136              382.91  
    Male                              633             1867.68  
    Other / Non-Disclosed              11               35.74  



```python
'''Age Demographics
The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)
Purchase Count
Average Purchase Price
Total Purchase Value
Normalized Totals''';
bins=[]
group_names=[]

bins.append(0)
x=10
bins.append(x)
y=0

if df["Age"].max()>60:
    print("Please increase the bin!")
else:
    while x<60:
        x+=4
        bins.append(x)
        group_names.append(str(bins[y])+"-"+str(bins[y+1]))
    #     print(bins)
    #     print(group_names)
        y+=1

del bins[-1]
# print(bins)

#
df["Age"].max()
df["Age"].min()

df_grp5=pd.DataFrame({"SN":df["SN"],"Gender":df["Gender"],"Age":df["Age"]})
df_grp5_uni=df_grp5.drop_duplicates()

df_grp5_uni["Age Group"]=pd.cut(df_grp5_uni["Age"],bins,labels=group_names)
df_group_uni=df_grp5_uni.groupby("Age Group")
df_grp_c=df_group_uni.count()["SN"]

df["Age Group"]=pd.cut(df["Age"],bins,labels=group_names)
df_group=df.groupby("Age Group")
df_grp_tp=df_group["Price"].sum().round(2)
df_grp_ap=df_group["Price"].mean().round(2)

df_grp_nt=(df_group["Price"].sum()/df_group_uni.count()["SN"]).round(2)
df_ag=pd.DataFrame({"Count":df_grp_c,"Average Price":df_grp_ap, 
                    "Tot Purchase Value":df_grp_tp,"Normalized Totals":df_grp_nt})
df_ag[["Count","Average Price","Tot Purchase Value","Normalized Totals"]]
    
```

    /Users/lena/anaconda3/envs/PythonData/lib/python3.6/site-packages/ipykernel_launcher.py:36: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Count</th>
      <th>Average Price</th>
      <th>Tot Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0-10</th>
      <td>22</td>
      <td>3.02</td>
      <td>96.62</td>
      <td>4.39</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>20</td>
      <td>2.70</td>
      <td>83.79</td>
      <td>4.19</td>
    </tr>
    <tr>
      <th>14-18</th>
      <td>84</td>
      <td>2.88</td>
      <td>319.32</td>
      <td>3.80</td>
    </tr>
    <tr>
      <th>18-22</th>
      <td>178</td>
      <td>2.93</td>
      <td>676.20</td>
      <td>3.80</td>
    </tr>
    <tr>
      <th>22-26</th>
      <td>153</td>
      <td>2.94</td>
      <td>608.02</td>
      <td>3.97</td>
    </tr>
    <tr>
      <th>26-30</th>
      <td>44</td>
      <td>2.98</td>
      <td>187.99</td>
      <td>4.27</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>34</td>
      <td>3.07</td>
      <td>141.24</td>
      <td>4.15</td>
    </tr>
    <tr>
      <th>34-38</th>
      <td>25</td>
      <td>2.81</td>
      <td>104.06</td>
      <td>4.16</td>
    </tr>
    <tr>
      <th>38-42</th>
      <td>11</td>
      <td>3.13</td>
      <td>62.56</td>
      <td>5.69</td>
    </tr>
    <tr>
      <th>42-46</th>
      <td>2</td>
      <td>3.26</td>
      <td>6.53</td>
      <td>3.26</td>
    </tr>
    <tr>
      <th>46-50</th>
      <td>0</td>
      <td>NaN</td>
      <td>0.00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50-54</th>
      <td>0</td>
      <td>NaN</td>
      <td>0.00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>54-58</th>
      <td>0</td>
      <td>NaN</td>
      <td>0.00</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
'''Top Spenders
Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
SN
Purchase Count
Average Purchase Price
Total Purchase Value''';
df_grp1=df.groupby("SN")
df_grp1_cn=df_grp1["Price"].count()
df_grp1_tot=df_grp1["Price"].sum()
df_grp1_avg=(df_grp1_tot/df_grp1_cn).round(2)
df_grp1_fin=pd.DataFrame({"Purchase Count":df_grp1_cn,
                          "Avg Purchase Price":df_grp1_avg,"Tot Purchase Value":df_grp1_tot})
df_grp1_fin.sort_values("Tot Purchase Value",ascending=False).head()



```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Avg Purchase Price</th>
      <th>Purchase Count</th>
      <th>Tot Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>3.41</td>
      <td>5</td>
      <td>17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>3.39</td>
      <td>4</td>
      <td>13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>3.18</td>
      <td>4</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>4.24</td>
      <td>3</td>
      <td>12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3.86</td>
      <td>3</td>
      <td>11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
'''Most Popular Items
Identify the 5 most popular items by purchase count, then list (in a table):
Item ID
Item Name
Purchase Count
Item Price
Total Purchase Value''';
df_grp2=df.groupby(["Item ID","Item Name"])
df_grp2_cn=df_grp2["Price"].count()
df_grp2_p=df_grp2["Price"].mean()
df_grp2_tot=df_grp2["Price"].sum()

df_grp2_fin=pd.DataFrame({"Purchase Count":df_grp2_cn, "Item Price": df_grp2_p,
                          "Tot Purchase Value":df_grp2_tot})
df_grp2_fin.sort_values("Purchase Count",ascending=False)[["Purchase Count",
                                                           "Item Price","Tot Purchase Value"]].head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Tot Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>2.35</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>2.23</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>2.07</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <td>9</td>
      <td>1.24</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>1.49</td>
      <td>13.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
'''Most Profitable Items
Identify the 5 most profitable items by total purchase value, then list (in a table):
Item ID
Item Name
Purchase Count
Item Price
Total Purchase Value''';

df_grp2_fin.sort_values("Tot Purchase Value",ascending=False)[["Purchase Count",
                                                           "Item Price","Tot Purchase Value"]].head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Tot Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>7</td>
      <td>4.25</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>6</td>
      <td>4.95</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>6</td>
      <td>4.87</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>8</td>
      <td>3.61</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
import pandas as pd
import os
from IPython.display import display, HTML

file = os.path.join('HeroesOfPymoli', 'purchase_data.json')

# Read our Kickstarter data into pandas
df = pd.read_json(file)
print("Heros of Pymoli Stats")
print("-"*50+"\n")
print("Total Number of Players: "+ str(df["SN"].unique().size))

print("\n"+"-"*10+"\n")
print("Purchasing Analysis - Total\n")
print("Number of Unique Items: "+str(df["Item Name"].unique().size))
print("Average Purchase Price: "+str(df["Price"].mean().round(2)))
print("Total Number of Purchases: "+str(df["Price"].count()))
print("Total Revenue: "+str(df["Price"].sum()))

print("\n"+"-"*10+"\n")
print("Gender Demographics\n")
display(df_grp3_fin)

print("\n"+"-"*10+"\n")
print("Purchasing Analysis - Gender")
print("The below each broken by gender\n")
print("note: normalized total is calculated as total purchasing price"+ 
      " divided by number of female/male, not the count of transactions.")
display(df_grp4_fin)

print("\n"+"-"*10+"\n")
print("Age Demographics")
print("The below each broken into bins of 4 years\n")
print("note: normalized total is calculated as total purchasing price"+ 
      " divided by count of age group, not the count of transactions.")
display(df_ag[["Count","Average Price","Tot Purchase Value","Normalized Totals"]])

print("\n"+"-"*10+"\n")
print("Top Spenders")
print("Identify the the top 5 spenders in the game by total purchase value\n")
display(df_grp1_fin.sort_values("Tot Purchase Value",ascending=False).head())

print("\n"+"-"*10+"\n")
print("Most Popular Items")
print("Identify the 5 most popular items by purchase count:\n")
display(df_grp2_fin.sort_values("Purchase Count",ascending=False)[["Purchase Count",
                                                           "Item Price","Tot Purchase Value"]].head())

print("\n"+"-"*10+"\n")
print("Most Profitable Items\n")
display(df_grp2_fin.sort_values("Tot Purchase Value",ascending=False)[["Purchase Count",
                                                           "Item Price","Tot Purchase Value"]].head())

print("Description of three observable trends based on file 1 data")
print("-"*10)
print("1. While some players brought 1 item, other players made more than 1 purchase.")
print("2. There are about 4.5x male players than female players.")
print("3. The age group that made the most purchases are 18-22.")





```

    Heros of Pymoli Stats
    --------------------------------------------------
    
    Total Number of Players: 573
    
    ----------
    
    Purchasing Analysis - Total
    
    Number of Unique Items: 179
    Average Purchase Price: 2.93
    Total Number of Purchases: 780
    Total Revenue: 2286.33
    
    ----------
    
    Gender Demographics
    



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Count</th>
      <th>Percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>465</td>
      <td>81.15</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>100</td>
      <td>17.45</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>8</td>
      <td>1.40</td>
    </tr>
  </tbody>
</table>
</div>


    
    ----------
    
    Purchasing Analysis - Gender
    The below each broken by gender
    
    note: normalized total is calculated as total purchasing price divided by number of female/male, not the count of transactions.



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Normalized Totals</th>
      <th>Purchase Count</th>
      <th>Tot Purchase Value</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>2.82</td>
      <td>3.83</td>
      <td>136</td>
      <td>382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>2.95</td>
      <td>4.02</td>
      <td>633</td>
      <td>1867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>3.25</td>
      <td>4.47</td>
      <td>11</td>
      <td>35.74</td>
    </tr>
  </tbody>
</table>
</div>


    
    ----------
    
    Age Demographics
    The below each broken into bins of 4 years
    
    note: normalized total is calculated as total purchasing price divided by count of age group, not the count of transactions.



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Count</th>
      <th>Average Price</th>
      <th>Tot Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0-10</th>
      <td>22</td>
      <td>3.02</td>
      <td>96.62</td>
      <td>4.39</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>20</td>
      <td>2.70</td>
      <td>83.79</td>
      <td>4.19</td>
    </tr>
    <tr>
      <th>14-18</th>
      <td>84</td>
      <td>2.88</td>
      <td>319.32</td>
      <td>3.80</td>
    </tr>
    <tr>
      <th>18-22</th>
      <td>178</td>
      <td>2.93</td>
      <td>676.20</td>
      <td>3.80</td>
    </tr>
    <tr>
      <th>22-26</th>
      <td>153</td>
      <td>2.94</td>
      <td>608.02</td>
      <td>3.97</td>
    </tr>
    <tr>
      <th>26-30</th>
      <td>44</td>
      <td>2.98</td>
      <td>187.99</td>
      <td>4.27</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>34</td>
      <td>3.07</td>
      <td>141.24</td>
      <td>4.15</td>
    </tr>
    <tr>
      <th>34-38</th>
      <td>25</td>
      <td>2.81</td>
      <td>104.06</td>
      <td>4.16</td>
    </tr>
    <tr>
      <th>38-42</th>
      <td>11</td>
      <td>3.13</td>
      <td>62.56</td>
      <td>5.69</td>
    </tr>
    <tr>
      <th>42-46</th>
      <td>2</td>
      <td>3.26</td>
      <td>6.53</td>
      <td>3.26</td>
    </tr>
    <tr>
      <th>46-50</th>
      <td>0</td>
      <td>NaN</td>
      <td>0.00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50-54</th>
      <td>0</td>
      <td>NaN</td>
      <td>0.00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>54-58</th>
      <td>0</td>
      <td>NaN</td>
      <td>0.00</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>


    
    ----------
    
    Top Spenders
    Identify the the top 5 spenders in the game by total purchase value
    



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Avg Purchase Price</th>
      <th>Purchase Count</th>
      <th>Tot Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>3.41</td>
      <td>5</td>
      <td>17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>3.39</td>
      <td>4</td>
      <td>13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>3.18</td>
      <td>4</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>4.24</td>
      <td>3</td>
      <td>12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3.86</td>
      <td>3</td>
      <td>11.58</td>
    </tr>
  </tbody>
</table>
</div>


    
    ----------
    
    Most Popular Items
    Identify the 5 most popular items by purchase count:
    



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Tot Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>2.35</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>2.23</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>2.07</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <td>9</td>
      <td>1.24</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>1.49</td>
      <td>13.41</td>
    </tr>
  </tbody>
</table>
</div>


    
    ----------
    
    Most Profitable Items
    



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Tot Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>7</td>
      <td>4.25</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>6</td>
      <td>4.95</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>6</td>
      <td>4.87</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>8</td>
      <td>3.61</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>


    Description of three observable trends based on file 1 data
    ----------
    1. While some players brought 1 item, some players made more than 1 purchase.
    2. There are about 4.5x male players than female players.
    3. The age group that made the most purchases are 18-22.

