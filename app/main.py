from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from content.contact_details import BUSINESS_EMAIL, MOBILE_NUMBER

from lichess import get_current_lichess_ratings
from content.role_history import ROLES
from content.who_am_i import WHO_AM_I

templates = Jinja2Templates(directory="templates")


async def homepage(request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "context": {
                "who_am_i": WHO_AM_I,
                "roles": ROLES,
                "lichess_classical_rating": await get_current_lichess_ratings(),
                "contact_details": {
                    "mobile_number": MOBILE_NUMBER,
                    "business_email": BUSINESS_EMAIL,
                },
            },
        },
    )


routes = [
    Route("/home", endpoint=homepage),
    Mount("/static", StaticFiles(directory="static"), name="static"),
]

app = Starlette(debug=False, routes=routes)
