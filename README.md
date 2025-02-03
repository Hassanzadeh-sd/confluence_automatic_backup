# automatic_backup_confluence
This project implements a robust automatic backup solution for Confluence version 9.0 and later. The primary goal is to ensure the integrity and availability of critical data by regularly creating secure backups of the Confluence instance, including all spaces, pages, attachments, and configurations.

# Project Setup Guide

This guide will help you create a Python virtual environment and install the required dependencies for your project using a `requirements.txt` file.

## Prerequisites

- Ensure you have Python 3.6 or later installed on your system.
- Make sure you have `pip` (Python package installer) installed.

## Steps to Create a Virtual Environment and Install Requirements

### 1. Navigate to Your Project Directory

Open your terminal and change to the directory where your project is located. For example:

cd /path/to/your/project


### 2. Create a Virtual Environment

To create a virtual environment, run the following command:

 python -m venv .venv 


This command will create a new directory named `.venv` in your project folder, containing a fresh Python environment.

### 3. Activate the Virtual Environment

Before installing any packages, you need to activate the virtual environment.

- **On macOS and Linux**:

    ```
    source .venv/bin/activate
    ```

- **On Windows**:

    ```
    .venv\Scripts\activate
    ```

Once activated, your terminal prompt will change to indicate that you are now working inside the virtual environment.

### 4. Install Dependencies from `requirements.txt`

With the virtual environment activated, you can install the required packages listed in `requirements.txt` by running:


pip install -r requirements.txt


This command will read the `requirements.txt` file and install all specified packages into your virtual environment.

### 5. Verify Installation

To verify that the packages have been installed correctly, you can list the installed packages with:

pip list

## Conclusion

You have successfully created a Python virtual environment and installed all necessary dependencies for your project. You can now proceed with development or running your application within this isolated environment.

For any further questions or issues, please refer to the documentation or contact the project maintainers.