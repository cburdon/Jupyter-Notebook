
# Heroes of Pymoli Data Analysis

Of the 573 active players, roughly 81% are male.  There exists a smaller but not insignificant proportion of female players (17%), and a very small percentage (1.4%) that do not identify as either.

Our peak age demographic is 20-24 (45%), with the two runners up being 15-19 (17.4%) and 25-29 (15%) respectively.
While the older gamers make up a smaller percentage of the active player base (~2%), they also spend more on average on items ($4.89 per user normalized by player count).  The trend also includes gamers up to age 14 (above $4 per user) as they are not earning the income that they are spending.

Our most popular item is Betrayal, Whisper of Grieving Widows (11 purchases), while the top earner is the Retribution Axe ($37.26 total earnings). We can expect each of our active players across all major demographics to spend about $3 on in-game items.




```python
#import dependencies
import pandas as pd

```


```python
#import and read JSON file as dataframe
filepath = "purchase_data.json"
game_df = pd.read_json(filepath)
game_df.head()

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



# Player Count


```python
#find total number of players in the game by unique SN
player_count = game_df["SN"].unique()
players = len(player_count)
player_dict = {"Total Players" : [players]}
player_df = pd.DataFrame(player_dict)
player_df

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
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>




```python
#do a similar operation to find the total number of unique Item names
item_name = game_df["Item Name"].unique()
items = len(item_name)
item_dict = {"Total # of unique items" : [items]}
item_df = pd.DataFrame(item_dict)
```

# Purchasing Analysis (Total)


```python
#find average item price, purchase total, purchase count
avg_price = game_df["Price"].mean()
avg_price
purchase_total = game_df["Price"].sum()
purchase_total
purchase_count = game_df["Price"].count()
purchase_count
totalpricedict = {"Unique Items" : [items], "Average Price" : [avg_price], "Purchase Count" : [purchase_count], "Purchase Total": [purchase_total]}
totalprice_df = pd.DataFrame(totalpricedict)
totalprice_df["Average Price"] = totalprice_df["Average Price"].map("${:.2f}".format)
totalprice_df["Purchase Total"] = totalprice_df["Purchase Total"].map("${:,.2f}".format)
totalprice_df
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
      <th>Average Price</th>
      <th>Purchase Count</th>
      <th>Purchase Total</th>
      <th>Unique Items</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>$2.93</td>
      <td>780</td>
      <td>$2,286.33</td>
      <td>179</td>
    </tr>
  </tbody>
</table>
</div>



# Gender Demographics


```python
#find number/percent of players in each gender using groupby("Gender") and len
playerlist = game_df.groupby(["Gender"])
genderlist = playerlist["SN"].unique()
Females = len(genderlist["Female"])
Males = len(genderlist["Male"])
Other = len(genderlist["Other / Non-Disclosed"])
MalePercent = round((Males/players) * 100, 2) 
FemalePercent = round((Females/players) * 100, 2)
OtherPercent = round((Other/players) * 100, 2)
demographicdict = {" " : ["Number of Players", "Percent of Total Players"], "Male" : [Males, MalePercent], "Female" : [Females, FemalePercent], "Other / Non-Disclosed" : [Other, OtherPercent]}
demograph_df = pd.DataFrame(demographicdict)
demograph_df


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
      <th>Female</th>
      <th>Male</th>
      <th>Other / Non-Disclosed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Number of Players</td>
      <td>100.00</td>
      <td>465.00</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Percent of Total Players</td>
      <td>17.45</td>
      <td>81.15</td>
      <td>1.4</td>
    </tr>
  </tbody>
</table>
</div>



# Purchasing Analysis (Gender)


```python
#make separate dataframes for each gender using .loc[] and pull relevant demographic info
gender_df = game_df.set_index("Gender")
Male_df = gender_df.loc["Male", :]
Female_df = gender_df.loc["Female", :]
Other_df = gender_df.loc["Other / Non-Disclosed", :]
Male_purchases_count = Male_df["Price"].count()
Female_purchases_count = Female_df["Price"].count()
Other_purchases_count = Other_df["Price"].count()
Male_purchase_total = round(Male_df["Price"].sum(), 2)
Female_purchase_total = round(Female_df["Price"].sum(), 2)
Other_purchase_total = round(Other_df["Price"].sum(), 2)
Male_avg_purchase = round(Male_df["Price"].mean(), 2)
Female_avg_purchase = round(Female_df["Price"].mean(), 2)
Other_avg_purchase = round(Other_df["Price"].mean(), 2)
gender_purchase_dict = {"Gender": ["Male", "Female", "Other/Non-Disclosed"], "Total Number of Purchases" : [Male_purchases_count, Female_purchases_count, Other_purchases_count], "Purchase Amount" : [Male_purchase_total, Female_purchase_total, Other_purchase_total], "Purchase Amount Average" : [Male_avg_purchase, Female_avg_purchase, Other_avg_purchase]}
gender_purchase_df = pd.DataFrame(gender_purchase_dict)
gender_purchase_df["Normalized Total"] = [round(Male_purchase_total/Males, 2), round(Female_purchase_total/Females, 2), round(Other_purchase_total/Other, 2)]
gender_purchase_df["Purchase Amount Average"] = gender_purchase_df["Purchase Amount Average"].map("${:.2f}".format)
gender_purchase_df["Purchase Amount"] = gender_purchase_df["Purchase Amount"].map("${:.2f}".format)
gender_purchase_df["Normalized Total"] = gender_purchase_df["Normalized Total"].map("${:.2f}".format)
gender_purchase_df
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
      <th>Gender</th>
      <th>Purchase Amount</th>
      <th>Purchase Amount Average</th>
      <th>Total Number of Purchases</th>
      <th>Normalized Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Male</td>
      <td>$1867.68</td>
      <td>$2.95</td>
      <td>633</td>
      <td>$4.02</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Female</td>
      <td>$382.91</td>
      <td>$2.82</td>
      <td>136</td>
      <td>$3.83</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Other/Non-Disclosed</td>
      <td>$35.74</td>
      <td>$3.25</td>
      <td>11</td>
      <td>$4.47</td>
    </tr>
  </tbody>
</table>
</div>



# Age Demographics


```python
#Use binning and .cut to get counts of players in several age ranges
bins = [0, 9, 14, 19, 24, 29, 34, 39, 100]
labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
test_score_series = pd.cut(game_df["Age"], bins, labels=labels)
game_df_new = pd.read_json(filepath)
game_df_new["Age Demographics"] = test_score_series
game_df_new["SN"] = game_df_new["SN"].drop_duplicates()
age_groups = game_df_new.groupby("Age Demographics")
age_groups_df = pd.DataFrame(age_groups["SN"].count())
age_groups_df["Percent of Total Players"] = round(age_groups_df["SN"]/ players * 100, 2)
age_groups_df = age_groups_df.rename(columns = {"SN" : "Player Count"})
age_groups_df["Percent of Total Players"] = age_groups_df["Percent of Total Players"].map("{:.2f}%".format)
age_groups_df
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
      <th>Player Count</th>
      <th>Percent of Total Players</th>
    </tr>
    <tr>
      <th>Age Demographics</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>19</td>
      <td>3.32%</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>23</td>
      <td>4.01%</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>100</td>
      <td>17.45%</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>259</td>
      <td>45.20%</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>87</td>
      <td>15.18%</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>47</td>
      <td>8.20%</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>27</td>
      <td>4.71%</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>11</td>
      <td>1.92%</td>
    </tr>
  </tbody>
</table>
</div>



# Purchasing Analysis (Age)


```python
#Use previous groupby series to get purchase amount, purchase count, normalized totals, and avg purchase by age range
age_purchase_df = pd.DataFrame(age_groups["Price"].count())
age_purchase_df = age_purchase_df.rename(columns = {"Price" : "Purchase Count"})
age_purchase_df["Total Purchase Amount"] = age_groups["Price"].sum()
age_purchase_df["Average Purchase"] = round(age_groups["Price"].mean(), 2)
age_purchase_df["Normalized Totals"] = round(age_purchase_df["Total Purchase Amount"] / age_groups_df["Player Count"], 2)
age_purchase_df["Total Purchase Amount"] = age_purchase_df["Total Purchase Amount"].map("${:.2f}".format)
age_purchase_df["Average Purchase"] = age_purchase_df["Average Purchase"].map("${:.2f}".format)
age_purchase_df["Normalized Totals"] = age_purchase_df["Normalized Totals"].map("${:.2f}".format)
age_purchase_df
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
      <th>Purchase Count</th>
      <th>Total Purchase Amount</th>
      <th>Average Purchase</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Age Demographics</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>28</td>
      <td>$83.46</td>
      <td>$2.98</td>
      <td>$4.39</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>35</td>
      <td>$96.95</td>
      <td>$2.77</td>
      <td>$4.22</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133</td>
      <td>$386.42</td>
      <td>$2.91</td>
      <td>$3.86</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>336</td>
      <td>$978.77</td>
      <td>$2.91</td>
      <td>$3.78</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>125</td>
      <td>$370.33</td>
      <td>$2.96</td>
      <td>$4.26</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>64</td>
      <td>$197.25</td>
      <td>$3.08</td>
      <td>$4.20</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>42</td>
      <td>$119.40</td>
      <td>$2.84</td>
      <td>$4.42</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>17</td>
      <td>$53.75</td>
      <td>$3.16</td>
      <td>$4.89</td>
    </tr>
  </tbody>
</table>
</div>



# Top Spenders


```python
#Groupby SN to get similar values for top spending players, sort values by highest amount.
top_spenders_group = pd.DataFrame()
top_spenders_group["Purchase Count"] = game_df.groupby("SN")["Price"].count()
top_spenders_group["Average Purchase Price"] = round(game_df.groupby("SN")["Price"].mean(), 2)
top_spenders_group["Total Purchase Amount"] = round(game_df.groupby("SN")["Price"].sum(), 2)
sorted_spenders_group = top_spenders_group.sort_values(by="Total Purchase Amount", ascending = False).head()
sorted_spenders_group["Total Purchase Amount"] = top_spenders_group["Total Purchase Amount"].map("${:.2f}".format)
sorted_spenders_group["Average Purchase Price"] = top_spenders_group["Average Purchase Price"].map("${:.2f}".format)
sorted_spenders_group
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
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Amount</th>
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
      <td>5</td>
      <td>$3.41</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>$3.39</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>$3.18</td>
      <td>$12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>3</td>
      <td>$4.24</td>
      <td>$12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3</td>
      <td>$3.86</td>
      <td>$11.58</td>
    </tr>
  </tbody>
</table>
</div>



# Most Popular Items


```python
#groupby ID and Item Name to pull purchase info on individual items using count and sum, then sort by purchase count
top_items_group = pd.DataFrame()
top_items_group["Purchase Count"] = game_df.groupby(["Item ID", "Item Name"])["Price"].count()
top_items_group["Total Purchase Value"] = game_df.groupby(["Item ID", "Item Name"])["Price"].sum()
top_items_group["Item Price"] = top_items_group["Total Purchase Value"] / top_earners_group["Purchase Count"]
sorted_items_group = top_items_group.sort_values(by="Purchase Count", ascending = False).head()
sorted_items_group["Total Purchase Value"] = sorted_items_group["Total Purchase Value"].map("${:.2f}".format)
sorted_items_group["Item Price"] = sorted_items_group["Item Price"].map("${:.2f}".format)
sorted_items_group

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
      <th>Total Purchase Value</th>
      <th>Item Price</th>
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
      <td>$25.85</td>
      <td>$2.35</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>$24.53</td>
      <td>$2.23</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>$18.63</td>
      <td>$2.07</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <td>9</td>
      <td>$11.16</td>
      <td>$1.24</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>$13.41</td>
      <td>$1.49</td>
    </tr>
  </tbody>
</table>
</div>



# Most Profitable Items


```python
#use unsorted version of previous dataframe and sort by total purchase value
sorted_top_earners = top_items_group.sort_values(by="Total Purchase Value", ascending=False).head()
sorted_top_earners["Total Purchase Value"] = sorted_top_earners["Total Purchase Value"].map("${:.2f}".format)
sorted_top_earners["Item Price"] = sorted_top_earners["Item Price"].map("${:.2f}".format)
sorted_top_earners
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
      <th>Total Purchase Value</th>
      <th>Item Price</th>
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
      <td>$37.26</td>
      <td>$4.14</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>7</td>
      <td>$29.75</td>
      <td>$4.25</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>6</td>
      <td>$29.70</td>
      <td>$4.95</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>6</td>
      <td>$29.22</td>
      <td>$4.87</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>8</td>
      <td>$28.88</td>
      <td>$3.61</td>
    </tr>
  </tbody>
</table>
</div>


