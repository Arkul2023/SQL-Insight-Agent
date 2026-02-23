ALLOWED_COLUMNS = {
    "student_id",
    "student_name",
    "english",
    "maths",
    "science",
    "french"
}

def is_safe_query(query: str):

    banned = ["INSERT", "UPDATE", "DELETE", "DROP", "ALTER", "TRUNCATE"]

    if any(word in query.upper() for word in banned):
        return False

    # Detect hallucinated columns
    tokens = query.replace(",", " ").replace(";", " ").split()

    for token in tokens:
        if token.isidentifier() and token.lower() not in ALLOWED_COLUMNS \
            and token.lower() not in ["select", "from", "order", "by", "limit", "desc", "asc", "where"]:
            return False

    return True

