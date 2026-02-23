from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_NAME = "NumbersStation/nsql-350M"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# HARD schema grounding
SCHEMA = """
Table: Student_Marks
Columns:
- student_id (integer)
- student_name (text)
- english (integer)
- maths (integer)
- science (integer)
- french (integer)
"""

def question_to_sql(question: str) -> str:

    prompt = f"""
You are an expert PostgreSQL query generator.

Database Schema:
Table: Student_Marks(student_id, student_name, english, maths, science, french)

You must write ONLY SQL using these columns.

### Examples:

Question: Who scored highest in science?
SQL: SELECT student_name FROM Student_Marks ORDER BY science DESC LIMIT 1;

Question: Who scored highest in maths?
SQL: SELECT student_name FROM Student_Marks ORDER BY maths DESC LIMIT 1;

Question: Show all students
SQL: SELECT * FROM Student_Marks;

Question: What is the average english marks?
SQL: SELECT AVG(english) FROM Student_Marks;

Question: List students sorted by french marks
SQL: SELECT student_name, french FROM Student_Marks ORDER BY french DESC;

### Now generate SQL for:

Question: {question}
SQL:
"""

    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=80,
        do_sample=False,
        temperature=0.0
    )

    sql = tokenizer.decode(outputs[0], skip_special_tokens=True)

    sql = sql.split("SQL:")[-1].strip()

    if ";" not in sql:
        sql += ";"

    return sql
