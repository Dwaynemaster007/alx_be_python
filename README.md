# 🐍 ALX Backend Python Basics

Python fundamentals from the **ALX ProDev Backend** programme, from a first script to object-oriented programming and unit tests.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

## Projects

| Folder | Topics | Highlights |
| --- | --- | --- |
| [`python_introduction/`](python_introduction/) | Variables, arithmetic, input/output | Simple interest, finance calculator, future age, rectangle area |
| [`control-flow/`](control-flow/) | `if`/`elif`, `match`/`case`, loops | Weather advice, `match`-based calculator, multiplication table, pattern drawing, daily reminder |
| [`fns_and_dsa/`](fns_and_dsa/) | Functions, lists, `datetime` | Arithmetic operations, shopping list manager, temperature converter, date exploration |
| [`programming_paradigm/`](programming_paradigm/) | Exceptions, OOP, testing | Bank account, robust division calculator, library management, `unittest` tests for a calculator |
| [`oop/`](oop/) | Classes, magic methods, inheritance, polymorphism | Book class, library system, class and static methods, polymorphism demo |

## Run it

You only need Python 3.10+ (for `match`/`case`). Run any script from its folder:

```bash
git clone https://github.com/Dwaynemaster007/alx_be_python.git
cd alx_be_python/control-flow
python3 match_case_calculator.py
```

Some scripts take command-line arguments:

```bash
cd ../programming_paradigm
python3 main-0.py deposit:50        # also withdraw:20 or display
python3 main.py 10 2                # safe division
python3 -m unittest test_simple_calculator.py
```

The files in `oop/` and `library_management.py` are modules to import, for example `python3 -c "from book_class import Book; print(Book('1984', 'George Orwell', 1949))"` from `oop/`.

## Author

**Thubelihle Dlamini**, [GitHub](https://github.com/Dwaynemaster007) · [LinkedIn](https://linkedin.com/in/thubelihledlamini)
