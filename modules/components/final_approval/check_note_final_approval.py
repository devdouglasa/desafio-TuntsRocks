
# Check the final grade for approval

# Calculation basis to get the grade for final approval
def check_note_final_approval(sum_of_notes):
    final_note = 21 - sum_of_notes
    if final_note <= 0:
        return 0
    else:
        return final_note
