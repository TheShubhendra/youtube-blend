import {useGoogleLogin} from "@react-oauth/google";
import {googleLoginOptions} from '../utilities.tsx';

const Home = () => {
    const googleLogin = useGoogleLogin(googleLoginOptions);
    return (
        <div>
            <div className="flex flex-col items-center justify-center h-screen">
                <h1 className="text-6xl">Welcome to YouTube Blend</h1>
                <p className="text-lg">Login to get started</p>
                <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onClick={googleLogin}>Login as Google</button>
            </div>

        </div>
    )
}
export default Home