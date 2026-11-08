---
name: metamath-guidelines
description: Use when writing, reviewing, or refactoring code, especially when requirements are illustrated by examples or fixes risk adding case-specific complexity.
---

# Metamath Guidelines

Behavioral guidelines to reduce common LLM coding mistakes, based on Andrej Karpathy's observations on LLM coding pitfalls, with an additional fifth principle focused on preserving generality and avoiding case-specific overfitting.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:

```text
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

## 5. Preserve Generality

**Examples illustrate requirements. They do not define the system.**

- Don't hard-code examples into production behavior.
- Keep reusable logic independent of case-specific content.
- Don't narrow valid behavior just to make one example pass.
- When a case fails, fix the underlying assumption - don't stack exceptions.
- If each fix makes the implementation more complex, stop adding layers. Look for a simpler underlying model or design, explain what you find to the user, and plan the next step together.
- Preserve existing capabilities unless the user explicitly asks to restrict them.
- Test with materially different valid cases, not just the original example.

The test: "Would a different valid example work without adding another special case?"
