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
"""Roles"""

software_engineer = Role(
    "Software Engineer",
    BLACK_COW,
    (
        "Currently working within a close-knit team to build state of the art backend systems for online-gaming.",
        "Creating Complex SQL functions and database migrations",
        "Containerizing cutting-edge multiplayer servers using Docker",
    ),
    "October 2021",
    "Present",
)
jr_software_engineer = Role(
    "Jr. Software Engineer",
    ZENDBOX,
    (
        "Designed and delivered API-driven dashboards",
        "Responsible for building data ETL scripts and creating automated data integrity tests",
        "Designing and producing elegant and pragmatic solutions to meet evolving business needs",
    ),
    "January 2021",
    "October 2021",
)

ROLES = software_engineer, jr_software_engineer