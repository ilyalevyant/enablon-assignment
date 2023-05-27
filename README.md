# TODOS UI tests

To execute test:
```
/bin/bash run.sh
```

## General project description:
```
Tests are implemented with PageObject pattern: for each testing page should be created according class. 
Setup implemented with Python fixture 'main_page'. It is initializing driver instance and open start page.
Routine work, such a task creation, was implemented as fixture 'add_task' and performs before a test itself.
Web elements defined by XPATHs with as much as possible dynamic values.
Test plan can be found here: https://docs.google.com/spreadsheets/d/1DyvyNuGi7-SIzyxfoRJN6sdwKIlveA9lnamBKpOrEO4/edit#gid=0
Only some of this scenarios were implemented, as PoC.
```

## Implemented scenarios:
```
1. Open main page.
2. Add task.
3. Delete task.
4. Select task.
5. Edit task.
```
## Bugs & Issues:
```
1. Create task -> Change it -> Refresh the page: changes were not saved.
2. Create 2 identical tasks: 2nd task was created, despite service should prevent duplications
(unless the documentation states otherwise).
3. Create 2 tasks -> Change one of them with title of another : task was updated, despite service should prevent duplications 
(unless the documentation states otherwise).
```


