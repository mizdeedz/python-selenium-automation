# Created by jessi at 10/12/2021
Feature: Amazon bestseller page tests


  Scenario: Verify users can see all category links
    Given Open Amazon Best Sellers page
    Then Verify 5 best sellers links are present

  Scenario: Bestsellers links can be opened
    Given Open Amazon Best Sellers page
    Then User can click through top links and verify correct page opens