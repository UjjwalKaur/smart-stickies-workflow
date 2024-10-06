# smart-stickies-ai-workflow

Project Overview

Input (user prompt):
    - "Create an interface with two buttons and a video embedding."

Open-source AI model (that we import):
    - Parses prompt
    - Retrieves user preferences for each of the following UI elements (since this is a proof of concept, we can just store the user preferences in a text file):
        - Page color
        - Button colors
        - Button and video sizes
        - Order of buttons and video
        - Font style
        - Font size

Workflow generator:
    - AI model calls an API function from a database of existing API calls for UI element creation.

Output:
    - A personalized user interface