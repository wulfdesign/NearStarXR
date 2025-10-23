# NearStarXR

An interactive and immersive WebXR application that visualizes the nearest stars to our solar system. This project allows users to explore our stellar neighborhood in 3D, either on a standard web browser or in a virtual reality headset.

This project is the latest iteration of a personal passion for stellar cartography that has spanned decades. It represents a modern approach to visualizing our stellar neighborhood, leveraging AI-assisted development workflows and immersive technologies like WebXR to create a more engaging and accessible experience.

### Controls

The application starts with a slow, cinematic orbit around the Sun.

*   **Move Position:** Use the **WASD** keys.
*   **Zoom:** Use the **Mouse Wheel**.
*   **Manual Orbit:** **Click and Drag** the mouse to stop the auto-orbit and take manual control.
*   **Look Around:** Hold **Shift + Click and Drag** to look around from your current position.
*   **Toggle Auto-Orbit:** A **single click** on the background will stop or start the automatic rotation.

### Technical Overview

The backend is a Python server that processes astronomical data into XYZ coordinates, which is then served to a frontend built with A-Frame. The entire application is containerized with Docker and designed for easy deployment on Google Cloud Run.

### Project Context

This project was created as an entry for the **Seattle AI Festival** and the **Chroma Awards 2025** in the Simulation / Sandbox and Experimental / Open categories.