# Roadmap: Autocomplete + Spell Checker in Python (learning project)

## Context
The user (SEM student at GU) wants a concrete side project that builds strong, interview-ready Python
skills and reuses their love of DSA. A plain "DSA library" felt like copying course material because the
structures had no purpose. This project gives every data structure a job: a terminal tool that
autocompletes words and suggests spelling corrections. **The user writes the code; Claude acts as a tutor**:
explaining concepts, reviewing, and giving hints, not handing over full implementations.

Environment: Python 3.13.7, git 2.51 available. No existing project yet.

## Project setup
- Location: `C:\Users\herma\projects\spellbook\` 
- `git init` from the first commit; commit after every milestone
- Layout: `src/spellbook/` (package), `tests/`, `pyproject.toml`, `README.md`
- Dev dependencies (**ask the user before adding**): `pytest`, later optionally `hypothesis`
- Word data: a free word-frequency list (e.g. a public English frequency list .txt), stored in `data/`

## Milestones (each one is small and shippable)
1. **Trie: prefix autocomplete.** `Trie` class with `insert`, `__contains__`, `__len__`, `__iter__`,
   `starts_with(prefix)`. Python skills: dunder methods, type hints, `@dataclass` for nodes, pytest basics.
2. **Ranked suggestions.** Store word frequencies and return the top-k completions using a heap.
   Write a small binary heap yourself first, then compare it with `heapq`. Skills: `heapq`, generics (`class Heap[T]`).
3. **Edit distance.** Levenshtein distance with dynamic programming (DP): first recursion with `functools.cache`, then a
   bottom-up table, then the O(n)-memory version. Skills: decorators, profiling with `timeit`.
4. **BK-tree: fast spell correction.** Find words within distance ≤ k without scanning the whole dictionary.
   Benchmark it against a brute-force scan. Skills: recursion, benchmarking, honest measurement.
5. **CLI.** `python -m spellbook complete "pyth"` / `correct "speling"` using `argparse`. Skills: packaging,
   `__main__.py`, `pathlib`, file I/O.
6. **Polish (stretch goals).** Property-based tests (hypothesis) comparing the trie against a `set`; an interactive
   REPL mode; a README with benchmark results. This becomes a portfolio piece to talk about in interviews.

## Working style per milestone
1. Claude explains the concept and the interface to build (the *why*).
2. The user implements it and writes tests.
3. Claude reviews it: correctness, Pythonic style, complexity, and likely interview follow-up questions.

## Verification
- `pytest` passes at every milestone
- Milestone 4: benchmark shows the BK-tree beats brute force on the full word list
- End to end: `python -m spellbook complete "pro"` returns ranked words; `correct "recieve"` suggests "receive"

## Alongside the project
Do 2–3 LeetCode-style problems a week focused on built-ins (`dict`, `Counter`, `deque`, `heapq`) for interview speed.
