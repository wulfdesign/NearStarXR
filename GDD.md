# Game Design Document: NearStarXR

## 1. Core User Experience
The user loads into a dark, empty space and is immediately presented with a three-dimensional map of glowing stars around them. They can look around freely to understand the relative positions of our stellar neighbors. By pointing their cursor at a star, they can learn its name. The experience is designed to be awe-inspiring, minimalist, and educational.

## 2. Controls
*   **Flatscreen (Desktop):**
    *   **Look:** Mouse movement.
    *   **Interact:** A static cursor is fixed to the center of the screen. Interaction occurs when this cursor "gazes" over an object.
*   **VR Headset:**
    *   **Look:** Head movement.
    *   **Interact:** A gaze-based cursor tracks with the user's head movement.

## 3. Art & Aesthetics
*   **Environment:** A pure black or very dark navy blue background to simulate deep space.
*   **Stars:**
    *   **Model:** Simple spheres.
    *   **Effect:** A combination of a solid color and an emissive glow/halo effect to make them look like celestial bodies rather than simple balls.
    *   **Color Palette (by Spectral Type):**
        *   **O-type:** Bright Blue-White (`#9bb0ff`)
        *   **B-type:** Blue-White (`#aabfff`)
        *   **A-type:** White (`#cad8ff`)
        *   **F-type:** Yellow-White (`#f8f7ff`)
        *   **G-type (Sun-like):** Yellow (`#fff4ea`)
        *   **K-type:** Orange (`#ffd2a1`)
        *   **M-type (Red Dwarf):** Orange-Red (`#ffb568`)
        *   **D-type (White Dwarf):** Pale White (`#FFFFFF`)
*   **UI/Text:** Clean, sans-serif white font (e.g., Roboto, Lato) that is highly readable on a dark background, especially in VR.

## 4. Future Features (Post-MVP Vision)
*   **Information Panels:** Clicking on a star brings up a detailed panel with stats (mass, luminosity, etc.).
*   **Jump Lines Animation:** When activated, a glowing line animates between two connected stars.
*   **Sound Design:** A subtle, ambient space-themed soundtrack.