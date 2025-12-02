This project sets up a simple developer environment with:
- A **PostgreSQL database** containing a `Frogs` table and sample data
- A **Flask web app** that connects to the database using `psycopg2-binary`

## How to Run
1. Clone or download this project.
2. Open a terminal in the project folder (`elfroggo`).
3. Run:
   ```bash
   docker compose up --build


- **elfroggo-dev-env/
├─ docker-compose.yml
├─ web/
│  ├─ Dockerfile
│  ├─ app.py
│  ├─ requirements.txt
│  └─ config.py
├─ db/
│  ├─ init.sql
│  └─ seeds.sql
├─ .env
└─ README.md**
