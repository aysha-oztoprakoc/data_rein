---
name: isometric-system-map
description: >-
  Generate an interactive isometric system map of a codebase or infrastructure
  using 3D HTML/CSS blocks, SVG tracing paths, and a cited legend/explainer panel.
  Use when the user asks to "create an isometric system map" or "show infrastructure as varied 3d building on a grid".
---

# Isometric System Map Generator

This skill guides you through generating an interactive, isometric 3D system map of a repository's infrastructure or architecture. It is designed to visualize components, nodes, data flows, and control paths as a beautiful HTML artifact.

## 1. Analysis Phase
- **Map the Domain**: Read the primary architectural documents (e.g., `ORCHESTRATION_GOAL.md`, `blueprint.yaml`, `ARCHITECTURE.md`).
- **Identify Nodes**: Find the physical or logical nodes (e.g., Workstations, Servers, Routers, Databases).
- **Identify Paths**: Understand the control paths (routing/validation) versus data paths (payloads/state).
- **Collect Citations**: For every node or core component, note the exact file paths that define it so they can be cited in the explainer panel.

## 2. Artifact Generation
- Create an HTML artifact (e.g., `isometric_system_map.html`).
- **Grid Setup**: Use CSS `transform: rotateX(60deg) rotateZ(-45deg);` to create an isometric grid plane with a subtle thin-line grid background.
- **3D Nodes (Stacked Plates)**: Instead of solid boxes, represent nodes as a stack of semi-transparent horizontal glass plates or wireframe layers using CSS `transform-style: preserve-3d`. 
  - Construct nodes from multiple `.layer` divs translated along the Z-axis (e.g., `translateZ(10px)`, `translateZ(20px)`).
  - Use dark, translucent backgrounds with thin, crisp borders (e.g., `rgba(255,255,255,0.1)`).
- **Floating Tags**: Above each node (e.g., at `translateZ(100px)`), place a small rectangular label/tag (e.g., "CM", "RL") connected to the node by a thin vertical line.
- **Paths**: Overlay an `<svg>` element with sharp, orthogonal (right-angled) glowing blue lines (solid or dashed) connecting the nodes. Use `<path>` elements. Add glowing dots (e.g., `<circle>` or CSS animations) moving along these paths to represent payloads in motion.
- **Interactive Explainer Panel**: Include a sidebar panel. When a user clicks or hovers over a node, update the panel to show the node's details and the collected citations (e.g., `knowledge_base/HARDWARE.md`).

## 3. Aesthetic Constraints
- **Monochrome & Glowing Blue**: Avoid multi-colored rainbow blocks. The palette should be deep black/grey background, translucent dark grey/blue nodes, stark white/grey typography, and vivid blue (`#58a6ff` or similar) for active paths and highlights.
- **Crisp & Minimalist**: Use thin borders (1px) and a monospace font (like Fira Code or standard UI monospace) for all tags and UI elements.
- **Glass/Acrylic Look**: Use `backdrop-filter: blur(...)` and semi-transparent backgrounds to simulate layers of glass.
