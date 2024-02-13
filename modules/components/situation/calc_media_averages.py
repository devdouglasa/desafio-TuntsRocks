from math import ceil

# Calculates grade point average
def calc_media_averages(notes: list):
  if len(notes) > 1:
    sum_notes = sum_of_notes(notes)
    return ceil(sum_notes / len(notes))
  else:
    return 0
  
def sum_of_notes(notes: list):
  sum_notes = 0
  for note in notes:
    sum_notes += note
  
  return sum_notes
  