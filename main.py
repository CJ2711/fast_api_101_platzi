from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse

# Pydantic es para definir clases con sus respectivos schemas y que drectamente las detecte el sistema 
from pydantic import BaseModel, Field
# PARA VALIDACIONES: Se importa la libreria Field desde pydantic (Se debe modificar en el schema)

class Movie(BaseModel):
    id: int | None = None
    title: str
    overview: str
    year: int
    rating: float
    category: str

# Instanciar FastApi
app = FastAPI()
app.title = 'Mi aplicación con Fast API'
app.version = '0.0.1'

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "It",
        "overview": "Bla bla bla...",
        "year": "2021",
        "rating": 9,
        "category": "Terror"
    }
]


# Metodos GET sin parametros ni body ----------------------------------------------------

@app.get('/', tags=['home'])
def message():
    return JSONResponse(
        content={
            "Saludo": "Hola mundo"
        })

@app.get('/movies', tags=['movies'])
def get_movies():
    return JSONResponse(
        content = movies,
        status_code= 400
    )


# Metodo GET con un parametros de ruta en el endpoint -----------------------------------------
@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    # Usamos list comprehentions para filtrar por medio de la función "next" (Se compila en C, por lo que es más optimo para filtrado)
    result = next((item for item in movies if item["id"] == id), None)
    if result != None:
        return JSONResponse(result, 200)
    return JSONResponse([], 404)
        

# Metodo GET con query params -----------------------------------------
# Filtro por categoría
# Si no se le pasa a la ruta la variable como en el paso anterior, FastAPI determinará que será un Query Param
@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str
                        #    , year: str
                           ):
    result = next((item for item in movies if item["category"] == category), None)
    if result != None:
        return JSONResponse(result, 200)
    return JSONResponse([], 404)



# Metodo GET que devuelve un html ----------------------------------------------------
@app.get('/html_content', tags=['html_content'])
def html_content():
    return HTMLResponse("<h1>Hola xd</h1>")

# Metodo POST ----------------------------------------------------

@app.post('/movies', tags=['movies'])
def create_movie(movie: Movie):
    movies.append(movie)
    return JSONResponse(movies, 200)

# Metodo PUT ----------------------------------------------------
# Se agrega el id como parte del parametro del endpoint
@app.put('/movies/{id}', tags=['movies'])
def create_movie(id: int, movie: Movie):
    # Y se quita el Body desde el id ya que no viene desde el id sino desde el endpoint, el resto serían los datos para actualizar el dato
    
    result = next((item for item in movies if item["id"] == id), None)
    if result != None:
        result["title"] = movie.title
        result["overview"] = movie.overview
        result["year"] = movie.year
        result["rating"] = movie.rating
        result["category"] = movie.category

        return JSONResponse(movies, 200)
    return JSONResponse([], 403)

# Metodo DELETE ----------------------------------------------------
# Se agrega el id como parte del parametro del endpoint
@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    # Y se quita el Body desde el id ya que no viene desde el id sino desde el endpoint, el resto serían los datos para actualizar el dato
    
    result = next((item for item in movies if item["id"] == id), None)
    movies.remove(result)
    return JSONResponse({
        "result": "Se ha borrado con exito",
        "data": movies
        }, 200)