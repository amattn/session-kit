I red-penned `grid_section.md` for a product-management reader and edited it in place. All the facts, numbers, and cross-references (§7.5, §10.3) are unchanged. The changes are about clarity, structure, and making the decisions easier to see.

**What I changed**

- **Fixed a miscount in §6.3.** It said "three mechanisms that shape how densely an advisor's day fills," but one of them (adjacent-slot checking) is deprecated and nothing calls it. It now reads as two live mechanisms plus one retired one, marked "(deprecated)".
- **Renamed §6.3** from "Why this matters for calendar packing" to "Interaction with how slots are ranked," since that is what the section actually covers.
- **Replaced "lattice" and "span" with plain wording** ("the 15-minute grid", "a 45-minute block"). It's the same idea without the engineering vocabulary.
- **Made the decisions easy to find:**
  - §6.2 now ends with a bolded **Recommendation**: keep the 15-minute grid and treat length as a block on it, and don't ship 45 as its own rhythm. I moved that last point up from §6.3, where it was buried.
  - The trigger and switch-vs-weighting questions in §6.3 are now an explicit list of open questions.
  - The heading "not a priority" is now in the subsection title.
  - §6.5 is labelled "Open issue."
- **Cut repetition:**
  - The noon-scoring explanation was stated twice; it's now stated once.
  - The closing paragraph of §6.4, which repeated §6.2's conclusion, is shortened.
  - Some hedging and filler is gone, e.g. "really," "genuine," "simply," "at all."
- **Two small accuracy fixes:**
  - "repeats only every three hours" is now "realigns with the hour only every three hours."
  - §6.5 now notes that the current duration-as-grid behaviour is exactly the 45-minute-rhythm model §6.2 recommends against. A PM should notice that tension.

**Worth checking before it circulates**

- **§6.5's "appears to"** is still a hedge about observed behaviour. If someone can confirm what picking 45 minutes actually does, state it flatly.
- **Mixed grids in §6.2.** The "fill a 90-minute opening / align to 15-minute bookings" approach assumes a 15-minute base grid, but six of the ten meeting types are on a 30-minute grid. The doc doesn't say whether 45-minute support would move those types to a 15-minute base. That's a product decision the section leaves open.
