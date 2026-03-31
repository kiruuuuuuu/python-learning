# Python Learning Journey - A118

My daily learning progress through Python fundamentals.

---

## 📚 Course Overview

This repository contains daily Python lessons progressing from basic print statements to complex data types and operators. Each day builds upon the previous concepts to create a comprehensive understanding of Python fundamentals.

---

## 📅 Day-by-Day Topics

### **Day 1: Print Statement & Keywords**
- **Topics Covered:**
  - `print()` function for displaying output
  - Python reserved keywords list
  - Checking if a string is a keyword using `keyword.iskeyword()`
  
- **Key Concepts:**
  - Keywords are reserved words in Python with special meaning
  - Cannot use keywords as variable names
  - Examples: `if`, `for`, `class`, `while`, etc.

---

### **Day 2: Identifiers & Variables**
- **Topics Covered:**
  - Variable naming rules and conventions (identifiers)
  - Case sensitivity in variable names
  - Multi-valued variable assignment
  - Variable IDs using `id()` function
  - Escape sequences in strings
  - Single-line and multi-line comments
  
- **Key Concepts:**
  - Identifiers must start with letter or underscore, followed by alphanumeric characters
  - Python is case-sensitive: `name` and `Name` are different variables
  - Multi-variable assignment: `a, b, c = 1, 2, 3`
  - Common escape sequences: `\n` (newline), `\t` (tab), etc.

---

### **Day 3: Data Types in Python**
- **Topics Covered:**
  - Single-valued data types: `int`, `float`, `complex`, `bool`
  - Multi-valued data types: `string`, `list`, `tuple`, `set`, `dict`
  - Type checking with `type()` function
  - Default values for each data type
  
- **Key Concepts:**
  - **int**: Integer numbers (positive, negative, zero)
  - **float**: Decimal numbers
  - **complex**: Numbers in the form of `a + bj`
  - **bool**: True/False values
  - **String**: Sequence of characters
  - **List, Tuple, Set, Dict**: For storing collections

---

### **Day 4: List Data Type**
- **Topics Covered:**
  - Homogeneous and heterogeneous lists
  - Positive and negative indexing
  - Nested lists and accessing nested elements
  - List slicing with start, stop, and step parameters
  
- **Key Concepts:**
  - Lists are mutable (can be modified after creation)
  - Indexing: first element is at index 0, last at index -1
  - Slicing syntax: `list[start:stop:step]`
  - Nested lists can be accessed using multiple brackets: `list[4][1]`

---

### **Day 5: Tuple Data Type**
- **Topics Covered:**
  - Homogeneous and heterogeneous tuples
  - Accessing elements using positive and negative indexing
  - Tuple slicing with various step values
  - Negative slicing for reverse access
  
- **Key Concepts:**
  - Tuples are immutable (cannot be modified after creation)
  - Similar indexing and slicing to lists
  - Syntax: `tuple = (element1, element2, ...)`
  - Useful for protecting data that shouldn't change

---

### **Day 6: Set, Dictionary & Range Data Types**
- **Topics Covered:**
  - **Sets**: Unordered collections with unique elements
    - Duplicate values are automatically removed
    - Cannot access elements by index
    - Can convert to list for indexing
  
  - **Dictionaries**: Key-value pairs
    - Access values using keys
    - Support nested dictionaries
    - Useful for storing structured data
  
  - **Range**: Sequence of numbers
    - `range(stop)`: 0 to stop-1
    - `range(start, stop)`: start to stop-1
    - Commonly used in loops
  
- **Key Concepts:**
  - Sets eliminate duplicates: `{10, 20, 20}` becomes `{10, 20}`
  - Dictionary syntax: `{'key': value, 'key2': value2}`
  - Range creates immutable sequence of numbers
  - Nested structures can store complex data

---

### **Day 7: Type Casting**
- **Topics Covered:**
  - Implicit type casting (automatic conversion)
  - Explicit type casting (manual conversion)
  - Converting between int, float, complex, bool, and str
  - Type conversion limitations
  
- **Key Concepts:**
  - **Implicit**: `5 + 3.5` automatically converts int to float → `8.5`
  - **Explicit**: `int("5")` → `5`, `str(100)` → `"100"`
  - `bool()` treats non-zero as True, zero as False
  - Cannot directly convert int to list/tuple/set/dict without iteration

---

### **Day 8: Input, Eval & Operators**
- **Topics Covered:**
  - User input with `input()` function
  - Dynamic evaluation with `eval()` function
  - **Arithmetic Operators**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
  - **Assignment Operators**: `=`, `+=`, `-=`, `*=`, `/=`, etc.
  - **Membership Operators**: `in`, `not in`
  - **Identity Operators**: `is`, `is not`
  
- **Key Concepts:**
  - `input()` always returns a string
  - `eval()` converts string to its actual data type
  - `/` (true division) returns float; `//` (floor division) returns int
  - `%` (modulus) gives remainder
  - `**` (exponentiation) raises to power
  - String concatenation: `"hello" + "world"`
  - List concatenation: `[1, 2] + [3, 4]`

---

### **Day 9: Relational Operators**
- **Topics Covered:**
  - Greater than `>`
  - Less than `<`
  - Equal to `==`
  - Not equal to `!=`
  - Greater than or equal to `>=`
  - Less than or equal to `<=`
  
- **Key Concepts:**
  - Relational operators return boolean values (True/False)
  - Comparisons work with numbers, strings, and collections
  - String comparison is based on lexicographic order
  - `==` compares values; useful for comparing lists, tuples, etc.
  - Case sensitivity matters: `'abc' == 'ABC'` is False

---

## 🎯 Learning Objectives

By completing this course, you will understand:
- ✅ Basic Python syntax and conventions
- ✅ How to work with different data types
- ✅ Collections (lists, tuples, sets, dictionaries)
- ✅ Type conversion and casting
- ✅ User input and output
- ✅ All types of operators in Python
- ✅ How to write and compare values effectively

---

## 🚀 How to Use This Repository

1. **Start with Day 1** and progress sequentially
2. **Run each file** to see the output and understand the concepts
3. **Modify the code** to experiment and deepen your understanding
4. **Practice with examples** provided in each day's file
5. **Try to solve problems** using the concepts learned

---

## 💻 Requirements

- Python 3.x installed
- A text editor or IDE (VS Code recommended)
- Basic computer literacy

---



## 🤝 Contributing

Feel free to fork this repository and add more examples or advanced topics!

---

## 📄 License

This educational material is shared freely for learning purposes.

---

## 📞 Support

If you have any questions about the concepts covered, feel free to review the day-by-day breakdown above or reach out for clarification!

---

**Happy Learning! 🎓**
