
# Project Fastzero

Repositório da implementação do conteúdo do curso [Fastapi do Zero](https://fastapidozero.dunossauro.com).

## Dependencies

- **Python:** 3.12.*
- **FastAPI:** 0.111.0
- **SQLAlchemy:** 2.0.31
- **Pydantic-settings:** 2.3.4
- **Alembic:** 1.13.2
- **Pwdlib:** 0.2.0
- **Python-multipart:** 0.0.9
- **PyJWT:** 2.8.0
- **Psycopg:** 3.2.1

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/paullosergio/fast_zero.git
   ```
2. Install [Poetry](https://python-poetry.org/).
3. Install project dependencies:
   ```bash
   poetry install
   ```
4. Create a `.env` file and configure the following environment variables:
   - `DATABASE_URL`
   - `SECRET_KEY`
   - `ALGORITHM`
   - `ACCESS_TOKEN_EXPIRE_MINUTES`
5. Start the project using Docker Compose:
   ```bash
   docker-compose up
   ```

## Usage

1. Access the FastAPI Swagger documentation at `http://localhost:8000/docs` to explore API endpoints.
2. Test authentication by obtaining an access token through the `/token` endpoint.
3. Use the available endpoints to interact with the database and test file uploads.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Implement your changes and commit them:
   ```bash
   git commit -m 'Add new feature'
   ```
4. Push your branch to the repository:
   ```bash
   git push origin feature/new-feature
   ```
5. Submit a pull request for review.

## Testing and Code Formatting

- **Run tests:** Enter the Poetry shell and execute:
  ```bash
  task test
  ```
- **Format code:** Use the command:
  ```bash
  task format
  ```
