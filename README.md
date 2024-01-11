# Introduction:
This repository contains Python code for a web crawling and information extraction assignment in the context of the FIFA World Cup 2022 Wikipedia page. The tasks involve retrieving the HTML content of the webpage, extracting specific information such as stadium details, teams, and match-related data, and implementing a menu-driven program using the PLY package for parsing.

# Crawling and Saving HTML:
The initial task involves using the requests library to fetch the HTML content from the FIFA World Cup 2022 Wikipedia page and saving it in a file named "world_cup_page.html." The code checks the status code to ensure a successful retrieval.

# Extracting Stadium Data:
The PLY package is utilized to create a lexer and parser that extract information about stadiums from the saved HTML file. This step involves defining appropriate grammar rules to capture relevant details.

# Extracting Teams:
Building upon the PLY lexer and parser, additional rules are implemented to extract information about all teams participating in the tournament.

# Creating Grammar for Various Fields:
 Extending the PLY grammar rules to cover a range of fields such as team details, venue specifics, and match details, both in the group and knockout stages. The grammar accommodates queries about stadiums, attendance, goal scorers, referees, and teams advancing to knockout stages.

# Error Handling:
Consideration is given to potential errors that may occur during parsing, and the implementation includes error-handling mechanisms to enhance the robustness of the code.

# Coding Style/Design:
 The Python code adheres to the PEP 8 style guide for readability and maintainability. A well-organized structure ensures clarity and ease of understanding.

# Menu-Driven Program:
 The assignment involves the creation of a menu-driven program that utilizes the parsed data to respond to user queries. The menu is designed to be user-friendly, allowing navigation between different queries.

 # Logging:
  Results from the program are logged in a specific format, adhering to the assignment requirements. This ensures that the output can be reviewed and assessed systematically.
