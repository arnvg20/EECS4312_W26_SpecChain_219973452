# Requirement ID: FR1

- Description: The system shall provide guided breathing and grounding exercises for users experiencing anxiety or stress.
- Source Persona: Stressed Student
- Traceability: Derived from review group G1
- Acceptance Criteria: Given a user selects an anxiety support tool, when the session begins, then the breathing exercise must load and start within 2 seconds.

# Requirement ID: FR2

- Description: The system shall provide mood reframing prompts to help users convert negative thoughts into constructive thoughts.
- Source Persona: Stressed Student
- Traceability: Derived from review group G1
- Acceptance Criteria: Given a user enters a negative thought, when the system processes the input, then it shall provide at least one reframing suggestion.

# Requirement ID: FR3

- Description: The system shall provide sleep and meditation audio sessions for users with trouble sleeping.
- Source Persona: Sleep Support User
- Traceability: Derived from review group G2
- Acceptance Criteria: Given a user opens the sleep support section, when the user presses play, then the audio must begin successfully.

# Requirement ID: FR4

- Description: The system shall provide guided relaxation tools including breathing, mindfulness, and sleep exercises.
- Source Persona: Sleep Support User
- Traceability: Derived from review group G2
- Acceptance Criteria: Given the user accesses the relaxation menu, when it loads, then at least 3 support tools shall be available.

# Requirement ID: FR5

- Description: The system shall maintain conversation context across a single active chat session.
- Source Persona: Conversation Quality User
- Traceability: Derived from review group G3
- Acceptance Criteria: Given a user asks a follow-up question, when the system responds, then it shall reference the previous message context.

# Requirement ID: FR6

- Description: The system shall avoid repetitive chatbot responses for similar user inputs.
- Source Persona: Conversation Quality User
- Traceability: Derived from review group G3
- Acceptance Criteria: Given a user sends two different emotional concerns, when the system replies, then the responses must be contextually different.

# Requirement ID: FR7

- Description: The system shall clearly display subscription pricing before requesting payment details.
- Source Persona: Budget Conscious User
- Traceability: Derived from review group G4
- Acceptance Criteria: Given a user accesses premium features, when pricing is shown, then subscription cost and billing period must be clearly visible.

# Requirement ID: FR8

- Description: The system shall allow access to essential free mental health tools without requiring a paid subscription.
- Source Persona: Budget Conscious User
- Traceability: Derived from review group G4
- Acceptance Criteria: Given a non-premium user logs in, when opening the main dashboard, then at least one support tool must remain accessible.

# Requirement ID: FR9

- Description: The application shall load all chatbot messages within 2 seconds.
- Source Persona: Reliability Focused User
- Traceability: Derived from review group G5
- Acceptance Criteria: Given a user sends a message, when waiting for the reply, then the response must load within 2 seconds.

# Requirement ID: FR10

- Description: The application shall not crash during active user sessions.
- Source Persona: Reliability Focused User
- Traceability: Derived from review group G5
- Acceptance Criteria: Given the user is actively using any feature, when interacting continuously for 10 minutes, then the app must remain stable.
