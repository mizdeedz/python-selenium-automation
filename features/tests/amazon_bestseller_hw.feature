# Created by jessi at 10/12/2021
Feature: Amazon bestseller page tests


  Scenario: Verify users can see all category links
    Given Open Amazon Best Sellers page
    Then Verify 5 best sellers links are present