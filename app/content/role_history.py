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
    start: str  # e.g Jan 2021
    end: str  # e.g Feb 2021


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

QMUL = Company(
    "Queen Mary, University of London",
    "https://www.qmul.ac.uk/",
    "qmul-white.svg"
)
"""Roles"""

software_engineer_1 = Role(
    "Software Engineer",
    BLACK_COW,
    (
        "Currently working within a close-knit team to build state of the art backend systems for online-gaming",
        "Creating Complex SQL functions and database migrations",
        "Containerizing cutting-edge multiplayer servers using Docker",
    ),
    "October 2021",
    "Present",
)
software_engineer_0 = Role(
    "Software Engineer",
    ZENDBOX,
    (
        "Designed and delivered API-driven dashboards",
        "Responsible for building data ETL scripts and creating automated data integrity tests",
        "Designing and producing elegant and pragmatic solutions to meet evolving business needs",
    ),
    "January 2021",
    "October 2021",
)

undegraduate = Role(
    "BSc Theoretical Physics",
    QMUL,
    (
        "Studied a breadth of topics, from astrophysics to statistical mechanics and quantum physics",
        "Completed postgraduate electives in AI and ML",
        "Graduated first class, with honours",
    ),
    "2018",
    "2020",
)

ROLES = software_engineer_1, software_engineer_0, undegraduate