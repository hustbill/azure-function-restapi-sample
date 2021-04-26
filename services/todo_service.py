from services.dummy_data import get_todos, add_todo, edit_todo, delete_todo

def list_todos():
    return get_todos()

def add_todos(scenario):
    return add_todo(scenario)

def edit_todos(scenario):
    return edit_todo(scenario)

def delete_todos(scenario_id):
    return delete_todo(scenario_id)