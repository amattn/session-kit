We have two open process observations in SHARPEN.md:

1. **SPI_1: Agents skip consistency pass after file renames** [convention] — Noticed in sessions 2, 4, and 5. After renaming a file or variable, agents proceed without checking for stale references. Three occurrences, confirmed pattern.

2. **SPI_2: Review cycles take too many round-trips** [friction] — The "anything else?" pattern forces 3+ rounds when structured options would take 1. This was previously resolved by adding interaction conventions to CLAUDE.md, but was reopened because it's still happening in sessions 7 and 8 despite the fix.

There is also one resolved observation (SPI_3: commit message inconsistency), which was closed after adding a commit style section to CLAUDE.md.
