# gherkinsible
Call ansible roles from Cucumber features via the Suitable wrapper

# Install

- Install ansible https://github.com/ansible/ansible/
- Install behave https://github.com/behave/behave
- Install suitable  https://github.com/seantis/suitable
- Install PyHamcrest

# Download this repo into a directory
Let say you have installed it in ${HOME}/gherkinsible

When you are in this directory simply type 
```
behave
```

Behave then plays all the features present into the **features** directory

**simple_ansible_call.feature** should return (if you are the **root** user) :

```
Feature: Showing off behave + suitable + ansible capability # features/simple_ansible_call.feature:1

  Scenario: Run a simple test using ansible  # features/simple_ansible_call.feature:3
    Given I connect on localhost             # features/steps/steps_simple_ansible_call.py:14 0.071s
    When I ask who am I                      # features/steps/steps_simple_ansible_call.py:23 0.585s
    Then the answer is root                  # features/steps/steps_simple_ansible_call.py:27 0.000s

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
```

# Todo
Integrate inventories

