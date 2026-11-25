# User Guide (Hinglish)

## Ye library kya hai?
Ye alag-alag AI agents ke liye reusable Skills ka collection hai. Skill ek instruction package hai. Ye khud AI model, executable software, permission ya tool access nahi hoti.

## Shuru kaise karein?
1. [CATALOG.json](../CATALOG.json) aur [Skills Directory](../skills/README.md) dekhein.
2. Apne kaam ke liye sirf zaroori Skills chunein.
3. Chuni hui Skill ki poori `SKILL.md` padhein. Saath mein [GLOBAL_RULES.md](../GLOBAL_RULES.md), [SKILL_RULES.md](../SKILL_RULES.md) ke relevant rules aur user ka `AI_CONTEXT.md` ho to use load karein. Agar file nahi hai, to available jankari se kaam jaari rakhein; zaroori detail missing ho to ek baar mein ek sawal poochhein.
4. Apne AI client ke hisaab se [INSTALLATION.md](../INSTALLATION.md) follow karein.
5. Real kaam se pehle ek safe example par test karein.

## Ek se zyada Skills kab chahiye?
Agar kaam kai areas mein hai, to chhota aur sahi combination use karein. Example: pehle specification, phir PHP/database engineering, security audit aur testing. Bina zaroorat sabhi Skills install na karein.

## AI platform compatibility
ChatGPT, Claude, Gemini, Codex aur IDE agents ka Skill load karne ka tareeka alag ho sakta hai. Folder, linked files, tools aur permissions har client mein verify karein. Har jagah same result ka promise nahi hai.

## Update kaise karein?
[CHANGELOG.md](../CHANGELOG.md) aur [MIGRATION.md](../MIGRATION.md) padhein. Apne local changes ka backup lein, naye aur purane version compare karein, phir update aur validation karein. Bina dekhe purani files overwrite na karein.

## Status ka matlab
- PASS: test hua aur sahi nikla.
- FAIL: test hua aur fail hua.
- NOT RUN: test kiya hi nahi.
- UNVERIFIED: proof nahi mila.
- BLOCKED: permission ya dependency nahi mili.

## License
Skills aur documentation CC BY 4.0 hain. Scripts, tests aur workflow code MIT hain. Share karne se pehle license aur attribution rules padhein.
