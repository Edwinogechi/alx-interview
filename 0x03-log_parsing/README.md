Project - 0x03. Log Parsing
Description
This project is designed to parse and analyze log files. It aims to extract relevant information from log files, such as timestamps, error messages, and other data points, and present them in a structured format for further analysis or processing. Log parsing is a common task in software development, system administration, and data analysis, as it allows for understanding system behavior, identifying issues, and monitoring performance.

Features
Log Parsing: The project provides functionality to parse log files and extract relevant information.
Timestamp Extraction: It can extract timestamps from log entries to analyze the sequence of events.
Error Detection: The system is capable of identifying and categorizing errors or warning messages within log files.
Customizable: The parsing mechanism can be customized or extended to handle specific log formats or extract additional information as needed.
Output Formats: The parsed data can be outputted in various formats such as JSON, CSV, or plain text, depending on the requirements.
Installation
To use this project, follow these steps:

Clone the repository: git clone <repository_url>
Navigate to the project directory: cd log-parsing
Install dependencies: pip install -r requirements.txt
Usage
To parse a log file, execute the following command:

php
Copy code
python log_parser.py <log_file_path>
Replace <log_file_path> with the path to the log file you want to parse.

Additional options and flags can be used to customize the parsing behavior or specify output formats. Use the --help flag for more information:

bash
Copy code
python log_parser.py --help
Examples
Parse a log file named example.log:
c
Copy code
python log_parser.py example.log
Parse a log file and output results in JSON format:
lua
Copy code
python log_parser.py example.log --json
Parse a log file and extract only error messages:
lua
Copy code
python log_parser.py example.log --error-only
Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:

Fork the repository
Create a new branch (git checkout -b feature)
Make your changes
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature)
Create a new pull request
Please ensure that your pull request follows the project's coding conventions and includes appropriate documentation or tests if applicable.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Special thanks to the contributors and maintainers of libraries used in this project.

Contact
For questions or support, feel free to contact the project maintainer: Edwin Ogechi


Tasks
0. Log parsing
mandatory
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
Warning: In this sample, you will have random value - it’s normal to not have the same output as this one.
