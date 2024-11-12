# Election Results Calculator Borda Count 

This Streamlit app is designed to help users calculate election results using two different voting systems: Borda Count. It also includes functionality to check for the presence of a Condorcet loser among the candidates.

## Features

- **Borda Count**: Calculates scores based on the position of each candidate in the voter rankings.
- **Condorcet Loser Checker**: Determines if there is a candidate who loses to every other candidate in head-to-head comparisons.

## Installation

To run this app locally, you will need Python and Streamlit installed on your computer.

1. **Install Python**: If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).
2. **Install Streamlit**: Run the following command in your command line:
   ```
   pip install streamlit
   pip install pandas
   ```
3. **Download the App**: Clone or download this app from the repository.

## Usage

To use the app:

1. **Start the App**: Navigate to the app's directory in your command line and run:
   ```
   streamlit run main.py
   ```
2. **Input Data**:
   - Enter the number of different voting profiles you want to consider.
   - For each profile, enter the candidate ranking (e.g., 'abc') and the number of votes it received.

3. **Calculate Results**: After entering all the data, press the 'Calculate Results' button to view the election results and check for a Condorcet loser.

## Example Input and Output

### Input
- **Number of Profiles**: 3
- **Voting Method**: Borda
- **Profiles**:
  - Profile 1: Ranking 'abc', Votes 10
  - Profile 2: Ranking 'bca', Votes 5
  - Profile 3: Ranking 'cab', Votes 8

### Output
- **Borda Scores**:
  - Candidate A: 34 points
  - Candidate B: 29 points
  - Candidate C: 29 points
- **Condorcet Loser Check**: There is no Condorcet loser.

## Contributing

Contributions to the development and enhancement of this Streamlit app are welcome. Please feel free to fork the repository, make changes, and submit pull requests.
