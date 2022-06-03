from dataclasses import dataclass
from collections.abc import Iterable


@dataclass
class Category:
    singular_name: str
    plural_name: str


@dataclass
class Technology:
    category: Category
    name: str
    paragraphs: Iterable[str]

    lower_case_name: str = name.lower()


backend_framework = Category("Backend Framework", "Backend Frameworks")

starlette = Technology(
    backend_framework,
    "Starlette",
    (
        """Starlette is a modern async python web framework for building high performance apps. It's perhaps best
              known for the FastAPI framework, which extends Starlette. I first encountered starlette in my role at
              Black Cow, where I contributed to the development of innovative multiplayer online games.""",
        """Since embracing the new async style of Python, I've enjoyed working with
              Starlette - in fact this app is served by a Starlette + Uvicorn solution.""",
    ),
)

flask = Technology(
    backend_framework,
    "Flask",
    """Flask was my initial entrypoint into web-development. Flask prides itsself on a very 'hands-off',
     un-opinionated approach that contrasts sharply with some of it's contemporaries like Django.""",
    """I'm grateful that I started with Flask because it gave me the opportunity to mistakes that perhaps another framework wouldn't have.
     Those mistakes taught me the value of a lot of the web-development design-patterns and best practices that I swear by today.""",
)
