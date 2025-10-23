# Minimum Viable Product (MVP) Definition: NearStarXR

The goal of the MVP is to deliver a functional, deployed WebXR application that successfully demonstrates the core concept for the Chroma Awards deadline.

---

### **MUST-HAVE** Features for MVP:
*   **Backend:** A Python Flask server that can serve a pre-processed `stars.json` file via a single API endpoint.
*   **Data:** The `stars.json` file contains at least 15-20 of the nearest stars with pre-calculated XYZ coordinates.
*   **Frontend:** An A-Frame scene that fetches and displays the stars from the backend API.
*   **Core Visualization:**
    *   Stars are rendered as simple spheres at their correct XYZ positions.
    *   Stars are correctly color-coded based on their spectral type.
*   **Basic Interaction:** Gazing at a star with the on-screen cursor displays its name as simple text.
*   **XR Functionality:** The scene includes a "Enter VR/AR" button and is viewable in a VR headset.
*   **Deployment:** The entire application is successfully containerized with Docker and deployed to a public URL on Google Cloud Run.

---

### **OUT OF SCOPE** for MVP:
*   **Stellar Highways / Jump Lines:** This feature will be implemented post-MVP.
*   **Variable Star Sizes/Luminosity:** All stars in the MVP will be the same size for simplicity.
*   **Advanced UI Panels:** Information will be displayed using simple text, not complex UI panels.
*   **User Controls:** No user movement controls (teleportation, etc.) are required for the MVP.
*   **Dynamic Data:** The star data is fixed; there will be no searching, filtering, or live data scraping.