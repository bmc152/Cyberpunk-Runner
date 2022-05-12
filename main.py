import fastapi as _fastapi
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

#Decorator when creating endpoints
app = _fastapi.FastAPI()

#Imports HTML Templates via Jinja2
templates = Jinja2Templates(directory="htmlDirectory")

if __name__ == "__main__":
    uvicorn.run(app)

##################
#Display Web Pages
##################
@app.get("/")
async def read_home():
    html_content = """
    <html>
        <head>
            <title>Cyberpunk Runner Home</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        </head>
        <br><br>
        <body style = background-color:red>
            <div class="container">
                <div class="row">
                    <div class="col">
                        <h1>Cyberpunk Helper</h1>
                    </div>
                </div>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/lore")
async def read_lore():
    html_content = """
    """
    return HTMLResponse(content=html_content, status_code=200)