data = {
    "todos": [
      {
        "id": 1,
        "scenario": 'scenario1',
        "dataset": 'dataset1000',
        "status": 'completed'
      },
      {
        "id": 2,
        "scenario": 'scenario2',
        "dataset": 'dataset1001',
        "status": 'completed'
      },
      {
        "id": 3,
        "scenario": 'scenario3',
        "dataset": 'dataset1002',
        "status": 'completed'
      },
      {
        "id": 4,
        "scenario": 'scenario4',
        "dataset": 'dataset1000',
        "status": 'completed'
      },
      
    ]
}

def get_todos():
    return data['todos']

def add_todo(scenario):
    scenario["id"] = len(data['todos']) + 1
    data['todos'].append(scenario)
    return {
      "message": "scenario added",
      "number of scenarios": len(data['todos'])
    }

def edit_todo(scenario):
    for i,todo in enumerate(data["todos"]):
        if todo["id"] == scenario["id"]:
           data["todos"][i] = scenario
    
    return {
      "message": "scenario edited",
      "number of scenarios": len(data['todos'])
    }

def delete_todo(scenario_id):
    item_to_remove = '';
    for todo in data["todos"]:
        if int(scenario_id) == todo["id"]:
            item_to_remove = todo
    if item_to_remove:
        data["todos"].remove(item_to_remove)
    
    return {
      "message": "scenario deleted",
      "number of scenarios": len(data['todos'])
    }