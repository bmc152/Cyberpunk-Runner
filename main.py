import uvicorn
import requests
import fastapi as _fastapi
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

#Decorator when creating endpoints
app = _fastapi.FastAPI()

#Imports HTML Templates via Jinja2
app.mount("/static", StaticFiles(directory="static"), name="static")
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
                        <form action="http://127.0.0.1:8000/lore/">
                            <input type="submit" value="Info" class="btn btn-dark" />
                        </form>
                    </div>
                </div>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

############
#Lore Pages#
############
@app.get("/lore", response_class=HTMLResponse)
async def read_lore(request: Request):
    return templates.TemplateResponse("lorepage.html", {"request": request})

@app.get("/lore/cyberware", response_class=HTMLResponse)
async def read_lore(request: Request):
    return templates.TemplateResponse("cyberwareinfo.html", {"request": request})

@app.get("/lore/neocorps", response_class=HTMLResponse)
async def read_lore(request: Request):
    return templates.TemplateResponse("neocorpinfo.html", {"request": request})