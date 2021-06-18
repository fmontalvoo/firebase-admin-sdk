# https://firebase.google.com/docs/auth/admin/custom-claims#python_3
# https://firebase.google.com/docs/admin/setup

import firebase_admin
from firebase_admin import auth, credentials

cred = credentials.Certificate("./serviceAccountKey.json")

app = firebase_admin.initialize_app(cred)


print(app.name)

user = auth.get_user_by_email('email@gmail.com')

print(user)
print(user.email_verified)

if user.email_verified:
    # Add custom claims for additional privileges.
    # This will be picked up by the user on token refresh or next sign in on new device.
    auth.set_custom_user_claims(user.uid, {
        'admin': True,
        'roles': ['admin', 'editor']
    })

    # Remove custom claims. 
    # auth.set_custom_user_claims(user.uid, None)

    # auth.update_user(user.uid, display_name="Frank Montalvo")
print(user.custom_claims)