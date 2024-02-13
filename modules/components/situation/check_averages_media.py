from modules.components.situation.calc_media_averages import calc_media_averages

# Checks the student's situation according to the average
def check_averages_media(notes):
    if calc_media_averages(notes) < 5:
        return "Reprovado por Nota"
    elif 5 <= calc_media_averages(notes) < 7:
        return "Exame Final"
    elif calc_media_averages(notes) >= 7:
        return "Aprovado"