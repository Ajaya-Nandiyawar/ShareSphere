# Developer Environment Check

**Instructions:**
Run the following commands on your local development machine and paste the output below to verify compliance with SRS Sec 2.4 and NFR-PRT-01.

Commands to run:
```bash
php -v
php -m | egrep -i "pdo_pgsql|openssl|mbstring|fileinfo|gd|json|sodium"
node -v
composer -V
psql --version
php -r "echo defined('PASSWORD_ARGON2ID') ? 'Argon2id OK' : 'Argon2id missing';"
```

---

## 1. Ajaya's Environment

| Component | Output / Version | Verified? |
|-----------|------------------|-----------|
| **PHP** (`php -v`) | *(paste output here)* | [ ] |
| **PHP Extensions** (`php -m`) | *(paste output here)* | [ ] |
| **Argon2id Support** | *(paste output here)* | [ ] |
| **Node.js** (`node -v`) | *(paste output here)* | [ ] |
| **Composer** (`composer -V`) | *(paste output here)* | [ ] |
| **PostgreSQL/psql** | *(paste output here)* | [ ] |

## 2. Rishi's Environment

| Component | Output / Version | Verified? |
|-----------|------------------|-----------|
| **PHP** (`php -v`) | *(paste output here)* | [ ] |
| **PHP Extensions** (`php -m`) | *(paste output here)* | [ ] |
| **Argon2id Support** | *(paste output here)* | [ ] |
| **Node.js** (`node -v`) | *(paste output here)* | [ ] |
| **Composer** (`composer -V`) | *(paste output here)* | [ ] |
| **PostgreSQL/psql** | *(paste output here)* | [ ] |

## 3. Abhijeet's Environment

| Component | Output / Version | Verified? |
|-----------|------------------|-----------|
| **PHP** (`php -v`) | *(paste output here)* | [ ] |
| **PHP Extensions** (`php -m`) | *(paste output here)* | [ ] |
| **Argon2id Support** | *(paste output here)* | [ ] |
| **Node.js** (`node -v`) | *(paste output here)* | [ ] |
| **Composer** (`composer -V`) | *(paste output here)* | [ ] |
| **PostgreSQL/psql** | *(paste output here)* | [ ] |

---
*Note: Do not proceed until all developer environments pass the checks.*
