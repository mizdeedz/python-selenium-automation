# Created by jessi at 10/13/2021
Feature: Amazon Sign In tests


  Scenario: Sign in page can be opened from Sign In popup
    Given Open Amazon page
    When Click Sign In from popup
    Then Verify Sign In page opens

  Scenario: Sign in popup is visible upon page opening, then disappears
    Given Open Amazon page
    When Sign In pop up appears
    And Wait for 5 sec
    Then Verify Sign In pop up disappeared