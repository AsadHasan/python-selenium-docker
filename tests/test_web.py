from pageobjects.Homepage import Homepage


def test_unanswered_questions_present(selenium, base_url):
    unanswered_questions = Homepage(selenium).open(base_url).browse_questions().get_unanswered_questions()
    assert len(unanswered_questions), "No unanswered questions found"
