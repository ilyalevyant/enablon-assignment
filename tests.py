
from test_helpers.constants import *


def test_authorize_main_page(main_page):
    """
    1. Go to main page.
    2. Validate input field for tasks.
    """
    assert main_page.get_header() == HEADER_VALUE, "header was not found"
    assert main_page.get_input_task_field().is_displayed(), "input field for tasks was not found"


def test_add_tasks(main_page):
    """
    1. Go to the main page.
    2. Add 2 tasks.
    3. Validate tasks saved and displayed.
    4. Item counter shows according value.
    """
    main_page.add_tasks(TASK_LIST)
    assert all(main_page.is_task_displayed(task) for task in TASK_LIST), f'task was not saved to task list'
    assert main_page.get_task_counter() == "2 items left", "counter value is not as expected"


def test_delete_task(main_page):
    """
    1. Go to the main page.
    2. Add task.
    3. Delete task.
    4. Validate task was deleted.
    """
    main_page.add_task(TASK_NAME)
    main_page.delete_task(TASK_NAME)
    assert not main_page.is_task_displayed(TASK_NAME)


def test_select_task(main_page):
    """
    1. Go to the main page.
    2. Add task.
    3. Select task.
    4. Validate button "Clear completed" is active.
    5. Validate task presentation was changed (another class was applied to the element).
    6. Counter of tasks shows "0 items left".
    """
    main_page.add_task(TASK_NAME)
    main_page.select_task(TASK_NAME)
    assert main_page.get_task_counter() == "0 items left", "counter value is not as expected"
    assert main_page.is_clear_completed_btn_displayed(), "'Clear completed' btn was not displayed after selecting task"
    assert main_page.is_task_presented_as_selected(TASK_NAME), "task is not displayed as selected"


def test_edit_task(main_page):
    """
    1. Go to the main page.
    2. Add task.
    3. Edit task.
    4. Validate changes.
    """
    main_page.add_task(TASK_NAME)
    main_page.edit_task(TASK_NAME, UPDATED_TASK_NAME)
    assert main_page.is_task_displayed(UPDATED_TASK_NAME), "changes were not saved"
