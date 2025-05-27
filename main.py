import pandas as pd 

#Extract data 
df = pd.read_csv("DMSP4-Task_02-movies.csv")

#Converting to numeric value
df["box_office"] = pd.to_numeric(df["box_office"], errors="coerce")

#Filter data
usa_df = df[df["country"] == "USA"]
russia_df = df[df["country"] == "Russia"]
uk_df = df[df["country"] == "UK"]
korea_df = df[df["country"] == "South Korea"]

#Adding new column 
usa_df["balance"] = usa_df["box_office"] - usa_df["budget"]
russia_df["balance"] = russia_df["box_office"] - russia_df["budget"]
uk_df["balance"] = uk_df["box_office"] - uk_df["budget"]
korea_df["balance"] = korea_df["box_office"] - korea_df["budget"]

#Removing columns
usa_df.drop(["language", "country", "duration", "budget", "box_office"],axis = 1, inplace = True)
russia_df.drop(["language", "country", "duration", "budget", "box_office"],axis = 1, inplace = True)
uk_df.drop(["language", "country", "duration", "budget", "box_office"],axis = 1, inplace = True)
korea_df.drop(["language", "country", "duration", "budget", "box_office"],axis = 1, inplace = True)

#Sorting data
usa_sorted= usa_df.sort_values(by="balance", ascending=False)
russia_sorted = russia_df.sort_values(by="balance", ascending=False)
uk_sorted = uk_df.sort_values(by="balance", ascending=False)
korea_sorted = korea_df.sort_values(by="balance", ascending=False)

#First 10 movies 
usa_top10 = usa_sorted.iloc[:9]
russia_top10 = russia_sorted.iloc[:9]
uk_top10 = uk_sorted.iloc[:9]
korea_top10 = korea_sorted.iloc[:9]

#Load data
usa_top10.to_excel("USA_top_10_profitable_movies.xlsx", index = False)
russia_top10.to_excel("Russia_top_10_profitable_movies.xlsx", index = False)
uk_top10.to_excel("UK_top_10_profitable_movies.xlsx", index = False)
korea_top10.to_excel("South_Korea_top_10_profitable_movies.xlsx", index = False)
