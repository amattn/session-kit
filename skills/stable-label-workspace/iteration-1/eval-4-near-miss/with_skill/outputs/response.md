# Top 5 Features to Build

Based on the project context (REST API for inventory management, Python/FastAPI/PostgreSQL, with mobile app support per REQ_5), here are the top 5 features to prioritize:

### FEA_1: CRUD Endpoints for Inventory Items
Core resource management — create, read, update, delete inventory items. This is the foundation everything else builds on. Responses follow the snake_case JSON format with top-level "data"/"error" keys (REQ_4).

### FEA_2: Authentication and Authorization
The API needs auth before it can be exposed. Open question in NOTES.md on JWT vs session tokens needs resolution first (likely JWT given the mobile app requirement in REQ_5). Gate all inventory endpoints behind auth.

### FEA_3: Search and Filtering
Allow querying inventory by name, category, stock level, date ranges, etc. Pagination is essential for mobile clients (REQ_5). FastAPI's query parameter validation (DEC_2) makes this straightforward.

### FEA_4: Offline Sync Support for Mobile
REQ_5 requires offline sync capabilities for the companion mobile app. This means conflict resolution, last-modified timestamps, and a sync endpoint that accepts batched changes. Design the sync protocol before building.

### FEA_5: Stock Level Alerts and Low-Inventory Notifications
Notify when items drop below configurable thresholds. This is the first "smart" feature beyond basic CRUD and drives real operational value. PostgreSQL's concurrent write support (DEC_1) ensures accurate stock tracking under load.

---

Added the `FEA` prefix to the stable label prefix table in NOTES.md. All feature IDs above are permanent and greppable — grep `FEA_3` to find this definition and any future references.
