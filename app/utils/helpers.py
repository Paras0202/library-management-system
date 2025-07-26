from datetime import date, timedelta

def calculate_due_date(issue_date: date, days: int = 14) -> date:
    """Returns a due date N days after the issue_date (default = 14 days)."""
    return issue_date + timedelta(days=days)

def is_overdue(due_date: date, return_date: date | None = None) -> bool:
    """Checks if the book is overdue."""
    today = date.today()
    if return_date:
        return return_date > due_date
    return today > due_date

def format_date(d: date) -> str:
    """Formats a date to string like YYYY-MM-DD."""
    return d.strftime("%Y-%m-%d")
