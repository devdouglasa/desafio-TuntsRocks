from modules.components.situation.is_disaproved_by_fouls import is_disapproved_by_fouls
from modules.components.situation.check_averages_media import check_averages_media
from modules.components.situation.calc_media_averages import sum_of_notes
from modules.components.final_approval.check_note_final_approval import check_note_final_approval


# Main Function
def situation_average(data, sheet, interval="G4"):
    list_situations_averages = []

    #Loop to cycle through the table data and add the values to Google Sheets
    for index, line in enumerate(data):
        notes = []
        if index > 0:
            fouls = int(line[2])
            notes.append(int(line[3]))
            notes.append(int(line[4]))
            notes.append(int(line[5]))
            if is_disapproved_by_fouls(fouls):
                situation_average = "Reprovado por Falta"
                final_note = 0
            else:
                situation_average = check_averages_media(notes)
                final_note = check_note_final_approval(sum_of_notes(notes)) if situation_average == "Exame Final" else 0
            list_situations_averages.append([situation_average, final_note])

        sheet.update_and_write_data(interval, list_situations_averages)

