# Created by jessi at 10/6/2021
Feature: test cases for cart functionality


  Scenario: User has no items in cart
    Given Open Amazon page
    When Click on the cart icon
    Then Verify cart has 0 items
    And Verify Your Amazon Cart is empty text present