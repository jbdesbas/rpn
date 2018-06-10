import geopandas as gpd

class rpn:
    
    def __init__(self,path):
        self.data=self.loadData(path)
    
    def loadData(self,path): #Charger un shape (ou autre)
        df=gpd.read_file(path)       
        return df 
    
    def observateurs(self,split=True):#TODO gerer les observateurs multiples sur une obs
        list_obs=list(self.data.observ.unique())
        if split:
            list_obs=list(set(','.join(list_obs).split(',')))
        return sorted(list_obs)
