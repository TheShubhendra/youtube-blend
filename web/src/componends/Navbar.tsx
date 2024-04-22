import {useGoogleLogin} from "@react-oauth/google";
import {googleLoginOptions} from '../utilities.tsx';


const Navbar = () => {

    const googleLogin = useGoogleLogin(googleLoginOptions);

    return (
        <nav className="bg-white border-gray-200 dark:bg-gray-900">
            <div className="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
                <a href="https://flowbite.com/" className="flex items-center space-x-3 rtl:space-x-reverse">
                    {/*Add icon here*/}
                    <span className="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">YouTube Blend</span>
                </a>
                <button data-collapse-toggle="navbar-default" type="button" className="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600" aria-controls="navbar-default" aria-expanded="false">
                    <span className="sr-only">Open main menu</span>
                    <svg className="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 17 14">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 1h15M1 7h15M1 13h15"/>
                    </svg>
                </button>
                <div className="absolute right-0 m-2">
                    {localStorage.getItem('token') == null ? (
                        <button onClick={googleLogin} className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Login</button>
                        ) : (
                        <img className="w-10 h-10 rounded-full" src="https://lh3.googleusercontent.com/a/ACg8ocIwelAuXAZf1h9epzKd6E09xsYm805tH5fgYm_3VYmgfiwX633GyA=s96-c" alt="Profile image"/>
                    )
                    }
                </div>
            </div>
        </nav>


    )
}

export default Navbar