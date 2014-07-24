"""
Database models for Fast Loan Search
"""

from sqlalchemy import Column, Integer, Float, String, Text, DateTime, func
from database import Base


class Result(Base):
    """Used as a cache for search results from Google's Custom Search engine API"""
    __tablename__ = 'result'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), unique=False)
    htmltitle = Column(String(255), unique=False)
    link = Column(String(255), unique=False)
    displaylink = Column(String(255), unique=False)
    snippet = Column(Text, unique=False)
    htmlsnippet = Column(Text)
    formatted_url = Column(String(255), unique=False)
    htmlformatted_url = Column(String(255), unique=False)
    type = Column(String(16), unique=False)
    created_at = Column(DateTime, default=func.now())

    def __init__(
            self,
            title,
            htmltitle,
            link,
            displaylink,
            snippet,
            htmlsnippet,
            formatted_url,
            htmlformatted_url,
            type
    ):
        self.title = title
        self.htmltitle = htmltitle
        self.link = link
        self.displaylink = displaylink
        self.snippet = snippet
        self.htmlsnippet = htmlsnippet
        self.formatted_url = formatted_url
        self.htmlformatted_url = htmlformatted_url
        self.type = type

    def __repr__(self):
        return "%s <%s>" % (self.title, self.displaylink)


class Product(Base):
    """Contains spidered data"""
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    provider = Column(String(255))
    loan_min = Column(Integer)
    loan_max = Column(Integer)
    apr = Column(Float)
    term_min_num = Column(Integer)
    term_max_num = Column(Integer)
    term_min_str = Column(String(6))
    term_max_str = Column(String(6))
    url = Column(String(255))
    created_at = Column(DateTime, default=func.now())

    def __init__(self, provider, loan_min, loan_max, apr, term_min_num, term_max_num, term_min_str, term_max_str):
        self.provider = provider
        self.loan_min = loan_min
        self.loan_max = loan_max
        self.apr = apr
        self.term_min_num = term_min_num
        self.term_max_num = term_max_num
        self.term_min_str = term_min_str
        self.term_max_str = term_max_str
