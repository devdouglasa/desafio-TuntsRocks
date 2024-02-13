from services.api_sheets import ApiSheets
from modules.situation_average import situation_average

# Run project
def main():
  # Instance Class API Sheets
  sheet = ApiSheets(name_sheet="engenharia_de_software", interval="A3:H27")
  # Get all data in sheet
  data = sheet.get_data()
  # Main
  situation_average(data, sheet)

if __name__ == "__main__":
  main()