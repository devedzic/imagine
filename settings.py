"""Project configuration settings (PROJECT_DIR, format strings, etc.).
"""

from pathlib import Path


PREFERRED_DATE_FORMAT = '%b %d, %Y'
PROJECT_DIR = Path(__file__).parent

# # Demonstrate __file__, type(__file__), Path(__file__), Path(__file__).parent and Path.cwd()
# print(__file__)
# print(Path(__file__))
# print(Path(__file__).parent)

# Define PROJECT_DIR as Path(__file__).parent




# import os
#
# print(__file__)
# print(os.path.abspath(__file__))
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print()
#
# PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
# print(PROJECT_DIR)
# print(type(PROJECT_DIR))

