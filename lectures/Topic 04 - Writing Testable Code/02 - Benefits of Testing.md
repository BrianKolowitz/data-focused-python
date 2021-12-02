---
layout: default
title: 02 - Benefits of Testing
parent: Topic 04 - Writing Testable Code
grand_parent: Lectures
nav_order: 2
---
# 8 Benefis of Unit Testing
[8 benefits of unit testing](https://dzone.com/articles/top-8-benefits-of-unit-testing)

The goal of unit testing is to segregate each part of the program and test that the individual parts are working correctly. 
1. It isolates the smallest piece of testable software from the remainder of the code and determines whether it behaves exactly as you expect. 
1. Unit testing has proven its value in that a large percentage of defects are identified during its use. 
1. It allows automation of the testing process, reduces difficulties of discovering errors contained in more complex pieces of the application, and enhances test coverage because attention is given to each unit.

## 1. Makes the Process Agile
One of the main benefits of unit testing is that it makes the coding process more Agile. When you add more and more features to a software, you sometimes need to change old design and code. However, changing already-tested code is both risky and costly. If we have unit tests in place, then we can proceed for refactoring confidently.

Unit testing really goes hand-in-hand with agile programming of all flavors because it builds in tests that allow you to make changes more easily. In other words, unit tests facilitate safe refactoring. 

## 2. Quality of Code
Unit testing improves the quality of the code. It identifies every defect that may have come up before code is sent further for integration testing. Writing tests before actual coding makes you think harder about the problem. It exposes the edge cases and makes you write better code. 

## 3. Finds Software Bugs Early
Issues are found at an early stage. Since unit testing is carried out by developers who test individual code before integration, issues can be found very early and can be resolved then and there without impacting the other pieces of the code. This includes both bugs in the programmer’s implementation and flaws or missing parts of the specification for the unit.

## 4. Facilitates Changes and Simplifies Integration
Unit testing allows the programmer to refactor code or upgrade system libraries at a later date and make sure the module still works correctly. Unit tests detect changes that may break a design contract. They help with maintaining and changing the code.

Unit testing reduces defects in the newly developed features or reduces bugs when changing the existing functionality. 

Unit testing verifies the accuracy of the each unit. Afterward, the units are integrated into an application by testing parts of the application via unit testing. Later testing of the application during the integration process is easier due to the verification of the individual units.

## 5. Provides Documentation
Unit testing provides documentation of the system. Developers looking to learn what functionality is provided by a unit and how to use it can look at the unit tests to gain a basic understanding of the unit’s interface (API).

## 6. Debugging Process
Unit testing helps simplify the debugging process. If a test fails, then only the latest changes made in the code need to be debugged.

## 7. Design
Writing the test first forces you to think through your design and what it must accomplish before you write the code. This not only keeps you focused; it makes you create better designs. Testing a piece of code forces you to define what that code is responsible for. If you can do this easily, that means the code’s responsibility is well-defined and therefore that it has high cohesion.

## 8. Reduce Costs
Since the bugs are found early, unit testing helps reduce the cost of bug fixes. Just imagine the cost of a bug found during the later stages of development, like during system testing or during acceptance testing. Of course, bugs detected earlier are easier to fix because bugs detected later are usually the result of many changes, and you don’t really know which one caused the bug. 
