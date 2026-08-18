# Context Map & Glossary

This file establishes the canonical domain language for the data_rein harness and the Sofia³ dashboard.

## Core Entities

- **Trail (Task Trail)**: The single source of truth for all agentic execution. It is a live, event-driven log of asynchronous work.
- **Task**: An individual execution entry within the Trail. Tasks belong to the Trail. They are not a separate system from the Trail.
- **Wiki**: The unified knowledge database (`wiki.db`) containing persistent, referenceable information.
- **Memory**: A specific type of entry residing *within* the Wiki. Memories belong to the Wiki. They are not a separate system from the Wiki.
- **Graph**: The visual, relational representation of the underlying data (Trail/Tasks + Wiki/Memories), rendered by Semantica. It acts as the primary navigational interface for the dashboard.
