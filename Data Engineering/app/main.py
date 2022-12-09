from fastapi import FastAPI
from starlette.responses import RedirectResponse
import pandas as pd

app = FastAPI()

@app.get("/")
def raiz():
    return RedirectResponse(url="/docs")

@app.get("/get_count_plataform/{plataforma}")
async def get_count_plataform(plataforma:str):
    df = pd.read_csv(r"C:\Users\Usuario\Desktop\Data Engineer\data\process\result.csv")
    df.query('plataform == @plataforma').groupby(['type'])["title"].count()
    return{
        df
    }

@app.get("/get_listed_in/{type}")
async def get_listed_in(type:str):
    df = pd.read_csv(r"C:\Users\Usuario\Desktop\Data Engineer\data\process\result.csv")
    cantidad= df[df['listed_in'].str.contains(type)].groupby(['plataform'])["listed_in"].count().head(1)
    return {
        cantidad
    }

