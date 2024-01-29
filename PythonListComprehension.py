##List Comprehension Alıştırmalar

## Alıştırma 1: car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çevrilip başına NUM eklenmesi.

import seaborn as sns
df = sns.load_dataset ("car_crashes")
df.columns

df.columns=["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]


## Alıştırma 2: car_crashes verisinde isminde "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazılması.

[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]


## Alıştırma 3: Verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini ile yeni bir dataframe oluşturulması.

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()