# QPI - Quick Project Initialiser

## Overview

QPI is a simple and efficient command-line utility designed to greatly speed-up the process of setting up projects.

This tool aims to save you time and effort by automating the initial project setup, so you can focus on what really matters - writing code.

## Features

- **Project Directory Structure**: The tool creates a well-organized project directory structure, ensuring consistency across your projects.

- **Python Support**: Currently, the tool is tailored for general purpose and Python projects.Use ```-py``` or ```--pysetup``` as an optional flag to setup the python files.

- **Extensible**: While Python is currently the only language-specific support, I have plans to expand support for other programming languages in the future.

## Installation

To get started with QPI, follow these steps:

1. **Clone this repository**:
```
git clone https://github.com/aryntaylor/qpi-tool.git
```

2. **Copy Path**:
eg. "D:Tools/qpi-tool/src"

3. **Setup Environment Variable**:
Search for Edit System Environment Variables.

Click the "Environment Variables..." button.

Open User Path.

Add New Variable.

Paste the Tool Path.

```
D:Tools/qpi-tool/src
```

Save and Apply, then Close the Window.

4. **Verify installation**:
Run the following command to ensure the tool is correctly installed:

```
qpi -v
```

OR

```
qpi --version
```

Be sure to try running this command after restarting your terminal, if open.

## Usage

### Initialize a New Project

To create a new project using the tool, follow these steps:

1. **Navigate to your desired project directory**:
```
cd path/to/your/project
```

2. **Run the tool**:
```
qpi
```

OR

```
qpi -b "path/to/your/project"
```

3. **Confirm It Has Been Successful**:
After entering the command, the project should be successfully created. Be sure to navigate to the directory and confirm this.

4. **Start coding**:
Your project directory is now set up and ready to go. You can start coding immediately!

## Enjoy

Happy coding! 🚀
