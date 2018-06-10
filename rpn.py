import geopandas as gpd
import os,uuid

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

class token:
    def __init__(self):
        self.uuid=str(uuid.uuid4())
    
    def extension(self):
        for ext in ['shp','gpkg']:
            if os.path.exists('data/temp/'+self.uuid+'.'+ext):
                return ext
        return False
