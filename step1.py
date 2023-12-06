import pandas as pd

carac = pd.read_csv("data/carac.csv", sep=";")
lieux = pd.read_csv("data/lieux.csv", sep=";")
veh = pd.read_csv("data/veh.csv", sep=";")
vict = pd.read_csv("data/vict.csv", sep=";")

donneesfusionnees = pd.merge(carac, lieux, on="Num_Acc")
donneesfusionnees = pd.merge(donneesfusionnees, veh, on="Num_Acc")
donneesfusionnees = pd.merge(donneesfusionnees, vict, on="Num_Acc")

donneesfusionnees.to_csv("step1/donneesfusionnees.csv", index=False)