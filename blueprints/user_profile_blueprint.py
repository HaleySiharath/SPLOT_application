# Implement all CRUD elements
# Reference this: https://github.com/jacobtie/itsc-3155-module-10-demo/blob/main/blueprints/book_blueprint.py
from flask import Blueprint, abort, redirect, render_template, request
from models import Userprofile, db

router = Blueprint('user_profile_router', __name__, url_prefix='/user_profile')

# Hirdhay
@router.get('')
def get_all_user_profile():
    all_users = Userprofile.query.all()
    return render_template('all_users.html', users = all_users)

# Haley
@router.get('/<user_id>')
def get_single_user_profile(user_id):
    single_user_profile = Userprofile.query.get_or_404(user_id)
    return render_template('single_user_profile.html', user = single_user_profile)

# Haley
@router.get('/new')
def create_user_profile_form():
    return render_template('signup.html')

# Haley
@router.post('')
def create_user_profile():
    name = request.form.get('first-name', '') + " " + request.form.get('last-name', '')
    email = request.form.get('email', '')
    password = request.form.get('password', '')

    if name == '' or email == '' or password == '':
        abort(400)

    new_user_profile = Userprofile(user_name=name, user_email=email, user_password=password)
    db.session.add(new_user_profile)
    db.session.commit()

    return redirect(f'/user_profile/{new_user_profile.user_id}')

# Hirdhay
@router.get('/<user_id>/edit')
def get_edit_user_profile_form(user_id):
    user_to_edit = Userprofile.query.get_or_404(user_id)
    return render_template('editprofile.html', user = user_to_edit)

# Hirdhay
@router.post('/<user_id>')
def update_user_profile(user_id):
    user_to_update = Userprofile.query.get_or_404(user_id)
    name = request.form.get('name', '')
    location = request.form.get('location', '')
    biography = request.form.get('biography', '')

    if location == '' or biography == '':
        abort(400)


    user_to_update.user_location = location
    user_to_update.user_biography = biography

    db.session.commit()

    return redirect(f'/user_profile/{user_id}')

# Hirdhay
@router.post('/<user_id>/delete')
def delete_user_profile(user_id):
    print("here" + user_id)
    user_to_endit = Userprofile.query.get_or_404(user_id)
    print(user_id)

    db.session.delete(user_to_endit)
    db.session.commit()
    return redirect('/user_profile')