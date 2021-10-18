# Created by jessi at 10/17/2021
Feature: Tests for privacy notice page


  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    Given Store original window
    When Click on Amazon Privacy Notice link
    And Switch to new window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window and switch back to original