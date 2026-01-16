# Django Backend Core Foundation

**Description:** Django/DRF backend foundation with **RBAC**, **tenant isolation**, and **audit logs**, ready as a secure base for enterprise applications.

## What I Implemented
- **Authentication**: JWT-based login, refresh, logout  
- **RBAC**: Roles – Admin, Reviewer, Requester, Vendor; custom DRF permission classes  
- **Tenant Isolation**: Users access only their org/vendor data  
- **Audit Logs**: Logs all critical write actions (create, approve, request remediation, upload evidence, etc.)  
- **OpenAPI/Swagger**: Interactive API docs with JWT auth  


## Setup Instructions
1. Clone repo & create virtual environment  
2. Install dependencies: `pip install -r requirements.txt`  
3. Add `.env` (SECRET_KEY, DEBUG, DATABASE_URL)  
4. Run migrations: `python manage.py migrate`  
5. Create superuser: `python manage.py createsuperuser`  
6. Run server: `python manage.py runserver`  

## API Endpoints
- `POST /auth/login` – Login  
- `POST /auth/refresh` – Refresh token  
- `POST /auth/logout` – Logout  
- Swagger UI: `/api/schema/swagger-ui/`  

## Notes
- Do **not** commit `.env` files  
- Use role-based permission decorators for all endpoints  
- Audit logs ensure traceability for critical actions

