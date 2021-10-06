# Created by jessi at 10/2/2021
Feature: test cases for search functionality

  Scenario: User can search for coffee on Amazon
    Given Open Amazon page
    When Input coffee into amazon search
    And Click on amazon search icon
    Then Verify "coffee" text is shown

#  Scenario Outline: User can search for a product on Amazon
#    Given Open Amazon page
#    When Input <search_word> into amazon search
#    And Click on amazon search icon
#    Then Verify <result> text is shown
#    Examples:
#    |search_word  |result   |
#    |table        |"table"  |
#    |mug          |"mug"    |