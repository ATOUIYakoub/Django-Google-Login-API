## Django Google Login API

This Django app provides integration with Google Login API using Django Rest Framework.

## Contents

1. **settings.py**: Configuration for integrating Google Login API credentials.
2. **views.py**: Contains view functions for handling Google OAuth authentication.
3. **urls.py**: Specifies URL patterns for accessing Google OAuth endpoints.
4. **serializers.py**: Contains serializer classes for handling authentication data.

## Authentication Flow

The authentication flow involves the following steps:

1. **User Request Authentication**: 
   - Send a request to `/api/google/login/` with the necessary parameters to initiate Google OAuth authentication.
   
2. **Google Authentication Redirect**: 
   - User is redirected to Google's authentication page to authorize the app.
   
3. **Callback URL Handling**: 
   - After successful authentication, Google redirects the user to the specified callback URL (`/api/google/callback/`).
   
4. **Token Retrieval**: 
   - Exchange the authorization code for an access token and retrieve user information from Google.

## Usage

1. **Setup Django Environment**

   Ensure your Django project is set up and running.

2. **Add Google API Credentials**

   Add your Google API credentials (Client ID and Client Secret) to your Django project's settings.

3. **Copy the App**

   Copy the `google_login` app directory to your Django project's directory.

4. **Include URLs**

   Include the URLs from the `google_login` app in your project's `urls.py`.

5. **Start the Server**

   Start the Django development server:


6. **Access Google Login**

Access the Google login functionality at `/api/google/login/` and handle the callback at `/api/google/callback/`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

