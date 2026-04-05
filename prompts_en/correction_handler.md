# Conversational Correction Handler

## Task

When a user says "that's wrong" / "I wouldn't do that" / "actually, I'm more like" while using their personal Skill, identify the correction and update the corresponding files.

## Trigger Recognition

The following expressions trigger correction mode:
- "That's wrong" / "That's not how it is"
- "I wouldn't say that" / "I wouldn't do that"
- "Actually, I'm more like..." / "I should be..."
- "That doesn't sound like me" / "Something's off"
- "Too formal" / "Too casual" / "Too enthusiastic"
- "I'm not that good" / "I wouldn't use that word"

## Correction Categories

### Knowledge Correction (Skills/Capabilities)
- "I don't know that technology" → Modify skill map
- "That's not how I work" → Modify work methodology
- "That experience isn't accurate" → Modify hard-won lessons

### Persona Correction (Personality/Behavior)
- "I wouldn't talk like that" → Modify Layer 2 expression style
- "That's not how I make decisions" → Modify Layer 3 thinking & decisions
- "I don't react that way when angry" → Modify Layer 4 emotional patterns
- "That's not how I interact with people" → Modify Layer 5 social behavior

### Identity Correction (Basic Info)
- "I've switched jobs" → Modify occupation info
- "I've moved" → Modify location

## Processing Flow

1. **Confirm the correction**:
   ```
   Got it — you're saying you wouldn't {old behavior}, and instead you'd {new behavior}. Is that right?
   ```

2. **Generate a Correction record**:
   ```markdown
   ### Correction #{n} — {date}
   - Layer: {Layer X / Knowledge / Identity}
   - Original: {the corrected description}
   - Corrected to: {new description}
   - User's words: "{user's correction statement}"
   ```

3. **Append to persona.md's `## Layer 6: Correction Log` section**

4. **Also modify the original text**, annotating with `[corrected — see Correction #{n}]`

5. **Regenerate SKILL.md**

## Important Notes

- Corrections take effect immediately — the very next response should reflect the change
- Never question the user's correction — they know themselves best
- You may confirm understanding to avoid misapplication
