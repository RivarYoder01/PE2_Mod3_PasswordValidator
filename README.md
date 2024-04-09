# CSC 365 Paired Programming #3 Password Validator
## Written by: Rivar Yoder and Jonathan Nissen

A variety of password options are passed throguh a default validator and an advanced validator. The default validator (Parent Class) test for the minimum (2 for all) uses of uppercase, lowercase, numbers, and symbols. The advanced validator (Child Class) tests for all those previous perameters aswell as length and the use of specific symbols.

**PasswordValidator Receives:**
* AAaa11!!, Abb12!!, AAb12!, AAbb1, AAbb12!, b!, bb

**PasswordValidator Checks for:**
* Minumus Lowercase- 2
* Minumum Uppercase- 2
* Minumum Numbers- 2
* Minimum Symbols- 2

**AdvPasswordValidator Receives:**
* AAaa11!!, Abb12!!, AAb12!, AAbb1, AAbb12!, b!, bb, AAbb!!12, AAbb!!12121212

**AdvancedPasswordValidator Checks for:**
* Minumum Lowercase- 2
* Minumum Uppercase- 2
* Minumum Numbers- 2
* Minimum Symbols- 2
* Minumum Length- 8
* Maximum Length- 12
* Can only use Symbols- '@', '_', '!', '#', '$', '%', '&', '*', '?', '~'
* 
‐------------------‐----------------------------------------------------------
### **What was Learned:**
* Object Oriented Programming(OOP)
* The use of super classes and sub classes
* Use of try and except
* Programs using multiple files
* Passing objects across classes and moduels

