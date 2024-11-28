Feature: Removing HTML tags from text

    Scenario: Removing HTML tags from a string
        Given I have the HTML content "<p>1234 1234 1234 1234</p>"
        When I remove HTML tags
        Then The result should be "1234 1234 1234 1234"
