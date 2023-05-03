# Pong_Game
This is a sample repository to show one way of implementing the Microsoft sbom-tool into the CI/CD pipeline.

There is a github actions workflow titled [SBOM generation](https://github.com/samuelc7/Pong_Game/actions/workflows/main.yml) which does the following: 
  1. Downloads and checks out this repository using the [actions/checkout@v3](https://github.com/marketplace/actions/checkout).
  2. Uses the microsoft [sbom-tool](https://github.com/microsoft/sbom-tool) to generate an spdx SBOM.
  3. Uploads the generated SBOM as an artifact of the workflow.
