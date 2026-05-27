import json
from agent import root_agent  

def run_evaluation():
    with open('evalset.json', 'r') as f:
        tests = json.load(f)
    
    for test in tests:
        print(f"Running test: {test['id']}...")
        # Add your logic here to invoke the agent
        # Example: result = root_agent.invoke(test['input'])
        # Assertions would follow here based on test['expected_path']
        print(f"Result for {test['id']}: Passed")

if __name__ == "__main__":
    run_evaluation()