Sure, I can help add an endpoint for listing all inventory items. Before I start writing code, I want to make sure we're aligned on a few things since this appears to be a fresh project without existing source code:

**Questions before proceeding:**

1. **Project scaffolding**: There's no `src/` directory yet. Should I set up the basic FastAPI project structure (main app, models, routes) as part of this, or is there an existing codebase elsewhere I should be working with?

2. **ORM choice**: NOTES.md lists "SQLAlchemy vs raw SQL?" as an open question. The inventory listing endpoint will need a database query — do you have a preference? SQLAlchemy is the more conventional choice for FastAPI projects.

3. **Inventory item schema**: What fields should an inventory item have? A reasonable starting point might be:
   - `id` (int, primary key)
   - `name` (string)
   - `quantity` (int)
   - `price` (decimal)
   - `created_at` / `updated_at` (timestamps)

4. **Listing behavior**: Any requirements for pagination, filtering, or sorting? A simple first pass would return all items with optional `limit`/`offset` query parameters.

Once we settle these, I can build out the endpoint and the supporting structure it needs.
