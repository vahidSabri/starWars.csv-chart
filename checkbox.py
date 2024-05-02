import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm



movies=["", "Star Wars: Episode I  The Phantom Menace", "Star Wars: Episode II  Attack of the Clones", "Star Wars: Episode III  Revenge of the Sith", "Star Wars: Episode IV  A New Hope", "Star Wars: Episode V The Empire Strikes Back", "Star Wars: Episode VI Return of the Jedi"] # This list for bar charts


# \\chart_{movieNumber}.png"


class checkbox:

    def graph(movieNumber=3 , csvSource=None , targetLocation=None, fileFormat="png", chartDpi=1000, colorMap=cm.tab10_r):
        global tempDF
        global df
        if csvSource == None : return "csv file not provided"
        df=pd.DataFrame
        df=pd.read_csv(csvSource, encoding="ISO-8859-1")
        
        tempDF= df.iloc[2:,(movieNumber+2)]
        seen= tempDF.notnull()
        colors = colorMap(np.linspace(0, 1, len(seen.value_counts())))
        seen.value_counts().plot.pie(autopct='%.2f%%',colors=colors, labels=["Yes", "No"])
        
        
        plt.title(f"Have you seen: '{movies[movieNumber]}'")
        plt.ylabel("")
        if targetLocation!= None : plt.savefig(f"{targetLocation}\\chart_{movieNumber}.{fileFormat}", format=fileFormat, dpi=chartDpi)
        plt.show()
        plt.clf()


    def viewCount(movieNumber, csvSource):
        global tempDF

        df=pd.DataFrame
        df=pd.read_csv(csvSource, encoding="ISO-8859-1")
        
        tempDF=pd.DataFrame
        tempDF= df.iloc[2:,(movieNumber+2)]
        
        seen= tempDF.notnull()
        return tempDF.count()


# example usage ::: checkbox.graph(movieNumber=4, csvSource="StarWars.csv",fileFormat="png", chartDpi=300, targetLocation="")

# example usage ::: checkbox.viewCount(movieNumber=6, csvSource="StarWars.csv")