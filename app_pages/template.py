import streamlit as st

def calculate_borda_scores(votes, weights, scoring_vec = [2, 1, 0]):
    """Calculate Borda scores from lists of voter preferences and weights."""
    candidate_map = {'a': 0, 'b': 1, 'c': 2}
    num_candidates = 3
    scores = [0] * num_candidates
    # Process each vote with its weight
    for vote, weight in zip(votes, weights):
        for i, candidate in enumerate(vote):
            scores[candidate_map[candidate]] += weight * scoring_vec[i]
    return scores


def check_condorcet_loser(votes, weights):
    """Check for the presence of a Condorcet loser in the voting profiles."""
    candidates = 'abc'
    defeats = {c: {o: 0 for o in candidates if o != c} for c in candidates}
    
    for vote, weight in zip(votes, weights):
        for i in range(len(vote)):
            for j in range(i + 1, len(vote)):
                defeats[vote[i]][vote[j]] += weight
                defeats[vote[j]][vote[i]] -= weight
    
    # Determine if there's a Condorcet loser
    for candidate, others in defeats.items():
        if all(score < 0 for score in others.values()):
            return f"Candidate {candidate.upper()} is a Condorcet loser."
    return "There is no Condorcet loser."


def template_page():
    st.header("Borda Count and Condorcet Loser Checker for 3 Candidates")
    
    with st.form(key='borda_form'):
        # Input for the number of different voting profiles
        num_profiles = st.number_input("Enter the number of different voting profiles", min_value=1, value=1, step=1)

        # Lists to store user inputs
        votes = []
        weights = []
        
        # Generate input fields for each profile
        for n in range(num_profiles):
            st.write(f"Profile {n+1}")
            c1, c2 = st.columns(2)
            with c1:
                vote = st.text_input("Enter ranking (e.g., 'abc')", key=f"vote{n}")
            with c2:
                weight = st.number_input("Enter number of votes", min_value=0, value=1, step=1, key=f"weight{n}")
            votes.append(vote)
            weights.append(weight)
        
        # Submit button in the form
        submit_button = st.form_submit_button(label='Calculate Results')
    
    if submit_button:
        # Calculate scores
        scores = calculate_borda_scores(votes, weights)
        
        # Check for Condorcet loser
        condorcet_result = check_condorcet_loser(votes, weights)
        
        # Output results
        st.subheader("Borda Scores")
        st.write(f"Candidate A: {scores[0]} points")
        st.write(f"Candidate B: {scores[1]} points")
        st.write(f"Candidate C: {scores[2]} points")
        
        st.subheader("Condorcet Loser Check")
        st.write(condorcet_result)

# To run the function if running the script directly
if __name__ == "__main__":
    template_page()