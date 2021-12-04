from typing import DefaultDict
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from lichess import get_current_lichess_ratings
from dataclasses import dataclass


@dataclass
class Company:
    name: str
    logo: str
    url: str  # website url of the company


@dataclass
class Role:
    title: str
    company: Company
    bullets: tuple[str]
    start: str # e.g Jan 2021
    end: str # e.g Feb 2021

"""Companies"""
BLACK_COW = Company(
    "Black Cow Technology",
    "blackcow_logo.png",
    "https://blackcowtech.uk/",
)

ZENDBOX = Company(
    "Zendbox",
    "zendbox_logo.svg",
    "https://zendbox.io",
)
"""Roles"""

SOFTWARE_ENG = Role(
    "Software Engineer",
    BLACK_COW,
    (
        "Currently working within a close-knit team to build state of the art backend systems for online-gaming.",
        "Creating Complex SQL functions and database migrations",
        "Containerizing cutting-edge multiplayer servers using Docker",
    ),
    "October 2021",
    "Present"
)
JR_SOFTWARE_ENG = Role(
    "Jr. Software Engineer",
    ZENDBOX,
    (
        "Designed and delivered API-driven dashboards",
        "Responsible for building data ETL scripts and creating automated data integrity tests",
        "Designing and producing elegant and pragmatic solutions to meet evolving business needs",
    ),
    "January 2021",
    "October 2021"
)


templates = Jinja2Templates(directory="templates")


async def homepage(request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "context": {
                "roles": (SOFTWARE_ENG, JR_SOFTWARE_ENG),
                "lichess_classical_rating": await get_current_lichess_ratings(),
            },
        },
    )


routes = [
    Route("/home", endpoint=homepage),
    Mount("/static", StaticFiles(directory="static"), name="static"),
]

app = Starlette(debug=True, routes=routes)
