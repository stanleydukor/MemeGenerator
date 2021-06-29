class QuoteModel():
    def __init__(self, body, author):
        """Create new quote"""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return str with "quote body text" - author."""
        return f"{self.body} - {self.author}"