# Agent Harness Reference

Different agent harnesses have different conventions for project-level directives. /warmup needs to know which file(s) to target. This document summarizes the landscape as of early 2026.

## Claude Code

- **Primary file:** `CLAUDE.md` (project root)
- **Discovery:** walks up the directory tree from the current working directory, loading CLAUDE.md at each level. Also discovers CLAUDE.md in subdirectories when files there are read.
- **Hierarchy:** managed policy (org-wide) → `~/.claude/CLAUDE.md` (user global) → `./CLAUDE.md` or `./.claude/CLAUDE.md` (project) → `./CLAUDE.local.md` (local, not committed)
- **Rules directory:** `.claude/rules/` — all `.md` files discovered recursively
- **Auto-memory:** native. Persistent project-scoped memory files, loaded before CLAUDE.md. Strongest tactic for ensuring behaviors survive across sessions.

## OpenAI Codex CLI

- **Primary file:** `AGENTS.md`
- **Discovery:** reads global `~/.codex/AGENTS.md` (or `AGENTS.override.md`), then walks from project root to current working directory, checking each level
- **Fallback:** if no `AGENTS.md` exists, checks `project_doc_fallback_filenames` from `~/.codex/config.toml`. Add `CLAUDE.md` here for cross-compatibility: `project_doc_fallback_filenames = ["CLAUDE.md"]`
- **Override:** `AGENTS.override.md` at any level takes precedence over `AGENTS.md`
- **Auto-memory:** native. Post-rollout extraction pipeline stores memories in SQLite, outputs to MEMORY.md and skills/. Runs asynchronously at startup.

## OpenCode

- **Primary file:** `AGENTS.md`
- **Fallback:** if no `AGENTS.md` exists, reads `CLAUDE.md` as fallback. Same for global: `~/.config/opencode/AGENTS.md` falls back to `~/.claude/CLAUDE.md`
- **Agents:** modular markdown-based agents in `.opencode/agents/` with YAML frontmatter
- **Auto-memory:** not built-in. Community plugins available (supermemory, vector DB, MCP-based). Auto-memory tactics may not be available without plugin setup.

## Cursor

- **Primary file:** `.cursorrules` (project root, legacy) or `.cursor/rules/` directory (modern)
- **Discovery:** `.cursorrules` detected automatically at project root. Modern rules in `.cursor/rules/` are included when matching files are referenced.
- **Global rules:** configured in Cursor Settings > General > Rules for AI
- **No AGENTS.md or CLAUDE.md support** — Cursor has its own convention entirely
- **Auto-memory:** none. No persistent memory system.

## Cross-Compatibility Strategy

For projects that need to work across multiple harnesses:

1. **Use AGENTS.md as the single source of truth** — read natively by Codex and OpenCode. Claude Code should be strongly directed (via auto-memory or CLAUDE.md) to read AGENTS.md as its first action. This is the preferred cross-platform approach: one file, all harnesses.
2. **Fallback: symlink or duplicate to CLAUDE.md** — if directing Claude Code to read AGENTS.md proves unreliable, symlink or duplicate the content. This is a last resort, not the default.
3. **Maintain `.cursorrules` or `.cursor/rules/` separately** — Cursor's format is different enough that a separate file is cleaner than trying to share.
4. /warmup should detect which harness is active and target the appropriate file(s).
