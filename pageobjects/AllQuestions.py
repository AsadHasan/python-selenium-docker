from pageobjects.Basepage import Basepage


class AllQuestions(Basepage):
    UnansweredQuestionsButtonLocator: str
    UnansweredQuestionsListLocator: str

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.UnansweredQuestionsButtonLocator = '[data-nav-value="Unanswered"][data-shortcut="U"]>div'
        self.UnansweredQuestionsListLocator = "#questions>.question-summary"
        self.driver = driver

    def get_unanswered_questions(self):
        super().click_when_ready(10, self.UnansweredQuestionsButtonLocator)
