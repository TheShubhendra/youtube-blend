
const BASE_URL = 'http://localhost:8000';
import axios from "axios";

type AuthCodeFlowResponse = {
    access_token: string;
    profile: object;
}
const authCodeFlow = async (code: string): Promise<void | AuthCodeFlowResponse> => {
    return await axios.post(
        `${BASE_URL}/auth/login-flow`, {
            code: code,
        }).then((response) => {
            return response.data;
        })
        .catch((error) => {
        console.log(error);
        alert('Error logging in');
    });
}

export { authCodeFlow };