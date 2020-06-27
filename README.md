# Django multiple-steps form<br/><br/>live at https://django-multistep-form.herokuapp.com/

This is an example of a Django application implementing a form splitted through multiple screens

## Code

* Global resources (for different projects) at [/general](./general): models, styles, ...
* Multistep form project at [/multistepform](./multistepform)
* REST api (using Django Rest framework) at [/api](./api); calls to get customer data using Vanilla JS

## Details

* Temporary data are stored in session and stored to database in last step
* Forms are automatically generated from models

### Devops

* Includes some tests for models and forms
* CI workflow (action) in GitHub: build, tests
* Automatically deployed to Heroku

## (I'd like) To-do

* Multilanguage
* Use TypeScript
* Some more tests
