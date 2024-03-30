# VisitorCategory.py
#imporing Enum
from enum import Enum
# Enum for different categories of visitors
class VisitorCategory(Enum):
    ADULT = "ADULT"
    CHILD = "CHILD"
    STUDENT = "STUDENT"
    SENIOR = "SENIOR"
    GROUP = "GROUP"
    TEACHER = 'TEACHER'
