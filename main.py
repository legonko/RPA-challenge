import time

from utils import read_excel
from rpa import RPA


def parse_form():
    url = "https://www.rpachallenge.com/"
    path = "./data/challenge.xlsx"
    data = read_excel(path)
    labels_names = data.columns
    rpa = RPA(url)
    rpa.click_button('Start')
    
    for i in range(len(data)):
        inputs = rpa.get_inputs(labels_names)
        rpa.fill_inputs(inputs, data.iloc[i])
        rpa.submit_form() 
  
    time.sleep(10)
    rpa.quit()


if __name__ == "__main__":
    parse_form()