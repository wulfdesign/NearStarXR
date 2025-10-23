# NearStarXR - Task Checklist

## Phase 1: Project Setup & Foundation
- [x] Initialize Git repository
- [x] Create core documentation files (README, PRD, MVP, GDD, TASKS, DEVLOG)
- [x] Link to GitHub remote repository
- [x] Populate documentation files with initial content
- [x] Create `server` and `app` directories

## Phase 2: Backend Development
- [ ] Create `server/stars.csv` with initial star data
- [ ] Create `server/process_data.py` to convert coordinates
- [ ] Create `server/requirements.txt` with dependencies (Flask, Pandas, etc.)
- [ ] Run `process_data.py` to generate `stars.json`
- [ ] Create `server/main.py` with a Flask app to serve the JSON file
- [ ] Test the server locally

## Phase 3: Frontend Development
- [ ] Create `app/index.html` with A-Frame boilerplate
- [ ] Write JavaScript to fetch star data from the backend API
- [ ] Dynamically create `<a-sphere>` entities for each star
- [ ] Implement logic to color-code stars based on spectral type
- [ ] Add `event-set-component` for gaze-based interaction
- [ ] Display star name on gaze

## Phase 4: Containerization & Local Test
- [ ] Create `Dockerfile` in the root directory
- [ ] Build the Docker image locally
- [ ] Run the Docker container locally and test the full application at `localhost:8080`

## Phase 5: Cloud Deployment
- [ ] Authenticate with `gcloud` CLI
- [ ] Submit the Docker build to Google Cloud Build
- [ ] Deploy the container image to Google Cloud Run
- [ ] Verify the application is live at the public URL

## Phase 6: Post-MVP Polish (Future)
- [ ] Implement "Jump Lines" feature
- [ ] Add variable star sizing based on luminosity/radius
- [ ] Design and implement a detailed information UI panel