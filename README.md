# Flight Information Retriever

This Python script allows you to retrieve scheduled flight information between two airports on a specific date using the AviationStack API. You can enter the origin airport code, destination airport code, and date to get detailed flight information.

## Prerequisites

Before running the script, you need to obtain an API key from AviationStack. You can sign up and get your API key [here](https://aviationstack.com/).

## Installation

1. Clone this repository to your local machine:
```bash
      git clone https://github.com/Jawabreh0/Flight-Info-Retriver.git
```

2. Navigate to the repository directory:
```bash
      cd Flight-Info-Retriver
```

3. Install the required Python libraries (requests):
```bash
      pip install requests
```

## Usage

1. Open the main.py file in a text editor.

2. Replace "YOUR_KEY_HERE" in the main() function with your AviationStack API key.

3. Save the file.

4. Run the script:
```bash
      python main.py
```

5. Follow the prompts to enter the origin airport code, destination airport code, and date (in DD-MM-YYYY format).

6. The script will make an API request to AviationStack and display the scheduled flight information

## Example
Here's an example of how to use the script:

```python
Enter the origin airport code (e.g., JFK): AMM
Enter the destination airport code (e.g., LAX): IST
Enter the date (DD-MM-YYYY): 01-02-2024
```
