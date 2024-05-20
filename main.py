"""
WholeBrainedIntelligence (WBI) Technology
Author: Reece "Colton" Dixon
Date: 2024
Email: reece.c.dixon@live.com
"""

from WBI import WBI, watermark
from modules import (SelfAwarenessModule, HeuristicPatternRecognitionModule, CounterfactualSimulatorModule, 
                     ValueAffectionModule, EmpathicInteractionModule, GlobalWorkspaceTheoryModule, 
                     LearningFromExperienceModule)

def display_terms_and_conditions():
    terms = """
    WholeBrainedIntelligence (WBI) Technology - Terms and Conditions

    By using this software, you agree to the following terms and conditions:

    1. License
    1.1 Grant of License: The Licensor grants you a non-exclusive, non-transferable, worldwide license to use the software for commercial and non-commercial purposes as specified in the Commercial Use License and Public Non-Commercial License agreements.
    1.2 Restrictions: You may not sublicense, sell, or distribute the software without explicit permission from the Licensor. Modifications and derivative works must maintain this license.

    2. Acceptable Use
    2.1 Compliance: You agree to comply with all applicable laws and regulations in connection with your use of the software.
    2.2 Prohibited Conduct: You agree not to use the software for any unlawful or harmful purposes, including but not limited to the creation of malicious software, unauthorized data mining, or activities that infringe on intellectual property rights.

    3. Intellectual Property
    3.1 Ownership: The Licensor retains all rights, title, and interest in and to the software, including all intellectual property rights.
    3.2 Attribution: Any use of the software must include appropriate attribution to the Licensor, including the author’s name and the project name.

    4. Privacy and Data Protection
    4.1 Data Handling: The software should be used in a manner that respects user privacy and complies with applicable data protection laws, such as GDPR and HIPAA.
    4.2 Anonymization: Sensitive data should be anonymized and securely handled to protect user privacy.

    5. Liability
    5.1 Disclaimer of Warranties: The software is provided "as is", without warranties of any kind, either express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement.
    5.2 Limitation of Liability: In no event shall the Licensor be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of the software, even if advised of the possibility of such damage.

    6. Indemnification
    You agree to indemnify, defend, and hold harmless the Licensor from and against any claims, liabilities, damages, losses, and expenses, including but not limited to legal fees and costs, arising out of or in any way connected with your use of the software or your violation of these terms.

    7. Termination
    7.1 Termination by You: You may stop using the software at any time.
    7.2 Termination by Licensor: The Licensor may terminate this agreement and your license to use the software at any time if you breach these terms.
    7.3 Effect of Termination: Upon termination, you must cease all use, distribution, and modification of the software.

    8. Governing Law and Dispute Resolution
    8.1 Governing Law: These terms and conditions are governed by and construed in accordance with the laws of the State of Kentucky, without regard to its conflict of laws principles.
    8.2 Dispute Resolution: Any disputes arising under or in connection with these terms shall be resolved through mediation or arbitration as mutually agreed upon by the parties.

    9. Amendments
    The Licensor reserves the right to modify these terms and conditions at any time. Your continued use of the software after any such changes constitutes your acceptance of the new terms.

    10. Contact Information
    For any questions regarding these terms and conditions, please contact Reece "Colton" Dixon at reece.c.dixon@live.com.
    """

    print(terms)
    response = input("Do you agree to the terms and conditions? (yes/no): ")
    if response.lower() != 'yes':
        print("You must agree to the terms and conditions to use this software.")
        exit()

def collect_sensor_information():
    return "sensor_data"

def formulate_aspirations():
    return "goals"

if __name__ == "__main__":
    # Display the terms and conditions at the start
    display_terms_and_conditions()

    # Add the watermark for identification
    watermark()

    wbi = WBI([SelfAwarenessModule(), HeuristicPatternRecognitionModule(),
               CounterfactualSimulatorModule(), ValueAffectionModule(),
               EmpathicInteractionModule(), GlobalWorkspaceTheoryModule(),
               LearningFromExperienceModule()])

    input_stimulus = collect_sensor_information()
    desired_goals = formulate_asp
