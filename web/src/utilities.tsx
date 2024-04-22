import axios from "axios";
import {authCodeFlow} from "./api.tsx";
import {UseGoogleLoginOptionsAuthCodeFlow} from "@react-oauth/google";


const googleLoginOptions: UseGoogleLoginOptionsAuthCodeFlow = {
    flow: 'auth-code',
    scope: 'https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile openid https://www.googleapis.com/auth/youtube.readonly',
    onSuccess: async (codeResponse: { code: any; }) => {
    const response = await authCodeFlow(codeResponse.code);
    if (!response) {
        return;
    }
    localStorage.setItem('token', response.access_token );
    localStorage.setItem('profile', JSON.stringify(response.profile));
    axios.defaults.headers.common['Authorization'] = `Bearer ${response.access_token}`;
},
    onError: (errorResponse: any) => console.log(errorResponse),
}
export { googleLoginOptions };