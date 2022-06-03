from dataclasses import dataclass


@dataclass
class SubSection:
    header: str
    content: str


professional = SubSection(
    "As a professional:",
    "I'm a deep thinker with a keen interest in good design and best practices.\
        Currently my favourite book is TDD by example, by Kent Beck. \
            I'm constantly looking to challenge myself and expand my talents in collaborative settings.",
)

personal = SubSection(
    "As an individual:",
    "I care deeply about the beliefs and perspectives that I hold. \
        Spirited discussion with others about topics that we're both passionate about excite me.",
)
values = SubSection(
    "My values:",
    "The qualities I most admire are integrity, kindness and thoughtfulness.",
)

WHO_AM_I = professional, personal, values
