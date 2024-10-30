# Created by nagamuralikotari at 28/10/24
Feature: Verify if books are added and deleted using Library API
  # Enter feature description here

  Scenario: Verify AddBook API functionality
    Given The book details which needs to be added to Library
    When we execute the addbook postAPI method
    Then book is successfully added