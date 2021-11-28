from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from lichess import get_current_lichess_ratings


templates = Jinja2Templates(directory='templates')


async def homepage(request):
    return templates.TemplateResponse('index.html', {'request': request, 'context':{'lichess_classical_rating': await get_current_lichess_ratings()}})


routes = [
    Route('/home', endpoint=homepage),
    Mount('/static', StaticFiles(directory='static'), name='static')
]

app = Starlette(debug=True, routes=routes)
