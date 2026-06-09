# Choice Circle

A Django selection project for a group choice game.

## Features
- Participants can choose exactly one other person.
- No one can select themselves.
- Each person can be selected by only one person.
- Uses a spin-style choice process and shows a large result name with hearts.
- Includes an admin dashboard for viewing status and resetting assignments.
- Built with the provided participant names, including Elder.

## Installation
1. Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```powershell
   python manage.py migrate
   ```
4. Create a superuser for Django admin (optional):
   ```powershell
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```powershell
   python manage.py runserver
   ```

## Usage
- Open the site at `http://127.0.0.1:8000/`
- Choose your name and spin to reveal your selected target.
- Visit `http://127.0.0.1:8000/admin-dashboard/` to view who has chosen and reset all choices.
- Use `/admin/` for the Django admin interface.
