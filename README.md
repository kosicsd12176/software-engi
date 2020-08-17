## Synopsis

This task requires to write the backend part for a web-app, using Python 3.8 and the Flask framework.

It is s intentionally open-ended and aims at fullfilling a requirement we set ourselves in our production environment. It will allow you to get a better understanding for the kind of challenges we are dealing with and help you decide if this class of challenges is something you personally find appealing. 

While there is no correct solution, beyond code that runs and fulfills the requirements, please keep the following in mind as bonus objectives, which will help us understand your approach better:

- how to demonstrate that the solution works
- how the code is structured for future extension, deployment, testing
- your approach to documenting
- what python features, additional libraries or external tools could be used to enhance readability of the codebase

Aim for a solution to take up 4-6 hours. Please do not spend time on making rendered pages look awesome,
 it is out of scope of this task (bootstrap is fine).

## Main user stories
1. As a User, I want to be able to see my account balance on the *Overview page*
2. As a User, I want to be able to send and receive payments, using sort code and account number, IBANs or other reference type.
3. As a User, I want to be able to see cashback tokens generated from each payment in the *Cashback page*
4. As a User, I want to see a list of choices for spending my cashback tokens on the *Impact page*

## Technical details
- example JSON payload for a IBAN payment is available in `examples/`
- the cashback ratio should be 5% of the total payment amount

