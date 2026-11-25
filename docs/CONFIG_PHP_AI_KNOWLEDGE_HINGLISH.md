# config.php ko AI ki Permanent Context File banana (Hinglish)

## Is file ka sahi use
Ye `config.php` kisi web server par install nahi hogi. User ise apne AI assistant ke private Knowledge / Files section mein upload karega. Agar Knowledge feature nahi hai, to chat mein attach karega. AI ise sirf text ki tarah padhega. PHP code ko kabhi execute, include ya evaluate nahi karega.

## Is file mein kya rakhein?
Sirf aisi jankari jo lambe samay tak sahi rahe aur future tasks mein baar-baar kaam aaye:
- jawab ki language aur simple/technical level;
- user ki confirmed preferences;
- confirmed business details;
- active long-term projects aur unke official repositories;
- important project decisions aur permanent limitations;
- technical defaults, lekin badalne wale versions ko deploy se pehle verify karna hoga;
- common legal/content preferences.

Password, OTP, API key, private key, recovery code, full bank/card number, customer details ya unnecessary sensitive data kabhi na rakhein. Ek din ke task, temporary amount, guess ya unconfirmed baat bhi is file mein na jodein.

## Har bade task ke baad AI kya kare?
AI har substantial task ke end mein current chat ko check kare:
1. Kya koi nayi permanent preference, confirmed decision, project rule ya reusable technical setting mili?
2. Kya ye future mein bhi kaam aayegi, ya sirf aaj ke task ki baat hai?
3. Kya ye pehle se kisi aur naam/key se file mein hai?
4. Kya purani value se conflict hai?
5. Kya baat sensitive ya uncertain hai aur user ki permission chahiye?

Agar kuch naya nahi mila, to update ka faltu message na de.

Agar useful nayi jankari mile, AI bataye:
- nayi jankari kya hai;
- ise save karna kyon useful hai;
- file ke kis section/key mein kya value add/change karni hai;
- user ki confirmation zaroori hai ya nahi.

AI file ko chupke se badle nahi. Pehle chhota exact code snippet ya patch de. User check kare, file update kare aur AI Knowledge mein purani file ko replace karke nayi upload kare.

## File update ka tarika
1. AI Knowledge se current `config.php` download/open karein.
2. Sirf sambandhit key/value update karein. Baaki sahi jankari na hatayein.
3. `config_version` badhayein aur `updated_at` update karein.
4. Duplicate, conflict, temporary data aur secrets check karein.
5. Nayi file AI ke Knowledge / Files mein upload karke purani file replace karein. Agar platform sirf chat attachment rakhta hai, to naye chat/project mein latest file attach karein.
6. AI se latest version padhkar version/date aur changed keys confirm karwayein.

## Zaroori seema
Har AI platform ka Knowledge upload alag hota hai. Ye GitHub repository khud se ChatGPT, Claude ya Gemini ki private Knowledge file update nahi kar sakti. User ko upload/replace karna hoga ya official authorized connector chahiye. AI tabhi save hone ka claim kare jab platform sach mein confirm kare.

## PHP file ko kaise padhein?
AI ise plain text ke roop mein padhega; server par run nahi karega. Agar kisi AI platform mein PHP upload allow nahi hai, to isi data ka JSON ya Markdown export use karein. Ek hi canonical file maintain karein, alag-alag copies mein conflicting data na rakhein.
