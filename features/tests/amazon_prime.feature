# Created by jessi at 10/10/2021
Feature: Amazon Prime tests


  Scenario: Verify user sees correct amount of benefit boxes
    Given Open Amazon Prime
    Then Verify 8 benefit boxes are present