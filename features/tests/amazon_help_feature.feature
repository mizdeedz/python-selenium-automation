# Created by jessi at 10/6/2021
Feature: test cases for help page functionality
  # Enter feature description here

  Scenario: User can search help library for cancel order
    Given Open Amazon help page
    When Input cancel order into help library and search
    Then Verify Cancel Items or Orders result is shown

