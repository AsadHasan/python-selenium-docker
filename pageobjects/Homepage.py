from __future__ import annotations

from pageobjects.AllQuestions import AllQuestions
from pageobjects.Basepage import Basepage


class Homepage(Basepage):
    BrowseQuestionsButtonLocator: str

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.BrowseQuestionsButtonLocator = "[data-ga*=\"browse questions click\"]"

    def open(self, url: str) -> Homepage:
        self.driver.get(url)
        return self

    def browse_questions(self) -> AllQuestions:
        self.click_when_ready(10, self.BrowseQuestionsButtonLocator)
        return AllQuestions(self.driver)
