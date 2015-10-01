Scenario Outline: Add new address
  Given a address list
  Given a address with <name>,<nickname>,<lastname>,<middlename>
  When I add the address to the list
  Then The new address list is equal to old list with the added address

  Examples:

  | name  | nickname  | lastname  | middlename |
  | Lilia | yoyxoxo   | asf       | sdjn       |
  | ;lkmdwfg | sdvfslj  | klnwg   | lkwng      |

Scenario: Delete a address
  Given a non-empty address list
  Given a random address from the list
  When I delete the address from the list
  Then the new address list is equal old list without the deleted address

Scenario: Edit a address
  Given a non-empty address list
  Given a random address from the list
  Given a new values for address fields with <new_name>
  When I edit the address from the list
  Then the new address list is equal old list with edited feature values

  | new_name |
  | Maria_edited |