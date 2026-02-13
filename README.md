
---

## 🗓️ Internship Progress

---

## ✅ Day 1: Welcome & Setup

### 📘 Topics Covered
- System Orientation & Tool Awareness
- Python Installation & Verification
- VS Code and Anaconda Installation
- GitHub Account & Repository Setup

### 📝 Assignments Completed
- **Task 1:** The "Version Check" Challenge
- **Task 2:** The Architect
- **Task 3:** The "Hello World" Plus

### 📤 Submission
- Day 1 Submission  
- Sample Student Entry  
- Student Comments & Diary Entry  

---

## ✅ Day 2: Python Fundamentals

### 📘 Topics Covered
- Variables and Data Types
- Arithmetic Operations & Operator Precedence
- User Input and Basic I/O
- Type Casting & Mini Script

### 📝 Assignments Completed
- **Task 1:** Age in 2030 Calculator
- **Task 2:** The Bill Splitter
- **Task 3:** The "Raw Data" Formatter

### 📤 Submission
- Day 2 Submission  
- Student Diary Entry  

---

## ✅ Day 3: Lists & Tuples

📂 Folder: `src/Day3/`

### 📘 Topics Covered
- Introduction to Lists & Tuples
- Indexing & Slicing
- List Methods & Mutability
- Tuple Immutability & Use Cases

### 📝 Assignments Completed
- **Task 1:** The Inventory Manager (List Methods)
- **Task 2:** The Data Slicer (Indexing & Slicing)
- **Task 3:** The Immutable Config (Tuples vs Lists)

### 📤 Submission
- Day 3 Submission  
- Student Diary Entry  

---

## ✅ Day 4: Dictionaries & Sets

📂 Folder: `src/Day4/`

### 📘 Topics Covered
- Dictionaries — Key-Value Pairs
- Dictionary Methods & Iteration
- Sets & Unique Collections
- Set Operations & Membership Testing

### 📝 Assignments Completed
- **Task 1:** The Personal Contact Book (Dictionaries)
- **Task 2:** The "Duplicate Cleaner" (Sets)
- **Task 3:** The Interest Matcher (Set Operations)

### 📤 Submission
- Day 4 Submission  
- Sample Student Diary Entry  

---

## ⏳ Day 5: Functions & Modules

📂 Folder: `src/Day5/`

### 📘 Topics Covered
- Introduction to Functions
- Arguments and Return Values
- Variable Scope (Local vs Global)
- Importing Standard Modules
- Creating and Importing Custom Modules

### 📝 Assignments
- **Task 1:** The Area & Perimeter Tool (Functions & Return Values)
- **Task 2:** The Logic Library (Custom Modules)

### 📤 Submission
- Day 5 Submission (Pending / Upcoming)


# Day 6 – Homework

## Objective
To practice using functions and modules in Python and understand how `return` works.

## Homework Tasks

### Task 1: Rectangle Calculation
- Created a function `calc_rectangle(length, width)`
- Calculated:
  - Area
  - Perimeter
- Returned both values from the function
- Took input from the user and displayed the results

### Task 2: Custom Module Creation
- Created a module named `math_operations.py`
- Defined the following functions:
  - `power(base, exp)` to calculate power
  - `average(numbers_list)` to find the average of numbers

### Task 3: Using the Module
- Created `main.py`
- Imported `math_operations` module
- Calculated:
  - Power of 2 raised to 10
  - Average of the list `[10, 20, 30, 40]`
---
# Day 7 – File Handling in Python

## Objective
To learn how to read and write data using files in Python.

## Topics Covered
- Introduction to file handling
- File modes:
  - `r` (read)
  - `w` (write)
  - `a` (append)
- Opening and closing files
- Using `with open()` statement
- Reading data from files
- Writing and appending data to files
- Difference between `w` and `a`
- Basics of Excel file handling using `openpyxl`

## Programs Practiced
- Writing user input (name and daily goal) into a text file
- Appending multiple records to the same file
- Reading and displaying file content
- Understanding overwrite vs append
- Reading data from an Excel file (`student.xlsx`)
- Handling file-related errors

## Learnings / Outcomes
- Learned how to permanently store data using files
- Understood the importance of append mode for logging
- Learned that `with open()` automatically closes files
- Gained basic knowledge of reading Excel files
- Improved understanding of real-world data storage

## Conclusion
Day 7 helped me understand file handling concepts in Python. These concepts are useful for data storage, logging, and file-based applications.

# Day 8 – NumPy Basics and Array Operations

## Objective
To learn the basics of NumPy and perform efficient numerical operations using arrays instead of loops.

## Topics Covered
- Introduction to NumPy
- Creating NumPy arrays
- Difference between Python lists and NumPy arrays
- Array attributes (shape, size, dtype)
- Generating arrays using:
  - `np.arange()`
  - `np.linspace()`
- Reshaping arrays
- Broadcasting in NumPy
- Vectorized operations
- Axis-based operations (row-wise and column-wise)

## Programs Practiced
- Creating 1D and 2D NumPy arrays
- Performing element-wise operations without loops
- Reshaping a 1D array into 2D and 3D arrays
- Normalizing student marks using broadcasting
- Calculating mean and standard deviation using `axis`
- Difference between element-wise multiplication (`*`) and matrix multiplication (`@`)

## Key Learnings / Outcomes
- Learned how NumPy arrays are faster and more efficient than Python lists
- Understood broadcasting and how NumPy handles arrays of different shapes
- Learned to reshape data to match machine learning model requirements
- Gained clarity on axis-based calculations (rows vs columns)
- Improved coding efficiency by replacing loops with vectorized operations

## Conclusion
Day 8 helped me understand the power of NumPy for numerical and data processing tasks. These concepts are very important for data science and machine learning applications.

# Day 9 – Introduction to Pandas

## Objective
To understand the basics of the Pandas library and learn how to work with Series and DataFrames.

## Topics Covered
- Introduction to Pandas
- Why Pandas is used in data analysis
- Creating a Pandas Series
- Creating a DataFrame
- Accessing data using index and column names
- Basic DataFrame operations
- Viewing data using:
  - head()
  - tail()
  - info()
  - describe()
- Selecting rows and columns

## Programs Practiced
- Creating a Series of student marks
- Creating a DataFrame with student details
- Accessing specific columns
- Filtering data based on conditions
- Finding mean, maximum, and minimum values
- Checking data types and structure

## Learnings / Outcomes
- Learned the difference between Series and DataFrame
- Understood how labeled data makes analysis easier
- Learned how to filter data using conditions
- Gained confidence in handling structured datasets
- Improved understanding of data analysis basics

## Conclusion
Day 9 helped me understand how Pandas simplifies data handling and analysis. It is a powerful library used in data science and machine learning.

# Day 10 – Data Cleaning with Pandas

## Objective
To learn how to detect and handle common data quality issues using Pandas.

## Topics Covered
- Understanding missing values (NaN)
- Checking missing data using:
  - isna()
  - isnull()
  - sum()
- Filling missing values using:
  - fillna()
  - median()
  - mean()
- Dropping missing values using:
  - dropna()
- Identifying duplicate records
- Removing duplicates using:
  - drop_duplicates()
- Checking unique values using:
  - unique()

## Programs Practiced
- Loaded a dataset (customer_orders.csv)
- Generated a report of missing values
- Replaced missing numeric values with median
- Removed duplicate rows
- Checked cleaned dataset shape
- Verified corrected text data using strip() and lower()

## Learnings / Outcomes
- Learned how missing data affects analysis
- Understood when to fill or drop missing values
- Learned how to remove duplicate records
- Improved skills in preparing data for analysis
- Gained confidence in handling real-world datasets

## Conclusion
Day 10 helped me understand the importance of data cleaning before analysis. Clean data leads to accurate results and better decision-making.

# Day 11 – Data Visualization using Matplotlib

## Objective
To learn how to visualize data using different types of plots in Matplotlib.

## Topics Covered
- Introduction to data visualization
- Importing matplotlib.pyplot
- Line plot
- Scatter plot
- Bar chart
- Adding:
  - Title
  - X-label and Y-label
  - Legend
  - Grid
- Using plt.subplot() for multiple plots

## Programs Practiced
- Created a line plot for monthly revenue growth
- Created a scatter plot to analyze relationships between two variables
- Created a bar chart for student marks comparison
- Added proper labels and titles to make plots meaningful
- Displayed multiple plots in one window using subplot()

## Learnings / Outcomes
- Learned how visualization helps understand trends clearly
- Understood when to use line plot, scatter plot, and bar chart
- Learned that plots without labels are difficult to understand
- Gained confidence in presenting data visually
- Improved ability to analyze relationships using scatter plots

## Conclusion
Day 11 helped me understand how visual representation makes data analysis easier and more effective. Data visualization is very important in data science and presentations.

## 🧠 Key Skills Gained
- Python Programming Fundamentals
- Data Structures (Lists, Tuples, Dictionaries, Sets)
- Problem Solving with Python
- Writing Reusable Functions
- Modular Code Design
- GitHub Version Control

---

## 🚀 Tools & Technologies
- Python
- VS Code
- GitHub
- Anaconda

---

✨ *This repository reflects my daily learning journey and hands-on practice during the internship.*  
