from WBI import WBI
from modules import (SelfAwarenessModule, HeuristicPatternRecognitionModule, CounterfactualSimulatorModule, 
                     ValueAffectionModule, EmpathicInteractionModule, GlobalWorkspaceTheoryModule, 
                     LearningFromExperienceModule)

def collect_sensor_information():
    return "sensor_data"

def formulate_aspirations():
    return "goals"

if __name__ == "__main__":
    wbi = WBI([SelfAwarenessModule(), HeuristicPatternRecognitionModule(),
               CounterfactualSimulatorModule(), ValueAffectionModule(),
               EmpathicInteractionModule(), GlobalWorkspaceTheoryModule(),
               LearningFromExperienceModule()])

    input_stimulus = collect_sensor_information()
    desired_goals = formulate_aspirations()
    
    perception = wbi.perceive(input_stimulus)
    decision = wbi.decide(desired_goals)
    selected_action = wbi.execute(decision)
    
    print(f"Selected action: {selected_action}")
