import geopandas as gpd
import os,uuid

class rpn:
    
    def __init__(self,path):
        self.data=self.loadData(path)
   
    def loadData(self,path): #Charger un shape (ou autre)
        df=gpd.read_file(path)       
        return df 
    
    def observateurs(self,split=True):
        list_obs=list(self.data.observ.unique())
        if split:
            list_obs=list(set(','.join(list_obs).split(',')))
        return sorted(list_obs)

    def especes(self):
        sp=list(self.data.nom_f.unique())
        return sorted(sp)

class token:
    def __init__(self,id=False):
        if not id:
            self.id=str(uuid.uuid4())
        else:
            self.id=id
    
    def extension(self):
        for ext in ['shp','gpkg','geojson']:
            if os.path.exists('data/temp/'+self.id+'.'+ext):
                return ext
        return False
    
    def exists(self):
        if self.extension():
            return True
        return False
    
    def save_file(self,ext='GPKG'):
        if self.exists():
            gpd.read_file('data/temp/'+self.id+'.'+self.extension()).to_file('data/'+self.id+'.gpkg','GPKG')
            return True
        return False
        
