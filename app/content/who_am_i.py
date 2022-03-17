from dataclasses import dataclass


@dataclass
class SubSection:
    header: str
    content: str


professional = SubSection(
    "As a professional:",
    "I'm a deep thinker with a keen interest in good design and best practices.\
        Currently my favourite book is TDD by example, by Kent Beck.",
)

personal = SubSection(
    "As an individual:",
    "I care deeply about the beliefs and perspectives that I hold. \
        Spirited discussion with others about topics that we're both passionate about excite me.",
)
values = SubSection(
    "My values:",
    "The qualities I most admire in people are integrity, kindness and conscientiousness",
)

WHO_AM_I = professional, personal, values
