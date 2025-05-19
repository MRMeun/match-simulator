
import streamlit as st

# Define the Gale-Shapley algorithm for the NRMP-style match
def gale_shapley(applicants, programs, slots):
    # Initialize match results
    matches = {program: [] for program in programs}
    unmatched_applicants = list(applicants.keys())
    
    # While there are unmatched applicants
    while unmatched_applicants:
        applicant = unmatched_applicants.pop(0)
        applicant_prefs = applicants[applicant]
        
        for program in applicant_prefs:
            if len(matches[program]) < slots[program]:
                matches[program].append(applicant)
                break
            else:
                current_applicants = matches[program]
                program_prefs = programs[program]
                
                for current_applicant in current_applicants:
                    if program_prefs.index(applicant) < program_prefs.index(current_applicant):
                        matches[program].remove(current_applicant)
                        matches[program].append(applicant)
                        unmatched_applicants.append(current_applicant)
                        break
                else:
                    continue
                break
    
    return matches

# Streamlit app
st.title("NRMP-style Match Simulator")

# Input fields for applicants and programs
num_applicants = 10
num_programs = 3

applicants = {}
programs = {}
slots = {}

st.header("Applicant Preferences")
for i in range(1, num_applicants + 1):
    applicant_name = f"Applicant{i}"
    prefs = st.text_input(f"Enter preferences for {applicant_name} (comma-separated):", key=f"applicant_{i}")
    applicants[applicant_name] = [p.strip() for p in prefs.split(",")]

st.header("Program Preferences")
for i in range(1, num_programs + 1):
    program_name = f"Program{i}"
    prefs = st.text_input(f"Enter preferences for {program_name} (comma-separated):", key=f"program_{i}")
    programs[program_name] = [p.strip() for p in prefs.split(",")]
    slots[program_name] = st.number_input(f"Enter number of slots for {program_name}:", min_value=1, value=3, key=f"slots_{i}")

# Run the match algorithm
if st.button("Run Match"):
    match_results = gale_shapley(applicants, programs, slots)
    
    st.header("Match Results")
    for program, matched_applicants in match_results.items():
        st.write(f"{program} matched with: {', '.join(matched_applicants)}")
