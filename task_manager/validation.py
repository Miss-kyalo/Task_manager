from datetime import datetime

def validate_task_title(title):
    if len(title.strip()) == 0:
        return False
    return True

def validate_task_description(description):
    if len(description.strip()) == 0:
        return False
    return True

def validate_due_date(due_date):
    try:
        cleaned_date = due_date.strip()
        if len(cleaned_date) != 10:
            return False
        datetime.strptime(cleaned_date, "%Y-%m-%d")
        return True
    except (ValueError, TypeError, AttributeError):
        return False