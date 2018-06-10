import geopandas as gpd
import os,uuid
import sqlite3

class rpn:
    
    def __init__(self,token):
        #self.data=self.loadData(path)
        self.conn=sqlite3.connect('data/database.gpkg')
        self.conn.row_factory = sqlite3.Row
        self.c=self.conn.cursor()
        self.token=token
    
    def loadData(self,path): #Charger un shape (ou autre)
        df=gpd.read_file(path)       
        return df 
    
    def observateurs(self,split=True):
        r=self.c.execute('SELECT DISTINCT observ as nom FROM "'+self.token.id+'"')
        return list(map(dict,r.fetchall()))
    
    def especes(self):
        r=self.c.execute('SELECT DISTINCT nom_f FROM "'+self.token.id+'"')
        return list(map(dict,r.fetchall()))
    
    def test(self):
        ca=self.c.execute('SELECT CD_NOM FROM taxref LIMIT 10')
        return ca
        

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
    
    def save_to_db(self):
        if self.exists():
            gpd.read_file('data/temp/'+self.id+'.'+self.extension()).to_file('data/database.gpkg','GPKG',layer=self.id)
            return True
        return False
        
