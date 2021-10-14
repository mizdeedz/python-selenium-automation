# Created by jessi at 10/13/2021
Feature: Tests for product page


  Scenario: User can select dress colors
    Given Open Amazon product 807NF5WGQ1 page
    Then Verify user can click through colors


   Scenario: User can click all shirt colors
     Given Open Amazon product B081YS2F7N page
     Then Verify user can select all colors