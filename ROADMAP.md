# NearStarXR Roadmap

This document outlines the future vision and planned improvements for the NearStarXR project.

---

### Near-Term Goals (Polishing the MVP)

*   **[ ] Enhanced Information on Hover:**
    *   Expand the hover-over text to display more than just the star's name.
    *   Include key data like Spectral Type, Distance from Sol, and the calculated X, Y, Z coordinates.
    *   Design a clean, non-intrusive UI panel for this information.

*   **[ ] Jump Lines / Stellar Highways:**
    *   Implement the initial concept of drawing lines between stars that are close to each other.
    *   This will provide a better sense of the 3D space and stellar density.

*   **[ ] UI/UX Polish:**
    *   Add a simple loading screen.
    *   Create a title or welcome text that fades in and out.
    *   Add on-screen control hints.

---

### Mid-Term Goals (Major Feature Expansion)

*   **[ ] MPC/Agent-Driven Data Expansion:**
    *   Re-implement the MPC (Model-View-Controller) pattern from the AI bootcamp to create a more robust data pipeline.
    *   Develop an agent capable of scraping detailed information from sources like Wikipedia for each star (e.g., mass, luminosity, metallicity).
    *   Use the agent to find and add data for known exoplanets, which can be rendered as smaller objects orbiting their parent stars.
    *   Create a workflow where an agent can be tasked to find and process data for additional stars beyond the initial dataset.

---

### Long-Term Goals (Architectural Overhaul)

*   **[ ] Core Engine Migration to Three.js:**
    *   Rewrite the frontend from A-Frame into pure Three.js to unlock the full power of WebGL.
    *   **Goal: Performance.** Utilize advanced techniques like Instanced Static Meshes to render thousands of stars at high frame rates.
    *   **Goal: Visual Fidelity.** Implement custom shaders for advanced graphical effects, such as dynamic, procedural halos, volumetric light rays, and twinkling effects.
    *   **Goal: Control.** Gain complete control over the render loop, user interactions, and VR/XR features for a more polished and professional experience.