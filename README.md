# Project Name: Pretty Clean Ingredients (PCI)

## Table of Contents
1. [General Info](#general-info)
2. [Technologies Used](#technologies-used)
3. [Features](#features)
4. [Screenshots](#screenshots)
5. [Setup](#setup)
6. [Usage](#usage)
7. [Project Status](#project-status)
8. [Room for Improvement](#room-for-improvement)
9. [Acknowledgements](#acknowledgements)
10. [Contact](#contact)

## General Info
Pretty Clean Ingredients (PCI) is a Python-based application designed to detect allergens in cosmetic products. It matches ingredients against the FDA's 5-class common allergens list and allows users to input custom allergens. The detection is based on a similarity threshold: 90% or above for a high certainty match, and 80-90% for a semi-certain match to account for misspellings and regional spelling differences (e.g., American vs. Australian English).

### What Problem Does It Solve?
This project was developed out of a personal interest in beauty care, especially to detect allergens that have caused adverse effects in the past, such as contact dermatitis and eczema.

### Purpose of the Project
The project was initially developed as a learning experience in Python and to fulfill an assignment requirement for the "Working with Data and Code" unit at UTS (University of Technology Sydney) in 2024 under the guidance of Evangeline Aguas.

### Why Python Was Chosen
Python was selected because of its simplicity and accessibility, making it a great choice for beginners. It allows for quick development and easy integration of external libraries, making it ideal for this project. The libraries used include:
- **Tkinter**: For building the GUI (Graphical User Interface).
- **FuzzyWuzzy**: For string matching to identify potential allergen matches, even with misspellings or regional variations.
- **python-Levenshtein**: To enhance the speed of FuzzyWuzzy’s string comparison.
- **Pillow (PIL)**: For image processing in Tkinter.

### Alternative Applications
- **Free of by Isabella**: A food allergen detector, whereas PCI detects allergens in cosmetics.
- **INKI Decoder**: A web-based alternative, while PCI is designed to run locally.

## Technologies Used
- **Python** (Version 2024.3.1)
- **PyCharm** (Version 2024.2.4, Professional Edition, using educational login)

## Features
- **Ingredient Allergen Checker**: Automatically checks ingredients for potential allergens from selected categories (e.g., fragrances, preservatives, metals).
- **Custom Allergen Input**: Users can input their own allergens for checking.
- **Fuzzy Matching**: Uses fuzzy string matching to account for variations in spelling.
- **Duplicate Removal**: Removes duplicate ingredients and allergens from the list.
- **User-Friendly Interface**: Simple, intuitive GUI using Tkinter.
- **Error Handling**: Alerts for missing ingredients or invalid inputs.
- **Customizable Allergen Categories**: Users can select allergen categories based on their needs.
- **Ingredient Processing**: Supports multiple ingredient formats for allergen checking.
- **Result Display**: Displays allergen matches with confidence levels.

## Screenshots 🌼
<img width="1462" alt="Screenshot 2024-12-15 at 11 47 59 pm" src="https://github.com/user-attachments/assets/17ceb763-e037-4b7d-ac82-30d6191d64f4" />
<img width="1456" alt="Screenshot 2024-12-15 at 11 47 52 pm" src="https://github.com/user-attachments/assets/cf63034a-70c8-4179-97a9-eab992ce0f92" />
<img width="820" alt="Screenshot 2024-12-15 at 11 47 44 pm" src="https://github.com/user-attachments/assets/c3d248d9-676f-468c-9c23-6081f1795807" />
<img width="1095" alt="Screenshot 2024-12-15 at 11 43 22 pm" src="https://github.com/user-attachments/assets/f477b969-feca-4696-b15a-3da33dcc19f5" />
<img width="1058" alt="Screenshot 2024-12-15 at 11 43 42 pm" src="https://github.com/user-attachments/assets/2bacb72c-b779-430a-a656-295e44bca895" />
<img width="1080" alt="Screenshot 2024-12-15 at 11 43 57 pm" src="https://github.com/user-attachments/assets/4309cf0f-4403-4b96-be48-5255b298f36a" />
<img width="1453" alt="Screenshot 2024-12-15 at 11 44 11 pm" src="https://github.com/user-attachments/assets/3dbb540d-f5c9-4442-9ff4-355fc4290dd3" />
<img width="1151" alt="Screenshot 2024-12-15 at 11 46 36 pm" src="https://github.com/user-attachments/assets/0bd37d9e-4aae-45d6-bfbe-097c7560ffe1" />
<img width="1029" alt="Screenshot 2024-12-15 at 11 46 42 pm" src="https://github.com/user-attachments/assets/29eec4d3-3116-4bc9-81f1-5367e289e559" />
<img width="973" alt="Screenshot 2024-12-15 at 11 46 51 pm" src="https://github.com/user-attachments/assets/83b86db7-abd7-4363-9382-2ad3c7b8c3a8" />
<img width="951" alt="Screenshot 2024-12-15 at 11 47 17 pm" src="https://github.com/user-attachments/assets/07d0e042-51d7-432b-9d88-936ef04ddb3e" />
<img width="835" alt="Screenshot 2024-12-15 at 11 47 30 pm" src="https://github.com/user-attachments/assets/44053656-1881-4ddf-8408-5d2a59f355a4" />
<img width="950" alt="Screenshot 2024-12-15 at 11 47 38 pm" src="https://github.com/user-attachments/assets/1ae43e1e-049d-42c7-b458-032a11f7fe19" />


## Setup

### Required Libraries and Packages
- **Tkinter**: For building the GUI.
- **FuzzyWuzzy**: For string matching.
- **Requests**: For making HTTP requests (if applicable).
- **Pillow**: For image processing.

These dependencies are listed in the `requirements.txt` file located in the root directory of the project. Navigation should be easy as it uses a simple user-friendly GUI. 

### Installation and Setup
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/PrettyCleanIngredients.git
    ```

2. **Create a Virtual Environment**:
    ```bash
    cd PrettyCleanIngredients
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:
   - For **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - For **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Project**:
    ```bash
    python PrettyCleanIngredients.py
    ```

### Troubleshooting
If you encounter any issues during setup, refer to the [Troubleshooting Section] or open an issue in the repository.

## Usage

1. **Clone the repository** (if you haven't already):
    ```bash
    git clone https://github.com/your-username/PrettyCleanIngredients.git
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Program**:
    ```bash
    python PrettyCleanIngredients.py
    ```

4. **Add Ingredients**:
   - Paste a list of ingredients into the input box.
   - Click **Add** to check for allergens.

5. **Tick pre-defined FDA allergen categories to scan for**:
   - Tick on the checkbox to the left of the ingredient you want to screen for. Tick one or multiple; it's up to you.

6. **Add/Edit Custom Ingredients**:
   - Add custom ingredients by typing them into the input box and clicking **➕Save/edit**.
   - Edit custom ingredients by double-clicking the list or using the **➕Save/edit** button.
   - Delete individual custom ingredients by clicking on the ingredient you want to delete in the list box, and then clicking **❌Delete custom ingredients** button.
   - Reset custom ingredients by clicking **🔄Reset custom ingredients** button.

7. **Analyze for your selected categories (both predefined and custom)**:
   - Analyze for allergens you selected for that screen by clicking the **ANALYSE** button.

8. **View Results**:
   - The program will display the detected allergens with confidence percentages under headings of category, corresponding found allergens, and in descending order of confidence percentages (e.g., Metals: gold (100%) then nickel (82%)).
     - If no allergens are found, the result box will say "No allergens found!" in that same box instead.
     - For longer results lists, the results window can be scrolled.

9. **Reset the program, return to home, and do another product**:
   - To reset and do another product from the beginning, click the **Do another** button.

### Example Usage
- **Input**: Paste a list of ingredients (e.g., from a product label).
    ```txt
    Water/aqua/eau, glycerin, coconut alkanes, niacinamide, retinol, jojoba oil, etc.
    ```

- **Output**: The program will highlight any allergens detected in the input list.

## Project Status
This project is complete and was submitted as part of a university assignment.

## Room for Improvement
- **Button Functionality**: Fix the "Go back" button behavior.
- **Audio and Haptic Feedback**: Add sound effects and haptic feedback for better accessibility.
- **API Integration**: Add barcode scanning and alternative product suggestions.
- **UI Enhancements**: Improve home button aesthetics, add animations, and enable page resizing.
- **Better Ingredient Notifications**: Handle non-ingredient entries and notify users.

## Key Challenges Overcome:
- **Button and Ingredient Management**: Successfully implemented editing and duplicate removal.
- **Fuzzy Matching**: Fine-tuned match percentages and string comparison logic.
- **UI & Backend Improvements**: Enhanced functionality for custom ingredients and ingredient processing.

## Acknowledgements
- This project was inspired by the [freeOf application by Isabella Fons](https://github.com/isabellafons/freeOf), which focuses on detecting food allergens.
- README template based on **Rita Lyczywek's README cheatsheet**.🌼
- Ky Staal (UTS IT graduate and friend) for guidance.
- Andre and Emily (Spring 2024 "Working with Data and Code" class) for peer feedback.
- Evangeline Aguas and Andrew Stapleton for granting an extension to complete the work.
- GEN AI was used to help create and edit this code. The following prompts and replies were used:
<img width="647" alt="Screenshot 2024-12-17 at 12 08 18 am" src="https://github.com/user-attachments/assets/a38ba998-34a5-4af6-aa35-590f425a7f70" />
<img width="477" alt="Screenshot 2024-12-17 at 12 08 30 am" src="https://github.com/user-attachments/assets/6e1cc0d8-2266-499e-adab-39766344a1f6" />
<img width="528" alt="Screenshot 2024-12-17 at 12 09 46 am" src="https://github.com/user-attachments/assets<img width="592" alt="Screenshot 2024-12-17 at 12 15 37 am" src="https://github.com/user-attachments/assets/4318eaa7-63ad-4b8d-a71c-0b53592918ed" />
/8346f5ed-db97-4807-85ff-11e64a<img width="533" alt="Screenshot 2024-12-17 at 12 16 16 am" src="https://github.com/user-attachments/assets/7040745d-4ad0-4331-909a-842d8ead0701" />
2fcb46" />
<img width="567" alt="Screenshot 2024-12-17 at 12 18 36 am" src="https://github.com/user-attachments/assets/3873fdb7-d231-46fe-b642-7a6d65ecad96" />
<img width="496" alt="Screenshot 2024-12-17 at 12 19 50 am" src="https://github.com/user-attachments/assets/8f4d45e0-7867-4341-bdf7-bc26f0814848" />
<img width="592" alt="Screenshot 2024-12-17 at 12 20 41 am" src="https://github.com/user-attachments/assets/10f302d2-a2ae-47a4-95af-dfd5c1be7312" />
<img width="479" alt="Screenshot 2024-12-17 at 12 21 44 am" src="https://github.com/user-attachments/assets/826cb0f5-17e2-4c8f-bb1c-5da4f6c2388c" />
<img width="515" alt="Screenshot 2024-12-17 at 12 22 49 am" src="https://github.com/user-attachments/assets/cde35261-591f-4a04-bea5-7e2251e11c78" />
<img width="455" alt="Screenshot 2024-12-17 at 12 23 02 am" src="https://github.com/user-attachments/assets/874e05e5-3b50-4883-b28c-73dfb1ab859b" />


## Contact
For any questions or issues, feel free to contact me at [olivia.u.bui@student.uts.edu.au](mailto:olivia.u.bui@student.uts.edu.au) or open an issue in the repository.
