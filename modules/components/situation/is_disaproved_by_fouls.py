
# Checks if the student is failing due to absence
def is_disapproved_by_fouls(fouls) -> bool:
    max_fouls = 0.25 * 60
    if fouls >= max_fouls:
        return True
    else:
        return False