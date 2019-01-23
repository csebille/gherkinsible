Feature: Showing off behave + suitable + ansible capability

Scenario: Run a simple test using ansible
    Given I connect on localhost
    When I ask who am I
    Then the answer is root
