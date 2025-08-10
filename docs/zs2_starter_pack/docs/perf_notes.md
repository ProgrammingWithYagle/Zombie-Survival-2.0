# Performance Notes
- Target: 60 FPS on mid-tier laptop iGPU.
- Draw calls: batch where possible; consider vertex arrays for repeated quads.
- Spatial partitioning for entities; avoid O(n^2) scans.
