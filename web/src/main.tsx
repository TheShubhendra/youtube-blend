import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'
import {GoogleOAuthProvider} from "@react-oauth/google";

const CLIENT_ID ="971995573422-ea0ik6i2n8hdkejerpfoe9c55952qfja.apps.googleusercontent.com";

ReactDOM.createRoot(document.getElementById('root')!).render(
    <GoogleOAuthProvider clientId={CLIENT_ID}>
        <React.StrictMode>
                <App />
        </React.StrictMode>
    </GoogleOAuthProvider>
,
)
