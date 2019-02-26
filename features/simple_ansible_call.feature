Feature: Showing off behave + suitable + ansible capability

Scenario: Run a simple test using ansible
    Given I connect on localhost
    When I ask who am I
    Then the answer is root

Scenario: Run a test using ansible copy module
    Given I copy the file /tmp/data.log on master.hdp in /tmp/remote/

Scenario: Run a simple test using an inventory
    Given I connect on every server in local group
    When I ask who am I
    Then the answer is root

Scenario: Run a simple test using an inventory
    Given I connect on every server in remote group
    When I ask who am I
    Then the answer is root
