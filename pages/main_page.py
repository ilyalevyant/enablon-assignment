
from page_objects import PageObject, PageElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(PageObject):

    __input_task_field: PageElement = PageElement(xpath="//*[@*='What needs to be done?']")
    __page_header: PageElement = PageElement(xpath="//h1")
    __task_counter: PageElement = PageElement(xpath="//*[@*='todo-count']")
    __clear_completed_btn: PageElement = PageElement(xpath="//*[*='Clear completed']")
    __input_field: PageElement = PageElement(xpath="//li/input")

    def double_click_element(self, element: PageElement):
        actions = ActionChains(self.w)
        actions.double_click(on_element=element).perform()

    def task_web_element(self, task_title):
        return self.w.find_element_by_xpath(f"//label[.='{task_title}']")

    def get_header(self):
        return self.__page_header.text

    def get_input_task_field(self):
        return self.__input_task_field

    def edit_task(self, task_title, new_task_title):
        task = self.task_web_element(task_title)
        self.double_click_element(task)
        task = self.__input_field
        task.click()
        task.send_keys(Keys.COMMAND + "a")
        task.send_keys(new_task_title)
        task.send_keys(Keys.RETURN)

    def add_task(self, task_title):
        input_field = self.__input_task_field
        input_field.click()
        input_field.send_keys(task_title)
        input_field.send_keys(Keys.RETURN)

    def add_tasks(self, tasks_list):
        for task in tasks_list:
            self.add_task(task)

    def get_task_counter(self):
        return self.__task_counter.text

    def is_clear_completed_btn_displayed(self):
        try:
            return self.__clear_completed_btn.is_displayed()
        except NoSuchElementException:
            return False

    def delete_task(self, task_title):
        task = self.task_web_element(task_title)
        delete_btn = self.w.find_element_by_xpath(f"//div//label[.='{task_title}']/../button[@*='destroy']")
        task.click()
        delete_btn.click()

    def select_task(self, task_title):
        checkbox = self.w.find_element_by_xpath(f"//div//label[.='{task_title}']/../*[@*='checkbox']")
        checkbox.click()

    def is_task_presented_as_selected(self, task_title):
        try:
            self.w.find_element_by_xpath(f"//*[@class='completed']//.//label[.='{task_title}']")
            return True
        except NoSuchElementException:
            return False

    def is_task_displayed(self, task_title):
        try:
            task = self.task_web_element(task_title)
            return task.is_displayed()
        except NoSuchElementException:
            return False
