from selenium import webdriver
from selenium.webdriver.common.by import By


class RPA:
    def __init__(self, url) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        
    def quit(self):
        self.driver.quit()

    def get_inputs(self, labels_names):
        inputs = {}
        
        for name in labels_names:
            inputs[name] = self._find_sibling_by_text('label', 'input', name)
        
        return inputs 
    
    def fill_inputs(self, inputs, data):
        for k, v in inputs.items():
            v.send_keys(str(data[k]))

    def submit_form(self):
        # form = self._find_element_by_tag('form')
        # form.submit()
        submit_btn = self._find_element_by_selector("input[type='submit']")
        submit_btn.click()
        
    def click_button(self, text):
        btn = self._find_element_by_text(text, 'button')
        btn.click()

    def _find_element_by_selector(self, selector):
        return self.driver.find_element(By.CSS_SELECTOR, selector)

    def _find_element_by_tag(self, tag):
        return self.driver.find_element(By.TAG_NAME, tag)

    def _find_element_by_text(self, text, element):
        return self.driver.find_element(By.XPATH, f"//{element}[contains(text(), '{text}')]")
    
    def _find_sibling_by_text(self, element, sibling, text):
        return self.driver.find_element(By.XPATH, f"//{element}[contains(text(), '{text.rstrip()}')]//following-sibling::{sibling}")