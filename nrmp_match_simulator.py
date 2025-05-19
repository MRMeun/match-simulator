
import streamlit as st

# Define the Gale-Shapley algorithm for the NRMP-style match
def gale_shapley(applicants, programs, slots):
    unmatched_applicants = list(applicants.keys())
    matches = {program: [] for program in programs.keys()}
    applicant_proposals = {applicant: [] for applicant in applicants.keys()}

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

# Define the applicants and programs with their preferences
applicants = {'Applicant1': ['Program2', 'Program1', 'Program3'], 'Applicant2': ['Program3', 'Program1', 'Program2'], 'Applicant3': ['Program3', 'Program2', 'Program1'], 'Applicant4': ['Program1', 'Program2', 'Program3'], 'Applicant5': ['Program2', 'Program3', 'Program1'], 'Applicant6': ['Program1', 'Program3', 'Program2'], 'Applicant7': ['Program3', 'Program1', 'Program2'], 'Applicant8': ['Program2', 'Program1', 'Program3'], 'Applicant9': ['Program1', 'Program3', 'Program2'], 'Applicant10': ['Program2', 'Program3', 'Program1']}

programs = {'Program1': ['Applicant8', 'Applicant7', 'Applicant5', 'Applicant1', 'Applicant2', 'Applicant3', 'Applicant4', 'Applicant6', 'Applicant9', 'Applicant10'], 'Program2': ['Applicant4', 'Applicant1', 'Applicant2', 'Applicant3', 'Applicant5', 'Applicant6', 'Applicant7', 'Applicant8', 'Applicant9', 'Applicant10'], 'Program3': ['Applicant3', 'Applicant8', 'Applicant9', 'Applicant1', 'Applicant2', 'Applicant4', 'Applicant5', 'Applicant6', 'Applicant7', 'Applicant10']}

slots = {'Program1': 3, 'Program2': 3, 'Program3': 3}

# Streamlit UI
st.title("NRMP-style Match Simulator")

if st.button("Run Match"):
    # Run the Gale-Shapley algorithm
    matches = gale_shapley(applicants, programs, slots)

    # Display the match results
    for program, matched_applicants in matches.items():
        st.write(f"{program} matched with: {', '.join(matched_applicants)}")
